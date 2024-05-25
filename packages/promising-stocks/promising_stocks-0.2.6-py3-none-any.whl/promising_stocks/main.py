import pandas_datareader.stooq as pdr
from pandas_datareader import data
from datetime import datetime

class PromisingStocks:
    def stooq(self, s_code, st_y, st_m, st_d, ed_y, ed_m, ed_d):
        st_da = datetime(st_y, st_m, st_d)
        ed_da = datetime(ed_y, ed_m, ed_d)
        return pdr.StooqDailyReader(s_code + '.JP',start=st_da,end=ed_da).read()