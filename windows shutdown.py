#shut down
import os 
import time

import tkinter as tk
def a():
    os.system('shutdown -s -f -t {}'.format(entry.get())) 
window = tk.Tk()
window.title('笑死')
window.geometry("300x100+250+150")

label = tk.Label(window, text = 'Please choose the number from 1 to 60')  # 顯示文字
label.pack()

entry = tk.Entry(window, width = 20)
entry.pack()

button = tk.Button(window, text = "OK", command = a)
button.pack()

window.mainloop()
