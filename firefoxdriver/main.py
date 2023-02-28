from webdiver_manager.firefox import FireFoxDriverManager
import time

url = 'https://www.vk.com/'
driver = webdriver.Firefox(executable_path='/home/akjol/Desktop/python24/Selenium/firefoxdriver/geckodriver')

try:
    driver.get(url=url)
    driver.save_screenshot('vk.png')
    time.sleep(5)
    # driver.get(url='https://youtube.com/')
    # time.sleep(5)

    # driver.refresh()
    # driver.get_screenshot_as_file('1.png')
    # driver.get(url='https://youtube.com/')
    # time.sleep(5)
    # driver.save_screenshot('2.png')
    # time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()