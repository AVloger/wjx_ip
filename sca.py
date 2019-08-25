from selenium import webdriver
import time
import random
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
from PIL import Image,ImageEnhance

browser = webdriver.Chrome(r"C:\Users\AVloger\AppData\Local\Google\Chrome\Application\chromedriver\chromedriver.exe")#����
#browser.get('https://www.wjx.cn/jq/31521246.aspx')
time.sleep(2)

for i in range(300):
    browser.get('https://www.wjx.cn/jq/43942468.aspx')
    b = random.randint(1,4)
    b = str(b)
    target = "a[rel='q1_"+b+"']"
    browser.find_element_by_css_selector(target).click()
    time.sleep(1)
    b = random.randint(1,4)
    b = str(b)
    target = "a[rel='q2_"+b+"']"
    browser.find_element_by_css_selector(target).click()
    time.sleep(1)
    b = random.randint(1,4)
    b = str(b)
    target = "a[rel='q3_"+b+"']"
    browser.find_element_by_css_selector(target).click()
    time.sleep(1)
    b = random.randint(1,4)
    b = str(b)
    target = "a[rel='q4_"+b+"']"
    browser.find_element_by_css_selector(target).click()
    time.sleep(1)

    b = random.randint(1,3)
    b = str(b)
    target = "a[rel='q5_"+b+"']"
    browser.find_element_by_css_selector(target).click()
    time.sleep(1)
    b = random.randint(1,3)
    b = str(b)
    target = "a[rel='q6_"+b+"']"
    browser.find_element_by_css_selector(target).click()
    time.sleep(1)
    b = random.randint(1,3)
    b = str(b)
    target = "a[rel='q7_"+b+"']"
    browser.find_element_by_css_selector(target).click()
    time.sleep(1)

    b = random.randint(1,2)
    b = str(b)
    target = "a[rel='q8_"+b+"']"
    browser.find_element_by_css_selector(target).click()
    time.sleep(1)
    b = random.randint(1,2)
    b = str(b)
    target = "a[rel='q9_"+b+"']"
    browser.find_element_by_css_selector(target).click()
    time.sleep(1)

    try:
        browser.find_element_by_id("yucinput").click()
        driver.switch_to.alert.accept()
        time.sleep(2)

        #imgsrc = driver.find_element_by_id("imgCode").get_attribute('src')
        browser.get_screenshot_as_file('D:/python_project/wholepage.png')
        
        im = Image.open("D:/python_project/wholepage.png")
        print("it is a error")
        box = (160, 180, 409, 308)
        region = im.crop(box)
        region.save("D://python_project//testwholepage.png")
        im = Image.open("D://python_project//testwholepage.png")
        im = im.convert("L")
        threshold = 55
        pixdata = im.load()
        w, h = im.size
        
        for y in range(h):
            for x in range(w):
                if pixdata[x, y] < threshold:
                    pixdata[x, y] = 0 
                else:
                    pixdata[x, y] = 255 
                for y in range(1, h - 1):
                    for x in range(1, w - 1): 
                        count = 0 
                        if pixdata[x, y - 1] > 245:
                            count = count + 1
                if pixdata[x, y + 1] > 245:
                    count = count + 1
                if pixdata[x - 1, y] > 245:
                    count = count + 1
                if pixdata[x + 1, y] > 245:
                    count = count + 1
                if count > 2:
                    pixdata[x, y] = 255

        im.save("D://python_project//newMethod.png")
        img = Image.open("D://python_project//newMethod.png")
        code = pytesseract.image_to_string(img, "eng")
        newCode = ''
        for c in code:
            if(c.isalnum()):
                newCode += c
            print(newCode)
        browser.find_element_by_id("yucinput").send_keys(newCode)
    except Exception:
        print("other_func()")
    browser.find_element_by_id("submit_button").click()
    time.sleep(2)