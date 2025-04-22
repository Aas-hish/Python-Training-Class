from datetime import datetime
import pytz
import time
import os
a = pytz.timezone('Asia/Kolkata')

while True:
    b = datetime.now(a)
    print(b.strftime("%H:%M:%S"))
    time.sleep(1)
    os.system("clear")
