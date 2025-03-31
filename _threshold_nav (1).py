from time import sleep
from playwright.async_api import TimeoutError as PlaywrightTimeoutError, Error as PlaywrightError
from playwright_helpers import *

goto_url = "https://www.thresholdenterprises.com"

def read_password(filename):
    with open(filename, "r") as f:
        return f.readline().rstrip("\n")
"""
The following sign_in function signs in to the thresholdenterprises website itself
using our username and password
"""
def sign_in(page):
    signin_url = "https://www.thresholdenterprises.com"
    credentials = {"username": "ordering@georgestreetcoop.com",
                   "password": "XXXXXXXXXX"}
    page.goto(signin_url)
    page.get_by_role("link", name="Login").click()
    page.wait_for_load_state(state="load")
    sleep(4)
    page.fill("#accountsEmail", credentials["username"])
    page.fill("#accountsPassword", credentials["password"])
    page.fill("#accountsKeepauth").check()
    page.get_by_role("button", name="Submit").click()
    page.wait_for_load_state(state="load")

def navigate_to_monthly_specials(page):
    page.goto(goto_url)
    page.get_by_role("link", name="Download Center").click()
    page.get_by_role("link", name="Monthly Specials").click()
    page.wait_for_load_state(state="load")

def navigate_to_threshold_pricing(page):
    page.goto(goto_url)
    page.get_by_role("link", name="Threshold Pricing").click()

def log_out(page):
    page.get_by_role("link", name="Logout").click()


