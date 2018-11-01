import bs4
from requests import get
import random
import webbrowser

def URLgen(model,size):
    base_size = 640
    shoe_size = size - 9.5
    raw_size = int((shoe_size * 20) + base_size)
    url = "http://www.adidas.com/us/" + str(model) + ".html?forceSelSize=" + str(model) + "_" + str(raw_size)
    return url

def check_stock(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    raw_html = requests.get(url,headers=headers)
    page = bs4.BeautifulSoup(raw_html.text,"lxml")

    #SelectorGadget to pull CSS code.
    list_raw_sizes = page.select(".size-dropdown-block")

    #Organizing the pulled text.
    sizes = str(list_raw_sizes[0].getText()).replace("\t","")
    sizes = sizes.replace("\n\n"," ")
    sizes.split() #Splits text by default parameter (space).
    sizes.remove("Select")
    sizes.remove("size")
    for size in sizes:
        print(str(model) + "Size:" + str(size) + "Available")

def main(model,size):
    url = URLgen()
    check_stock(url)