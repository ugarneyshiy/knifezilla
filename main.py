import api
import threading
import time

if __name__ == '__main__':
    list_streams = [
        "btcusdt@kline_5m",
    ]
    url = 'wss://stream.binance.com:443/ws/btcusdt@kline_5m'
    ws_binance = api.Socket_conn_Binance(url)
    threading.Thread(target=ws_binance.run_forever).start()


    while True:
        time.sleep(5)
        print("test", ws_binance.return_data())

