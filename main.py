from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

PATH = "chromedriver"
driver = webdriver.Chrome()


def find_element(selector, value, multiple=False):
    if not multiple:
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((selector, value))
        )
    else:
        return WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((selector, value))
        )


def click_element(element):
    element.click()


def input_text(element, text):
    element.send_keys(text)


def select_option_by_text(select_element, option_text):
    select = Select(select_element)
    select.select_by_visible_text(option_text)


def add_customer(first_name, last_name, post_code):
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Bank Manager Login')]"))
    driver.switch_to.window(driver.window_handles[0])
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Add Customer')]"))
    input_text(find_element(By.XPATH, "//input[@placeholder='First Name']"), first_name)
    input_text(find_element(By.XPATH, "//input[@placeholder='Last Name']"), last_name)
    input_text(find_element(By.XPATH, "//input[@placeholder='Post Code']"), post_code)
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Add Customer')]"))
    alert = driver.switch_to.alert
    alert.accept()
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Home')]"))


def open_account(customer_name, currency):
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Bank Manager Login')]"))
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Open Account')]"))
    select_option_by_text(find_element(By.ID, "userSelect"), customer_name)
    select_option_by_text(find_element(By.ID, "currency"), currency)
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Process')]"))
    alert = driver.switch_to.alert
    alert.accept()
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Home')]"))


def login_and_transact(customer_name, deposit_amount, withdraw_amount):
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Customer Login')]"))
    driver.switch_to.window(driver.window_handles[0])
    select_option_by_text(find_element(By.ID, "userSelect"), customer_name)
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Login')]"))
    
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Deposit')]"))
    input_text(find_element(By.XPATH, "//input[@placeholder='amount']"), deposit_amount)
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Deposit')]"))

    click_element(find_element(By.XPATH, "//button[contains(text(), 'Withdrawl')]"))
    input_text(find_element(By.XPATH, "//input[@placeholder='amount']"), withdraw_amount)
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Withdraw')]"))

    click_element(find_element(By.XPATH, "//button[contains(text(), 'Logout')]"))
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Home')]"))


def delete_customer(search_text):
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Bank Manager Login')]"))
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Customers')]"))
    input_text(find_element(By.XPATH, "//input[@placeholder='Search Customer']"), search_text)
    click_element(find_element(By.XPATH, "//button[contains(text(), 'Delete')]"))


def main():
    driver.maximize_window()
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    add_customer("Emin", "Abdullayev", "AZ1018")
    open_account("Emin Abdullayev", "Dollar")
    login_and_transact("Emin Abdullayev", "500", "200")
    delete_customer("Emin")


if __name__ == "__main__":
    main()
    driver.quit()
