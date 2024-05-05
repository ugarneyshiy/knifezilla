import _thread
import json
import traceback
import websocket
import threading
import time


class Socket_conn_Binance(websocket.WebSocketApp):
    def __init__(self, url):
        super().__init__(
            url=url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        #self.price = None
        self.run_forever()

    def on_open(self, ws):
        print(ws, 'WebSocket was opened')

    def on_error(self, ws, error):
        print('on_error', ws, error)
        print(traceback.format_exc())
        exit()

    def on_close(self, ws, status, msg):
        print('on_close', ws, status, msg)
        exit()

    def on_message(self, ws, msg):
        data = json.loads(msg)
        kline_high = float(data["k"]["h"])
        kline_low = float(data["k"]["l"])
        if ((kline_high - kline_low) / kline_high) >= 0.001:
            print("BTC🡣 > {:.1f}%".format(((kline_high - kline_low) / kline_high) * 100))


        #if "data" not in data:
        #    print(data)
        #    if data["s"] == "ADAUSDT":
        #        print(data['t'])
        #if 'kline_1s' in data.get('stream', "No data"):
        #    self.data = data['data']["k"]["t"]


    def return_data(self):
        return self.data

    def get_price(self):
        return self.price


#list_streams = [
#    "btcusdt@kline_5m",
#]
#url = f'wss://stream.binance.com:443/stream?streams={"/".join(list_streams)}'
#threading.Thread(target=Socket_conn_Binance, args=(url,)).start()
#
# Single stream
#url = 'wss://stream.binance.com:443/ws/btcusdt@depth10'
#threading.Thread(target=Socket_conn_Binance, args=(url,)).start()
#
# Single stream
#url = 'wss://stream.binance.com:443/ws/btcusdt@kline_5m'
#threading.Thread(target=Socket_conn_Binance, args=(url,)).start()
#print("Hello")