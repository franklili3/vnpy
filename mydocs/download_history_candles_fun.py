#下载bitfinex交易所历史K线数据
#1.导入所需模块
import os
import sys
import asyncio
sys.path.append("E:\MyProjects\myprojects\bitfinex")
from bfxapi import Client
bfx = Client(
  logLevel='DEBUG',
)

async def log_historical_candles(symbol_bitfinex):
  candles = await bfx.rest.get_public_candles(symbol_bitfinex, 0, then)
  print ("Candles:")
  [ print (c) for c in candles ]
async def run(symbol_bitfinex):
  await log_historical_candles(symbol_bitfinex)
    
