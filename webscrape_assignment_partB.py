import requests
from bs4 import BeautifulSoup

host = "https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"
hostNew = host[:-41]

"""
THE FOLLOWING CODE USES REQUESTS AND BEAUTIFULSOUP TO FIND AND DOWNLOAD
A WIKIPEDIA PAGE OF A GIVEN YEAR IN FILM. 
"""

def real_page_or_not_real(html_page, year):
    """
    The following function finds out if the page given is a real page with actual statistics. We do this
    by finding every div tag with the class listed below. If it does not have that class, it will return true, if not
    it returns false. (true meaning it is a real page, false meaning the opposite)
    """
    soup = BeautifulSoup(html_page, "html.parser")
    determiner = soup.find_all("div", class_ = "no-article-text-sister-projects")
    if len(determiner) <= 0:
        return True
    else:
        return False
def redirection_checker(html_page, year):
    """
    This function takes a html page content, and a year value (given by user)
    and determines whether or not it is a redirect based on if it has
    a 'span' class that is 'mw-redirectedfrom'
    """
    soup = BeautifulSoup(html_page, "html.parser")
    redirect = soup.find_all("span", class_ = "mw-redirectedfrom")
    if len(redirect) >= 1:
        return True
    else:
        return False

def get_html_file_wiki(page_content, year, session):
    """
    The following code retrieves the url of the wikipedia page based on the year that
    the user has inputted, and retrieves the page content of said page. Then, we use the page content
    to define 'keyword' a variable that will be used to name the html file that will eventually be downloaded.
    """
    url = new_url(year)
    page_content = getPageContent(session, url)
    url = determine_url(page_content, year)
    page_content = getPageContent(session, url)
    keyword = redefine_keyword(page_content,year)
    print(keyword)
    download_html_file(page_content, keyword + ".html")

def download_html_file(page_content, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(page_content)

def redefine_keyword(page_content,year):
    """
    The following code defines the name that will be used for the final html file,
    it will first check if it is a redirected page, then based on that it will choose
    the necessary name, (just the year for the regular page, and the broader term for
    the redirected page, ex: (2004) or (1870s in film)
    """
    soup = BeautifulSoup(page_content, "html.parser")
    keyword = soup.find_all("span", class_ = "mw-page-title-main")
    redirect = redirection_checker(page_content, year)
    if redirect is True:
        for i in keyword:
            return i.text
    else:
        return year

def getPageContent(session, url):
    return session.get(url).text

def determine_url(html_page,year):
    """
    The following code determines the URL while checking to see if it
    is a real page by using the real_page_or_not_real function. If it not a
    real page, then a system exit occurs, if else then a new URL is returned
    """
    newUrl = hostNew + "/wiki/" + year + "_in_film"
    errorMessage = "Your page does not exist."
    determiner = real_page_or_not_real(html_page, year)
    if determiner is True:
        return newUrl
    else:
        print(errorMessage)
        exit()

def new_url(year):
    theNew = hostNew + "/wiki/" + year + "_in_film"
    return theNew

def main():
    session = requests.session()
    year_input = str(input("What year would you like to find a url from this page?: "))

    host_new = get_html_file_wiki(host,year_input,session)

if __name__ == "__main__":
    main()