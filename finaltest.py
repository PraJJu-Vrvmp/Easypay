import tkinter as tk
from tkinter import filedialog
import tkinter
import tkinter.messagebox
import os
from tkinter import *
from peewee import *
from model import *

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
		 The title and geometry of the window is described.A canvas is created which is used to pack and place all other 
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

	def execu(self):
		self.firstname=self.e1.get()             #code
		self.lastname=self.e2.get()              #to retrive 
		self.email_id=self.e3.get()               #input data in entry boxes
		self.phone_no=self.e4.get()
		self.username=self.e5.get()
		self.password=self.e6.get()
		self.confirmpassinp=self.e7.get()
		self.signup(self.firstname,self.lastname,self.email_id,self.phone_no,self.username,self.password)
		self.new.destroy()
		tkinter.messagebox.showinfo("Signup Successful","Please login again with your username and password")

	def on_submit(self):
		self.usernameinp = self.entry1.get() 
		self.userpassword=self.entry2.get()
		self.check=self.login(self.usernameinp,self.userpassword)
		if self.check==True:
			self.option_call()
		else:
			tkinter.messagebox.showinfo("Signin Unsuccessful","Please login again with your valid username and password")
	def option_call(self):
		self.options=tk.Toplevel()
		self.options.configure()
		self.options.geometry("1366x768")
		self.options.title("OPTIONS")
		self.E= tk.Canvas(self.options, bg="blue")
		self.bgpic1=PhotoImage(file="backgrnd.gif")
		self.background_label = tk.Label(self.options, image=self.bgpic1)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
		self.E.pack(expand=1)

		self.card1=tk.Button(self.options,text="Add NEW CARD",anchor=CENTER,cursor="hand1",font="times 16",command=self.addcard)
		self.card1.pack()
		self.card1.place(x=600,y=80)

		self.photo6 = PhotoImage(file="mobile.gif")
		self.mobile=tk.Button(self.options,image=self.photo6,anchor=CENTER,height=220,width=220,bg="light blue",command=self.mobile_recharge)
		self.mobile.pack()
		self.mobile.place(x=175,y=200)

		self.photo7 = PhotoImage(file="d2h.gif")
		self.d2h=tk.Button(self.options,image=self.photo7,anchor=CENTER,height=220,width=220,bg="light blue",command=self.dth_recharge)
		self.d2h.pack()
		self.d2h.place(x=575,y=200)

		self.photo8 = PhotoImage(file="wifi.gif")
		self.wifi=tk.Button(self.options,image=self.photo8,anchor=CENTER,height=220,width=220,bg="light blue",command=self.wifi_recharge)
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
		self.card(self.card_holder_name1,self.card_number1,self.expiry_month1,self.expiry_year1,self.cvv1)
		self.add.destroy()

	def mobile_recharge(self):
		
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
		time.sleep(10)

		# Click on the coordinates of the last digit of the mobile number in the space provided to type the number. 
		pyautogui.click(772,269)

		# Erase the already pre-taken number if any.
		for i in range(10):
			pyautogui.typewrite(['backspace'])

		# Type the 'Mobile number' of the user in the erased space,followed by required amount of delay.
		numb1=self.ph(self.usernameinp)
		pyautogui.typewrite(numb1,0.1)
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
		chn1=self.c_h_n()
		time.sleep(1)
		pyautogui.click(350,338); pyautogui.typewrite(chn1,0.1)
		cn1=self.c_n()


		pyautogui.click(300,430); pyautogui.typewrite(cn1,0.1)
		expm2=self.expm()
		pyautogui.click(705,430); pyautogui.typewrite(expm2,0.1)
		expy2=self.expy()
		pyautogui.click(750,430); pyautogui.typewrite(expy2,0.1)
		cvv2=self.c_v_v()
		pyautogui.click(830,430); pyautogui.typewrite(cvv2,0.1)

		# Click on 'Continue to pay' option to receive an OTP to the associated number and to complete the payment.
		pyautogui.click(1000,600)

	def dth_recharge(self):
		import pyautogui,time
		pyautogui.press('win')
		pyautogui.typewrite('Google Chrome',0.1)
		pyautogui.typewrite(['enter'])
		time.sleep(5)
		pyautogui.hotkey('alt','space')
		pyautogui.press(['x'])
		pyautogui.click(151,51)
		pyautogui.typewrite('https://www.tatasky.com/wps/portal/TataSky/help/recharge-online')
		pyautogui.typewrite(['enter'])
		time.sleep(10)
		pyautogui.click(1119,120)
		time.sleep(2)
		pyautogui.press(['down'])
		pyautogui.press(['down'])
		pyautogui.click(720,470)
		pyautogui.typewrite('9945990000',0.1)
		pyautogui.click(618,592)
		pyautogui.typewrite('3175',0.1)
		time.sleep(2)
		pyautogui.click(665,682)
		time.sleep(10)
		pyautogui.click(330,405)
		pyautogui.click(1150,543)
		time.sleep(10)
		pyautogui.click(681,375)
		pyautogui.click(959,413)
		pyautogui.click(864,579)
		pyautogui.click(805,465)
		time.sleep(5)
		pyautogui.click(620,445)
		cn1=self.c_n()
		pyautogui.typewrite(cn1,0.1)
		expm2=self.expm()
		chn1=self.c_h_n()
		pyautogui.click(620,479); pyautogui.typewrite(chn1,0.1)
		pyautogui.click(552,512); pyautogui.typewrite(expm2,0.1)
		expy2=self.expy()
		expy3="20"+expy2
		cvv2=self.c_v_v()
		pyautogui.click(606,513); pyautogui.typewrite(expy3,0.1)

		pyautogui.click(550,550); pyautogui.typewrite(cvv2,0.1)
		pyautogui.click(373,634)

	def wifi_recharge(self):
		import pyautogui,time
		pyautogui.press('win')
		pyautogui.typewrite('Google Chrome',0.1)
		pyautogui.typewrite(['enter'])
		time.sleep(5)
		pyautogui.hotkey('alt','space')
		pyautogui.press(['x'])
		pyautogui.click(151,51)

	def signup(self,f_firstname, f_lastname, f_email_id ,f_phone_no ,f_username ,f_password):
		self.firstname = f_firstname
		self.lastname = f_lastname
		self.email_id = f_email_id
		self.phone_no = f_phone_no
		self.username = f_username
		self.password = f_password
		try:
			Customer.create(first_name = self.firstname, last_name = self.lastname, email_id = self.email_id ,phone_number = self.phone_no, user_name = self.username, password = self.password)
		except:
			Customer.update(first_name = self.firstname, last_name = self.lastname, email_id = self.email_id ,phone_number = self.phone_no, user_name = self.username, password = self.password)
	


	def login(self,f_username, f_password):

		self.username = f_username
		self.password = f_password


		try:
			query1 = Customer.select().where(Customer.user_name == self.username)
			
			if ((self.password == query1[0].password) and (query1[0].user_name == self.username)):
				print("loged In")
				return True
			else:
				print("Invalid username or password")
				return False

		except:
			print("user does not exist")
			return False
	def ph(self,f_username):
		self.username = f_username

		query2= Customer.select().where(Customer.user_name == self.username)
		self.ph_no = query2[0].phone_number
		return self.ph_no
	

	def card(self,f_card_holder,f_card_no,f_exp_month,f_exp_year,f_cvv):
		self.card_holder_name1 = f_card_holder
		self.card_number1 = f_card_no
		self.expiry_month1 = f_exp_month
		self.expiry_year1 = f_exp_year
		self.cvv1 = f_cvv

		
		Card_details.create(card_holder_name = self.card_holder_name1, card_number = self.card_number1, expiry_month = self.expiry_month1 ,expiry_year = self.expiry_year1 , cvv = self.cvv1)

	def c_h_n(self):

		query3= Card_details.select().where(Card_details.customer==1)
		self.chn = query3[0].card_holder_name
		return self.chn
	def c_n(self):

		query4= Card_details.select().where(Card_details.customer==1)
		self.cn = query4[0].card_number
		return self.cn
	def expm(self):

		query5= Card_details.select().where(Card_details.customer==1)
		self.expm1 = query5[0].expiry_month
		return self.expm1
	def expy(self):

		query6= Card_details.select().where(Card_details.customer==1)
		self.expy1 = query6[0].expiry_year
		return self.expy1
	def c_v_v(self):

		query7= Card_details.select().where(Card_details.customer==1)
		self.cvvn= query7[0].cvv
		return self.cvvn






		
app = EasyPayApp()
app.mainloop()




