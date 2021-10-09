import requests
import bs4

result = requests.get('https://www.example.com/')

#print(type(result))
'''
Si essentially what happened here is the request library that we downloaded goes and gets a response from https://www.example.com/
and we can actually then call result.text and it is an attribute. This will return the HTML of that page in a str format.
'''
#print(result.text)

# Now we are going to convert this in a soup with beautiful soup.
soup = bs4.BeautifulSoup(result.text, 'lxml')
#print(soup)

# Grab the title in the soup
site_title = soup.select("title") # Return a list of objects even if it returns only a result.
print(type(site_title))
print(site_title)

site_paragraphs = soup.select("p")
print(site_paragraphs)

# Grab the actual text (without the tags)
# For title
site_title = site_title[0].getText()
print(site_title)

# For paragraph
site_paragraph = site_paragraphs[0].getText()
print(site_paragraph)

# Grabbing a class
print("\n")
print("\n")

res = requests.get("https://es.wikipedia.org/wiki/Grace_Murray_Hopper")

soup1 = bs4.BeautifulSoup(res.text, "lxml")
index_content = soup1.select(".toctext")
new_index_content = [li_element.getText() for li_element in index_content]
print(new_index_content)

'''
    Syntax                                     Match Results
soup.select('div')                      All elements with 'div' tag
soup.select('#some_id')                 Elements containing id='some_id'
soup.select('.some_class')              Elements containing class='some_class'
soup.select('div span')                 Any elements named span within a div element.
soup.select('div > span')               Any elements named span DIRECTLY within a div element, with nothing in between.
'''

# Grabbing an image.
res_wiki = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup_wiki = bs4.BeautifulSoup(res_wiki.text, "lxml")
images_wiki = soup_wiki.select(".thumbimage")[0]
kasparov_picture = images_wiki['src']
print(kasparov_picture)

# Download the image
download_image = requests.get(f"https:{kasparov_picture}")
print(download_image.content) # See the raw content of the actual image. This is a binary file.

f = open("my_computer_image.png", 'wb')
f.write(download_image.content)
f.close()

