from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# check how the data on 8 seconds differs from the data on 9.5 seconds

url = 'https://csgorun.org'
 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

users_xpath = '//*[@id="app"]/div[2]/div[1]/div[2]/div[2]/ul/li[1]/b'
cash_xpath = '//*[@id="app"]/div[2]/div[1]/div[2]/div[2]/ul/li[2]/b'

iterations = 5

u = []
s = []


for i in range(iterations):
    users = None
    cash = None
    users_after = None
    cash_after = None
    while (users == None):
        parsed_users = driver.find_element_by_xpath(users_xpath).text
        print('inside, users: ' + parsed_users + ', iteration: ' + str(i))
        if int(parsed_users) in [0, 1, 2]:
                print('it is 0')
                time.sleep(8)
                print('slept 1')
                users = driver.find_element_by_xpath(users_xpath).text
                cash = driver.find_element_by_xpath(cash_xpath).text
                time.sleep(1.5)
                print('slept 2')
                users_after =  driver.find_element_by_xpath(users_xpath).text
                cash_after = driver.find_element_by_xpath(cash_xpath).text

                u_all = [users, users_after]
                s_all = [cash, cash_after]
                u.append(u_all)
                s.append(s_all)

print(u)
print(s)

for i in range(len(u)):
    perc_u = int(u[i][1])/100 * (int(u[i][1]) - int(u[i][0]))
    perc_s = int(float(s[i][1]))/100 * (int(float(s[i][1])) - int(float(s[i][0])))
    print('на ' + str(perc_u) + '%')
    print('на ' + str(perc_s) + '%')