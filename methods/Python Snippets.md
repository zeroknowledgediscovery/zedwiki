# Writing Latex Tables from Pandas

```
import pandas as pd
import numpy as np
DUMMY=False
STRA='L{1in}|L{1.25in}|L{1.25in}|L{1.5in}|L{.3in}|L{.3in}'

def texTable(df,tabname='tmp.tex',FORMAT='%1.2f',INDEX=True,DUMMY=DUMMY,USE_l=False):
    '''
        write latex table
    '''
    if DUMMY:
        return
    if INDEX:
        df=df.reset_index()
    columns=df.columns
    df.columns=[x.replace('_','\\_') for x in columns]
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col]=df[col].str.replace('_','\\_')
    
    if USE_l:
        TABFORMAT='l'*len(df.columns)
    else:
        TABFORMAT='L{1in}|'*len(df.columns)
        TABFORMAT=TABFORMAT[:-1]
    STR='\\begin{tabular}{'+TABFORMAT+'}\n'        
    with open(tabname,'w') as f:
        f.write(STR)
    df.to_csv(tabname,float_format=FORMAT,
              line_terminator='\\\\\\hline\n',
              sep='&',quotechar=' ',index=None,mode='a')
    
    with open(tabname,'a') as f:
        f.write('\\end{tabular}\n')
```

# Saving Publication Quality Figures from Matplotlib

```
def saveFIG(filename='tmp.pdf',AXIS=False):
    '''
        save fig for publication
    '''
    import pylab as plt
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
    plt.margins(0,0)
    if not AXIS:
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig(filename,dpi=300, bbox_inches = 'tight',
                pad_inches = 0,transparent=True) 
    return
```

# ICD CODE LOOKUP

```
#!/usr/bin/python
import os
import sys
sys.path.append('../../../../pycode/')
from tqdm import tqdm

import pandas as pd
import numpy as np
import glob
import pylab as plt
import subprocess
import urllib
import json
import tempfile
import argparse
from argparse import RawTextHelpFormatter
import re

DUMMY=False
STRA='L{1in}|L{1.25in}|L{1.25in}|L{1.5in}|L{.3in}|L{.3in}'

def texTable(df,tabname='tmp.tex',FORMAT='%1.2f',INDEX=True,DUMMY=DUMMY,USE_l=False):
    '''
        write latex table
    '''
    if DUMMY:
        return
    if INDEX:
        df=df.reset_index()
    columns=df.columns
    df.columns=[str(x).replace('_','\\_') for x in columns]
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col]=df[col].str.replace('_','\\_')
    
    if USE_l:
        TABFORMAT='l'*len(df.columns)
    else:
        TABFORMAT='L{1in}|'*len(df.columns)
        TABFORMAT=TABFORMAT[:-1]
    STR='\\begin{tabular}{'+TABFORMAT+'}\n'        
    with open(tabname,'w') as f:
        f.write(STR)
    df.to_csv(tabname,float_format=FORMAT,
              line_terminator='\\\\\\hline\n',
              sep='&',quotechar=' ',index=None,mode='a')
    
    with open(tabname,'a') as f:
        f.write('\\end{tabular}\n')

        
banner='GENERATE TABLE OF ICD DESCRIZPTIONS IN LATEX FORMAT BY LOOKING UP NAMES FROM WEB'
zed='copyright 2020 zed.uchicago.edu'
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

ICDDESC='../figfiles/ICD9desc'
NAME_TYPE='short_name'

parser = argparse.ArgumentParser(description='########\n'+banner+'\n'+zed,formatter_class=RawTextHelpFormatter)
parser._optionals.title="Program Options"

parser.add_argument('-list', metavar="", nargs='+',dest='CODELIST',
                    action="store", type=str,
                    default=[],
                    help="code list")
parser.add_argument('-codefile', metavar="",dest='CODEFILE',
                    action="store", type=str,
                    default=None,
                    help="code list file")
parser.add_argument('-pref', metavar="", dest='FILEPREF',
                    action="store", type=str,
                    default='tmp',
                    help="filepref")
parser.add_argument('-nametype', metavar="", dest='NAME_TYPE',
                    action="store", type=str,
                    default='short_name',
                    help="short or long names")
parser.add_argument('-fast', metavar="", dest='FAST',
                    action="store", type=str2bool,
                    default=False,
                    help="fast comp no web lookup of codes")
parser.add_argument('-dictsave', metavar="", dest='SAVE',
                    action="store", type=str2bool,
                    default=False,
                    help="save code dict to avoid future lookups")


 
if len(sys.argv[1:])==0:
    parser.print_help()
    parser.exit()
args=parser.parse_args()

fpref=args.FILEPREF
CODELIST=args.CODELIST
NAME_TYPE=args.NAME_TYPE
CODEFILE=args.CODEFILE
SAVE=args.SAVE

if CODEFILE is not None:
    with open(CODEFILE) as fp:
        CODELIST=CODELIST+fp.readline().split()

CODELIST=list(set(CODELIST))


if not os.path.isfile('ICDCODEDICT_.json'):
    ICDCODEDICT={}
else:
    ICDCODEDICT=json.load(open("ICDCODEDICT_.json"))
    
def getICDdesc(code,NUM_MAX=1):
    names=[]
    if code[0] == 'E':
        code=code.replace(".","")

    if code in ICDCODEDICT.keys():
        return ICDCODEDICT[code]
    
    f = tempfile.NamedTemporaryFile()
    url='https://clinicaltables.nlm.nih.gov/api/icd9cm_dx/v3/search?terms='+code+'&ef='+NAME_TYPE
    urllib.urlretrieve(url, filename=f.name)
    with open(f.name) as json_file:  
        data = json.load(json_file)
    if data[0]>0:
        for i in range(min([NUM_MAX, len(data[2][NAME_TYPE])] )):
            names=np.append(names,str(data[2][NAME_TYPE][i]).strip())
    f.close()
    if len(names) > 0:
        if NUM_MAX == 1:
            names=names[0].replace('&','\&').replace('<','less')
    else:
        names=None

    ICDCODEDICT[code]=names
    return names

codeDICT={str(code):getICDdesc(code) for code in tqdm(CODELIST)}
df=pd.DataFrame.from_dict(codeDICT,orient='index')
df.columns=['description']
df.index.name='code'
df.to_csv(fpref+'.csv')
texTable(df,tabname=fpref+'.tex')
if SAVE:
    json.dump(codeDICT, open( "ICDCODEDICT_.json", 'w' ) )
```


