############################ Start Imports #######################################
# Pandas -------- DataSience Lib, sorting manipulation of data etc.
import pandas as pd
 
#Beautifulsoup4 ------- Make the html code look pretty not messy
from bs4 import BeautifulSoup as bs

# Requests -------- For sending requests and getting the http responses for the webpages Html
import requests

#Return all non-overlapping matches of pattern in string, as a list of strings
import re
############################ END Imports #########################################








############################ ::START - Code:: #####################################
## 1 - Get html code
r = requests.get("https://en.wikipedia.org/wiki/Toy_Story_3") 


## 2 - Convert to beautiful soup object -------------------------------------------------->
soup = bs(r.content)
 
## Print html
#contents = soup.prettify()
#print(contents) # Print the whole phtml page






## 3 - Get the table infobox vevent by classes from the html------------------------------>
info_box = soup.find(class_="infobox vevent")
#print(info_box.prettify()) # Pritnt the info table html

info_rows = info_box.find_all("tr")
#for row in info_rows: # Get all rows and print them
#    print(row.prettify())








## 4 - Add it to Dictionary -- Helper Method - to get multiple names in tr --> li´s -------->
def get_content_value(row_data): # Get the row
    if row_data.find("li"): # if li in the row
        return [li.get_text(" ", strip=True).replace("\xa0", " ") for li in row_data.find_all("li")] # Get the data in all li´s as txt. Used for td where there is li's with multiple data like Writers: name1, name2 etc. etc.
    else:
        return row_data.get_text(" ", strip=True).replace("\xa0", " ") # Else get the data as txt and replace "\xa0" with space








## 5 - Add it to Dictionary ---------------------------------------------------------------->

movie_info = {} # Dictionary

for index, row in enumerate(info_rows): #info_rows = all <tr> elements
    if index == 0: # if index == 0 = title
        movie_info['title'] = row.find("th").get_text(" ", strip=True) # Get the Title
    elif index == 1:
        continue
    else:
        content_key = row.find("th").get_text(" ", strip=True) # Get the TableHead -  ex. Country, Language ..etc.
        content_value = get_content_value(row.find("td")) # Get the Value of every TableHead - ex. USA, English.. etc.
        movie_info[content_key] = content_value # Add the <th> and the <td> to the dictionary - headers and values

 
#print(movie_info) # Check the autput 













## Get all Movies ############################## ::START:: ########################################
## 2.1 - Make request and get the html
r_movies = requests.get("https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films")

 
###########################################################################################
## 2.2 - Convert to beautiful soup object -------------------------------------------------->
movies_soup = bs(r_movies.content) # The whole Html content
 
#movies_contents = movies_soup.prettify()
#print(movies_contents)


###########################################################################################
## 2.3 - Get all tables with the movies
movies_tables = movies_soup.select(".wikitable.sortable") # Get the tables by classes


# Links List
raw_movies_links = "" 
 
# Domain
domain = "https://en.wikipedia.org/wiki"

# Get all movies links
for table in movies_tables: 
    if table.find_all("i"): 
        raw_movies_links += str(table.find_all("i")) # All Raw links to string holder
 
#print(raw_movies_links) # Show links



 # Clean links list
filtered_movies_links = re.findall("href=[\"\'](.*?)[\"\']", raw_movies_links)
print(filtered_movies_links)



     
###########################################################################################


## 2.4 - Get the links of the movies





# -----------------TEST---------------------------------------------
#raw_movies_tbodys = movies_soup.find(class_="wikitable sortable jquery-tablesorter") 

 
## Tables
#movies_tbodys = raw_movies_tbodys.find_all("tbody")

#for table in movies_tbodys:
#    print(table.prettify())

 