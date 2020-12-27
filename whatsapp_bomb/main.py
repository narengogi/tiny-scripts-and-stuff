from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

target = input("Who is your target?\n")
number = int(input("How many times do you wish to iterate the message?\n"))
message = input("Enter message\n")
message = message.split(" ")
length_of_message = len(message)

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://web.whatsapp.com/")

while True:
    try:
        search = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]"
        )
        break
    except Exception:
        pass
search.click()
search.send_keys(target)

tries = 15

while tries:
    try:
        driver.find_element_by_xpath(
            '//span[@title = "{}"]'.format(target)).click()
        break
        tries -= 1

    except:
        pass
    else:
        print("Nigga not found \n")

msg_box = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[2]/div[1]/div[2]"
)

for i in range(number):
    for j in range(length_of_message):
        msg_box.send_keys(message[j], Keys.ENTER)
        sleep(0.5)

driver.quit()
