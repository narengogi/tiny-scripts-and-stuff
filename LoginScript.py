# This was probably the first practical program I ever wrote.
# I find it funy now, how hard it felt then
# But it was everybit worth it! 


from selenium import webdriver

driver = webdriver.Edge()

driver.get("172.16.104.64")

driver.implicitly_wait(5)

driver.find_element_by_id("moreInformationDropdownSpan").click()

driver.find_element_by_id("invalidcert_continue").click()

driver.find_element_by_id("user.username").send_keys('vinnakota.cs17')

driver.find_element_by_id("user.password").send_keys('7/12/1999')

driver.find_element_by_id("ui_login_signon_button").click()

driver.find_element_by_id("ui_post_access_continue_button").click()

driver.quit()
