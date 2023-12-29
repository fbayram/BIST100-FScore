from utils import Utils as utils

symbols =[
        'TUPRS','ADEL','KCHOL',
        'HEKTS','PNLSN','ECILC',
        'SISE','DOAS','ALARK',
        'THYAO','SAHOL','EKGYO',
        'ASTOR','ULKER','TARKM',
        'BASGZ','SAHOL','KONTR',
        'VESTL','SASA','TKFEN',
        'MGROS','BIMAS','EREGL']
        
year_periods = [
 [2023,9],
 [2023,6],
 [2023,3],
 [2023,12]
]

all_scores = utils.getScores(symbols,year_periods)

graph_data = utils.getGraphData(all_scores)

utils.showFScoreGraph(graph_data)




