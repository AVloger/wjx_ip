from selenium import webdriver
import time
import random
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
from PIL import Image,ImageEnhance

# -*- coding: utf-8 -*- 
import pymysql.cursors
import time

# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='proxypool', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
# 通过cursor创建游标
cursor = connection.cursor()
sql = "SELECT * FROM `proxypool`"
cursor.execute(sql)

#查询数据库多条数据
result = cursor.fetchall()
ip_get = []
for data in result:
    ip_get.append((data['ip']+":"+data['ip_port']))
connection.close()
for ip in ip_get:
    options = webdriver.ChromeOptions()

    options.add_argument('--proxy-server={}'.format(ip))
    browser = webdriver.Chrome(executable_path=r'C:\Users\AVloger\AppData\Local\Google\Chrome\Application\chromedriver\chromedriver.exe', chrome_options=options)
    try:
        for i in range(20):
            browser.get('https://www.wjx.cn/jq/43942468.aspx')
            b = np.random.choice(5,p=[0,0.25, 0.25, 0.25, 0.25])#按照P分布设定答案结果
            b = str(b)
            target = "a[rel='q1_"+b+"']"
            browser.find_element_by_css_selector(target).click()
            time.sleep(1)
            b = np.random.choice(5,p=[0,0.25, 0.25, 0.25, 0.25])
            b = str(b)
            target = "a[rel='q2_"+b+"']"
            browser.find_element_by_css_selector(target).click()
            time.sleep(1)
            b = np.random.choice(5,p=[0,0.25, 0.25, 0.25, 0.25])
            b = str(b)
            target = "a[rel='q3_"+b+"']"
            browser.find_element_by_css_selector(target).click()
            time.sleep(1)
            b = np.random.choice(5,p=[0,0.25, 0.25, 0.25, 0.25])
            b = str(b)
            target = "a[rel='q4_"+b+"']"
            browser.find_element_by_css_selector(target).click()
            time.sleep(1)

            b = np.random.choice(5,p=[0,0.25, 0.25, 0.25, 0.25])
            b = str(b)
            target = "a[rel='q5_"+b+"']"
            browser.find_element_by_css_selector(target).click()
            time.sleep(1)
            b = np.random.choice(4,p=[0,0.3, 0.3, 0.4])
            b = str(b)
            target = "a[rel='q6_"+b+"']"
            browser.find_element_by_css_selector(target).click()
            time.sleep(1)
            b = np.random.choice(4,p=[0,0.3, 0.3, 0.4])
            b = str(b)
            target = "a[rel='q7_"+b+"']"
            browser.find_element_by_css_selector(target).click()
            time.sleep(1)

            b = np.random.choice(3,p=[0,0.5, 0.5])
            b = str(b)
            target = "a[rel='q8_"+b+"']"
            browser.find_element_by_css_selector(target).click()
            time.sleep(1)
            b = np.random.choice(3,p=[0,0.5, 0.5])
            b = str(b)
            target = "a[rel='q9_"+b+"']"
            browser.find_element_by_css_selector(target).click()
            time.sleep(1)

            browser.find_element_by_id("submit_button").click()
            time.sleep(2)
    except:
        continue