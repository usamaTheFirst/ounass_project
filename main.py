from selenium import webdriver

from BagTest import BagTest
from Login import Login
from Signup import Signup

driver = webdriver.Chrome()

# signup = Signup(driver)
# signup.go()
# signup.first_name.input_text('usama')
# signup.last_name.input_text('fiaz')
# signup.email.input_text('lobihi1869@zevars.com')
# signup.password.input_text('<@pass12/>')
# signup.create_account.click_button()

login = Login(driver)
login.email.input_text('lobihi1869@zevars.com')
login.password.input_text('<@pass12/>')
login.login_button.click_button()
# login.customer_setting.click_button()
# login.edit.click_button()
#
# print(login.email_verification.is_editable())
# print(login.email_verification.get_attribut())

bag = BagTest(driver)
bag.go()
bag.select_color.click_button()
bag.select_size()
bag.add_to_bag.click_button()
bag.go_to_bag.click_button()
bag.checkout.click_button()
bag.enter_phone_number.input_text('50122134')
bag.select_size()
bag.select_emirate()
bag.enter_area('Al Zahiyah, Abu Dhabi Mall')

bag.enter_street.input_text('abdjd d')
bag.apartment.input_text('diksdj sldi')
bag._continue.click_button()

