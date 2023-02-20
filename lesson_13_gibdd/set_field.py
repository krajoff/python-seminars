import requests
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from create_driver import driver


def set_field(data):
    url = 'https://xn--90adear.xn--p1ai/request_main'
    message = "{date} года около {time} водитель автомобиля {model} (регистрационный знак" \
              "{sign}) нарушил п. 12.2 правил дорожного движения и поставил свой автомобиль на " \
              "стоянку на тротуар. Нарушение произошло по адресу {place}. " \
              "Прошу принять меры в соответствии с КоАП п.3, ч.1, ст.28.1 и сообщить о рассмотрении " \
              "данного обращения.".format(time=data["time"], date=data["date"], model=data["model"],
                                          sign=data["sign"], place=data["place"])
    # driver.get(url)
    # First page
    # driver.find_element(By.CLASS_NAME, 'checkbox').click()
    # driver.find_element(By.CLASS_NAME, 'u-form__sbt').click()
    # Second page
    select = Select(driver.find_element(By.CLASS_NAME, 'regionlist'))
    select.select_by_value('78')
    time.sleep(1)
    select = Select(driver.find_element(By.XPATH, "//select[@name='subunit']"))
    select.select_by_value('41')
    driver.find_element(By.XPATH, "//input[@name='surname']").send_keys(data["surname"])
    driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys(data["firstname"])
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys(data["email"])
    driver.find_element(By.XPATH, "//textarea[@name='message']").send_keys(message)
    if not data["photo"]:
        driver.find_element(By.XPATH, "//input[@name='file']").send_keys(data["photo"])
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@name='captcha']").send_keys(data["captcha"])
    driver.find_element(By.CLASS_NAME, 'js-u-form__sbt').click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[@id='confirm_but']").click()
    # print(driver.page_source)
    # time.sleep(30)
