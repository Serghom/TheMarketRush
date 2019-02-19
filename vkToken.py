from selenium import webdriver
import re

def getTokenFromWeb():
    driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
    driver.get("https://vk.cc/8GIRRY")
    url = ''
    done = True
    while done:
        result = re.match(r'http://api.vk.com/blank', driver.current_url)
        if result != None:
            url = driver.current_url
            done = False
            driver.close()
    token = url[re.search('access_token=', url).end() : re.search('&', url).start()]
    writeToken(token)
    return token


def writeToken(token):
    f = open('.token', 'w')
    f.write(token)
    f.close()


def readToken():
    f = open('.token')
    token = f.read()
    f.close()
    return token

def getToken():
    try:
        return readToken()
    except:
        return getTokenFromWeb()

# print(getToken())
