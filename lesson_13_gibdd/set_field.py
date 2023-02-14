from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


def set_field(data):
    url = 'https://xn--90adear.xn--p1ai/request_main'
    message = "{date} {year} года около {time} водитель автомобиля {model} (регистрационный знак" \
              "{sign}) нарушил п. 12.2 правил дорожного движения и поставил свой автомобиль на " \
              "стоянку на тротуар. Нарушение произошло по адресу {place}." \
              "Прошу принять меры в соответствии с КоАП п.3, ч.1, ст.28.1 и сообщить о рассмотрении " \
              "данного обращения.".format(time=data["time"], date=data["date"], year=data["year"],
                                          model=data["model"], sign=data["sign"], place=data["place"])
    driver = webdriver.Chrome()
    driver.get(url)
    # First page
    driver.find_element(By.CLASS_NAME, 'checkbox').click()
    driver.find_element(By.CLASS_NAME, 'u-form__sbt').click()
    # Second page
    select = Select(driver.find_element(By.CLASS_NAME, 'regionlist'))
    select.select_by_value('78')
    time.sleep(1)
    select = Select(driver.find_element(By.XPATH, "//select[@name='subunit']"))
    select.select_by_value('41')
    driver.find_element(By.XPATH, "//input[@name='surname']").send_keys('Яшин')
    driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys('Николай')
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys('t0k@bk.ru')
    driver.find_element(By.XPATH, "//textarea[@name='message']").send_keys(message)
    time.sleep(15)
