from bs4 import BeautifulSoup
from selenium import webdriver
from  selenium.webdriver.support.wait import WebDriverWait
import time


def login():

    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.eastmoney.com/")
        try:
          login_obj  = WebDriverWait(driver, 10).until(lambda d:d.find_element_by_partial_link_text("登录"))
        except Exception as e:
            print("无法获取登录标签对象")
            quit_(driver)
        else:
            login_obj.click()
            time.sleep(2)
        windows_ = driver.window_handles
        if len(windows_) == 2:
            driver.switch_to.window(windows_[1])
            print(driver.title)

        else:
            print("登录页面没有渲染成功！")
            quit_(driver)


    except Exception as e:
        print(e)

def quit_(d):
    d.close()
    d.quit()

if __name__ == "__main__":
    login()
