import requests
import re
from bs4 import BeautifulSoup

host = "https://www.scrapethissite.com"

def downloadWikiPage(session, download_url, filename):
    response = session.get(download_url)
    if response.status_code == 200:
        page_content = response.text
        with open(filename, "w", encoding="utf-8") as file:
            file.write(page_content)
        print("Successfully downloaded!")
    else:
        errorMessage(f"Failed to download {download_url} with response status {response.status_code}")
def errorMessage(message):
    print("Error: " + message)

def getPageContent(session, url):
    return session.get(url).text

def urlNavigator(html_page, keyword):
    soup = BeautifulSoup(html_page, "html.parser")
    keyword = keyword.lower()
    for tag in soup.find_all("a"):
        if tag.string is not None and tag.string.lower().find(keyword) >= 0:
            return host + tag["href"]
    return keyword

def main():
    session = requests.session()
    sandboxUrl = host + "/pages/"
    wikiUrl = 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'
    get_webscrape_page = getPageContent(session, host)
    get_sandbox_page = getPageContent(session, sandboxUrl)

    winning_films_scrape_url = urlNavigator(get_sandbox_page, keyword="Oscar Winning Films: AJAX and Javascript")
    get_films_page = getPageContent(session, winning_films_scrape_url)

    find_wikipedia_url = urlNavigator(get_films_page, keyword=wikiUrl + ' ')
    getPageContent(session, find_wikipedia_url)

    filename = "award-winning-films-by-year.html"
    downloadWikiPage(session, wikiUrl, filename)
    session.close()


if __name__ == "__main__":
    main()
