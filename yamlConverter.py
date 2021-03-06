"""

Project: FTIRDB
File: yamlConverter.py

Function: 

This program is released under the GNU Public Licence (GPL V3)

--------------------------------------------------------------------------
Description:

Script called from command line with name and location of yaml file will convert yaml to tsv file


Example 
============


"""







import csv
import pandas as pd
import os
import yaml
import pathlib
import path
import time
import sys

#need to consider checking the file input is the correct format
#need to create tests 

start = time.process_time()

seq = sys.argv[1]

dirname = os.path.dirname(os.path.abspath(__file__))
test = os.path.join(dirname,'partis1g2t.yaml')

def openYaml(sequence):
    with open (sequence, 'r') as f:
        doc = yaml.safe_load(f)
    return(doc)

def extractRequired(yamlFile):
    fieldNames = ['v', 'd', 'j']
    dirname = os.path.dirname(os.path.abspath(__file__))
    txt = yamlFile["germline-info"]["seqs"]
    requiredFields = {}
    for field in fieldNames:
        v = list(txt[field].values())
        k = field
        requiredFields[k]=v
    
    cdr3 = yamlFile["events"][0]["cdr3_seqs"]
    requiredFields['cdr3'] = cdr3
    fieldNames.append('cdr3')
    tsvfilename = os.path.join(dirname, 'TSVFile.tsv')

    df = pd.DataFrame(requiredFields)
    df.to_csv(tsvfilename, sep='\t', index=False, header=fieldNames, encoding='utf-8')
    return('saved at:  ' + str(dirname))

yaml = openYaml(seq)
savedFile = extractRequired(yaml)
print(savedFile)
print(time.process_time()-start)
