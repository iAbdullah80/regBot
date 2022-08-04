from selenium import webdriver
import os
import time as time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

os.environ['PATH'] += r"C:\seleniumD"  # add Chrome version 104... to the PATH

opts = uc.ChromeOptions()  # coped from stackoverflow
opts.add_argument("--window-size=1020,900")  # coped from stackoverflow
driver = uc.Chrome(options=opts, use_subprocess=True)  # coped from stackoverflow

driver.get('https://iussb.imamu.edu.sa/PROD_ar/twbkwbis.P_GenMenu?name=homepage')  # go to the uni site
time.sleep(2)
userName = driver.find_element(By.XPATH, '//*[@id="UserID"]')  # find the username textbox by its xpath
userName.send_keys("442019225")  # enter ur username and send it to the textbox
pas = driver.find_element(By.XPATH, '//*[@id="PIN"]/input')  # find the password textbox by its xpath
pas.send_keys("4802077Aa")  # enter ur password and send it to the textbox
login = driver.find_element(By.XPATH, '/html/body/div[3]/font/form/p/input')  # find the login button by its xpath
login.click()  # click on it!
time.sleep(2)
student = driver.find_element(By.XPATH, '/html/body/div[3]/p/table[1]/tbody/tr[2]/td[2]/a')  # find (الطالب) link
student.click()  # click on it
time.sleep(2)
register = driver.find_element(By.XPATH, '/html/body/div[3]/table[1]/tbody/tr[1]/td[2]/a')  # find (التسجيل) link
register.click()  # click on it
time.sleep(2)
addingCourses = driver.find_element(By.XPATH,
                                    '/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a')  # find(الحذف او الاضافة)
addingCourses.click()  # click on it
time.sleep(2)
enterSem = driver.find_element(By.XPATH, '/html/body/div[3]/form/input')  # find the (تنفيذ) button by xpath
enterSem.click()  # click on it

inc = 0  # increment variable to make sure we don't refresh the page to much
boolToExit = True
while boolToExit and inc < 10:  # use a while loop to refresh the page until registration is open
    time.sleep(1)  # sleep a second to make sure that the page has loaded
    """ to find if the registration is open or not,  we will try to find the XPATHs for the reference numbers textboxes.
        we know that these boxes does not show up until registration time, so when we (try) to find the xpath while
         registration is closed we will get a compilation error then except will catch the error and refresh the page
         until the textboxes show up we will fill them and submit then exit from the loop."""
    try:
        firstCourse = driver.find_element(By.XPATH, '//*[@id="crn_id1"]')  # find the frst reference textbox by xpath
        firstCourse.send_keys("11851")  # send your reference number
        secondCourse = driver.find_element(By.XPATH, '//*[@id="crn_id2"]')  # find the second reference textbox by xpath
        secondCourse.send_keys("11527")  # send your reference number
        thirdCourse = driver.find_element(By.XPATH, '//*[@id="crn_id3"]')
        thirdCourse.send_keys("11361")
        forthCourse = driver.find_element(By.XPATH, '//*[@id="crn_id4"]')
        forthCourse.send_keys("11767")
        fifthCourse = driver.find_element(By.XPATH, '//*[@id="crn_id5"]')
        fifthCourse.send_keys("21829")
        # submit = driver.find_element(By.XPATH, '/html/body/div[3]/form/input[19]')  # find (تنفيذ التغييرات) button
        # submit.click()  # click on it
        print("Submitted!")
        boolToExit = False  # set the boolean to false, so we can exit the loop

    except:
        driver.refresh()  # refresh the page
        print("refreshing...")
        time.sleep(2)
        inc += 1

print("I will logout in 30 seconds...")
time.sleep(30)
end = driver.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr/td[2]/p/span/a[4]') # find (الخروج) button
end.click() # click and logout!
print("Existing in 5 seconds...")
time.sleep(5)