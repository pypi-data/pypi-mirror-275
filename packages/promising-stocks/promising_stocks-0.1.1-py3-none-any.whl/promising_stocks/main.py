# ライブラリのインポート
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import pandas_datareader.stooq as pdr
from pandas_datareader import data
import matplotlib.pyplot as plt
%matplotlib inline

def stooq(s_code):
  return data.DataReader(s_code + '.JP', 'stooq')