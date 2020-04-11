from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from math import floor
import numpy
url = 'https://csgorun.org'
 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
 
coef_xpath = '//*[@id="app"]/div[2]/div[1]/div[1]/div[1]/ul/li[1]/a/span'
users_xpath = '//*[@id="app"]/div[2]/div[1]/div[2]/div[2]/ul/li[1]/b'
cash_xpath = '//*[@id="app"]/div[2]/div[1]/div[2]/div[2]/ul/li[2]/b'
 
coef = None
users = None
cash = None
 
coef_arr = []
users_arr = []
cash_arr = []

iterations = 1000

for i in range(iterations):
    coef = None
    users = None
    cash = None
    while (users == None):
        parsed_users = driver.find_element_by_xpath(users_xpath).text
        print('inside, users: ' + parsed_users + ', iteration: ' + str(i))
        if int(parsed_users) in [0, 1, 2]:
                print('it is 0')
                time.sleep(9)
                print('slept')
                users = driver.find_element_by_xpath(users_xpath).text
                cash = driver.find_element_by_xpath(cash_xpath).text
                coef = driver.find_element_by_xpath(coef_xpath).text
                print('old coef ' + coef)
                while (True):
                    parsed_coef = driver.find_element_by_xpath(coef_xpath).text
                    print('old ' + coef)
                    print('new ' + parsed_coef)
                    if (parsed_coef != coef):
                        coef = parsed_coef
                        
                        coef_arr.append(round(float(coef.replace('x', '')), 2))
                        users_arr.append(int(users))
                        cash_arr.append(int(float(cash)))
                        break

users_cash_arr = [list(a) for a in zip(users_arr, cash_arr)]


print(coef_arr)
print(users_cash_arr)

numpy.savetxt('coefs', coef_arr, delimiter=',')
numpy.savetxt('users_cash', users_cash_arr, delimiter=',')