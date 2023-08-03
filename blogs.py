import os
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import gspread
from urllib.parse import urlparse, urlunparse
import re
import cleantext
from categories import publishers



gc = gspread.service_account()
sh = gc.open("Dataset")
worksheet = sh.get_worksheet(1)
header_names = worksheet.row_values(1)
#['file_name', 'url', 'info', 'status', 'score', 'category', 'title', 'author', 'tags', 'date', 'source']

rows = worksheet.get_all_records()  # Assuming the first column contains URLs and the second contains status

output_dir = 'downloads'
os.makedirs(output_dir, exist_ok=True)

def get_first_sentence(text):
    # Regular expression to match text before the first white line
    sentence_pattern = r"^(.*?)(?:\n\s*\n|\n)"

    # Find the first sentence before the first white line
    match = re.search(sentence_pattern, text, re.DOTALL)

    if match:
        first_sentence = match.group(1).strip()
        return first_sentence
    

def search_info(url):
    return

def sanitize_title(title, max_length=50):
    sanitized_title = re.sub(r'\W+', '_', title)
    return sanitized_title[:max_length]


def download_content(url, output_dir, row, row_id):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 403:
            row['status'] = "Error: 403"
        elif response.status_code == 406:
            row['status'] = "Error: 406" 
    except Exception as e:
        row['status'] = "Error: " + str(e)
        return list(row.values())

    # Archive.org
    if 'https://archive.org/details/' in url:

        ## Metadata
        if (row["title"] == '' or row["author"] == '' or row["date"] == ''):
            metadata_link = requests.get(url)
            metadata = BeautifulSoup(metadata_link.text, 'html.parser')
            date_element = metadata.find('span', itemprop='datePublished')
            if date_element is not None:
                row["date"] = date_element.text
            tags_element = metadata.find(itemprop='keywords')
            if tags_element is not None:
                tags = ', '.join([a.text for a in tags_element.find_all('a')])
                if tags is not None:
                    row["tags"] = tags
            title = metadata.find(itemprop="name").text
            if title is not None:
                row["title"] = title
            author_element = metadata.find(class_="metadata-definition")
            text_content = author_element.get_text()
            pattern = r"by\s+([^\d]+)"
            match = re.search(pattern, text_content)
            author = match.group(1).strip()
            if author is not None:
                row["author"] = author.rstrip(",")
            
        ## Download
        if row["status"] != "Success":
            id = url.split('/details/')[1].split('/')[0]
            download_url = f'https://archive.org/stream/{id}/{id}_djvu.txt'
            response = requests.get(download_url)
            print(row['title'])
            filename = f"{str(row_id).zfill(4)}_{row['title']}.pdf"
            with open(os.path.join(output_dir, filename), 'w') as f:
                f.write(response.text)  
                row["file_name"] = filename
                row["status"] = "Success"
        return list(row.values())
   
    # PDF
    elif url.endswith('.pdf'):
        if row["status"] != "Success":
            response = requests.get(url)
            filename = f"{str(row_id).zfill(4)}_{row['title']}.pdf"
            with open(os.path.join(output_dir, filename), 'wb') as f:
                f.write(response.content)
                row["file_name"] = filename
                row["status"] = "Success"
            return list(row.values())
   
 # Webpage
    else:
        if row["status"] != "Success":
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                for script_or_style in soup(["script", "style"]):
                    script_or_style.decompose()
                markdown_text = md(soup.prettify())
                words = markdown_text.split()
                custom_threshold = 300
                if len(words) > custom_threshold:

                    # Get Title
                    if len(row['title']) < 1:
                        title_tag = soup.find('h1') or soup.find('h2')
                        if title_tag:
                            row['title'] = title_tag.text.strip()

                    sanitized_title = sanitize_filename(row['title'])
                    filename = f"{str(row_id).zfill(4)}_{sanitized_title}.md"

                    #Find date
                    if 'date' in row and row['date'] is not None:
                        if len(str(row['date'])) < 1: 
                            year_pattern = r"(1[0-9]{3}|2[0-9]{3})"
                            match = re.search(year_pattern, markdown_text)
                            if match:
                                row["date"] = match.group(1)

                    #Category is Science?
                    if len(row['category']) < 1:
                        if url in publishers:
                            row['category'] =  "Science"              

                    #Prepare file
                    cleaned_markdown_text = cleantext.clean(markdown_text,
                        lower=False,                    
                        no_line_breaks=False,         
                        no_urls=True,                  
                        no_emails=True,               
                        no_phone_numbers=True,        
                        replace_with_url="",
                        replace_with_email="",
                        replace_with_phone_number=""
                        )
                    
                    with open(os.path.join(output_dir, filename), 'w') as f:
                        f.write(cleaned_markdown_text)
                        row["file_name"] = filename
                        row["status"] = "Success"

                else:
                    row["status"] = "Error: Article too short"
            except Exception as e:
                    row["status"] = "Error: " + str(e)
        return list(row.values())



# Main script
for i, row in enumerate(rows, start=2):
    if row['status'] == 'Success':
        continue
    url = row['url']
    new_row = download_content(url, output_dir, row, i)
    if new_row is not None:
        if new_row[3].startswith("Error: "):
            print(f"❌ for {new_row[2]} with error: {new_row[3]}")
        else:
            print(f"✅ Downloaded: {new_row[4]}")
            for j in range(len(new_row)):  # Fixing the loop here
                if isinstance(new_row[j], list):
                    new_row[j] = ''
        print(new_row)
        cell_range = f"A{i}:{chr(65+len(new_row))}{i}"
        worksheet.update(cell_range, [new_row])
        print(f"Row {i} updated")
    else:
        continue


