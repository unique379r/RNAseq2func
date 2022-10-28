# RNAseq2func
A comprehensive RNA analysis from sequence to function and pathway reporting.


<p align="center">
  <img width="400" alt="RNAseq2func_logo" src="https://raw.githubusercontent.com/unique379r/RNAseq2func/main/images/RNAseq2func_logo.png">
</p>


## Introduction

## Workflow

## Quick start

### 1.1 Install Miniconda if not already installed.

`Download Miniconda installer from here: https://docs.conda.io/en/latest/miniconda.html and Install it.`

### 1.2 Install 3rt party tools to run RNAseq2func workflow.

  - python=>3.6.7
  - R=>3.6.0
  - scipy
  - seaborn
  - pandas
  - numpy
  - matplotlib
  - fastqc=>0.11.9
  - samtools=>1.16.1
  - star=>2.7.10a
  - picard=>2.27.4
  - trim-galore=>0.6.7
  - samstats=>0.2.2
  - rsem=>1.3.3
  - subread=>2.0.1
  - multiqc=>1.13
  - bwa=>0.7.17
  - qualimap=>2.2.2d
  - bbmap=>39.01
  - rna-seqc=1.1.8

```
git clone git@github.com:unique379r/RNAseq2func.git
cd RNAseq2fun
bash setup/RNAseq2func_setup.sh
```


### 1.3 Activate the environment

```
conda activate RNAseq2func_env
```


## 1.4 Run the pipeline (RNAseq2func)

```
Snamkemake / Python wrapper
```

### 1.5 deactivate the environment

```
Conda deactivate
```

## Lazy mode

### Install a Docker if not already installed.

```
Download and install docker https://docs.docker.com/engine/install/
```

### Build a docker container 

```
docker container run --name=RNAseq2func -it unique379r/RNAseq2func
```

### Run RNAseq2func

```
Snamkemake / Python wrapper
```

## Tutorial

## Cite


