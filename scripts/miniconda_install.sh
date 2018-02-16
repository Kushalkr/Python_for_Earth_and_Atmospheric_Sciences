#!/bin/bash
#set -x


# Installs Miniconda and required basic packages for Earth and Atmospheric Science
#on a macOS machine or Linux Machine
# 
# Author: Kushal Keshavamurthy Raviprakash
#
# Date Created: May 19 2017
# Date Modified: 2nd June 2017
#
# Usage: bash macOSX_install.sh
# or
# chmod +x macOSX_install.sh
# ./ macOSX_install.sh
#
# PS: Please say "YES" when it asks if you want to add Anaconda python to your PATH
# variable.

printf 'what is your OS? [Linux/MacOS]? ' ; read OS

if [ $OS == 'MacOS' ]; then
	ifile=Miniconda3-latest-MacOSX-x86_64.sh
	if ! [ -f $ifile ]; then
		curl -O https://repo.continuum.io/miniconda/$ifile
	else
		check=$(md5 "$ifile" | cut -d' ' -f 4)
		echo $check
		if [ $check != 'e46f4555439134cd41ccb914ba283958' ]; then
			curl -O https://repo.continuum.io/miniconda/$ifile
		fi
	fi

	bash $ifile

	source ~/.bash_profile
elif [ $OS == 'Linux' ]; then
	ifile=Miniconda3-latest-Linux-x86_64.sh
	if ! [ -f $ifile ]; then
		wget -c https://repo.continuum.io/miniconda/$ifile
	else
		check=$(md5 "$ifile" | cut -d' ' -f 4)
		echo $check
		if [ $check != 'fc6fc37479e3e3fcf3f9ba52cae98991' ]; then
			curl -O https://repo.continuum.io/miniconda/$ifile
		fi
	fi

	bash $ifile

	source ~/.bashrc
else
	echo 'Please Enter MacOS or Linux'
	exit 1
fi

if [ $? -ne 0 ]; then
	echo $?
	exit 1
fi

conda update -c conda-forge conda
conda install -c conda-forge numpy scipy numexpr scikit-learn sympy \
pandas matplotlib basemap cartopy netcdf4 hdf5 cython ipython notebook \
nomkl mpi4py spyder xarray

# Remove the unwanted file
printf 'do you want to keep the downloaded miniconda installation file? [y/n] '
read opt

if [ $opt == 'n' ]; then
	rm $ifile
fi

exit 0

