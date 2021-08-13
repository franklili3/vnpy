from typing import List, Dict
from datetime import datetime

import numpy as np

from vnpy.app.portfolio_strategy import StrategyTemplate, StrategyEngine
from vnpy.trader.utility import BarGenerator, ArrayManager
from vnpy.trader.object import BarData
from vnpy.trader.constant import Interval


class PairTradingStrategy(StrategyTemplate):
    """"""

    author = "Frank li"

    volitility_window = 2
    stocks_number = 1
    rebalance_days = 1
    
    #leg1_symbol = ""

    parameters = [
        "volitility_window",
        "stocks_number",
        "rebalance_days"
    ]
    #variables = [
        #"leg1_symbol",
    #]

    def __init__(
        self,
        strategy_engine: StrategyEngine,
        strategy_name: str,
        vt_symbols: List[str],
        setting: dict
    ):
        """"""
        super().__init__(strategy_engine, strategy_name, vt_symbols, setting)

        self.bgs: Dict[str, BarGenerator] = {}
        self.targets: Dict[str, int] = {}
        self.last_tick_time: datetime = None
        self.amplitude_data: Dict[str, np.array] = {}
        self.volitility_data: Dict[str, int] = {}
        self.sorted_volitility_data: list[np.array] = [] 
        self.selected_symbols: list[str] = []
        self.bar_count: int = 0
        
        for vt_symbol in self.vt_symbols:
            self.amplitude_data[vt_symbol] = np.zeros(volitility_window)
            self.volitility_data[vt_symbol] = np.zeros(1)

        # Obtain contract info
        #self.leg1_symbol, self.leg2_symbol = vt_symbols

        def on_bar(bar: BarData):
            """"""
            pass

        for vt_symbol in self.vt_symbols:
            self.targets[vt_symbol] = 0
            self.bgs[vt_symbol] = BarGenerator(on_bar, Interval.Day)

    def on_init(self):
        """
        Callback when strategy is inited.
        """
        self.write_log("策略初始化")

        self.load_bars(2)

    def on_start(self):
        """
        Callback when strategy is started.
        """
        self.write_log("策略启动")

    def on_stop(self):
        """
        Callback when strategy is stopped.
        """
        self.write_log("策略停止")

    def on_tick(self, tick: TickData):
        """
        Callback of new tick data update.
        """
        if (
            self.last_tick_time
            and self.last_tick_time.day != tick.datetime.day
        ):
            bars = {}
            for vt_symbol, bg in self.bgs.items():
                bars[vt_symbol] = bg.generate()
            self.on_bars(bars)

        bg: BarGenerator = self.bgs[tick.vt_symbol]
        bg.update_tick(tick)

        self.last_tick_time = tick.datetime

    def on_bars(self, bars: Dict[str, BarData]):
        """"""
        self.cancel_all()
        self.bar_count += 1
        
        # Return if one leg data is missing
        #if self.leg1_symbol not in bars or self.leg2_symbol not in bars:
        #    return

        # Calculate current signal
        bar_0 = bars[0]
        #leg2_bar = bars[self.leg2_symbol]
        for vt_symbol in self.vt_symbols:
            self.amplitude_data[vt_symbol].append((bars[vt_symbol].high_price -\
                bars[vt_symbol].low_price) / bars[vt_symbol].open_price)
        
        # Filter time only run on 
        if self.bar_count % rebalance_days != 0:
            return
        
        # Update to data array
        for vt_symbol in self.vt_symbols:
            if (self.amplitude_data[vt_symbol]) < volitility_window:
                self.amplitude_data[vt_symbol].append((bars[vt_symbol].high_price -\
                    bars[vt_symbol].low_price) / bars[vt_symbol].open_price)
            else:
                self.amplitude_data[vt_symbol][:-1] = self.amplitude_data[vt_symbol][1:]
                self.amplitude_data[vt_symbol].append((bars[vt_symbol].high_price -\
                    bars[vt_symbol].low_price) / bars[vt_symbol].open_price)
            self.volitility_data[vt_symbol] = self.amplitude_data[vt_symbol].std()
        #self.current_spread = (
        #    leg1_bar.close_price * self.leg1_ratio - leg2_bar.close_price * self.leg2_ratio
        
        # select stock name
        self.sorted_volitility_data = sorted(self.volitility_data.items(), key=lambda\
                         item: item[1], reverse=True)
        i = 0
        for item in self.sorted_volitility_data.items():
            if i < stocks_number:
                self.selected_symbols.append(item[0])
        print('self.selected_symbols:', self.selected_symbols)
                
        '''
        self.spread_data[:-1] = self.spread_data[1:]
        self.spread_data[-1] = self.current_spread

        self.spread_count += 1
        if self.spread_count <= self.boll_window:
            return

        # Calculate boll value
        buf: np.array = self.spread_data[-self.boll_window:]

        std = buf.std()
        self.boll_mid = buf.mean()
        self.boll_up = self.boll_mid + self.boll_dev * std
        self.boll_down = self.boll_mid - self.boll_dev * std
        '''
        # Calculate new target position
        # 等权重
        weight = 1 / len(self.selected_symbols)
        # 目前持仓列表    
        stock_hold_now = [equity.symbol for equity in self.get_pos()]
        print('stock_hold_now:', stock_hold_now)

        # 需要买入的股票列表
        stock_to_buy = [i for i not in stock_hold_now  if i in self.selected_symbols]
        print('stock_to_buy:', stock_to_buy)

        # 继续持有股票列表
        no_need_to_sell = [i for i in stock_hold_now  if i in self.selected_symbols]
        print('no_need_to_sell:', no_need_to_sell)

        # 卖出股票列表 
        stock_to_sell = [i for i in stock_hold_now if i not in no_need_to_sell]
        print('stock_to_sell:', stock_to_sell)

        # 执行卖出
        for stock in stock_to_sell:
            current_pos = self.get_pos(stock)
            volume = current_pos
            bar = bars[stock]
            price = bar.close_price + self.price_add
            self.sell(stock, price, volume)

        # 如果当天没有买入就返回
        if len(stock_to_buy) == 0:
            return

        # 执行买入
        for s_t_b in stock_to_buy:
            bar = bars[stock]
            price = bar.close_price + self.price_add
            volume = 1
            self.buy(s_t_b, volume)
            
        self.put_event()
