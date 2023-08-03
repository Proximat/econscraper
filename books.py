import os
import requests
from bs4 import BeautifulSoup as BS
import wget
import json
import gspread
import re

gc = gspread.service_account()
sh = gc.open("Dataset")
worksheet = sh.get_worksheet(0)
header_names = worksheet.row_values(1)

# Filter Rows based on score
score_idx = header_names.index('score')
rows_selection = []
for row in worksheet.get_all_values()[1:]:
    score_value = int(row[score_idx])
    if score_value > 50:
        rows_selection.append(row)

def search(query):
    search_base = "http://libgen.rs/search.php?req={}&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"
    search_page = search_base.format(query.replace(' ', '+'))
    page = requests.get(search_page)
    if page.status_code != 200:
        # TODO use the other mirror.
        pass
    raw_html = page.text
    soup = BS(raw_html, features='html5lib')
    
    results = []
    table_body = soup.find_all(valign="top")[1:]
    for row in table_body:
        item = {}
        download_links = row.find_all('a', href=True)
        item['url'] = [link['href'] for link in download_links if 'library.lol' in link['href']][0] # Direct download link
        tds = row.find_all('td')
        
        # Extracting authors
        authors = [a.get_text() for a in tds[1].find_all('a')]
        item['author'] = ', '.join(authors)
        
        # Extracting other details
        item['title'] = tds[2].get_text(strip=True)
        item['publisher'] = tds[3].get_text(strip=True)
        
        try:
            item['year'] = int(tds[4].text)
        except ValueError:
            item['year'] = tds[4].text
        
        item['pages'] = tds[5].text
        item['language'] = tds[6].text
        item['extension'] = tds[8].text
        
        results.append(item)
        
    return results

def decide(results):
    for ext in ['pdf', 'epub', 'mobi']:
        with_year = [result for result in results if result['extension'] == ext and type(result['year']) == int]
        without_year = [result for result in results if result['extension'] == ext and type(result['year']) != int]
        if with_year:
            selected_result = sorted(with_year, key=lambda i: i['year'], reverse=True)[0]
        elif without_year:
            selected_result = sorted(without_year, key=lambda i: i['year'], reverse=True)[0]
        else:
            continue
        return selected_result  # Return the selected result dictionary, not just the download_url
    return None



def download(url, save_name):
    print(f"Downloading {save_name}...")
    download_path = 'downloads/books'
    if not os.path.exists(download_path):
        os.makedirs(download_path)  # Create the directory if it doesn't exist
    save_path = os.path.join(download_path, save_name)
    wget.download(url, out=save_path)
    print(f"Downloaded to {save_path}")


def do_it_all(row):
    title = row['title']
    results = search(title)
    # if not results:
    #     author, title = query.split(',', 1)
    #     author_first_part = author.split()[0]
    #     title_shorter = title.split()[0]
    #     new_query = f"{author_first_part}, {title_shorter}"
    #     results = search(new_query)
    book = decide(results)
    print(book)
    if book:
        save_name = book['title'] + '.' + book['extension']
        download(book['url'], save_name)
        print(book, "✅Downloaded")
    else:
        print("❌ no download")


# Main script
for i, row in enumerate(rows_selection):
    row_dict = {header_names[j]: value for j, value in enumerate(row)}
    do_it_all(row_dict)

