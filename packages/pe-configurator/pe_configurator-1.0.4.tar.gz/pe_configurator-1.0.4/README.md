# Introduction
This package provides scripts that automatically try to determine some settings that must be applied for PE runs, especially for time-domain waveforms.
The settings try to strike a balance between being conservative and being feasible.

### Top-level description
The main script to use is `proc_samples.py`.  Given a preliminary PE run, it will perform some basic checks and then generate recommended PE settings. It can also optionally generate a `json` format result for automatic ingestion by `asimov` and a more detailed standalone, human-readable report. Users are _highly_ encouraged to take a look at the report.

### Usage
Here is a typical usage example:
```
peconfigurator --HM posterior_samples.h5  --dataset C01:IMRPhenomXPHM --json_file test.json --report_file test.pdf
```

For all the available options, please check
```
peconfigurator -h
```

If all goes right, it will print something like
```
Processing....
Estimating seglen based on posterior samples
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10885/10885 [02:22<00:00, 76.48it/s]
Estimating srate based on posterior samples
Using ell = 3 for Nyquist check
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10885/10885 [00:00<00:00, 30557.61it/s]
Estimating f_start based on posterior samples
Done processing

############################## SUMMARY ##############################
Posterior parameters
----------------------------------------
         total mass             q            Mc         chi1z         chi2z            dL
count  10885.000000  10885.000000  10885.000000  10885.000000  10885.000000  10885.000000
mean      93.716478      0.721174     39.633770      0.001211     -0.027717   3628.546845
std        8.950171      0.171014      3.951967      0.261996      0.297189   1048.258790
min       66.155982      0.145312     25.004179     -0.967360     -0.953884   1026.785460
25%       87.516019      0.595916     37.017804     -0.131398     -0.196356   2904.252323
50%       93.068042      0.729647     39.459142      0.005121     -0.012037   3506.855087
75%       99.238665      0.863340     42.139057      0.152395      0.134719   4216.193654
max      124.959332      0.999992     53.957413      0.906870      0.973028   7975.515016
----------------------------------------
Sanity checks
Checking for railing in chirp mass: PASSED
Checking for railing in luminosity distance: PASSED
Checking that f_ref is not above f_MECO: PASSED

++++++++++++++++++++++++++++++ Suggested settings ++++++++++++++++++++++++++++++
Real required srate  753.7701187444659, as power of 2: 1024
Real seglen: 4.046571094240219, with padding+rollon: 6.44657109424022, as power of 2: 8.0
Check from samples:
Real seglen: 0.8090184427276651, with padding+rollon: 3.209018442727665, as power of 2: 4.0
f_start: 13.333333333333334
Real bounds on chirp mass: [25.004179128030085,53.95741304487518], suggested bounds: [20.00334330242407,64.74889565385021]
Real distance max: 8000.0

```

The `test.json` file contains some machine-readable information as shown below:

```json
{
    "srate": 1024,
    "f_start": 13.333333333333334,
    "f_ref": 20.0,
    "seglen": 8.0,
    "chirpmass_min": 20.00334330242407,
    "chirpmass_max": 64.74889565385021,
    "metadata": {
        "date": "2020-11-05 04:38:55.172784",
        "command_line_args": "Namespace(HM=True, bounds_tol=0.2, dataset='C01:IMRPhenomXPHM', ell_max=3, f_ref=20.0, flow=20.0, json_file='test.json', nbins=50, q_min=None, report_file='test.pdf', samples_file='./posterior_samples.h5', tolerance=2.0)"
    }
```

An `html` report will also be generated.

### Running on many events
To run on many events, a separate script, `run_on_many_events.py` is provided. The most important settings to it are the path to the repo containing the superevents (specified via `--repo`) and a json file containing the names of events to run on and the corresponding preferred data set inside the PEsummary metafile (specified via `--run_map`). An example of such a json file is below:
```json
{
    "S150914":"EXP1",
    "S190521":"EXP4"
}
```
Here is an example of calling the script:
```bash
python  run_on_many_events.py --repo ./my_events/ --run_map ../test_run_map.json --json_output --full_reports --output_dir example
```
With these options, a separate directory will be created for each superevent inside the `example` directory. Inside each directory there will be 4 files, corresponding to the raw log (ending in `.log`), the machine readable json file with recommended settings (ending in `.json`), and 2 files corresponding to a more verbose report (ending with `.ipynb` and `.html`). The `html` report is the executed and rendered version of the `ipynb` file, provided for debugging purposes.

Examples can be found in `example` folder.


### Detailed description of internal logic
This section describes the detailed logic used in deciding the various settings.  Many of these settings depend on the masses of the binary and are thus affected by proposed changes to the chirp mass prior which is described below.  For every setting we generate 2 estimates: one coming directly from the samples and a conservative one, which takes into account the wider chirp mass prior. In particular,  the following strategy is adopted:

1. Estimate the quantity of interest from the samples.
2. Pick the most extreme value of the quantity of interest (e.g. max seglen or min $f_{\rm start}$) and find its parameters (mass ratio and spins)
3. Use either the lower or upper proposed chirp mass bounds (as appropriate) and the mass ratio from step 2 to estimate a new total mass
4. Use this total mass along with the other params (as appropriate) to produce a new estimate of the quantity of interest



#### Deciding the chirp mass bounds for the prior
The script suggests a chirp mass prior that is wider than the minimum and maximum chirp masses found in the samples, to guard against the moving around of the posterior due to e.g. using a different waveform model.

The script proposes chirp mass bounds in 2 steps:
1. Given the preliminary PE run, it checks of railing is present in the chirp mass posterior. This process involves a couple of free parameters that control how strict this check is. This is governed by the options `--tolerance` and `nbins`. See `-h` for more details.
2. If no railing is found, the proposed bounds are computed depending on the width of the chirp mass posterior $`\Delta\mathcal{M}=\mathcal{M}_{\rm max}-\mathcal{M}_{\rm min}`$. If the width is greater than $`30M_{\otol}`$, then the proposed bounds are given by $`[(1-f)\mathcal{M}_{\rm min},(1+f)\mathcal{M}_{\rm max}]`$ where $`f`$ is a free parameter, given by the option `--bounds_tol` with the default value of **0.2**. If the width is smaller than $`30M_{\otol}`$, then the bound are given by $`[\mathcal{M}_{\rm min}-f\Delta\mathcal{M},\mathcal{M}_{\rm max}+f\Delta\mathcal{M}f]`$.


#### Deciding the sampling rate
The sampling rate is determined by the requirement that it's high enough to resolve the highest frequency we are interested in. This is generally given by the frequency of the highest $`(\ell,m)`$ mode in the ringdown. This is estimated by using the `SEOBNRv4HM` routines.  The user is given control which $`\ell`$ is used for this Nyquist frequency check via the option `--ell-max`. By default it is set to **3**.  To be precise, the sampling rate is computed as $`2f_{\rm max}`$ and then rounded up to the next power of 2.

#### Deciding the starting frequency
The starting frequency determines the length of the generated waveform. For time-domain family of waveforms there are two considerations that may come into play:
1. The starting frequency (which corresponds to the frequency of the (2,2) mode) has to be such that the desired $`(\ell,m)`$ mode is present at the provided `flow` (which gives the lower bound of the likelihood integral and is an argument supplied by the user, set by default to **20 Hz**). The script uses the PN relation (valid in the inspiral) that $`f_{\ell m}=\frac{m}{2}f_{22}`$ to dermine this. _In principle, this consideration applies to any time-domain waveform, but need not be used for frequency-domain waveforms_
2. The starting frequency is not too close to merger. This is a limitation of the `SEOBNR` time domain waveforms due to the need i) for a long enough inspiral to attach ringdown ii) to generate quasi-circular initial conditions. The script uses the same condition as the waveform model internally to check if the starting frequency is below this frequency limit.

#### Deciding the seglen
The raw segment length is determined by the following formula
$`t = T(1+s)+t_{\rm pad}+t_{\rm rollon}`$, where $`T`$ is an estimate of the duration of the waveform, including inspiral, merger and ringdown; $`s`$ is a safety factor (default value of 0.03), $`t_{\rm pad}`$ is padding (default is 2 seconds) and $`t_{\rm rollon}`$ is the Tukey window roll on duration (default is 0.4 seconds).  The duration $`T`$ is taken to be a function of the 2 component masses $`m_{i}`$, the z-components of the dimensionless spin $`\chi_{i}`$ and of course the low frequency cutoff `flow` and computed using the SEOBNRv4_ROM function.  *Notice that this means explicitly that we only care about the duration of the waveform from `flow` onwards and not from `f_start`*.   Finally the seglen is rounded to the next power of 2.


#### Checking the reference frequency
The reference frequency is an **input** parameter, encoded in the option `--f_ref` with a default value of **20 Hz**. The script then computes the MECO frequency for all the samples, and checks that $`f_{\rm ref}\leq 0.97f_{\rm MECO}`$. If not, a message is printed out and $`f_{\rm ref}`$ is overwritten to be $`0.97f_{\rm MECO}`$ (or $`f_{\rm start}`$ if this is greater).

**Note that the failing of any railing checks and the reference frequency check can be ignored by passing the flag `--override_safeties`.**
