#!/usr/bin/env python
# coding=utf-8

import tushare

print(tushare.__version__)
token="fad44a75ef72bc004fd64fa3f22ff383dc9d7bc5b6f729493dcdca57"
print("tushare token : {}".format(token))

# 设置token
tushare.set_token(token)

# 初始化pro接口
pro=tushare.pro_api()

# --- 数据调取 ---

# (1) 获取交易日历信息
# df = pro.trade_cal(exchange='', start_date='20220101', end_date='20220301', fields='exchange,cal_date,is_open,pretrade_date', is_open='1')
df=pro.query('trade_cal',exchange="",start_date='20220101', end_date='20220201', fields='exchange,cal_date,is_open,pretrade_date')
# print(df)

# (2) 获取日线行情
df=pro.daily(trade_date="20220116",ts_code="300353.SZ")
# print(df)

# (3) IPO新股列表
df=pro.new_share(start_date="20220116",end_date="20220118")
# print(df)

# (4) 上市公司基本信息
# df=pro.stock_company(exchange='SSE',ts_code='601818.SH',fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
df=pro.stock_company(exchange='SZSE',ts_code='000001.SZ',fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
print(df)
