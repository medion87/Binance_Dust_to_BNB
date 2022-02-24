import configparser
import pathlib
import itertools
import pandas as pd
import numpy as np
import time
from time import sleep
from binance import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException

parser = configparser.ConfigParser()
parser.read_file(open("settings.cfg"))
client = Client(parser.get("default", "api_key"), parser.get("default", "api_secret"))

class DataManager:
	def Symbols():
		sList = client.get_all_tickers()
		symbols = []
		expected = ""
			
		for x in range(len(sList)):
			if parser.get("default", "currency") in sList[x]['symbol']:
				if sList[x]['symbol'] in expected:
					symbols.append(sList[x]['symbol'])
				if expected == "":
					symbols.append(sList[x]['symbol'])
		return symbols
	
	def MarketPrice(symbol):
		ticker = client.get_ticker(symbol=symbol)
		marketprice = float(ticker['bidPrice'])
		return marketprice
	
	def wallet(asset):
		balance = client.get_asset_balance(asset=asset)
		balance = float(balance['free'])
		return balance
	
	def Exchange(symbol):
		info = client.get_symbol_info(symbol)

		status = info['status']
		BaseAsset = info['baseAsset']
		QouteAsset = info['quoteAsset']
		
		Exchange = {
			"status": status,
			"BaseAsset": BaseAsset,
			"QouteAsset": QouteAsset,
		}
		return Exchange

class main:
	def run():
		DUST = []
		seperator = ','
		symbols = DataManager.Symbols()

		for symbol in symbols:
			Exchange = DataManager.Exchange(symbol)
			time.sleep(0.01)
			balance = DataManager.wallet(Exchange['BaseAsset'])
			time.sleep(0.01)
			marketprice = DataManager.MarketPrice(symbol)
			time.sleep(0.01)
			Dust_Valua = float(marketprice) * float(balance)
				
				
			if float(Dust_Valua)>=float('0.00001') and float(Dust_Valua)<=float(parser.get("default", "max")) and Exchange['BaseAsset']!=parser.get("default", "currency"):
				DUST.append(Exchange['BaseAsset'])
				time.sleep(1)

			elif symbol==symbols[-1]:
				CDUST = seperator.join(DUST)
				print(CDUST)

				if DUST!=[]:
					client.transfer_dust(asset=CDUST)
					return

				else:
					return
			else:
				time.sleep(1)

if __name__ == '__main__':
	itertools.repeat(main.run())
	time.sleep(28800)