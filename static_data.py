assets_names = {
    '^NSEI': 'NIFTY 50',
    '^NSEBANK': 'NIFTY BANK',
    '^CNXIT': 'NIFTY IT',
    '^BSESN': 'S&P BSE SENSEX',
    'NIFTY_MIDCAP_100.NS': 'NIFTY MIDCAP 100',
    '^CNXPSUBANK': 'NIFTY PSU BANK',
    '^CNXAUTO': 'NIFTY AUTO',
    'NIFTY_FIN_SERVICE.NS': 'NIFTY FIN SERVICE',
    '0P00005WL6.BO': 'UTI Nifty 50 Index Fund',
    'UTINEXT50.BO': 'UTI-Nifty Next 50 Exchange Traded Fund',
    '0P0000MLHH.BO': 'Axis Bluechip Fund Gr',
    '0P0000KV39.BO': 'SBI Small Cap Fund Reg Gr',
    '0P00009J3K.BO': 'HDFC Mid-Cap Opportunities Gr',
    '0P0001BAB5.BO': 'ICICI Prudential Equity & Debt Fund',
    '0P0001EI18.BO': 'HDFC Hybrid Eq Dir Gr',
    '0P0001BA1R.BO': 'Edelweiss Balanced Advantage Fund',
    '0P00005WEY.BO': 'SBI Equity Hybrid Fund',
    '0P0000XUXL.BO': 'Axis Banking & PSU Debt Dir Gr',
    '0P0000XUYZ.BO': 'ICICI Pru Short Term Dir Gr',
    '0P0000XW8D.BO': 'HDFC Corporate Bond Dir Gr',
    '0P0000XVER.BO': 'Nippon India Liquid Dir Gr',
    '0P0000XUYS.BO': 'ICICI Pru Nifty Next 50 Index Dir Gr',
    '0P0000XW7I.BO': 'HDFC Gold Dir Gr',
    '0P0000U3OG.BO': 'ICICI Prudential Regular Gold Savings Fund(FOF) Growth',
    'SETFGOLD.NS': 'SBI Gold ETF',
    'BSLGOLDETF.NS': 'Aditya Birla Sun Life Gold ETF',
    'gold_bond': 'Sovereign Gold Bond'
}

index = [
    '^NSEI', # NIFTY 50
    '^NSEBANK', # NIFTY BANK
    '^CNXIT', # NIFTY IT
    '^BSESN', # S&P BSE SENSEX
    'NIFTY_MIDCAP_100.NS',
    '^CNXPSUBANK',
    '^CNXAUTO',
    'NIFTY_FIN_SERVICE.NS'
]

mutual_funds = [
    '0P00005WL6.BO',
    'UTINEXT50.BO',
    '0P0000MLHH.BO',
    '0P0000KV39.BO',
    '0P00009J3K.BO',
    '0P0001BAB5.BO',
    '0P0001EI18.BO',
    '0P0001BA1R.BO',
    '0P00005WEY.BO',
    '0P0000XUXL.BO',
    '0P0000XUYZ.BO',
    '0P0000XW8D.BO',
    '0P0000XVER.BO',
    '0P0000XUYS.BO',
    '0P0000XW7I.BO',
    '0P0000U3OG.BO',
    'SETFGOLD.NS',
    'BSLGOLDETF.NS'
]

import pandas as pd
fd_rates = pd.DataFrame({
    "Bank Name": [
        "ICICI Bank", 
        "HDFC Bank", 
        "Axis Bank", 
        "Bank of Baroda", 
        "State Bank of India", 
        "Bank Of India", 
        "Equitas small finance bank", 
        "AU small finance bank"
    ],
    "Return Rate for Adults (%)": [6.7, 6.6, 6.7, 6.85, 6.8, 6.8, 7.0, 7.25],
    "Return Rate for Senior Citizens (%)": [7.2, 7.1, 7.2, 7.35, 7.3, 7.3, 7.2, 7.75]
})

stepwise_model_order = {
    "Index": {
        "^NSEI": (2, 1, 2),
        "^NSEBANK": (2, 1, 2),
        "^CNXIT": (3, 1, 0),
        "^BSESN": (5, 2, 0),
        "NIFTY_MIDCAP_100.NS": (5, 2, 0),
        "^CNXPSUBANK": (0, 1, 0),
        "^CNXAUTO": (2, 1, 0),
        "NIFTY_FIN_SERVICE.NS": (5, 1, 4),
    },
    "Mutual_Funds": {
        "0P00005WL6.BO": (2, 1, 2),
        "UTINEXT50.BO": (0, 1, 0),
        "0P0000MLHH.BO": (0, 1, 0),
        "0P0000KV39.BO": (2, 1, 2),
        "0P00009J3K.BO": (5, 2, 0),
        "0P0001BAB5.BO": (1, 1, 0),
        "0P0001EI18.BO": (0, 1, 0),
        "0P0001BA1R.BO": (0, 1, 0),
        "0P00005WEY.BO": (0, 1, 0),
        "0P0000XUXL.BO": (5, 1, 1),
        "0P0000XUYZ.BO": (2, 1, 1),
        "0P0000XW8D.BO": (2, 1, 1),
        "0P0000XVER.BO": (5, 2, 5),
        "0P0000XUYS.BO": (2, 1, 2),
        "0P0000XW7I.BO": (1, 1, 0),
        "0P0000U3OG.BO": (0, 1, 0),
        "SETFGOLD.NS": (0, 1, 0),
        "BSLGOLDETF.NS": (1, 1, 0),
    },
    "Gold_Bond": {
        "gold_bond": (5, 2, 0), # 0, 1, 0
    }
}