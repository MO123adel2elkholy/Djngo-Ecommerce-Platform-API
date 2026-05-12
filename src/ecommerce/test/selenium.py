from django.contrib.auth.models import User
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def browser_instance_creating():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    yield driver

    driver.quit()


@pytest.fixture
def create_test_user(db):
    """
    Fixture to create a test user in the database.
    """
    user = User.objects.create_user(
        username='testuser', password='password123')
    print("Test user created with username:", user.username)
    return user
# Additional fixtures can be added here as needed for other tests.

# We can use fixcure as afactory to create multiple users with different attributes.


@pytest.mark.selenium
def user_factory_fixture(db):
    pass 








# arrange fixture for selenium driver Phase1







