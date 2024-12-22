from helium import *
import time
from datetime import timedelta

total_click = 10000000
start_chrome('https://neal.fun/sun-vs-moon/')

## sun-btn is the id of the button for the "sun"
sunbutton = S('#sun-btn')
## cllick it once so it locks in
click(sunbutton)

start = time.time()
for i in range(0, total_click):
    # don't be surprised if you get a 429 lmao.
    press(SPACE)
end = time.time()

print("Total Time Elapsed in Seconds: " + str(timedelta(seconds=end-start)))