import numpy as np
import pandas as pd
import time
import pyarrow.feather as feather


np.random.seed = 42
df_size = 10

df = pd.DataFrame({
    'a': np.random.rand(df_size),
    'b': np.random.rand(df_size),
    'c': np.random.rand(df_size),
    'd': np.random.rand(df_size),
    'e': np.random.rand(df_size)
})


# # save
t1 = time.time()
df.to_feather('test.fea')
t2 = time.time()
df.to_csv('test.csv')
t3 = time.time()
feather.write_feather(df, 'test2.fea')
t4 = time.time()
feather.write_feather(df, 'test3.fea', version=1)

print(f'保存test.fea耗时{t2-t1}')
print(f'保存test.csv耗时{t3-t2}')
print(f'保存test2.fea耗时{t4-t3}')


# read
t1 = time.time()
pd.read_feather('test.fea')
t2 = time.time()
pd.read_csv('test.csv')
t3 = time.time()
feather.read_feather('test2.fea')
t4 = time.time()
feather.read_feather('test3.fea')
t5 = time.time()


print(f'读取test.fea耗时{t2-t1}')
print(f'读取test.csv耗时{t3-t2}')
print(f'读取test2.fea耗时{t4-t3}')
print(f'读取test3.fea耗时{t5-t4}')


# feather
