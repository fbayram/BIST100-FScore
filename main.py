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

all_scores = utils.getScores(symbols,2023,[9,6,3,12])

graph_data = utils.getGraphData(all_scores)

utils.showFScoreGraph(graph_data)


