"""
FUNCTION DESCRIPTION

Inputs: 
Outputs: 
"""

def GetBreweryBeerTable(link, brewery, city, state):
    
    #Import packages
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import numpy as np
    import datetime
    import re

    #Get url and scrape data
    url = link
    page = requests.get(url, verify = False)
    soup = BeautifulSoup(page.text, "lxml")
    
    if soup.find_all("div", attrs = {"style":"margin:20px 0 0 20px;"}) == []:
        pass
    else:
        url = "https://www.ratebeer.com"+soup.find_all("div", attrs = {"style":"margin:20px 0 0 20px;"})[0].find_all("a")[0]["href"]
        page = requests.get(url, verify = False)
        soup = BeautifulSoup(page.text, "lxml")
        
    #Get brewery name and location
    #GetTitle = soup.find("title")
    #TitleLoc = GetTitle.text.split("|")[0].strip().split(", ")
    BreweryName = brewery#TitleLoc[0]
    CityName = city#TitleLoc[1]
    StateName = state#TitleLoc[2]
    
    #Get less opaque links    
    OpaqueLinks = soup.find_all("tr", attrs = {"class":"less-opaque"})
    LOpaqLinks = len(OpaqueLinks)
    DeleteBeers = []
    for i in range(0,LOpaqLinks):
        if OpaqueLinks[i].find("em", attrs={"class":"small"}) is not None:
            DeleteBeers.append(OpaqueLinks[i].find("a").text)
        else:
            pass
    DeleteBeers = pd.DataFrame(DeleteBeers)   
    
    #Get list of all active beer names, type, ABV, date added, and links to their reviews
    BeerList = soup.find_all("td", attrs = {"width":"50%"})
    DateAdd = soup.find_all("td", attrs = {"class":"real-small"})
    LBeerList = len(BeerList)
    BeerName = []
    BeerType = []
    BeerABV = []
    abvregex = re.compile(r"(\d)(\.)*(\d)*")
    DateAdded = []
    Links = []
    for i in range(0,LBeerList):
        BName = BeerList[i].find("a").text
        if not DeleteBeers.empty:
            TF = DeleteBeers.apply(lambda x: x == BName).sum(axis = 0)[0]
            if TF == 1:
                pass
            else:
                BeerName.append(BeerList[i].find("a").text)
                BeerType.append(BeerList[i].find("span").text)
                if abvregex.search(BeerList[i].find("div").text) is None:
                    abv = "N/A"
                else:
                    abv = abvregex.search(BeerList[i].find("div").text).group()
                BeerABV.append(abv)
                DateAdded.append(DateAdd[i].text)
                Links.append("https://www.ratebeer.com"+BeerList[i].find("a")["href"])
        else:
            BeerName.append(BeerList[i].find("a").text)
            BeerType.append(BeerList[i].find("span").text)
            BeerABV.append(BeerList[i].find("div").text[0:4])
            DateAdded.append(DateAdd[i].text)
            Links.append("https://www.ratebeer.com"+BeerList[i].find("a")["href"])
    
    #Get list of beer average score, style, and number of ratings
    ScoreNumRating = soup.find_all(lambda tag: tag.name == 'td' and 
                                   tag.get('class') == ['text-left'])
    StyleHTML = soup.find_all("td", attrs = {"class":"small", "align":"center"})  
    ScoreHTML = ScoreNumRating[0:len(ScoreNumRating):2]
    NumRatingHTML = ScoreNumRating[1:len(ScoreNumRating):2]
    Score = []
    Style = []
    NumRating = []
    L = len(StyleHTML)
    for i in range(0,L):
        Score.append(ScoreHTML[i].text)
        Style.append(StyleHTML[i].text)
        NumRating.append(NumRatingHTML[i].text)
    
    #Get number of active beers
    numactive = len(BeerName)
    
    #Fill data frame
    df = pd.DataFrame(np.reshape([0]*numactive*12,(numactive,12)), columns = ["Beer", "Type" ,"ABV", "DateAdded", "Score", "Style", "NumRating", "Brewery", "City", "State", "Link","DateCollected"])
    df["Beer"] = pd.DataFrame(BeerName)
    df["Type"] = pd.DataFrame(BeerType)
    df["ABV"] = pd.DataFrame(BeerABV)
    df["DateAdded"] = pd.DataFrame(DateAdded)
    df["Score"] = pd.DataFrame(Score)
    df["Style"] = pd.DataFrame(Style)
    df["NumRating"] = pd.DataFrame(NumRating)
    df["Brewery"] = pd.DataFrame([BreweryName]*len(df))
    df["City"] = pd.DataFrame([CityName]*len(df))
    df["State"] = pd.DataFrame([StateName]*len(df))
    df["Link"] = pd.DataFrame(Links)
    df["DateCollected"] = pd.DataFrame([datetime.date.today()]*numactive)
    
    return(df)