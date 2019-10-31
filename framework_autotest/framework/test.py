from selenium import webdriver
import os


dir_path = os.path.dirname(os.path.abspath('.')) + r'/tools/'
tool_path = dir_path + 'geckodriver.exe'
driver = webdriver.Firefox(executable_path=tool_path)

driver.get(r"https://www.baidu.com")
el = driver.find_elements_by_xpath("//*[@name='tj_trnews22']")
if len(el) == 0:
    print("0")
elif len(el) == 1:
    print("1")
else:
    print("2")
