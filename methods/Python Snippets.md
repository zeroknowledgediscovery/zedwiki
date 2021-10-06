# ICD10 API

```
https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?sf=code,name&terms=M35

```

## Getting all infection codes in ICD 10

```
https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?sf=code,name&terms=infect&maxList=716
```
Note: the default maxList is 7

## ear

```
https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?sf=code,name&terms=otiti&maxList=716
```

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

# PMID To BIBTEX

```
#!/usr/bin/python3
# script by Tommy https://www.biostars.org/u/1945/
import requests
import xml.etree.ElementTree as ET
import sys
import calendar

# Parse PubMed IDs from the command line.
pmids = sys.argv[1:]

## Fetch XML data from Entrez.
efetch = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
r = requests.get(
    '{}?db=pubmed&id={}&rettype=abstract'.format(efetch, ','.join(pmids)))
##print(r.text)

## Loop over the PubMed IDs and parse the XML.
root = ET.fromstring(r.text)
for PubmedArticle in root.iter('PubmedArticle'):
    PMID = PubmedArticle.find('./MedlineCitation/PMID')
    ISSN = PubmedArticle.find('./MedlineCitation/Article/Journal/ISSN')
    Volume = PubmedArticle.find('./MedlineCitation/Article/Journal/JournalIssue/Volume')
    Issue = PubmedArticle.find('./MedlineCitation/Article/Journal/JournalIssue/Issue')
    Year = PubmedArticle.find('./MedlineCitation/Article/Journal/JournalIssue/PubDate/Year')
    Month = PubmedArticle.find('./MedlineCitation/Article/Journal/JournalIssue/PubDate/Month')
##    Year = PubmedArticle.find('./MedlineCitation/Article/ArticleDate/Year')
##    Month = PubmedArticle.find('./MedlineCitation/Article/ArticleDate/Month')
    Title = PubmedArticle.find('./MedlineCitation/Article/Journal/Title')
    ArticleTitle = PubmedArticle.find('./MedlineCitation/Article/ArticleTitle')
    MedlinePgn = PubmedArticle.find('./MedlineCitation/Article/Pagination/MedlinePgn')
    Abstract = PubmedArticle.find('./MedlineCitation/Article/Abstract/AbstractText')
    authors = []
    for Author in PubmedArticle.iter('Author'):
        try:
            LastName = Author.find('LastName').text
            ForeName = Author.find('ForeName').text
        except AttributeError:  # e.g. CollectiveName
            continue
        authors.append('{}, {}'.format(LastName, ForeName))
    ## Use InvestigatorList instead of AuthorList
    if len(authors) == 0:
        ## './MedlineCitation/Article/Journal/InvestigatorList'
        for Investigator in PubmedArticle.iter('Investigator'):
            try:
                LastName = Investigator.find('LastName').text
                ForeName = Investigator.find('ForeName').text
            except AttributeError:  # e.g. CollectiveName
                continue
            authors.append('{}, {}'.format(LastName, ForeName))
    if Year is None:
        _ = PubmedArticle.find('./MedlineCitation/Article/Journal/JournalIssue/PubDate/MedlineDate')
        Year = _.text[:4]
        Month = '{:02d}'.format(list(calendar.month_abbr).index(_.text[5:8]))
    else:
        Year = Year.text
        if Month is not None:
            Month = Month.text
    try:
        for _ in (PMID.text, Volume.text, Title.text, ArticleTitle.text, MedlinePgn.text, Abstract.text, ''.join(authors)):
    ##        assert '"' not in _, _
            if _ is None:
                continue
            assert '{' not in _, _
            assert '}' not in _, _
    except AttributeError:
        pass
    ## Print the bibtex formatted output.
    try:
        print('@Article{{{}{}pmid{},'.format(
            authors[0].split(',')[0], Year, PMID.text))
    except IndexError:
        print('IndexError', pmids, file=sys.stderr, flush=True)
    except AttributeError:
        print('AttributeError', pmids, file=sys.stderr, flush=True)
    print(' Author="{}",'.format(' AND '.join(authors)))
    print(' Title={{{}}},'.format(ArticleTitle.text))
    print(' Journal={{{}}},'.format(Title.text))
    print(' Year={{{}}},'.format(Year))
    if Volume is not None:
        print(' Volume={{{}}},'.format(Volume.text))
    if Issue is not None:
        print(' Number={{{}}},'.format(Issue.text))
    if MedlinePgn is not None:
        print(' Pages={{{}}},'.format(MedlinePgn.text))
    if Month is not None:
        print(' Month={{{}}},'.format(Month))
    if Abstract is not None:    
        print(' Abstract={{{}}},'.format(Abstract.text))
    print(' ISSN={{{}}},'.format(ISSN.text))
    print('}')

```

# Fancy Pivot to Latex

```

def chk(val,FLAG=True):
    if FLAG:
        if not isinstance(val, str):
            val=str(val)
            if len(val) > 4:
                return val[:4]
    return val
        


def fancyPivot(df,INDEX=None,COLUMN=None,
               SUBINDEX=None,STRL=None,FLAG=False,
              HFORMAT='\\bf\\sffamily ',
              FONTSMALL='\\fontsize{8}{8}\\selectfont'):
    vI=df[INDEX].value_counts().index.values
    vC=df[COLUMN].value_counts().index.values
    D={}
    for i in vI:
        for c in vC:
            df_=df[(df[INDEX]==i) & (df[COLUMN]==c)].drop([INDEX,COLUMN],axis=1).set_index(SUBINDEX)
            df_.index.name=SUBINDEX
            df_=df_.sort_index()
            D[(i,c)]=df_
            subcols=len(df_.columns)+1
            subrows=len(df_.index.values)+1
    Tcols=len(vC)*subcols+1
    Trows=len(vI)*subrows
    
    STR='\\begin{tabular}{'
    
    if STRL is None:
        STR=STR+'L{1in}||'
        for i in np.arange(len(vC)):
            STR=STR+'L{.7in}'*(subcols)  +'|'
        STR=STR[:-1]+'}'
    else:
        STR=STR+STRL+'}'
        
    S2='\\hline'
    for i in vC:
        S2=S2+'&'+'\multicolumn{'+str(subcols)+'}{c}{'+HFORMAT+FONTSMALL+' '+i+'}'
    S2=S2+'\\\\\\cline{2-'+str((len(df.columns)-2)*2+1)+'}'
    
    for i in vI:
        S2=S2+'\multirow{'+str(subrows)+'}{*}{'+HFORMAT+FONTSMALL+' '+i+'}&'+'\n'
        for c in vC:
            S2=S2+HFORMAT+SUBINDEX+'&'
            for cc in df_.columns:
                S2=S2+HFORMAT+FONTSMALL+' '+cc+'&'
        S2=S2[:-1]+'\\\\\cline{2-'+str((len(df.columns)-2)*2+1)+'}'
        for r in df_.index:
            S2=S2+'\multirow{'+str(subrows)+'}{*}{}&'
            for c in vC:
                S2=S2+r+'&'
                for cc in df_.columns:
                    S2=S2+"{}".format(chk(D[(i,c)].loc[r,cc],FLAG))+'&'
            S2=S2[:-1]+'\\\\'
        S2=S2+'\\hline'
    
    return STR+S2+'\\end{tabular}'
```

## Example use of fancy-pivot

```
BF1.columns=['target problem', 'gender', 'subcohort', 'auc', '\% change']
s=fancyPivot(BF1,INDEX='target problem',COLUMN='gender',SUBINDEX='subcohort',STRL="L{.8in}||L{1in}C{.35in}R{.65in}|L{1in}C{.35in}R{.65in}")

with open("../figfiles/tex/Figures/subcohort.tex", "w") as text_file:
    text_file.write("%s" % s)
```
