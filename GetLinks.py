"""
This function will scrape the links for all U.S. state and top city locations on RateBeer.
Once the links are scraped, then we will iterate through each link and download the brewery
reviews

Inputs: 1. URL to page containing links (Can be any string)
Outputs: 1. Desired links to sub-pages
"""

def GetLinks(ParentURL):

    #import packages
    import requests
    from bs4 import BeautifulSoup
    import re
    import pandas as pd

    #URL to scrape links from
    url = ParentURL
    url = "https://www.ratebeer.com/breweries/"

    #Get html data and parse with BeautifulSoup
    page = requests.get(url, verify = False)
    soup = BeautifulSoup(page.text, "lxml")

    #Define regular expression to find links of interest
    link_regex = re.compile(r"(/breweries/)([\D|])+(/)([0-9]){1,2}(/213/)")

    #Search html data for all links
    links = soup.find_all("a", href = True)

    #Initialize list for desired links and iterate through all links to find the
    #ones that are of interest
    tlinks = []
    for link in links:
        if link_regex.search(str(link)) is not None:
            tlinks.append(link_regex.search(str(link)).group())
        else:
            pass

    #Create data frame of true or desired links
    #These include the links to all U.S. states and top cities containing brewery reviews
    tlinks = pd.DataFrame(tlinks, columns = ["links"])

    #Get number of links
    L = len(tlinks)

    #Join prefix to url
    for i in range(0,L,1):
        tlinks["links"][i] = "https://www.ratebeer.com" + tlinks["links"][i]

    return(tlinks)
