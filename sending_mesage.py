from selenium import webdriver
from selenium.webdriver.common.keys import Keys     # giving fulll adress of Keys class in selenium library
from selenium.webdriver.common.by import By
import time   # to  wait

driver = webdriver.Chrome() # this will gave teh acesss of chrome means opening chrome to python variba;e chrome
driver.get("https://web.whatsapp.com") # by .get python will automaticaly whatsapp


input("Scan Qr code and press enter ")
time.sleep(7)
 
number = ["000000000",'111111111','1221121210']
msg = ["Hlo","hey","How are u "]

for i in range(len(number)):

    driver.get(f"https://web.whatsapp.com/send?phone={number[i]}") # "Open WhatsApp Web and go directly to the chat for the phone number
                                                            # stored in the variable number.
    if (i==0):
        time.sleep(20)
    else:
        time.sleep(10)


    message_box = driver.switch_to.active_element  # this will open the textbox
    message_box.send_keys(msg[i])
    message_box.send_keys(Keys.ENTER) # it willpress the enter key on ehatapp and msg will be sent

    print("Sent:", msg[i])
    time.sleep(4) # waiting for sending ,sg to another person

input("Press Enter to close browser...")
