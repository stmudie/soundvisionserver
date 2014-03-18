from pyplayshow import pyplayshow
from time import sleep
from yamaha import yamaha
import redis
import subprocess

class Soundvisionserver:
    def __init__(self):
        self.input = 'V-AUX'
	self.changedelay = 2 
        self.soundpath = '/root/'
        self.p = pyplayshow()
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
        
        while True:
            command = (self.r.brpop('soundvision:queue'))[1].split('#')
            if len(command) > 1:
		message, sound = command
            else :
                message = command[0]
                sound = ''
            if message[0] == '@':
                self.command(message[1:],sound,video=True)
            else:
	        self.command(message, sound)
            
    def command(self,message, sound, video=False):
        y = yamaha(config='yamaha/config.yml')
        current = y.currentinput()
        y.changeinput(self.input)
        sleep(self.changedelay)
        if video:
            self.p.show('', colour=(200,200,200),background=(0,0,0),time = 0)
            subprocess.call(['omxplayer','%s%s' % (self.soundpath,message)])
        else:
            self.p.show(message, colour=(200,200,200),background=(100,100,100),time = 0)
            sound = self.p.play('%s%s' % (self.soundpath,sound))    
            sleep(sound.get_length())
        try:
            y.changeinput(current)
        except:
            y = yamaha(config='yamaha/config.yml')
            y.changeinput(current)
        del y

if __name__ == '__main__':

    svs = Soundvisionserver()


#    y = yamaha(config='yamaha/config.yml')
    
#    current = y.currentinput()
#    y.changeinput('V-AUX')
    
#    a = pyplayshow()
    
#    a.show('Scan Finished', colour=(200,100,200),background=(200,100,100),time = 0)
#    sound = a.play('/root/ExampleNorm.ogg')
#    sleep(sound.get_length())
    
#    y.changeinput(current)
