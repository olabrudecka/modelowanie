import requests
from urllib.parse import urlparse
import pandas as pd
from numpy import linspace
from random import random, uniform,randint

# fetch data from  API
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)



#TASKS (11p)
#To use the requests library you have to install it first. If you have pip and you're using python3 interpreter in your project
# then simply pip3 install requests

# 1 Find another public API with cryptocurrency and compare prices. As an output print:
# "Currently the XXX exchange market is better for buying whilst YYY is better for selling" (3p)
# 2 Use https://randomuser.me API to download a random user data.
# Create and store 100 random users with ids, username, name (first + last name) using this API (2p)
# 3 Prepare a simulation of transactions between these users
# Take random user and pair him/her with another one. Assume a random amount but take real world price. Sum up the transaction printing:
# username1 exchanged X.XXX BTC with username2 for PLN YYYYY.YYY PLN. (2p)
# Simulate real time - do not proceed all transactions at once. Try to make around 100 transactions per minute (2p)
# Simulate user's assets. Creating a user assign random amount of a given currency. Take it into account while performing a transaction.
# Remember to amend user's assets after the transaction. (2p)

############zadanie1#############
#
# bitbay = "https://bitbay.net/API/Public/BTCPLN/ticker.json"
# bitmarket = "https://www.bitmarket.pl/json/BTCPLN/ticker.json"
#
# class Cryptoinfo:
#     def __init__(self,url):
#         self.response = requests.get(url)
#         self.data = self.response.json()
#         self.best_bid=self.data['bid']
#         self.best_ask=self.data['ask']
#         self.name = urlparse(url).netloc
#
# crypto_api = [bitbay, bitmarket]
#
# for i in range(len(crypto_api)-1):
#     crypto = Cryptoinfo(crypto_api[i])
#     crypto2 = Cryptoinfo(crypto_api[i+1])
#     if crypto.best_bid > crypto2.best_bid:
#         best_crypto_bid = crypto.name
#     else:
#         best_crypto_bid = crypto2.name
#     if crypto.best_ask > crypto2.best_ask:
#         best_crypto_ask = crypto.name
#     else:
#         best_crypto_ask = crypto2.name
# print(f"Currently the {best_crypto_bid} exchange market is better for buying whilst {best_crypto_ask} is better for selling")
#

############zadanie2#############

url = "https://randomuser.me/api/?results=100"
class GetUser:
    def __init__(self,url):
        self.response = requests.get(url)
        self.data = self.response.json()

class UserInfo:
    def __init__(self,data,i):
        self.data = data
        self.id = self.data['results'][i]['login']['uuid']
        self.username = self.data['results'][i]['login']['username']
        self.name = self.data['results'][i]['name']['first'] + " " + self.data['results'][i]['name']['last']

        self.transaction = round(random())
        if self.transaction == 0:
            self.transaction = 'B'
        else:
            self.transaction = 'S'

        self.exchangevalue = 12000 - round(uniform(-3,3),2)
        self.usd = random() * 1000
        self.btc = round(random() * 2, 2)
        self.HowMuch = round(random() * 2, 2)
        while self.transaction == 'S' and self.HowMuch > self.btc:
            self.HowMuch = round(random() * 2, 2)
        while self.transaction == 'B' and self.HowMuch * self.btc > self.usd:
            self.HowMuch = round(random() * 2, 2)
        self.info = [self.id, self.username, self.usd, self.btc, self.transaction, self.exchangevalue, self.HowMuch, self.name]
n = 100
index = linspace(1,n,n)
df = pd.DataFrame(columns = ['Id', 'Username', 'WalletUSD', 'WalletBTC', 'BuyOrSell','exchangeValue', 'HowMuch','Name'])
users = GetUser(url)
for i in range(n):
    user = []
    user_info = UserInfo(users.data,i)
    data = user_info.info
    df.loc[i] = data

df.set_index(pd.Index(index))
print(df)
############zadanie3################
def pickUserToBuy():
    user = df.loc[randint(0,99)]
    while user.BuyOrSell == 'S':
        user = df.loc[randint(0, 99)]
    return user

def pickUserToSell():
    user = df.loc[randint(0,99)]
    while user.BuyOrSell == 'B':
        user = df.loc[randint(0, 99)]
    return user

def exchange():
    user_buy = pickUserToBuy()
    user_sell = pickUserToSell()

    if user_buy.exchangeValue >= user_sell.exchangeValue and user_buy.HowMuch >0:
        if user_buy.HowMuch <= user_sell.HowMuch:
            amount = (user_buy.exchangeValue+user_sell.exchangeValue)/2 * user_buy.HowMuch
            user_buy.WalletBTC = user_buy.WalletBTC + user_buy.HowMuch
            user_buy.WalletUSD = user_buy.WalletUSD - amount
            user_sell.WalletBTC = user_sell.WalletBTC - user_buy.HowMuch
            user_sell.WalletUSD = user_sell.WalletUSD + amount
            user_sell.HowMuch = user_sell.HowMuch - user_buy.HowMuch
            print(f'User {user_buy.Username} exchanged {user_buy.HowMuch} BTC with user {user_sell.Username} for {amount} USD')
            user_buy.HowMuch = 0
        else:
            amount = (user_buy.exchangeValue + user_sell.exchangeValue) / 2 * user_sell.HowMuch
            user_buy.WalletBTC = user_buy.WalletBTC + user_sell.HowMuch
            user_buy.WalletUSD = user_buy.WalletUSD - amount
            user_buy.HowMuch = user_buy.HowMuch - user_sell.HowMuch
            user_sell.WalletBTC = 0
            user_sell.WalletUSD = user_sell.WalletUSD + amount
            print(f'User {user_buy.Username} exchanged {user_sell.HowMuch} BTC with user {user_sell.Username} for {amount} USD')
        exchange()
    else:
        exchange()


exchange()