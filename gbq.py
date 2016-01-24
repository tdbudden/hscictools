import subprocess,time,sys
import hashlib
import os.path
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


def read_from_cache(sql,cache):
    sqlhash=hashlib.md5(sql).hexdigest()
    os.path.isfile(fname) 

def query_():

    if cache and not dirty:
        pass
        #read the cache
    else:
        pass
        # query gbq
        #

    if cache and (dirty): #or not fileexists!!!:
        pass
        #write the cache

    #convert to df


def to_df_(j,cast,index):
    t0=time.time()
    df=pd.DataFrame(j)
    for k,func in cast.items():
      if k in df.columns:
        try:
          df[k]=df[k].apply(func)
        except Exception, e:
          print "Couldn't cast",k,e
    if index:
      try:
        df.set_index(index,inplace=True)
      except Exception, e:
        print "Couldn't set index",index
    print "%i rows converted to DataFrame in %.2f seconds" % (len(df),time.time()-t0)
    return df


def query(sql,max_rows=100,cast={},index=None,cachedir=None,dirty=False):

    if dirty and cachedir is None:
        print "Need to specify cachedir if dirty flag set"
        return

    if cachedir:
        cachefile=os.path.join(cachedir,hashlib.md5(sql).hexdigest()+'.json')

    if cachedir is None or dirty or not os.path.exists(cachefile):
        t0=time.time()
        args = ['bq','--format=json','query','--max_rows=%i' % max_rows ,sql]
        p=subprocess.Popen(args,stdout=subprocess.PIPE)
        (out,err)=p.communicate()
        if not err:
            t1=time.time()
            print "Big Query returned in %.2f seconds" % (t1-t0)
            sys.stdout.flush()
            for i in out.split('\n'):
                try:
                    j=json.loads(i)
                    df=to_df_(j,cast,index)
                    if cachedir:
                        with open(cachefile,'w') as f:
                            json.dump(j,f)
                    return df
                except Exception,e:
                    print i
        else:
            print err

    else:
        print "Reading cached results from", cachefile
        with open(cachefile,'r') as f:
            j=json.load(f)
            df=to_df_(j,cast,index)
            return df

