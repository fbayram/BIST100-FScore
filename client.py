import bs4 as bs
import urllib.request
import json
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',10)

class Client:
  def getDataYFinance(stock_name):
   stock = yf.Ticker(stock_name + '.IS')
   return {
      'financials': stock.financials,
      'balance_sheet': stock.balance_sheet,
       'cash_flow': stock.cash_flow
    }
  def getDataISYatirim(req,args):
    base_uri = "https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common"
    
    last_year = args["year"]
    
    if args["periods"][3] == 12: last_year = last_year - 1

    if req == "MaliTablo":
        query = "/Data.aspx/MaliTablo?companyCode={}&exchange=TRY&financialGroup=XI_29&year1={}&period1={}&year2={}&period2={}&year3={}&period3={}&year4={}&period4={}&_=1703768818811"
        query = query.format(args["stock_name"],args["year"],args["periods"][0],args["year"],args["periods"][1],args["year"],args["periods"][2],last_year,args["periods"][3])
        return json.loads(urllib.request.urlopen(base_uri + query).read())
    elif req == "ChartData":
        query = "/ChartData.aspx/IndexHistoricalAll?period=60&from={}&to={}&endeks={}.E.BIST"
        query = query.format(args["start_date"],args["end_date"],args["stock_name"])
        return json.loads(urllib.request.urlopen(base_uri + query).read())
