# Easypay-An Automated Payment Application
Easypay is an automated payment application which is developed in order to automate the things we do repeatedly in our day-today lives.Here we have considered an example of mobile and d2h recharge.
The application is developed based on Tkinter, Pyautogui and PeeWee.
Tkinter is used to design the frontend of the application, Pyautogui is used for automation process and PeeWee is used for creating and maintaining database.

Initially, after running the application, a new window appears which is referred as homepage. The user needs to signup first inorder to use the application for the first time.
Click on Signup, then a new signup window appears, fill the required details and click on submit. The data entered in the signup page gets stored in the database.
User needs to login in the home page with valid credentials and a new options window will apper. User needs to add their card details for first time usage by clicking on add card, fill all the deatils and press submit.
Then user needs to choose either mobile recharge or d2h recharge.After choosing the option user doesnt need to do any work, pyautogui proceeds the work till the user gets OTP on their mobile. 
If the user is already registered the data is retrieved from the database and used for recharge process. About us option on homepage displays about the easypay application in new window.
Database can be viewed by opening easypay.db file.
## Running the application
Pre-requisites to run the application:
In command prompt,
pip install pyautogui ,
pip install peewee

In a new folder, pull all the files in the repository and run(double click) the batchfile.bat
Carry the process explained above.
