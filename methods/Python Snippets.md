```
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
import pylab as plt
import seaborn as sns

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