import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.django_db
@pytest.mark.selenium
def test_admin_user(create_admin_user):
    assert create_admin_user.username == "admin"




@pytest.mark.django_db
@pytest.mark.selenium
def test_admin_login(live_server,create_admin_user ,browser_instance_creating):
    selenium_driver = browser_instance_creating
    selenium_driver.get(f"{live_server.url}/admin/")
    username_input = selenium_driver.find_element(By.NAME, "username")
    password_input = selenium_driver.find_element(By.NAME, "password")
    login_button = selenium_driver.find_element(
            By.XPATH, '//input[@type="submit"]')

    username_input.send_keys("admin")
    password_input.send_keys("admin")
    login_button.click()

        # الانتظار حتى يتم تحميل الصفحة التالية

    assert "Site administration" in selenium_driver.page_source


												
										


