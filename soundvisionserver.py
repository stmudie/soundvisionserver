from pyplayshow import pyplayshow
from time import sleep
from yamaha import yamaha

y = yamaha(config='yamaha/config.yml')

current = y.currentinput()
y.changeinput('V-AUX')

a = pyplayshow()

a.show('Scan Finished', colour=(200,100,200),background=(200,100,100),time = 0)
sound = a.play('/root/ExampleNorm.ogg')
sleep(sound.get_length())

y.changeinput(current)
