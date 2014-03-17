from pyplayshow import pyplayshow
from time import sleep
from yamaha import yamaha
import redis

class Soundvisionserver:
    def __init__(self):
        self.input = 'V-AUX'
        self.soundpath = '/root/'
        self.y = yamaha(config='yamaha/config.yml')
        self.p = pyplayshow()
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
        
        while True:
            message, sound = (self.r.brpoplpush('logline:queue', 'logline:processed')).split('#')
            self.command(message, sound)
            
    def command(self,message, sound):
        current = self.y.currentinput()
        self.y.changeinput(self.input)
        self.p.show('message', colour=(200,100,200),background=(200,100,100),time = 0)
        sound = p.play('%s%s' % (self.soundpath,sound))    
        self.y.changeinput(self.currentinput)

if __name__ == '__main__':

    y = yamaha(config='yamaha/config.yml')
    
    current = y.currentinput()
    y.changeinput('V-AUX')
    
    a = pyplayshow()
    
    a.show('Scan Finished', colour=(200,100,200),background=(200,100,100),time = 0)
    sound = a.play('/root/ExampleNorm.ogg')
    sleep(sound.get_length())
    
    y.changeinput(current)
