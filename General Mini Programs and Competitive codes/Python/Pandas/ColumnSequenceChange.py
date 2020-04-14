import pandas as pd
import numpy as np

ff={'a':[ 1, 4, 3,4,5],'b':[4, 5, 6,7,8],'c':[7,8,9,0,1]}
df=pd.DataFrame(ff)
df.columns=['Col1','Col2','Col3']
df=df[['Col2','Col1','Col3']]
print(df)