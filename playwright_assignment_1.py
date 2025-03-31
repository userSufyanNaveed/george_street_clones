from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright, x=" ") -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.youtube.com/")
    page.get_by_placeholder("Search").click()
    page.get_by_placeholder("Search").fill(x)
    page.get_by_placeholder("Search").press("Enter")
    page.wait_for_selector(".style-scope ytd-video-renderer")
    page.locator(".style-scope ytd-video-renderer").first.click()
    ## I couldn't find a way to full screen the video easily, it often times just misses or doesn't click
    ## the button


    ##page.hover("Full screen keyboard shortcut f")
    ##page.wait_for_selector("Full screen keyboard shortcut f")
    ##page.keyboard.press('F')
    ##page.get_by_label("Full screen keyboard shortcut f").click()

    context.close()
    browser.close()


def main():
    x = str(input("What would you like to put in the YouTube search bar? "))
    with sync_playwright() as playwright:
        run(playwright, x)


if __name__ == "__main__":
    main()