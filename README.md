# twoprecessingspins

Data release supporting 

- _Characterization of merging black holes with two precessing spins_. Viola De Renzis, Davide Gerosa, Geraint Pratten, Patricia Schmidt, Matthew Mould.

## Credits

You are welcome to use this database in your research. We kindly ask you to cite our above mentioned paper. In order to cite the database specifically, the DOI code is:


## Database

Here we provide our data to reproduce _Fig.2_, _Fig.4_, _Fig.5_, _Fig.6_ and _Fig.7_ of the paper.
The database's size is ~30GB, and needs to be downloaded in chunks from the GitHub release page. 

The database contains two types of files. 

1) The _.json_ files are the BILBY outputs (see https://lscsoft.docs.ligo.org/bilby/bilby-output.html to discover their content and how to read them). Every _.json_ file is a nested set of dictionaries that contains all the information for each simulation (injected values, waveform arguments, priors, posteriors, log evidence ecc...). In particular you can find here the posterior samples for each of the 15 injected parameters.
2) The _.dat_ files are the posterior samples for the *averaged* definition of $\chi_{p}$


