# twoprecessingspins

Data release supporting 

- _Characterization of merging black holes with two precessing spins_. Viola De Renzis, Davide Gerosa, Geraint Pratten, Patricia Schmidt, Matthew Mould.

## Credits

You are welcome to use this database in your research. We kindly ask you to cite our above mentioned paper. In order to cite the database specifically, the DOI code is:


## Database

Here we provide our data to reproduce _Fig.2_, _Fig.4_, _Fig.5_, _Fig.6_ and _Fig.7_ of the paper.
The database's size is ~30GB, and needs to be downloaded in chunks from the GitHub release page (https://github.com/ViolaDeRenzis/twoprecessingspins/releases). 

The database contains two types of files. 

1) The _result.json_ files are the BILBY outputs (see https://lscsoft.docs.ligo.org/bilby/bilby-output.html to discover their content and how to read them). Every _.json_ file is a nested set of dictionaries that contains all the information for each simulation (injected values, waveform arguments, priors, posteriors, log evidence ecc...). In particular you can find here the posterior samples for each of the 15 injected parameters.
2) The _chipav.dat_ files are the posterior samples for the **averaged** definition of the precessing spin parameter $\chi_{p}$. The samples for the  **heuristic** definition of $\chi_{p}$, instead, are contained in the _.json_ files.

In order to reproduce _Fig.2_ of the paper you'll need to use the files with prefixes **DL_0200,DL_0500,DL_0700,DL_0900,DL_01300,DL_01700**. Here DL stands for luminosity distance.

The 100 injections in _Fig.4_, _Fig.5_ can be reproduced using the files with prefix **uni**. This prefix stands for 'uniform' because we choose the samples for each of the 100 simulation, reweighting the $\chi_{p}$ prior toward a uniform distribution between [0,2].

The red posterior in _Fig.6_ 




