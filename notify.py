'''This script will notify you on brithday 
	that your set on 'bridhday'
'''
__author__  = "Mehadi Hasan Menon"
__version__ = "1.0"
__email__   = "mehadi@semanticslab.net"

import os
import time

script_path   = os.path.realpath(__file__)
root_path     = '/'.join(script_path.split('/')[:-1])
birthday_file = root_path + '/' + 'birthday'
audio_path    = root_path + "/" + 'beep.ogg'

def check_todays_birthdays():
    file_name = open(birthday_file, 'r')
    today = time.strftime('%d-%m-%y')
    today_is_brithday = False
    
    for line in file_name:
        # print('today', today, 'brithday', line)
        if today in line:
            line = str(' '.join(line.split(' ')[1:])).strip('\n')
            today_is_brithday = True
            os.system('notify-send "Today: ' + str(line) + ' \'s birthday' + '"')
            os.system('paplay ' + audio_path)
            time.sleep(10)
    if today_is_brithday is False:
            os.system('notify-send "No Birthday Today!"')
            os.system('paplay ' + audio_path)

if __name__ == '__main__':
	# after login this program is execute 10 second letter
	# if your system takes more time to login then increase this time
    time.sleep(10)
    check_todays_birthdays()
