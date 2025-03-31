from playwright.async_api import TimeoutError as PlaywrightTimeoutError, Error as PlaywrightError
from time import sleep
from playwright_helpers import click_element_by_text
import _threshold_nav as nav
import os
from datetime import date

"""
The following function converts the month input (format most likely MM-YYYY) into
Month Year formatted string
"""
def month_to_string_converter(month):
    month_string = month.strftime("%B %Y")
    return month_string

"""
The following function downloads the monthly specials using a bunch of different
other written functions
"""
def download_monthly_specials(page, month, _format):
    month_string = month_to_string_converter(month)
    nav.sign_in(page)
    nav.navigate_to_monthly_specials(page)
    click_specific_month(page, month_string)
    filename = create_filename(month, _format)
    download_and_parse(page, filename)
    return filename


"""
The following picks whichever month the user chose
using the full string created by the date-to-string converter
created in the beginning of the program
"""
def click_specific_month(page, month):
    full_str = month + " Newsletter Specials in excel"
    page.get_by_role("link", name=full_str).click()


"""
This function creates a filename to save the file under
"""
def create_filename(month, _format):
    filename = "Newsletter Specials"
    return month + '_' + filename + _format


"""
The following function downloads and saves the file under
the filename stated in one of the parameters
"""
def download_and_parse(page, filename):
    with page.expect_download() as download_info:
        click_on_download_button(page)
    download = download_info.value
    ### these next few lines I wasn't sure what to put due to not knowing where specifically
    ### these files will be going, this is a placeholder.
    tilde = os.environ['HOME']
    filepath = tilde + '/datafeeds/products/threshold/downloads/' + filename
    download.save_as(filepath)


"""
This function is a download button clicker
"""
def click_on_download_button(page):
    page.get_by_role("link", name="Download File").click()
