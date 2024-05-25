class promising_stocks():

  def stooq(self, s_code):
    return data.DataReader(s_code + '.JP', 'stooq')