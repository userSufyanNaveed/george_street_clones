from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep

host = "https://www.thresholdenterprises.com"


def run(playwright: Playwright) -> None:
    credentials = {"username": "ordering@georgestreetcoop.com",
                   "password": "XXXXXXXXXXXX"}
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(host)
    page.get_by_role("link", name="Login").click()
    page.wait_for_load_state(state="load")
    sleep(4)
    page.locator("#accountsEmail").fill(credentials["username"])
    page.locator("#accountsPassword").fill(credentials["password"])
    page.locator("#accountsKeepauth").check()
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("link", name="Threshold Pricing").click()
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download the pricelist").click()
    download = download_info.value
    sleep(2)

    context.close()
    browser.close()

def main():
    with sync_playwright() as playwright:
        run(playwright)

if __name__ == "__main__":
    main()