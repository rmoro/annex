#//////////////////////////////////////////////////////////////////
# AUTHOR:   Robert Morouney
# EMAIL:    robert@morouney.com 
# FILE:     logger.py
# CREATED:  2016-11-22 15:48:55
# MODIFIED: 2016-11-22 17:00:31
#//////////////////////////////////////////////////////////////////
import pyxhook
import datetime

#change this to your log file's path
log_file='/home/duck/Projects/annex/logs/randy.log'


#get the inital time 
global prev_time
prev_time = datetime.datetime.now()



#this function is called everytime a key is pressed.
def OnKeyPress(event):
  global prev_time
  press_time = datetime.datetime.now()

  flight_time = press_time - prev_time
  prev_time = press_time

  #flight_time_ms = (flight_time.seconds * 1000) + (flight_time.microseconds / 1000) 
  flight_time_ms = flight_time.total_seconds() * 1000
  
  fob=open(log_file,'a')
  event_string = '{},{}\n'.format(event.Ascii, int(flight_time_ms))
  fob.write(event_string)
  print(event_string)
  fob.close()

  if event.Ascii==96: exit(0);

print("setting up hook manager")
#instantiate HookManager class
new_hook=pyxhook.HookManager()

print("set callback")
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress

print("hooking the keyboard")
#hook the keyboard
new_hook.HookKeyboard()

print("starting")
#start the session
new_hook.start()
print("finished")
 
