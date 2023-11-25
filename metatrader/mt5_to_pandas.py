import os, sys
sys.path.insert(0,os.getcwd() + '/libs') ### enabling subfolder

## Importing cached libs
import pandas as pd
import MetaTrader5 as mt5
from config import MT5Config

if not mt5.initialize(login=int(MT5Config.MT5_CL_ACC),
                          password=MT5Config.MT5_PW,
                          server=MT5Config.MT5_CL_SRV,
                          path=MT5Config.MT5_PATH):
    print("initialize() failed, error code =",mt5.last_error())
    mt5.shutdown()

df             = pd.DataFrame(mt5.copy_rates_from_pos('EURUSD', mt5.TIMEFRAME_M1, 0, 1000 )).reset_index(drop=True)
df['datetime'] = pd.to_datetime(df['time'], unit='s')

print(df.shape)
print(df.head().to_string())