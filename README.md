# twoprecessingspins

Data release supporting 

- _Characterization of merging black holes with two precessing spins_. Viola De Renzis, Davide Gerosa, Geraint Pratten, Patricia Schmidt, Matthew Mould.

## Credits

You are welcome to use this database in your research. We kindly ask you to cite our above mentioned paper. In order to cite the database specifically, the DOI code is:


## Database

Here we provide our data to reproduce _Fig.2_, _Fig.4_, _Fig.5_, _Fig.6_ and _Fig.7_ of the paper.
The database's size is ~30GB, and needs to be downloaded in chunks from the GitHub release page (https://github.com/ViolaDeRenzis/twoprecessingspins/releases). 

The database contains two types of files, described by the two suffix _result.json_ and _chipav.dat_. 

1) The _result.json_ files are the BILBY outputs (see https://lscsoft.docs.ligo.org/bilby/bilby-output.html to discover their content and how to read them). Every _result.json_ file is a nested set of dictionaries that contains all the information for each simulation (injected values, waveform arguments, priors, posteriors, log evidence ecc...). In particular you can find here the posterior samples for each of the 15 injected parameters.
2) The _chipav.dat_ files are the posterior samples for the **averaged** definition of the precessing spin parameter $\chi_{p}$. The samples for the  **heuristic** definition of $\chi_{p}$, instead, are contained in the _result.json_ files.

In order to reproduce _Fig.2_ of the paper you'll need to use the files with prefixes **DL_0200,DL_0500,DL_0700,DL_0900,DL_01300,DL_01700**. Here DL stands for luminosity distance.

The 100 injections in _Fig.4_ and _Fig.5_ can be reproduced using the files with prefix **uni_#number**. Here #number can be a value from 00 to 99 that indicate the injection number in ascendig order of $\chi_{p}$ magnitude. This prefix **uni** stands for 'uniform' because we chose the samples for each of the 100 simulation, reweighting the $\chi_{p}$ prior toward a uniform distribution between [0,2]. The injection and recovery for these 100 simulations are done with the _IMRPhenomXPHM_ waveform, using the standard uninformative priors. 

In _Fig.6_ , the red posteriors in the left and right panels correspond, respectively, to the injections **uni_25** and **uni_98** performed with the standard LIGO priors. The green posteriors are performed using volumetric priors and can be reproduced using the files with prefix **prior_#number_vol**. The yellow posteriors are done increasing the SNR value with the standard LIGO priors and can be reproduced through the files with prefix **prior_#number_SNR_#snr value**.

Finally _Fig.7_ is done with using the injections number 21 and 81. The posteriors obtained injecting and recovering with _IMRPhenomXPHM_ are the ones with prefix **uni_#number_**. The other posteriors performed with different combination of _IMRPhenomXPHM_,_IMRPhenomTPHM_ and _NRSur7dq4_ (shortened respectively as XP, TP and NR) can be reproduced using the files with prefix **syst_#number_#injection_#recovery**. Here #number can be 21 or 81, #injection and #recovery can be XP,TP or NR and represent the name of the injecting and recovery waveforms.




