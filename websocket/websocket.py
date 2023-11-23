import websocket
import threading
import time

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_message):
    print(f"Close with status code: { close_status_code}, message: {close_message}")

def on_open(ws):
    def run():
        ws.send("Hello Server")
        time.sleep(1)
        ws.close()
    threading.Thread(target=run).start()

if __name__ == "__main__":
    ws_url = "ws://ttc.gojosatoru.stream"
    ws = websocket.WebSocketApp(ws_url, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()