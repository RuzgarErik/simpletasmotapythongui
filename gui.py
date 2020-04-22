import tkinter as tk
import requests 
window = tk.Tk()
window.title("Tasmota Switch")
def ac(event):
	x = requests.post('http://192.168.1.103/cm?cmnd=Power%20ON')
def kapat(event):
	x = requests.post('http://192.168.1.103/cm?cmnd=Power%20OFF')
button1 = tk.Button(
	text="Turn On",
	width=40,
	height="5",
	bg="Green",
	fg="white"
	)
button1.bind("<Button-1>", ac)

button2 = tk.Button(
	text="Turn Off",
	width=40,
	height="5",
	bg="Red",
	fg="white"
	)
button2.bind("<Button-1>", kapat)

button1.pack()
button2.pack()

window.mainloop()
