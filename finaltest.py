import tkinter as tk
from tkinter import filedialog
import os
from tkinter import *


class EasyPayApp(tk.Tk):
	"""The class is instantiated. This creates a toplevel 
	widget of Tk which usually is the main window of an application which is developed to automate the recursive things."""

	def __init__(self):
		
		#Initializing the object for window.
		tk.Tk.__init__(self)
		
		#Title of the window.
		self.title("EASYPAY")
		
		#Shape of the window.
		self.geometry("1366x768+10+10")

		#Creating canvas for the window.
		self.C = tk.Canvas(self, bg="blue")
		self.filename = PhotoImage(file = "bg.gif")
		self.background_label = Label(self, image=self.filename)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
		self.C.pack()

		#Initializing required components like buttons,labels and entry boxes.
		self.photo = PhotoImage(file="speckbit.gif")
		self.speckbit = tk.Button(self, image=self.photo,anchor=CENTER,)
	
		self.entry1=tk.Entry(self,width=30)
		
		
		self.usern=tk.Label(self,text="Username:",anchor=CENTER,font="sansserif 10")
		self.entry2=tk.Entry(self,width=30,show="*")
		self.passw=tk.Label(self,text="Password:",anchor=CENTER,font="sansserif 10")
		self.submit=tk.Button(self,text="SUBMIT",cursor="hand1",activebackground="blue",font="times 10",anchor=CENTER,width=10,command=self.on_submit)
		self.cancel=tk.Button(self,text="CANCEL",cursor="hand1",anchor=CENTER,font="times 10",activebackground="blue",width=10)
		
		self.newuser=tk.Label(self,text="New user?",anchor=CENTER,font="sansserif 10")
		self.register=tk.Button(self,text="Sign Up",cursor="hand1",fg="blue",activebackground="blue",bd=0,anchor=CENTER,font="sansserif 10",command=self.on_signup)
		self.about=tk.Button(self,text="About EASYPAY",cursor="hand1",fg="red",bd=0,anchor=CENTER,activebackground="blue",font="sansserif 12")
		
		#Generating components on the window.
		self.speckbit.pack()
		self.speckbit.place(x=30,y=80)

		self.entry1.pack()
		self.entry1.place(x=600,y=300)

		self.usern.pack()
		self.usern.place(x=523,y=297)

		self.entry2.pack()
		self.entry2.place(x=600,y=340)

		self.passw.pack()
		self.passw.place(x=523,y=338)

		self.submit.pack()
		self.submit.place(x=590,y=380)

		self.cancel.pack()
		self.cancel.place(x=688,y=380)
		
		self.newuser.pack()
		self.newuser.place(x=620,y=425)

		self.register.pack()
		self.register.place(x=685,y=423)

		self.about.pack()
		self.about.place(x=1200,y=80)


		

	def on_signup(self):
		"""This function describes the components required for the new window which appears after signup button is clicked.
		 The title and geometry of the window is described. A canvas is created which is used to pack and place all other 
		 components of the window.

		 A background image is set using PhotoImage attribute.

		 Additional images to decorate the window are also added using PhotoImage widget 
		 """
		
		#Creating new window
		self.new=tk.Toplevel()

		#Shape of the window.
		self.new.geometry("1366x768")

		#Title of the window.
		self.new.title("SIGN UP")

		#Creating canvas for the window.
		self.D = tk.Canvas(self.new, bg="blue")
		self.bgpic=PhotoImage(file="backgrnd.gif")
		self.background_label = tk.Label(self.new, image=self.bgpic)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
		self.D.pack(expand=1)

		#Initializing and generating required components like buttons,labels and entry boxes.
		self.photo1 = PhotoImage(file="signup.gif")
		self.l=tk.Label(self.new,image=self.photo1,anchor=CENTER)
		self.l.pack()
		self.l.place(x=560,y=40)

		self.l1=tk.Label(self.new,text="First Name:",anchor=CENTER,font="times 14")
		self.l1.pack()
		self.l1.place(x=485,y=176)

		self.e1=tk.Entry(self.new,width=35)
		self.e1.pack()
		self.e1.place(x=645,y=180)

		self.photo2 = PhotoImage(file="user.gif")
		self.b1=tk.Label(self.new,image=self.photo2,anchor=NW,bd=0)
		self.b1.pack()
		self.b1.place(x=125,y=125)

		self.l2=tk.Label(self.new,text="Last Name:",anchor=CENTER,font="times 14")
		self.l2.pack()
		self.l2.place(x=485,y=216)

		self.e2=tk.Entry(self.new,width=35)
		self.e2.pack()
		self.e2.place(x=645,y=220)

		self.photo3 = PhotoImage(file="email.gif")
		self.b2=tk.Label(self.new,image=self.photo3,anchor=NW,bd=0)
		self.b2.pack()
		self.b2.place(x=160,y=400)

		self.l3=tk.Label(self.new,text="Email Id:",anchor=CENTER,font="times 14")
		self.l3.pack()
		self.l3.place(x=485,y=256)

		self.e3=tk.Entry(self.new,width=35)
		self.e3.pack()
		self.e3.place(x=645,y=260)

		self.photo4= PhotoImage(file="password.gif")
		self.b3=tk.Label(self.new,image=self.photo4,anchor=NW,bd=0)
		self.b3.pack()
		self.b3.place(x=950,y=400)


		self.l4=tk.Label(self.new,text="Phone No.:",anchor=CENTER,font="times 14")
		self.l4.pack()
		self.l4.place(x=485,y=296)

		self.e4=tk.Entry(self.new,width=35)
		self.e4.pack()
		self.e4.place(x=645,y=300)

		self.photo5 = PhotoImage(file="phone.gif")
		self.b4=tk.Label(self.new,image=self.photo5,anchor=NW,bd=0)
		self.b4.pack()
		self.b4.place(x=900,y=150)

		self.l5=tk.Label(self.new,text="Username:",anchor=CENTER,font="times 14")
		self.l5.pack()
		self.l5.place(x=485,y=336)

		self.e5=tk.Entry(self.new,width=35)
		self.e5.pack()
		self.e5.place(x=645,y=340)

		self.l6=tk.Label(self.new,text="Password:",anchor=CENTER,font="times 14")
		self.l6.pack()
		self.l6.place(x=485,y=376)

		self.e6=tk.Entry(self.new,width=35,show="*")
		self.e6.pack()
		self.e6.place(x=645,y=380)

		self.l7=tk.Label(self.new,text="Confirm Password:",anchor=CENTER,font="times 14")
		self.l7.pack()
		self.l7.place(x=485,y=416)

		self.e7=tk.Entry(self.new,width=35,show="*")
		self.e7.pack()
		self.e7.place(x=645,y=420)

		self.submit1=tk.Button(self.new,text="SUBMIT",anchor=CENTER,font="times 10",cursor="hand1",width=10,command=self.execu)
		self.submit1.pack()
		self.submit1.place(x=560,y=480)

		self.cancel1=tk.Button(self.new,text="CANCEL",anchor=CENTER,font="times 10",cursor="hand1",width=10,command=self.new.destroy)
		self.cancel1.pack()
		self.cancel1.place(x=750,y=480)
		mainloop()

	def on_submit(self):
		self.usernameinp = self.entry1.get() 
		self.userpassword=self.entry2.get()
		
		self.options=tk.Toplevel()
		self.options.configure()
		self.options.geometry("1366x768")
		self.options.title("OPTIONS")
		self.E= tk.Canvas(self.options, bg="blue")
		self.bgpic1=PhotoImage(file="backgrnd.gif")
		self.background_label = tk.Label(self.options, image=self.bgpic1)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
		self.E.pack(expand=1)

		self.card=tk.Button(self.options,text="Add NEW CARD",anchor=CENTER,cursor="hand1",font="times 16",command=self.addcard)
		self.card.pack()
		self.card.place(x=600,y=80)

		self.photo6 = PhotoImage(file="mobile.gif")
		self.mobile=tk.Button(self.options,image=self.photo6,anchor=CENTER,height=220,width=220,bg="light blue",command=self.autopress)
		self.mobile.pack()
		self.mobile.place(x=175,y=200)

		self.photo7 = PhotoImage(file="d2h.gif")
		self.d2h=tk.Button(self.options,image=self.photo7,anchor=CENTER,height=220,width=220,bg="light blue")
		self.d2h.pack()
		self.d2h.place(x=575,y=200)

		self.photo8 = PhotoImage(file="wifi.gif")
		self.wifi=tk.Button(self.options,image=self.photo8,anchor=CENTER,height=220,width=220,bg="light blue")
		self.wifi.pack()
		self.wifi.place(x=975,y=200)

		mainloop()

	def addcard(self):
		self.add=tk.Toplevel()
		self.add.configure()
		self.add.geometry("470x300")
		self.add.title("ADD CARD")


		self.F= tk.Canvas(self.add, bg="blue")
		self.bgpic=PhotoImage(file="backgrnd.gif")
		self.background_label = tk.Label(self.add, image=self.bgpic)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
		self.F.pack(expand=1)

		self.details=tk.Label(self.add,text="CARD DETAILS",anchor=CENTER,font="times 18")
		self.details.pack()
		self.details.place(x=150,y=20)

		self.name=tk.Label(self.add,text="NAME OF CARD HOLDER:",anchor=CENTER,font="times 12")
		self.name.pack()
		self.name.place(x=30,y=70)
		self.e8=tk.Entry(self.add,width=30)
		self.e8.pack()
		self.e8.place(x=230,y=72)

		self.number=tk.Label(self.add,text="CARD NUMBER:",anchor=CENTER,font="times 12")
		self.number.pack()
		self.number.place(x=30,y=100)
		self.e9=tk.Entry(self.add,width=16)
		self.e9.pack()
		self.e9.place(x=230,y=102)

		self.expmonth=tk.Label(self.add,text="EXPIRY MONTH:",anchor=CENTER,font="times 12")
		self.expmonth.pack()
		self.expmonth.place(x=30,y=130)
		self.e10=tk.Entry(self.add,width=2)
		self.e10.pack()
		self.e10.place(x=230,y=132)

		self.expyear=tk.Label(self.add,text="EXPIRY YEAR:",anchor=CENTER,font="times 12")
		self.expyear.pack()
		self.expyear.place(x=30,y=160)
		self.e11=tk.Entry(self.add,width=2)
		self.e11.pack()
		self.e11.place(x=230,y=162)

		self.cvv=tk.Label(self.add,text="CVV:",anchor=CENTER,font="times 12")
		self.cvv.pack()
		self.cvv.place(x=30,y=190)
		self.e12=tk.Entry(self.add,width=3)
		self.e12.pack()
		self.e12.place(x=230,y=192)

		self.submit2=tk.Button(self.add,text="SUBMIT",anchor=CENTER,font="times 12",cursor="hand1",width=10,command=self.on_submit_carddetails)
		self.submit2.pack()
		self.submit2.place(x=190,y=230)


		mainloop()

	def on_submit_carddetails(self):
		self.card_holder_name1=self.e8.get()
		self.card_number1=self.e9.get()
		self.expiry_month1=self.e10.get()
		self.expiry_year1=self.e11.get()
		self.cvv1=self.e12.get()
		self.carddetails(self.card_holder_name1,self.card_number1,self.expiry_month1,self.expiry_year1,self.cvv1)
		self.add.destroy()

	def autopress(self):
		
		"""
		This function eliminates the need for mouse clicks and keypresses,
		which are to be manually given by the user, and runs the whole process automaticlly
		"""

		# Import the necessary libraries.
		import pyautogui,time

		# Open 'Google Chrome' after the command from the user.
		pyautogui.press('win')
		pyautogui.typewrite('Google Chrome',0.1)
		pyautogui.typewrite(['enter'])

		# Give a delay for about 5 sec, to make the system open Google Chrome.
		time.sleep(5)

		# To maximize the new tab window which will be opened on the screen, after the delay.
		pyautogui.hotkey('alt','space')
		pyautogui.press(['x'])

		# Place the cursor into the URL bar to start typing the link.
		pyautogui.click(151,51)
		pyautogui.typewrite('https://www.airtel.in/prepaid-recharge?icid=prepaid_row_1_column_1')
		pyautogui.typewrite(['enter'])

		# Give a delay for about 20 seconds to open the mentioned webpage.
		time.sleep(55)

		# Click on the coordinates of the last digit of the mobile number in the space provided to type the number. 
		pyautogui.click(772,269)

		# Erase the already pre-taken number if any.
		for i in range(10):
			pyautogui.typewrite(['backspace'])

		# Type the 'Mobile number' of the user in the erased space,followed by required amount of delay.
		pyautogui.typewrite('9972549978',0.1)
		time.sleep(10)

		# Type the 'Amount of recharge' to be done, followed by required amount of delay.
		pyautogui.typewrite('35')
		time.sleep(5)

		# Press 'Enter' key to activate Recharge and proceed to payment, followed by required amount of delay.
		pyautogui.keyDown('enter')
		pyautogui.keyUp('enter')
		time.sleep(20)

		# Fill the 'Card details' consisting of Name on the card, Card Number, Expiry date and CVV in the respective space provided.  
		pyautogui.click(100,475)
		pyautogui.click(300,335); pyautogui.typewrite('PRAJWAL S',0.1)
		pyautogui.click(300,430); pyautogui.typewrite('5089440016858525',0.1)
		pyautogui.click(705,430); pyautogui.typewrite('01',0.1)
		pyautogui.click(750,430); pyautogui.typewrite('22',0.1)
		pyautogui.click(830,430); pyautogui.typewrite('247',0.1)

		# Click on 'Continue to pay' option to receive an OTP to the associated number and to complete the payment.
		#pyautogui.click(1000,600)



app = EasyPayApp()
app.mainloop()




