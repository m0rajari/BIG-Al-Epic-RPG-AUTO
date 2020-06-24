from tkinter import *
import time
import keyboard
class Window(Frame):


	def __init__(self, master=None):
		Frame.__init__(self, master)                 
		self.master = master
		self.init_window()

	#Creation of init_window
	def init_window(self):

		# changing the title of our master widget      
		self.master.title("GUI")
		startbutton = Button(self, text="Start", command=self.client_start)
		startbutton.place(x=0, y=0)

		# allowing the widget to take the full space of the root window
		self.pack(fill=BOTH, expand=1)

		# creating a button instance
		quitButton = Button(self, text="Quit", command=self.client_exit)

		# placing the button on my window
		quitButton.place(x=35, y=0)
		
	def client_exit(self):
		exit()

	def client_start(self):
			time.sleep(4)
			for i in range(2):
				keyboard.write('rpg hunt')
				keyboard.press_and_release('enter')
				time.sleep(5)
				keyboard.write('rpg heal')
				keyboard.press_and_release('enter')
				keyboard.write('rpg heal')
				keyboard.press_and_release('enter')
				time.sleep(4)
				keyboard.write('rpg adv')
				keyboard.press_and_release('enter')
				time.sleep(3)
				keyboard.write('rpg heal')
				keyboard.press_and_release('enter')
				time.sleep(3)
				keyboard.write('rpg tr')
				keyboard.press_and_release('enter')
				time.sleep(4)
				keyboard.write('rpg axe')
				keyboard.press_and_release('enter')

				time.sleep(40)

root = Tk()

#size of the window
root.geometry("200x100")

app = Window(root)
root.mainloop()  