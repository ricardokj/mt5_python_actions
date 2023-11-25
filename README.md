# MetaTrader 5 + python + Actions

This repo is a sample to run the MetaTrader 5 within the GitHub Actions.

To turn it faster, there is a cache for:
* The MT5 installation
* The python libraries
* The python environment

Run the build_cache.yml workflow first.

The python libraries are being installed in a `/libs` subfolder. Then the `mt5_to_pandas.py` is using the cached libs by adding it to the path:
```python
import os, sys
sys.path.insert(0,os.getcwd() + '/libs')
```

To set your secrets, go to "Settings" -> "secrets and variables" -> "Actions".

It was not possible to establish the connection with the server by using the hostname. I could only connect by using the ip:port 
