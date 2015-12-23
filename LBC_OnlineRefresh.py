import requests
import hmac
import hashlib
import json
from datetime import datetime
import time
import sys

class LBCAPI(object):
    def __init__ (self, API_KEY, API_SECRET):
        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET
        self.min_counter = 13
                
        if (self.API_KEY == ''):
            self.API_KEY = raw_input('Please enter your LocalBitcoins.com API KEY: \r\n')
        if (self.API_SECRET == ''):
            self.API_SECRET = raw_input('Please enter your LocalBitcoins.com API SECRET: \r\n') 
        try:
            myself = self.getMyself()
            self.cprint("\r\nHello, " + myself['data']['username'] + ".\r\n")
        except Exception: 
            self.cprint("Error authenticating API KEY + API SECRET, or error parsing data. Please try again.")
            sys.exit()
            
        while True:
            self.min_counter -= 1
            if (self.min_counter == 0):
                self.cprint('Refreshing online status for ' + myself['data']['username'] + '.')
                self.getMyself()
                self.min_counter = 13
            else:
                self.cprint(str(self.min_counter) + ' minutes remaining until refresh.')
            time.sleep(60)
       
    def cprint(self, smsg):
       print smsg
       sys.stdout.flush()     
    def message(self, relative_path, params):
        return (str(self.nonce()) + self.API_KEY + relative_path + params).encode('utf-8')
        
    def signature(self, message):
        return hmac.new(self.API_SECRET, msg=message, digestmod=hashlib.sha256).hexdigest().upper()
        
    def nonce(self):
        return int(((datetime.utcnow() - datetime.utcfromtimestamp(0)).total_seconds()) * 1000) 
        
    def sendMessage(self, relative_path, params):
        headers = {}
	message = self.message(relative_path, params)
	headers['Apiauth-Key'] = self.API_KEY
	headers['Apiauth-Nonce'] = self.nonce()
	headers['Apiauth-Signature'] = self.signature(message)
	result = requests.get('https://localbitcoins.com' + relative_path, headers = headers)
	return result.json()
	
    def getMyself(self):
        return self.sendMessage('/api/myself/','')
	
if __name__ == '__main__':
    LBC = LBCAPI('', '')
