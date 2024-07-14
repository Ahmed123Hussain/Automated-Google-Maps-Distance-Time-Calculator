from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#assign url in the webdriver object
driver = webdriver.Chrome()
driver.get("https://www.google.com/maps/@17.3873874,78.4117656,14z?entry=ttu")
sleep(2)


#search location
srcloc = input("Write The Starting address")
destloc = input ("Write destination address")
sleep(7)
def searchplace():
    Place  = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[1]/form/input")
    Place.send_keys(srcloc)
    Submit= driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[1]/div[1]/button/span")

    Submit.click()
searchplace()

#get directions
def getdir():
    sleep(5)
    directions = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/span")
    directions.click()

getdir()

#Put Destination

def dest():
    sleep(5)
    dest = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
    dest.send_keys(destloc)
    Submit = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]/span")
    Submit.click()
dest()

#get kilometers
def kilometers():
    sleep(5)
    Totalkilometers = driver.find_element(
        By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div/div[1]/div/div[1]/div[2]/div")
    print("Total Kilometers:", Totalkilometers.text)
    sleep(2)
    Time = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div/div[1]/div/div[1]/div[1]")
    print("Time Required:", Time.text)
    
 
 
kilometers()

