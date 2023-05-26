# updowninjections

Data release supporting:

- _Parameter estimation of binary black holes in the endpoint of the up-down instability_. Viola De Renzis, Davide Gerosa, Matthew Mould, Riccardo Buscicchio, Lorenzo Zanga. [arXiv:2304.13063](https://arxiv.org/abs/2304.13063).

## Credits

You are welcome to use this dataset in your research. We kindly ask you to cite the paper above. If you want to cite this data release specifically, the DOI code is: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6777952.svg)](https://doi.org/10.5281/zenodo.6777952).


## Data

Data need to be downloaded from the [github release page](https://github.com/ViolaDeRenzis/updowninjections/releases). The total size is ~35GB. To download the entire dataset use our `download_all.py` script.



We provide data products in `*json` format. The `result.json` files are the raw bilby outputs, see [here](https://lscsoft.docs.ligo.org/bilby/bilby-output.html) for instructions. Each of these files contains a nested set of dictionaries with all the information of the injection (true values, waveform arguments, priors, posteriors, log evidence etc...). 


## Readme

The data provided refer to the results of the paper as follows:

- Data to reproduce Fig. 2 and Fig. 3 of the paper are listed as `ud_rX_SNR_YYY.json` where `ud` stands for *up-down*,`X` ranges from 1 to 8, referring to the 8 series of injections performed with a certain value of the orbital separation `r` and with an `YYY` value of the SNR. The chosen values of the SNR for the 8 series are SNR=150,100,80,60,40,20. The files that reproduce Fig.2 are `ud_r1_SNR_YYY`, which is also reported in Fig. 3 with the orange scatter points.

- The

- The files for the 151 injections used in Fig. 5 of the paper are named as `updown_X_0_result.json`, where `X` ranges between 0 and 150. For all these runs, injection and recovery are done with the IMRPhenomXPHM waveform model using the standard uninformative priors (see the paper).



