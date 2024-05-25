from pandas_datareader import data

class PromisingStocks:

    def stooq(self, s_code):
        return data.DataReader(s_code + '.JP', 'stooq')
