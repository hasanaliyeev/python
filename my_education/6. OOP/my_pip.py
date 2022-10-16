import progressbar
import time

bar = progressbar.ProgressBar(maxval=100)
bar.start()

for i in range(1, 101):
    bar.update(i)
    time.sleep(0.01)

bar.finish()
