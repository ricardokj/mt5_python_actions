import os 

class MT5Config:
    MT5_CL_ACC = os.getenv('MT5_AT_ACC')
    MT5_CL_SRV = os.getenv('MT5_AT_SRV')
    MT5_PW = os.getenv('MT5_PW')
    MT5_PATH = "C:\\Program Files\\MetaTrader 5\\terminal64.exe"