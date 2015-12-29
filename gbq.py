import subprocess,time
try: 
    import ujson as json
except:
    import json
import pandas as pd

'''

This is a simple wrapper around bq.

For it to work, you must first configure the environment for bq using the gcloud tool:

- set the appropriate account: gcloud config set account <account>
- log in: gcloud auth login
- set to the required project: gcloud config set project <full project id, NOT just the number> 

'''

def query(sql,max_rows=100,cast={},index=None):
    t0=time.time()
    args = ['bq','--format=json','query','--max_rows=%i' % max_rows ,sql]
    p=subprocess.Popen(args,stdout=subprocess.PIPE)
    (out,err)=p.communicate()
    if not err:
        for i in out.split('\n'):
            try:
                j=json.loads(i)
                df=pd.DataFrame(j)
                for k,func in cast.items():
                  if k in df.columns:
                    df[k]=df[k].apply(func)
                if index:
                  df.set_index(index,inplace=True)
                print "%i rows in %.2f seconds" % (len(df),time.time()-t0)
                return df

            except Exception,e:
                print i
    else:
        print err