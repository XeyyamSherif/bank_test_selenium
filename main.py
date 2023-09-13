from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

PATH = "chromedriver"
driver = webdriver.Chrome()


def select_button(button_str, type_button):
    if type_button == 'text':
        return driver.find_element(By.XPATH, f"//button[contains(text(), '{button_str}')]")
    elif type_button == 'list':
        return driver.find_elements(By.XPATH, f"//button[contains(text(), '{button_str}')]")
    else:
        return driver.find_element(By.XPATH, f"//input[@placeholder='{button_str}']")


def main():
    driver.maximize_window()
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    time.sleep(1)

    ################     Yeni user yaratmaq
    select_button('Bank Manager Login', "text").click()

    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])

    select_button("Add Customer", "list")[0].click()

    time.sleep(1)

    select_button('First Name', 'submit').send_keys("Emin")
    select_button('Last Name', 'submit').send_keys("Abdullayev")
    select_button('Post Code', 'submit').send_keys("AZ1018")

    select_button("Add Customer", "list")[1].click()
    time.sleep(1)

    alert = driver.switch_to.alert
    alert.accept()

    select_button('Home', "text").click()
    time.sleep(1)

    #############     Yeni yaradilmis user ucun process aparilmasi
    select_button('Bank Manager Login', "text").click()
    time.sleep(1)
    select_button('Open Account', "text").click()
    time.sleep(1)

    dropdown_users = driver.find_element(By.ID, "userSelect")
    dropdown_users.click()
    Select(dropdown_users).select_by_visible_text("Emin Abdullayev")

    dropdown_users = driver.find_element(By.ID, "currency")
    dropdown_users.click()
    Select(dropdown_users).select_by_visible_text("Dollar")

    select_button('Process', "text").click()

    time.sleep(1)
    alert = driver.switch_to.alert
    alert.accept()

    select_button('Home', "text").click()
    time.sleep(1)

    ######### User login deposit withdraw
    select_button('Customer Login', "text").click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    dropdown_users = driver.find_element(By.ID, "userSelect")
    dropdown_users.click()
    Select(dropdown_users).select_by_visible_text("Emin Abdullayev")

    select_button('Login', "text").click()
    time.sleep(1)
    select_button('Deposit', "list")[0].click()
    time.sleep(1)
    select_button('amount', 'submit').send_keys(500)
    time.sleep(1)
    select_button('Deposit', "list")[1].click()

    select_button('Withdrawl', "list")[0].click()
    time.sleep(1)
    select_button('amount', 'submit').send_keys(200)
    time.sleep(1)
    select_button('Withdraw', "list")[1].click()
    select_button('Logout', "text").click()
    time.sleep(1)
    select_button('Home', "text").click()
    time.sleep(1)

    ########## Delete user
    select_button('Bank Manager Login', "text").click()
    time.sleep(1)
    select_button('Customers', "text").click()
    time.sleep(1)

    select_button('Search Customer', 'submit').send_keys("Emin")
    time.sleep(1)
    select_button('Delete', "text").click()


if __name__ == "__main__":
    main()
    time.sleep(2131)
