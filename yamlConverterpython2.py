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







from __future__ import with_statement
from __future__ import absolute_import
import csv
import pandas as pd
import os
import yaml
import pathlib
import path
import time
import sys
from io import open

#need to consider checking the file input is the correct format
#need to create tests 

#start = time.process_time()

seq = sys.argv[1]

dirname = os.path.dirname(os.path.abspath(__file__))
test = os.path.join(dirname,u'partis1g2t.yaml')

def openYaml(sequence):
    with open (sequence, u'r') as f:
        doc = yaml.safe_load(f)
    return(doc)

def extractRequired(yamlFile):
    fieldNames = ['v', 'd', 'j']
    dirname = os.path.dirname(os.path.abspath(__file__))
    txt = yamlFile[u"germline-info"][u"seqs"]
    requiredFields = {}
    for field in fieldNames:
        gene = list(txt[field].keys())
        sequence = list(txt[field].values())
        columnname = field
        requiredFields[columnname]=[gene + sequence]
    
    cdr3 = yamlFile[u"events"][0][u"cdr3_seqs"]
    requiredFields[u'cdr3'] = cdr3
    fieldNames.append(u'cdr3')
    tsvfilename = os.path.join(dirname, 'TSVFile2.tsv')

    df = pd.DataFrame(requiredFields)
    df.to_csv(tsvfilename, sep='\t', index=False, header=fieldNames, encoding=u'utf-8')
    return('saved at:  ' + unicode(dirname))

yaml = openYaml(seq)
savedFile = extractRequired(yaml)
print savedFile

