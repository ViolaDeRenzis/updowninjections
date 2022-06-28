# twoprecessingspins

Data release supporting:

- _Characterization of merging black holes with two precessing spins_. Viola De Renzis, Davide Gerosa, Geraint Pratten, Patricia Schmidt, Matthew Mould.

## Credits

You are welcome to use this dataset in your research. We kindly ask you to cite the paper above. If you want to cite this data release specifically, the DOI code is:


## Data

Data need to be downloaded from the GitHub release page (https://github.com/ViolaDeRenzis/twoprecessingspins/releases). The total size is ~30GB,

We provide to data products, named `*_result.json` and `*_chipav.dat`. 

- The `result.json` files are the raw BILBY outputs (see [https://lscsoft.docs.ligo.org/bilby/bilby-output.html](lscsoft.docs.ligo.org/bilby/bilby-output) for instructions). Each of these files contains a nested set of dictionaries with all the information of the injection (true values, waveform arguments, priors, posteriors, log evidence etc...). 
- The `chipav.dat` files contain the posterior samples of the averaged $\chi_{p}$ estimators. The samples for the  **heuristic** definition of $\chi_{p}$  are provided by default and can be found in `result.json`.

## Readme

The data provided refer to the results of the paper as follows:

- Data to reproduce Fig. 2 and Fig. 3 of the paper are listed as `DL_XXXX` where `DL` stands for *luminosity distance* and `XXXX` refers to the value in Mpc.

- The 100 injections used in Fig. 4 and Fig. 5 are listed as `uni_XX` where `XX` ranges from 00 to 99. Injections are sorted in in ascendig order of $\chi_{p}$. The prefix `uni` stands for *uniform* because of our targeted $\chi_{p}$ distribution. For all these runs, injection and recovery are done with the *IMRPhenomXPHM* waveform models using the standard uninformative priors (see the paper).

- In Fig.6, the red posteriors correspond to the injections labeled `uni_XX` from above with `XX`=[25,98]. The green posteriors are performed using volumetric priors and can be reproduced using files starting with `prior_XX`. The yellow posteriors are done at higher SNR value and are provided as `prior_XX_SNR_YY`. 

- In Fig. 7, the posteriors obtained injecting and recovering with *IMRPhenomXPHM* are the ones are those labeled `uni_XX` with `XX`=[21,81]. The other runs obtained with different combination of `IMRPhenomXPHM`, `IMRPhenomTPHM` and `NRSur7dq4` (shortened respectively as XP, TP and NR) can be reproduced using files named ``syst_XX_WINJ_WREC** where `WINJ` and `WREC` indicate the waveform model used in injection and recovery, respectively.



