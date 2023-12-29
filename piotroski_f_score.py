from enum import Enum

class codes(Enum):
  net_income = '2OCF'
  total_assets = '1BL'
  long_term_debt = '2BA'
  current_assets = '1A'
  current_liabilities = '2A'
  operating_cash_flow = '4C'
  common_stock = '2O'
  gross_profit = '3CAB'
  total_revenue = '3C'

class FScore: 
  def piotroski_f_score(data):
    # Initialize the score to 0
    score = 0

    # Create a dictionary to store the results for each criterion
    results = {
        'Net Income': False,
        'return_on_assets': False,
        'CFO': False,
        'CFO > Net Income': False,
        'Long Term Debt Decreased': False,
        'Current Ratio Increased': False,
        'No New Shares Issued': False,
        'Gross Margin Increased': False,
        'Asset Turnover Ratio Increased': False
    }

    if Functions.net_income(data) > 0:
        results['Net Income'] = True
        score +=1

    if Functions.return_on_assets(data) > 0:
        results['return_on_assets'] = True
        score +=1

    if Functions.operating_cash_flow(data) > 0:
       results['CFO'] = True
       score +=1

    if Functions.operating_cash_flow(data) > Functions.net_income(data):
        results['CFO > Net Income'] = True
        score +=1

    if Functions.long_term_debt(data) > 0:
        results['Long Term Debt Decreased'] = True
        score +=1

    if Functions.current_ratio(data) > 0:
        results['Current Ratio Increased'] = True
        score +=1

    if Functions.new_shares(data) < 1:
        results['No New Shares Issued'] = True
        score +=1


    if Functions.gross_margin(data) > 0:
       results['Gross Margin Increased'] = True
       score +=1


    if Functions.asset_turnover_ratio(data) > 0:
       results['Asset Turnover Ratio Increased'] = True
       score +=1

    return score, results

 #----------------------------------------------------------------------------

class Functions:
  def getCodeValue(data,code):
    return list(filter(lambda data: data['itemCode'] == code, data))[0]

  def net_income(data):
    return int(Functions.getCodeValue(data,codes.net_income.value)["value1"])

  def return_on_assets(data):
    roa = Functions.getCodeValue(data,codes.total_assets.value)
    avg = (int(roa["value1"]) + int(roa["value2"])) / 2
    return Functions.net_income(data) / avg

  def long_term_debt(data):
   data = Functions.getCodeValue(data,codes.long_term_debt.value)
   return int(data["value2"]) - int(data["value1"])

  def operating_cash_flow(data):
   return int(Functions.getCodeValue(data,codes.operating_cash_flow.value)["value1"])

  def current_ratio(data):
   current_assets =Functions.getCodeValue(data,codes.current_assets.value)
   current_liabilities = Functions.getCodeValue(data,codes.current_liabilities.value)
   ratio1 = int(current_assets["value1"]) / int(current_liabilities["value1"])
   ratio2 = int(current_assets["value2"]) / int(current_liabilities["value2"]) 
   return ratio1 - ratio2

  def new_shares(data):
   current = int(Functions.getCodeValue(data,codes.common_stock.value)["value1"])
   previous = int(Functions.getCodeValue(data,codes.common_stock.value)["value2"])
   return current - previous

  def gross_margin(data):
    gross_profit =Functions.getCodeValue(data,codes.gross_profit.value)
    total_revenue = Functions.getCodeValue(data,codes.common_stock.value)
    current = (int(gross_profit["value1"]) ) / int(total_revenue["value1"])
    previous = int(gross_profit["value2"]) / int(total_revenue["value2"])
    return current - previous

  def asset_turnover_ratio(data):
    total_assets = Functions.getCodeValue(data,codes.total_assets.value)
    total_revenue = Functions.getCodeValue(data,codes.common_stock.value)
    avg_assets1 = (int(total_assets["value1"]) + int(total_assets["value2"])) / 2
    avg_assets2 = (int(total_assets["value2"]) + int(total_assets["value3"])) / 2
    atr1 = int(total_revenue["value1"]) / avg_assets1
    atr2 = int(total_revenue["value2"]) / avg_assets2
    return atr1 - atr2


