from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup as bs
import components

FirstVariable =  input("What is the first friend you want to compare? ")
SecondVariable =  input("What is the second friend you want to compare? ")


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(40)
LINK = 'https://www.facebook.com/login.php?login_attempt=1&lwv=111'
LINK2 = "https://www.facebook.com/profile.php?id=100008206841293&sk=friends"
LOGIN = components.LOGIN
PASS = components.PASS



def login(LOGIN_URL, login, password):
    driver.get(LOGIN_URL)
    # wait for the login page to load
    driver.find_element_by_id('email').send_keys(login)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_id('loginbutton').click()

login(LINK, LOGIN, PASS)
driver.find_element_by_class_name('_1vp5').click()
driver.find_elements_by_class_name('_6-6')[2].click()
for x in range(30):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    html = driver.execute_script("return document.documentElement.innerHTML;")
#driver.close()
soup = bs(html, "html.parser")

#print(soup.prettify()) #The variable with the text in it is soup.

listOfLinks = []

for div in soup.find_all('div',{"class": "fsl fwb fcb"}):
    listOfLinks.append(div.find_all("a")[0].text)
print(listOfLinks)


for z in range(30):
    driver.execute_script("window.scrollTo(0, 0);") #Scrolls back up



driver.find_element_by_link_text(FirstVariable).click() #Finds the link with that name

max_attemps = 10

while True:
    linker = driver.find_elements_by_class_name('_6-6')[2]
    if linker is not None:
        sleep(6)
        driver.find_elements_by_class_name('_6-6')[2].click()
        break
    else:
        sleep(0.5)
        max_attemps -= 1
    if max_attemps == 0:
        print("Cannot find element.")



for x in range(50):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    html = driver.execute_script("return document.documentElement.innerHTML;")
#driver.close()
soup = bs(html, "html.parser")

firstFriendsList = []

for div in soup.find_all('div',{"class": "fsl fwb fcb"}):
    firstFriendsList.append(div.find_all("a")[0].text)
print(firstFriendsList)

driver.back()
driver.back()

driver.implicitly_wait(3)

while True:
    try:
        driver.find_element_by_link_text(SecondVariable).click() #Finds the link with that name
        break
    except:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.implicitly_wait(40)

max_attemps = 10

while True:
    linker = driver.find_elements_by_class_name('_6-6')[2]
    if linker is not None:
        sleep(3)
        driver.find_elements_by_class_name('_6-6')[2].click()
        break
    else:
        sleep(0.5)
        max_attemps -= 1
    if max_attemps == 0:
        print("Cannot find element.")



for x in range(50):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    html = driver.execute_script("return document.documentElement.innerHTML;")
#driver.close()
soup = bs(html, "html.parser")

secondFriendsList = []

for div in soup.find_all('div',{"class": "fsl fwb fcb"}):
    secondFriendsList.append(div.find_all("a")[0].text)
print(secondFriendsList)

driver.close()

marker = False
mutualFriends = []

for x in firstFriendsList:
    for y in secondFriendsList:
        if x==y:
            marker = True
            mutualFriends.append(x)
makeitastring = ','.join(map(str, mutualFriends))
if marker == False:
    print("You have no mutual friends unfortunately")
else:
    print("Your mutual friends are: ", makeitastring)



