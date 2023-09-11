import requests
from bs4 import BeautifulSoup as bs
import json
import re

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-63486521-27ea95a10f3ccd69476b99e1"
  }
  
  
def search_faculty():
    url = "https://www.cs.stonybrook.edu/people/faculty"
    html_text = requests.get(url, headers = headers)
    soup=bs(html_text.content,"lxml")
    soup=bs(soup.prettify(),"lxml")
    items=soup.find('div', class_="item-list")
    items = items.find('ul')
    items = items.find_all('div', class_= "views-field views-field-title")
    for count,each in enumerate(items):
        try:
            Prof_link = each.find('a')['href']
            Prof_name = each.text.strip()
            Prof_link_url = "https://www.cs.stonybrook.edu/" + Prof_link
            if (count == 0):
                f_url = open('bio_urls.txt','w')
            else: f_url = open('bio_urls.txt','a')
            url_line = "{} {}".format(Prof_name, Prof_link_url)
            f_url.write(url_line)
            f_url.write('\n')
            f_url.close()
            try:
                if (count == 0):
                    f_bio = open('bios.txt','w')
                else: f_bio = open('bios.txt','a')
                html_text = requests.get(Prof_link_url, headers = headers)
                soup=bs(html_text.content,"lxml")
                soup=bs(soup.prettify(),"lxml")
                bio_field = soup.find('div', class_="field field-name-field-biography field-type-text-with-summary field-label-hidden")
                bio = bio_field.find('p').text.strip()
                bio = re.sub(r'\s+', ' ',bio)
                bio = "Biography: "+ bio
                bio_line = "{} {}".format(Prof_name,bio)
                f_bio.write(bio_line)
                f_bio.write("\n")
                f_bio.write("*****")
                f_bio.write("\n")
                f_bio.close()
            except:
                if (count == 0):
                    f_bio = open('bios.txt','w')
                else: f_bio = open('bios.txt','a')
                bio = "Bio of professor is not present in website"
                f_bio.write(bio)
                f_bio.write("\n")
                f_bio.write("*****")
                f_bio.write("\n")
                f_bio.close()
            try:
                if (count == 0):
                    f_taught = open('courses_taught.txt','w')
                else: f_taught = open('courses_taught.txt','a')
                html_text = requests.get(Prof_link_url, headers = headers)
                soup=bs(html_text.content,"lxml")
                soup=bs(soup.prettify(),"lxml")
                teach_field = soup.find('div', class_="field field-name-field-teachingsummary field-type-text field-label-hidden")
                courses = teach_field.find('div', class_="field-items").text.strip()
                courses = re.sub(r'\s+', ' ',courses)
                courses = "courses they teach: "+ courses
                taught_line = "{} {}".format(Prof_name,courses)
                f_taught.write(taught_line)
                f_taught.write("\n")
                f_taught.close()
            except:
                if (count == 0):
                    f_taught = open('courses_taught.txt','w')
                else: f_taught = open('courses_taught.txt','a')
                courses = "Courses they teach not listed in Website"
                taught_line = "{} {}".format(Prof_name,courses)
                f_taught.write(taught_line)
                f_taught.write("\n")
                f_taught.close()
        except: pass

    
search_faculty()
  
