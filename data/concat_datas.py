import pandas as pd
file_names_prefix = ['1inchusdt', 'aacusdt', 'aaveusdt', 'abtusdt', 'achusdt', 'actusdt', 'adausdt', 'aeusdt', 'akrousdt', 'algousdt', 'ankrusdt',\
                     'antusdt', 'api3usdt', 'apnusdt', 'arpausdt', 'arusdt', 'astusdt', 'atomusdt', 'atpusdt', 'auctionusdt', 'avaxusdt',\
                    'axsusdt', 'badgerusdt', 'bagsusdt', 'balusdt', 'bandusdt', 'batusdt', 'bchusdt', 'bethusdt', 'bhdusdt', 'bixusdt', 'blzusdt',\
                    'bntusdt', 'boringusdt', 'bsvusdt', 'btcusdt', 'btmusdt', 'btsusdt', 'bttusdt', 'canusdt', 'chrusdt', 'chzusdt',\
                     'ckbusdt', 'cmtusdt', 'cnnsusdt', 'compusdt', 'creusdt', 'crousdt', 'cruusdt', 'crvusdt', 'csprusdt', 'ctsiusdt',\
                     'ctxcusdt', 'cvcusdt', 'cvpusdt', 'dacusdt', 'dashusdt', 'dcrusdt', 'dfusdt', 'dhtusdt', 'dkausdt', 'dockusdt',\
                    'dogeusdt', 'dotusdt', 'dtausdt', 'egtusdt', 'ektusdt', 'elausdt', 'elfusdt', 'emusdt', 'enjusdt', 'eosusdt', 'etcusdt', 'ethusdt',\
                     'fildausdt', 'filusdt', 'firousdt', 'fisusdt', 'flowusdt', 'forthusdt', 'forusdt', 'frontusdt', 'fsnusdt', 'ftiusdt',\
                    'fttusdt', 'glmusdt', 'gnxusdt', 'gofusdt', 'grtusdt', 'gxcusdt', 'hbarusdt', 'hbcusdt', 'hcusdt', 'hitusdt', 'hiveusdt', 'hotusdt',\
                    'hptusdt', 'htusdt', 'icpusdt', 'icxusdt', 'injusdt', 'insurusdt', 'iostusdt', 'iotausdt', 'iotxusdt', 'irisusdt', \
                    'itcusdt', 'jstusdt', 'kanusdt', 'kavausdt', 'kcashusdt', 'ksmusdt', 'kncusdt', 'lambusdt', 'latusdt', 'lbausdt', 'letusdt', 'lhbusdt', 'linausdt',\
                    'linkusdt', 'lolusdt', 'loomusdt', 'lrcusdt', 'ltcusdt', 'lunausdt', 'lxtusdt', 'manausdt', 'maskusdt', 'massusdt',\
                     'maticusdt', 'mdsusdt', 'mdxusdt', 'mirusdt', 'mkrusdt', 'mlnusdt', 'mtausdt', 'mxcusdt', 'mxusdt', 'nanousdt', 'nasusdt',\
                    'nbsusdt', 'nearusdt', 'neousdt', 'nestusdt', 'newusdt', 'nexousdt', 'nftusdt', 'nhbtcusdt', 'nknusdt', 'nodeusdt', 'nsureusdt', 'nulsusdt',\
                     'nuusdt', 'o3usdt', 'ocnusdt', 'ognusdt', 'ogousdt', 'omgusdt', 'oneusdt', 'ontusdt', 'oxtusdt', 'paiusdt', 'paxusdt',\
                    'pearlusdt', 'phausdt', 'polsusdt', 'pondusdt', 'pvtusdt', 'qtumusdt', 'raiusdt', 'reefusdt', 'renusdt', 'ringusdt', 'rlcusdt',\
                    'rndrusdt', 'rsrusdt', 'ruffusdt', 'rvnusdt', 'sandusdt', 'scusdt', 'seeleusdt', 'shibusdt', 'sklusdt', 'skmusdt', 'smtusdt', 'sntusdt',\
                    'snxusdt', 'socusdt', 'solusdt', 'stakeusdt', 'steemusdt', 'stnusdt', 'storjusdt', 'stptusdt', 'sunusdt', 'sushiusdt', 'swftcusdt',\
                    'swrvusdt', 'thetausdt', 'titanusdt', 'tnbusdt', 'topusdt', 'trbusdt', 'trxusdt', 'ttusdt', 'uipusdt', 'umausdt', 'uniusdt',\
                    'utkusdt', 'uuuusdt', 'valueusdt', 'vetusdt', 'vidyusdt', 'vsysusdt', 'wavesusdt', 'waxpusdt', 'wbtcusdt', 'wiccusdt',\
                    'wnxmusdt', 'woousdt', 'wtcusdt', 'wxtusdt', 'xchusdt', 'xecusdt', 'xemusdt', 'xlmusdt', 'xmrusdt', 'xmxusdt', 'xrpusdt', 'xrtusdt',\
                    'xtzusdt', 'yamusdt', 'yeeusdt', 'yfiiusdt', 'yfiusdt', 'zecusdt', 'zenusdt', 'zilusdt', 'zksusdt', 'zrxusdt']
file_name_0 = file_names_prefix[0] + '.csv'
price_symbol_full = pd.read_csv(file_name_0, index_col = 0)
for i in range(1, 234, 1):
    file_name = file_names_prefix[i] + '.csv'
    price_symbol = pd.read_csv(file_name, index_col = 0)
    price_symbol_full = pd.concat([price_symbol_full, price_symbol])
price_symbol_full.to_csv('price_symbol_full.csv')