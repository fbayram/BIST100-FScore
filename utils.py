import pandas as pd
import matplotlib.pyplot as plt
from piotroski_f_score import FScore as fscore
from client import Client as client



class Utils:
  def getScores(symbols,year,periods):
    result = []
    for symbol in symbols:
      data = client.getDataISYatirim("MaliTablo",{"stock_name":symbol,"year":year,"periods":periods})["value"]
      all_scores = fscore.piotroski_f_score(data)
      result.append({'Score':all_scores[0],'Stock':symbol})

    return result

  def getGraphData(data):
    x_point = []
    y_point = []
    sorted_data = sorted(data, key=lambda x: x['Score'], reverse=True) 
    for d in sorted_data:
     x_point.append(d['Stock'])
     y_point.append(d['Score'])

    result = dict();
    result['x'] = x_point
    result['y'] = y_point
    return result

  def showFScoreGraph(data):
    colors = ['blue' if s in [7, 8, 9] else 'orange' if s in [4, 5, 6] else 'red' for s in data['y']]

    bars = plt.barh(data['x'], data['y'], color=colors, height=0.8)
    plt.ylabel('')
    plt.xlabel('Piotroski F Score')
    plt.title('Piotroski F Scores for Selected Stocks')
    plt.xlim(0, 9)
    plt.show()
