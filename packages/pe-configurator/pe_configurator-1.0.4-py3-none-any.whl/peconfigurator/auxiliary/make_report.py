# Copyright (C) 2020  Serguei Ossokine <serguei.ossokine@ligo.org>
# Based on pesummary file make_public.py by Charlie Hoy.

from .run_analyzer import SNR_threshold, distance_checks, mass_ratio_checks, NS_check, spin_checks, highmass_check, NSBH_check
import datetime
import hashlib
import os
import subprocess as sp

import numpy as np
import pandas as pd
from importlib.metadata import version
from pesummary import __version__
from pesummary.io import read
#from run_analyzer import *
from pesummary.core.notebook import (
    NoteBook,
    imports,
    pesummary_read,
    posterior_samples,
    samples_dict_plot,
)

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        hash_md5.update(f.read())
    return hash_md5.hexdigest()


def markdown_table_writer_extra(date, version, complete_args):
    """Write the extra metadata"""
    body = f"""
|  |  |
|--|--|
|Date| {date}|
|Script revision| {version}|
|Complete arguments | {complete_args}|
"""
    return body


def markdown_writer_heuristics(samples, seglen):
    """Write the rules-based analysis out

    Args:
        samples ([array-like]): the samples
    """
    msgs = []
    msgs.extend(distance_checks(samples))
    msgs.extend(NS_check(samples))
    msgs.extend(mass_ratio_checks(samples))
    msgs.extend(SNR_threshold(samples))
    msgs.extend(spin_checks(samples))
    msgs.extend(highmass_check(samples))
    msgs.extend(NSBH_check(samples, seglen))
    result = ""
    for msg in msgs:
        if msg:
            result += f"""
* **{msg}**\n
"""
    return result


def markdown_table_writer_settings(settings):
    body = f"""
|  |  |
|--|--|
|  seglen | {settings['seglen']} sec. |
|  srate       |  {settings['srate']}     |
|  $f_{{\\rm start}}$     | {np.round(settings['f_start'],4)} Hz|
|  $f_{{\\rm ref}}$     | {np.round(settings['f_ref'],4)} Hz|
| reference-frame | {settings["reference_frame"]} |
| time-reference | {settings["time_reference"]} |
| $\\mathcal{{M}}$ bounds | [{np.round(settings['chirpmass_min'],4)},{np.round(settings['chirpmass_max'],4)}]|
| mass-ratio bounds | [{np.round(settings['q_min'],4)},1] |
"""
    if settings.get("dL_min") is not None:
        body += f"""| $d_\\mathrm{{L}}$ bounds | [{np.round(settings['dL_min'],1)},{np.round(settings['dL_max'],1)}] |"""
    return body


def markdown_table_writer_checks(checks, recommendations=None, exclude=None,detchar_checks={}):
    body = f"""
| |  | Recommendation  |
|--|--|--|
"""
    for key, item in checks.items():
        if exclude is not None:
            if key in exclude:
                continue
        if item is True:
            text = "<font color='green'>PASSED</font>"
        else:
            if key == 'f_ref':
                # Check for the reason why f_ref was changed

                if detchar_checks.get("consistent_seglen",True):
                    # Detchar segment length was OK, so MECO test must have failed
                    text = "<font color='red'>FAILED. MECO test failed, f_ref has been overwritten to a safe value.</font>"
                else:
                    # Detchar recommendation forced us to overwrite f_ref
                    text = "<font color='red'>Attention: Due to a restriction on the segment length, the reference frequency is lower than the starting frequency of the waveform. Overwritting reference frequency to f_start.</font>"
            else:
                text = "<font color='red'>FAILED."

        if key in recommendations.keys():
            rec = recommendations[key]
        else:
            rec = ""
        body += f"|{key}|**{text}**| {rec}| \n"
    return body


def markdown_table_writer_input(dc, auxillary_vars):
    """Turn a dictionary into a markdown table"""

    input_settings_headers = [
        "$f_{\\rm low}$",
        "$f_{\\rm ref}$",
        "Max $\\ell$ for Nyquist check",
        "Tolerance for railing",
        "nbins for railing",
    ]
    input_settings_values = [
        f"{dc['flow']} Hz",
        f"{dc['f_ref']} Hz",
        f"{dc['ell_max']}",
        f"{dc['tolerance']}",
        f"{dc['nbins']}",
    ]
    body = f"""
**Data provenance**

|  |  |
|--|--|
| PE summary file | {dc['samples_file']} |
|  Data set       |  {dc['dataset']}     |
| md5sum of file      |     {auxillary_vars['hash']}     |

**Settings**

| | |
|--|--|
"""
    for i in range(len(input_settings_headers)):
        body += f"|{input_settings_headers[i]}|{input_settings_values[i]}|\n"
    dc.pop("samples_file")
    dc.pop("dataset")

    return body


def make_config_table(args, auxillary_vars):
    """Create a markdown table of settings"""
    dc = vars(args)
    return markdown_table_writer_input(dc, auxillary_vars)


def make_report(
    pesummary_file,
    recommended_settings,
    args,
    f_ref,
    checks=None,
    recommendations=None,
    analysis=None,
    optional_name=None,
    filename="posterior_samples.ipynb",
    outdir="./",
    detchar_checks=None,
):
    """Make a jupyter notebook showing how to use the PESummary result file

    Parameters
    ----------
    """
    chirpmass_min = recommended_settings["chirpmass_min"]
    chirpmass_max = recommended_settings["chirpmass_max"]
    checks_passed = all(checks.values())

    q_min = recommended_settings.get("q_min", None)

    nb = NoteBook()
    f = read(pesummary_file)
    if analysis is None:
        analysis = f.labels[0]
    elif analysis not in f.labels:
        raise ValueError(
            "The analysis '{}' does not exist in '{}'. The available analyses "
            "are {}".format(analysis, pesummary_file, ", ".join(f.labels))
        )
    samples = f.samples_dict[analysis]
    # Header
    cell = f"# configurator report\n This notebook contains the automatic `configurator` report based on preliminary PE results.\n"
    nb.add_cell(cell, markdown=True)

    auxillary_vars = dict(hash=md5(pesummary_file))
    # Config table
    config_table = make_config_table(args, auxillary_vars)
    nb.add_cell(config_table, markdown=True)

    # Imports (hidden)
    text, cell = imports(
        module_imports=["pesummary", "pesummary.io:read"],
        extra_lines=[
            "import numpy as np",
            "import matplotlib.pyplot as plt",
            "import pandas as pd",
            "%config InlineBackend.figure_format = 'retina'",
            "import warnings",
            "warnings.filterwarnings('ignore')",
        ],
    )
    nb.add_cell(cell, code=True)

    # Automatically generated warnings
    nb.add_cell("## Automatically generated analysis", markdown=True)
    report = markdown_writer_heuristics(samples, recommended_settings["seglen"])
    if report:
        nb.add_cell(report, markdown=True)
    else:
        nb.add_cell("Nothing to report", markdown=True)

    # Warn people if there is detchar recommendations
    if args.detchar_seglen > 0:
        nb.add_cell("## Detchar recommendations",markdown=True)
        txt = f"""
<font color='red'>**Note: DetChar recommends a maximum safe duration of {args.detchar_seglen} seconds.
The settings should be scrutinized!**</font>
        """
        nb.add_cell(txt,markdown=True)

    # Read samples (hidden)
    text, cell = pesummary_read(pesummary_file, read_variable="data",)
    nb.add_cell(cell, code=True)

    # Get the right dataset (hidden)
    text, cell = posterior_samples(
        "data",
        metafile=True,
        default_analysis=analysis,
        print_parameters=False,
        samples_variable="posterior_samples",
    )
    nb.add_cell(cell, code=True)
    cell = "## Summary of posterior sample parameters\n"
    nb.add_cell(cell, markdown=True)

    # Summary of the PE sample properties
    cell = """
mtot = np.array(posterior_samples["total_mass"])
q = np.array(posterior_samples["mass_ratio"])
chi1z = np.array(posterior_samples["spin_1z"])
chi2z = np.array(posterior_samples["spin_2z"])
dist = np.array(posterior_samples["luminosity_distance"])
chirp_mass = np.array(posterior_samples["chirp_mass"])

dc = {
    r"$\\mathcal{M}\ (M_{\odot})$": chirp_mass,
    r"$M_{\\rm total}\ (M_{\odot})$": mtot,
    r"$q$": q,
    r"$d_{L} (Mpc)$": dist,
    r"$\\chi_{1z}$": chi1z,
    r"$\\chi_{2z}$": chi2z
}
df = pd.DataFrame(dc)
try:
    from pandas_profiling import ProfileReport
    have_report = True
except:
    from IPython.core.display import display, HTML
    have_report = False

have_report = False
if have_report:
    profile = ProfileReport(df, title='Pandas Profiling Report',minimal=True,progress_bar=False,
        html={"navbar_show": False})
    profile.to_widgets()
else:
    from IPython.core.display import display, HTML
    display(HTML(df.describe().to_html()))
    """
    nb.add_cell(cell, code=True)
    nb.add_cell("## Posterior railing visual check", markdown=True)
    text = "Automatic checks on railing. Note that the **recommendations are ad-hoc** and may not result in posteriors not being cut off."
    nb.add_cell(text, markdown=True)
    checks_table = markdown_table_writer_checks(
        checks, recommendations=recommendations, exclude=["f_ref"]
    )
    nb.add_cell(checks_table, markdown=True)
    # Diagnostic plot of the chirp mass

    cell = f"""
checks_passed = {checks_passed}
version = [int(x) for x in pd.__version__.split('.')]
if version[0]<1:
    j,k = 1,0
else:
    j,k = 0,0

N = len(df.columns)
if N%3 == 0:
    n = N//3
else:
    n = np.floor(N/3)+1

plt.rcParams['axes.titlesize'] =  'xx-large'
plt.rcParams['font.size'] = 18
plt.rcParams['text.usetex'] = False
axes=df.hist(figsize=(12,9),bins=50,layout=(n,3),histtype="step",density=True)
#if checks_passed:
axes[j,k].axvline(x={chirpmass_min}, ls="--", color="r")
axes[j,k].axvline(x={chirpmass_max}, ls="--", color="r")
_ = axes[j,k].set_xlim(0.95 * {chirpmass_min},1.05 * {chirpmass_max})
if {q_min} is not None:
    axes[0,2].axvline(x={q_min}, ls="--", color="r")
    _ = axes[0,2].set_xlim(0.95 * {q_min},df[r"$q$"].max())
plt.subplots_adjust(hspace=0.35)
"""
    text = f"Plot of selected posterior parameters. **All masses are in the detector frame**.  The red dashed lines show the proposed $\\mathcal{{M}}$ bounds,[{np.round(chirpmass_min,4)},{np.round(chirpmass_max,4)}]"
    nb.add_cell(text, markdown=True)
    nb.add_cell(cell, code=True)

    # MECO frequency check
    cell = f"""
import lalsimulation as LS

def MECO_freq(m_total, q, chi1z, chi2z):
    eta = q / (1.0 + q) ** 2
    fmeco_tmp = LS.SimIMRPhenomXfMECO(eta, chi1z, chi2z)
    fmeco = LS.SimIMRPhenomXUtilsMftoHz(fmeco_tmp, m_total)
    return fmeco

f_ref_input = {args.f_ref}
f_ref = {f_ref}
f_MECOs = np.array([
        MECO_freq(mt, 1 / qp, s1z, s2z)
        for mt, qp, s1z, s2z in list(zip(mtot, q, chi1z, chi2z))
    ])
plt.figure(figsize=(8,6))
plt.hist(f_MECOs,bins=50,histtype="step",density=True)
plt.axvline(f_ref_input,ls="--",color="r")
plt.axvline(f_ref,ls="--",color="g")
plt.xlabel(r"$f_{{\\rm MECO}}$ (Hz)")
_ = plt.ylabel(r"Probability density")
"""
    nb.add_cell(
        "## MECO frequency check\n The reference frequency is shown as a dashed green vertical line. If the reference frequency has been modified by the MECO test, the input value appears in red and the new value in green.",
        markdown=True,
    )
    # Automatic MECO check result
    # Exclude everything but f_ref
    exclusion = list(set(checks.keys())-set(["f_ref"]))
    checks_table = markdown_table_writer_checks(
        checks, exclude=exclusion, recommendations=recommendations,
        detchar_checks=detchar_checks
    )
    nb.add_cell(checks_table, markdown=True)
    nb.add_cell(cell, code=True)

    # NRSur7Dq4 check
    nrsur_cell = f"""
from peconfigurator.auxiliary.plotting import plot_nrsur_constraints

fig = plot_nrsur_constraints(
    chirpmass_min={chirpmass_min},
    chirpmass_max={chirpmass_max},
    q_min={q_min},
    posterior_samples=posterior_samples,
)
plt.show()
"""
    # Add NRSur7Dq4 only if q_min is defined
    if q_min is not None:
        nb.add_cell(
            (
                "## NRSur7Dq4 constraints check\n"
                "The solid blue line shows the proposed prior bounds. "
                "The dashed orange line shows the constraints on the mass space "
                "if using NRSur7Dq4."
            ),
            markdown=True
        )
        nb.add_cell(nrsur_cell, code=True)

    # The suggested settings
    nb.add_cell("## Recommended settings", markdown=True)
    if detchar_checks["consistent_seglen"] is False:
        extra_text = "<font color='red'>Detchar recommended segment length is more restrictive than posterior-based recommended segment length. Recommended segment length has been overridden to detchar recommendation.</font>"
        nb.add_cell(extra_text, markdown=True)
    settings = markdown_table_writer_settings(recommended_settings)
    nb.add_cell(settings, markdown=True)

    # Additional info
    script_version = version('pe-configurator')
    date = datetime.datetime.now()
    complete_args = str(args)
    extra = markdown_table_writer_extra(date, script_version, complete_args)
    nb.add_cell("## Extra information", markdown=True)
    nb.add_cell(extra, markdown=True)
    nb.write(filename=filename, outdir=outdir)
