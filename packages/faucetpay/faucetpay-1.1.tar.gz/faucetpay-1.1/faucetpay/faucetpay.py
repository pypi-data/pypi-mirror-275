import requests
import json

class SendError(Exception):
    pass

class FaucetPay:
    def __init__(self, api_key):
        self.apikey = api_key
        
    def balance(self, crypto="btc"):
        data = {"api_key": self.apikey, "currency": crypto}
        return json.loads(requests.post("https://faucetpay.io/api/v1/getbalance", data=data).text)
    
    def supported_coins(self):
        data = {"api_key": self.apikey}
        return json.loads(requests.post("https://faucetpay.io/api/v1/currencies", data=data).text)["currencies"]
    
    def checkaddress(self, address):
        data = {"api_key": self.apikey, "address": address}
        return json.loads(requests.post("https://faucetpay.io/api/v1/checkaddress", data=data).text)
    
    def send(self, amount=None, to=None, crypto="btc", ref=None, ip=None):
        if amount is None or to is None:
            raise SendError("Please Input Amount And Address To Use Faucet")
        else:
            if ref is not None and ip is None:
                data = {"api_key": self.apikey, "amount": amount, "to": to, "currency": crypto, "referral": ref}
            elif ip is not None and ref is None:
                data = {"api_key": self.apikey, "amount": amount, "to": to, "currency": crypto, "ip_address": ip}
            elif ip is not None and ref is not None:
                data = {"api_key": self.apikey, "amount": amount, "to": to, "currency": crypto, "referral": ref, "ip_address": ip}
            else:
                data = {"api_key": self.apikey, "amount": amount, "to": to, "currency": crypto}
            return json.loads(requests.post("https://faucetpay.io/api/v1/send", data=data).text)
    def recent_payout(self,crypto="btc",count=100):
        data = {"api_key": self.apikey,"currency":crypto,"count":count}
        return json.loads(requests.post("https://faucetpay.io/api/v1/payouts", data=data).text)["rewards"]

    def faucetlist(self):
        data = {"api_key": self.apikey}
        return json.loads(requests.post("https://faucetpay.io/api/listv1/faucetlist", data=data).text)

    def info():
        print("This Is unofficial python library for faucetpay api. you can make simple faucetpay faucet with this library. contact email : vboxvm512@gmail.com. create faucetpay account from : https://faucetpay.io/?r=5507597")
        return "This Is unofficial python library for faucetpay api. you can make simple faucetpay faucet with this library. contact email : vboxvm512@gmail.com. create faucetpay account from : https://faucetpay.io/?r=5507597"

