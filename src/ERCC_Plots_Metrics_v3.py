#! /usr/bin/env python
'''
@author: Rupesh Kesharwani
@email: rupesh.kesharwani@bcm.org
Copy Rights Reserved (C) 2022
'''
import os
import sys
import argparse
import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt 
plt.switch_backend('agg')
import seaborn as sns 

def ercc_qc (rsem, ercc, sample_name, output_dir):
    ### RSEM results
    print("Reading RSEM input file: " + rsem)
    expr = pd.read_csv(rsem, sep='\t') # rsem result
    ercc_expr = expr.loc[expr.gene_id.str.contains('ERCC-'), ['gene_id', 'TPM', 'FPKM']].rename(columns={'gene_id':'ERCC_ID'}) # select ERCC rows
    # TPM-based ERCC filter
    ercc_expr = ercc_expr[ercc_expr.TPM>0]
    ercc_expr['log2TPM'] = np.log2(ercc_expr['TPM']) # log2 transformation of TPM
    print("Detected ERCC Spike-in (TPM > 0) = " + str (ercc_expr.shape[0]))
    # FPKM-based ERCC filter
    ercc_expr = ercc_expr[ercc_expr.FPKM>0]
    print("Detected ERCC Spike-in (FPKM > 0) = " + str (ercc_expr.shape[0]))
    # log2 transformation of FPKM
    ercc_expr['log2FPKM'] = np.log2(ercc_expr['FPKM'])
    
    ### ERCC analysis file
    print("Reading ERCC input file: " + ercc)
    analysis = pd.read_csv(ercc, sep='\t').rename(columns=lambda x: x.replace(' ','_'))
    analysis['log2ConcMix1'] = np.log2(analysis['concentration_in_Mix_1_(attomoles/ul)'])
    analysis['log2ConcMix2'] = np.log2(analysis['concentration_in_Mix_2_(attomoles/ul)'])
    data = pd.merge(analysis, ercc_expr, how='right', on='ERCC_ID') # merge known conc and TPM

    def metrics(metric_tsv):
        sys.stdout=open(metric_tsv,"w")
        print("R^2\tCorrelation\tNumber of ERCC transcripts identified")
        print(str("%.3f"%r_value**2)+"\t"+str("%.3f"%r_value)+"\t"+str(data.shape[0]))
        # sys.stdout.close()

    def metricsZero(metric_tsv):
        # Mimic output from old pipeline when 0 ERCC transcripts detected
        sys.stdout=open(metric_tsv,"w")
        print("Identified 0 ERCC transcripts, not enough to make plot")
        # sys.stdout.close()

    def corrStats(output_file):
        sys.stdout=open(output_file,"w")
        print("""R value 
        Pearson product-moment correlation coefficient, also known as r, R, or Pearson’s r, a measure of the strength
        and direction of the linear relationship between two variables that is defined as the (sample) covariance of 
        the variables divided by the product of their (sample) standard deviations.""")
        print("Correlation Coefficient (R):\t" + str(r_value))

        print("""\nR squared 
        R square/coefficient of determination is literally the square of correlation between x and y.""")
        print("R-squared:\t" + str(r_value**2))

        print("""\nP value 
        The p-value is a function of the observed sample results (a test statistic) relative to a statistical model, 
        which measures how extreme the observation is.""")
        print("P-value:\t" + str(p_value))

        print("""\nStandard error 
        In regression analysis, the term “standard error” is also used in the phrase standard error of the regression
        to mean the ordinary least squares estimate of the standard deviation of the underlying errors.""")
        print("Standard error:\t" + str(p_value))
        # sys.stdout.close()

    if ercc_expr.shape[0] > 0:
        ### save table
        print("Saving dataframe of ERCC concentrations with TPM and FPKM values: " + sample_name)
        data.to_csv(os.path.join(output_dir, sample_name + ".ERCC-Table.txt"), index=False, sep='\t')

        ### scatter plot for log2CountMix1
        #print("Plotting as SampleName for ERCC mix 1: " + sample_name)
        slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(data["log2ConcMix1"], data["log2TPM"])
        corrStats(str(os.path.join(output_dir,sample_name+".ERCC-Mix1-ScatterStats.txt")))

        fig = plt.figure()
        ax = sns.regplot(x="log2ConcMix1", y="log2TPM", data=data, color = "blue")
        metrics(str(os.path.join(output_dir,sample_name+".ERCC-Mix1-Metrics.tsv")))
        ax.set_title('Correlation Coefficient (R) = ' +  str(round(r_value,2)) + '\n Number of ERCC transcripts identified (N) = ' + str (data.shape[0]))
        plt.savefig(os.path.join(output_dir, sample_name + '.ERCC-Mix1-ScatterPlot.png'))
        plt.close(fig)

        ### scatter plot for log2CountMix2
        #print("Plotting as SampleName for ERCC mix 2: " + sample_name)
        slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(data["log2ConcMix2"], data["log2TPM"])
        corrStats(str(os.path.join(output_dir,sample_name+".ERCC-Mix2-ScatterStats.txt")))

        fig = plt.figure()
        ax = sns.regplot(x="log2ConcMix2", y="log2TPM", data=data)
        metrics(str(os.path.join(output_dir, sample_name+".ERCC-Mix2-Metrics.tsv")))
        ax.set_title('Correlation Coefficient (R) = ' +  str(round(r_value,2)) + '\n Number of ERCC transcripts identified (N) = ' + str (data.shape[0]))
        plt.savefig(os.path.join(output_dir,sample_name + '.ERCC-Mix2-ScatterPlot.png'))
        plt.close(fig)
        #sys.stdout.close()
    else:
        metricsZero(str(os.path.join(output_dir,sample_name+".ERCC-Mix1-Metrics.tsv")))

    return data
    #print("Analysis done.")
def main():
    ### defining input/outout parameters
    parser = argparse.ArgumentParser(description = "RSEM ERCC expression plots and table", formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=40))
    parser.add_argument("-r", "--rsem", required = True, help="full path of RSEM result")
    parser.add_argument("-e", "--ercc", required = True, help="full path of ERCC_Controls_Analysis.txt")
    parser.add_argument("-s","--sample_name", required = True, help="output prefix name")
    parser.add_argument("-o", "--output_dir", required = True, help="output dir path")
    args = parser.parse_args()

    ercc_qc(args.rsem, args.ercc, args.sample_name, args.output_dir)
 
if __name__ == '__main__':
    main()
                                
