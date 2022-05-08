import pyautogui as pg
import time
i=0

j=1
k=2
l=3
m=4
n=5
while True:
    i=i+1

    j=j+1
    k=k+2
    l=l+3
    m=m+4
    n=n+5
    ok=(j,k,l,m,n)
    

    

    print(i)
    if(i==50000):
        
        print(ok)
        time.sleep(3)
        for i in range(1):
            pg.write(str(ok))

            pg.press('Enter')
