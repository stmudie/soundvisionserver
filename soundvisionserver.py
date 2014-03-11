from pyplayshow import pyplayshow
from time import sleep

a = pyplayshow()

a.show('test', time = 0)
a.play('/mnt/shared/ding.wav')
sleep(5)