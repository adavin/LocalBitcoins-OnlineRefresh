# LocalBitcoins-OnlineRefresh

LocalBitcoins app to automatically refresh online status every 14 minutes, keeping the "green lights" on. 

You enter your API KEY and API SECRET (with `read` permissions), and the script will begin its endless loop. 

# Script Execution Instructions
- Install `Python` (Python 2.7 was used for dev, https://www.python.org/downloads/)
- Open Shell or CMD to the directory with the `LBC_OnlineRefresh.py` file. 
- Execute `python -h LBC_OnlineRefresh.py`
- Enter your API KEY + API SECRET

#LocalBitcoins API KEY / API SECRET Creation
- Go to https://localbitcoins.com/accounts/api/
- Click `+ New HMAC Authentication`. 
- Write 'OnlineRefresh' or something for the app name. Give it `read` permissions *ONLY*! 
- Click `Create`, and then click the newly created API KEY to retrieve your API SECRET

Done!

