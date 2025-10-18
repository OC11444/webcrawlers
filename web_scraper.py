import requests 
from bs4 import BeautifulSoup
import csv 

url='https://books.toscrape.com/'  ##target  website 
response=requests.get(url) #get the webpage

#turn /parse messy html into a beautiful soup object
soup=BeautifulSoup(response.text,'html.parser')

#find the title of the webpage
print(soup.title.string)

#find all the book titles on the webpage
book_elements = soup.find_all('h3')

#open a new file to write to and write rows while file is open
with open('book_titles.csv','w',newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Book Title'])  # write header row

    # clean messy html output to get only book titles
    for book_elem in book_elements:
        # inside the h3 find the <a> tag and get the title attribute
        title = book_elem.a['title']
        writer.writerow([title])  # write book title to csv file

print("finished writing to book_titles.csv")