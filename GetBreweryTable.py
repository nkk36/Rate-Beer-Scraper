"""
FUNCTION DESCRIPTION

Inputs: 
Outputs: 
"""

def GetBreweryTable(links,j):

    #Import packages
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import numpy as np
    import re
    import datetime

    #Get url and scrape data
    url = links["link"][j]
    page = requests.get(url, verify = False)
    soup = BeautifulSoup(page.text, "lxml")
    
    #Get brewery name and city name and list of active breweries
    brewT = soup.find_all('table', attrs = {"id": "brewerTable"})[0].find_all("a")
    
    #Get brewery type and estimated year of opening
    BType = soup.find_all("td", attrs = {"class":"hidden-xs hidden-sm"})
    EstB = soup.find_all("td", attrs = {"style":"color:#ccc;text-align:right;"})
    
    #Get number of active breweries
    numRegex = re.compile(r"\d{1,4}")
    numactive = int(numRegex.search(soup.find_all("a", href = "#active")[0].text).group())
    
    #Obtain data from scraped html
    BreweryName = []
    CityName =[]
    BreweryType = []
    Est = []
    Link = []
    for i in range(0,numactive):
        BreweryName.append(brewT[2*i].text.strip())
        CityName.append(brewT[2*i+1].text.strip())
        BreweryType.append(BType[i].text.strip())
        Est.append(EstB[i].text.strip())
        Link.append("https://www.ratebeer.com"+brewT[2*i]["href"])
    
    #Get number of beers from scraped html
    NBeer = []
    for rows in soup.find_all("td"):
        NBeer.append(rows.text)
    NumBeer = NBeer[2:len(NBeer):5]
        
    #Fill data frame
    df = pd.DataFrame(np.reshape([0]*numactive*8,(numactive,8)), columns = ["Brewery","City" ,"State","Type","Est","NumBeer", "Link","DateCollected"])
    df["Brewery"] = pd.DataFrame(BreweryName)
    df["City"] = pd.DataFrame(CityName)
    df["State"] = pd.DataFrame([links["location"][j]]*numactive)
    df["Type"] = pd.DataFrame(BreweryType)
    df["Est"] = pd.DataFrame(Est)
    df["NumBeer"] = pd.DataFrame(NumBeer)
    df["Link"] = pd.DataFrame(Link)
    df["DateCollected"] = pd.DataFrame([datetime.date.today()]*numactive)

    return(df)
