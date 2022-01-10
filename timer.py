import time
  
def countdown(t):
    x = t/2

    while t>=0:
        min, sec = divmod(t, 60)
        print(min, ':', sec, end='\r')
        time.sleep(1)
        t = t - 1

        if t == x:
            print('Half time passed')

    print('Timer has ended.')
  
  
t = input("Enter the time in seconds: ")

countdown(int(t))
