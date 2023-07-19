import os
import requests
from bs4 import BeautifulSoup as BS
import wget


def cls():
    """Wipes the screen altogether. Works on Linux BASH and Windows Command Line.
    Should also work on Mac OS, not sure."""
    os.system('cls' if os.name == 'nt' else 'clear')


def search(query):
    ## Returns a list of dictionaries containing the search results from libgen.rs.
    search_base = "http://libgen.rs/search.php?req={}&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"
    search_page = search_base.format(query.replace(' ', '+'))
    page = requests.get(search_page)
    raw_html = page.text
    soup = BS(raw_html, features='html5lib')
    results = []
    table_body = soup.find_all(valign="top")[1:]
    for row in table_body:
        item = {}
        data = row.findAll(width="500")
        for record in data:
            href = record.find(name='a').get('href')
            item['url'] = 'http://libgen.rs/' + href
        tds = row.find_all('td')
        tds = [td.text for td in tds]
        item['author'] = tds[1]
        item['title'] = tds[2]
        item['publisher'] = tds[3]
        try:
            item['year'] = int(tds[4])
        except ValueError:
            item['year'] = tds[4]
        item['pages'] = tds[5]
        item['language'] = tds[6]
        try:
            if 'mb' in tds[7].lower():
                item['size'] = float(tds[7].split()[0])
            elif 'kb' in tds[7].lower():
                item['size'] = float(tds[7].split()[0]) / 1000
        except ValueError:
            item['size'] = tds[7]
        item['extension'] = tds[8]
        results.append(item)
    return results


def decide(results):
    ## Returns the most recent PDF result, or the most recent EPUB result if no PDFs are found.
    if results != []:
        epubs_with_year = []
        epubs_without_year = []
        for result in results:
            if result['extension'] == 'epub':
                if type(result['year']) == int:
                    epubs_with_year.append(result)
                else:
                    epubs_without_year.append(result)
            else:
                pass
        epubs = sorted(epubs_without_year,
                       key=lambda i: i['year'], reverse=True)
        if epubs_with_year != []:
            return epubs_with_year[0]
        elif epubs_without_year != []:
            return epubs[0]
        else:
            pdfs_with_year = []
            pdfs_without_year = []
            for result in results:
                if result['extension'] == 'pdf':
                    if type(result['year']) == int:
                        pdfs_with_year.append(result)
                    else:
                        pdfs_without_year.append(result)
                else:
                    pass
            pdfs = sorted(pdfs_without_year,
                           key=lambda i: i['year'], reverse=True)
            if pdfs_with_year != []:
                return pdfs_with_year[0]
            elif pdfs_without_year != []:
                return pdfs[0]
            else:
                return None
    else:
        return None

def download(url, save_name):
    ###Downloads the file at the given URL and saves it as the given file name.
    print(f"Downloading {save_name}...")
    wget.download(url, out=save_name)


def log_download(book, mirror, save_name):
    """Logs the download of the book to a AIRTABLE."""
    # https://airtable.com/shrfhyd0hiRYYbnW6
    # https://airtable.com/appHTvuP660oTKhCl/tblElnRb1VtSuvmJY/viwiD6Rgq1rcGOujn?blocks=hide
    # API KEY: patW3oFhNZjcIsWOO.c38b88dd3f6ac0123a28480621ac4a38637e92e717ce22b074e2ef545a362cdb


def main():
    ##The main function of the script.
    cls()
    mirror = input("Select your preferred mirror.\n"
                   "1. Gen.lib.rus.ec\n"
                   "2. Libgen.lc\n> ")
    if mirror == "1":
        mirror = "gen-lib-rus-ec"
    elif mirror == "2":
        mirror = "libgen-lc"
    else:
        print("Invalid mirror.")
        return
    books = []
    url = "https://api.airtable.com/v0/appHTvuP660oTKhCl/tblElnRb1VtSuvmJY"
    headers = {
        "Authorization": "Bearer patW3oFhNZjcIsWOO.c38b88dd3f6ac0123a28480621ac4a38637e92e717ce22b074e2ef545a362cdb"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    for record in data["records"]:
        book = {
            "title": record["fields"]["Title"],
            "author": record["fields"]["Author"],
            "downloaded": record["fields"]["Downloaded"]
        }
        books.append(book)
    for book in books:
        if book["downloaded"] is False:
            do_it_all(book, mirror)
    print("BOOK LIST:")
    for book in books:
        downloaded_status = "Downloaded" if book["downloaded"] else "Not Downloaded"
        print(f"Title: {book['title']}\nAuthor: {book['author']}\nStatus: {downloaded_status}")


def main():
    ##The main function of the script.
    cls()
    mirror = input("Select your preferred mirror.\n"
                   "1. Gen.lib.rus.ec\n"
                   "2. Libgen.lc\n> ")
    if mirror == "1":
        mirror = "gen-lib-rus-ec"
    elif mirror == "2":
        mirror = "libgen-lc"
    else:
        print("Invalid mirror.")
        return
    books = []
    with open("book-list.txt", "r") as f:
        for line in f:
            book = json.loads(line)
            books.append(book)
    for book in books:
        if book["downloaded"] is False:
            do_it_all(book, mirror)
    print("BOOK LIST:")
    for book in books:
        downloaded_status = "Downloaded" if book["downloaded"] else "Not Downloaded"
        print(f"Title: {book['title']}\nAuthor: {book['author']}\nStatus: {downloaded_status}")


if __name__ == "__main__":
    main()