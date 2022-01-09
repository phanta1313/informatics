import time
  
def countdown(t):
    
    while t>=0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Timer has ended.')
  
  
t = input("Enter the time in seconds: ")
  
countdown(int(t))
