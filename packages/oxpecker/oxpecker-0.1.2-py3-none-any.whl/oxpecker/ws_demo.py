import io
import json
import sys
import threading
import time
from datetime import datetime

# 有些环境中，远端poc脚本找不到依赖包
import requests  # pylint: disable=unused-import


def on_message(ws, message):
    print("### websocket on_message ###")
    sys.stdout.flush()
    thread = threading.Thread(target=handle_message, args=(ws, message))
    thread.start()


def handle_message(ws, message):
    print("Received: " + message)
    biz_message = json.loads(message)
    event = biz_message.get("event")
    print("event: " + event)
    sys.stdout.flush()

    if event == "EVENT.RUN_PYTHON":
        script = biz_message.get("data")
        print("===exec script===: " + script)
        if script:
            old_stdout = sys.stdout
            try:
                output = io.StringIO()
                sys.stdout = output
                exec(script)
                sys.stdout = old_stdout
                captured_output = output.getvalue()
                output.close()
                biz_message["data"] = captured_output
                print("===exec result output===: " + captured_output)
                sys.stdout.flush()
            except Exception as e:
                sys.stdout = old_stdout
                print(f"发生异常：{e}")
                biz_message["data"] = repr(e)
        else:
            biz_message["data"] = "script is empty"
        ws.send(json.dumps(biz_message))
        return
    if event == "EVENT.TASK_FINISH":
        print("TODO task finish")


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print(f"### websocket close ###, at {datetime.now()}")


def on_open(ws):
    print(f"### websocket open ###，at {datetime.now()}")


def start_heartbeat(ws):
    def run():
        count = 0
        while True:
            time.sleep(15)
            count += 1
            print(f"### heartbeat {count} ###")
            ws.send(json.dumps({"event": "EVENT.HEARTBEAT.PING"}))

    thread = threading.Thread(target=run)
    thread.start()
