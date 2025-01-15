import time
import threading

def threadFunction(sleepTime):
    time.sleep(sleepTime)
    print(f"Finished sleeping {sleepTime}s")
t = threading.Thread(target=threadFunction, args=(10,))
t.start()
