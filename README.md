# Parklab_nchem_NCM_code

The code is used to calculate the average TEM intensity of NCM precursor.

This directory contains python code and example raw data files presented in Figure 1.
The raw data of TEM image should be prepared in txt. format file which contains intensity at each pixel as matrix and one can simply convert format of file from dm3 to txt in DigitalMicrograph software.

This code requires installation of numpy and matplotlib as libraries. 

One can run the code by simply enter the path of raw data file at line 13 and it will return the average intensity of particle.
// input.append(np.loadtxt("(path)", dtype='f')) 
