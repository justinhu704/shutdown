# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 19:56:07 2018

@author: 10091
"""

from datetime import datetime,time,date
import os


tmNow = datetime.now()
d = date.today()
t = time(17,30,00)
shtdownTime = datetime.combine(d,t)
def ShutDown():
     while True:
         tmNow = datetime.now()
         timedDelta = (shtdownTime - tmNow).total_seconds()
         if timedDelta < 60:
             print('還有59s關機，趕快儲存一下！')
             os.system('shutdown -s -f -t 30')           
             #break
             time.sleep(20)
         else:
             continue
             
if __name__ == '__main__':
     ShutDown()