############################ Start Imports #######################################
# Pandas -------- DataSience Lib, sorting manipulation of data etc.
import pandas as pd
 
#Beautifulsoup4 ------- Make the html code look pretty not messy
from bs4 import BeautifulSoup as bs

# Requests -------- For sending requests and getting the http responses for the webpages Html
import requests
############################ END Imports #########################################








############################ ::START - Code:: #####################################
## Get html code
r = requests.get("https://en.wikipedia.org/wiki/Toy_Story_3") 


# Convert to beautiful soup object -------------------------------------------------->
soup = bs(r.content)
 
## Print html
#contents = soup.prettify()
#print(contents) # Print the whole phtml page






## Get the table infobox vevent by classes from the html------------------------------>
info_box = soup.find(class_="infobox vevent")
#print(info_box.prettify()) # Pritnt the info table html

info_rows = info_box.find_all("tr")
#for row in info_rows: # Get all rows and print them
#    print(row.prettify())








## Add it to Dictionary -- Helper Method - to get multiple names in tr --> li´s -------->
def get_content_value(row_data): # Get the row
    if row_data.find("li"): # if li in the row
        return [li.get_text(" ", strip=True).replace("\xa0", " ") for li in row_data.find_all("li")] # Get the data in all li´s as txt. Used for td where there is li's with multiple data like Writers: name1, name2 etc. etc.
    else:
        return row_data.get_text(" ", strip=True).replace("\xa0", " ") # Else get the data as txt and replace "\xa0" with space








## Add it to Dictionary ---------------------------------------------------------------->

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

 
print(movie_info) # Check the autput 







