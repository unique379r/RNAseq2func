#!/bin/bash


# This file is part of RNAseq2func project.

# MIT License

# Copyright (c) 2022 unique379r

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# author: Rupesh Kesharwani <bioinrupesh2009 DOT au AT gmail DOT com>

#clear


# This file is part of RNAseq2func.

## some warnings before to start
echo -e "\n"
echo -e "\t\t\t\t#### Welcome to the installation of third-party software for RNAseq2func pipeline use ####"
echo -e "\t\t\t\t\t\t\t#### Before to Run this script ####"
echo -e "\n"
echo -e "#Make sure internet connection works properly in your privileges."
echo -e "# bash ./RNAseq2func_setup.sh"
echo -n "Continue ? (y/n) : "
read ans
if [[ "${ans}" != "y" ]] && [[ "${ans}" != "Y" ]]; then
	echo -e "\n"
	clear
	echo -e "#Please note that without tool packages, the pipeline RNAseq2func may not work for you !!"
	echo -e "\n^^^^^^^^^^^^^^^^^^^^^^^^^^BYE-BYE^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
	exit 0;
fi


#########################
#### Install Programs ###
#########################
#clear
echo -e "checking if RNAseq2func_env is already present...."
if hash conda >/dev/null 2>&1; then
	ENV=$(conda info --envs | grep ^RNAseq2func_env | awk '{print $1}')
	if [[ $ENV == "RNAseq2func_env" ]]; then
		echo -e "\n#The RNAseq2func virtual environment (i.e. RNAseq2func_env) has already been created/present, and packages should installed there as well"
		exit 1;
	fi
else
	echo -e "#conda/miniconda appears to have NOT installed ! please install it to continue.."
	exit 1;
fi

if hash conda >/dev/null 2>&1; then
	echo -e "#conda appears to have already installed !"
	echo -e "#attempting to make a conda env and install required packages.."
	conda env create -q -f environment.yml
	## reload terminal
	#source ~/.bashrc
	#source ~/.bash_profile
	echo -e "#Installation done, please restart the terminal."
	exit;
else
	clear
	echo -e "#conda/miniconda appears to have NOT installed ! please install it to continue.."
	exit 1;
fi

################ End of the Installation ###################
## reload terminal
#source ~/.bashrc
#source ~/.bash_profile
#clear
#exec bash --login


