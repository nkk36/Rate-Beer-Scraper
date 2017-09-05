"""
FUNCTION DESCRIPTION

Inputs: 
Outputs: 
"""

def GetBeerReviews(link):
    
    #Import packages
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import numpy as np
    import datetime


    #Get url and scrape data
    url = "https://www.ratebeer.com/beer/founders-porter/3173/430545/"#link
    page = requests.get(url, verify = False)
    soup = BeautifulSoup(page.text, "lxml")
    
    #Get beer and brewery name
    BBName = soup.find_all("span", attrs = {"itemprop":"name"})
    BeerName = BBName[0].text
    BreweryName = BBName[1].text
    
    #Get city and state location
    CityState = soup.find_all("div", attrs = {"class":"row description-container"})[0].find_all("a")
    CityName = CityState[2].text
    StateName = CityState[3].text
    
    #Get number of ratings, average, weighted average, seasonal, calories, ABV
    NumRatings = soup.find_all("big", attrs = {"style":"color: #777;"})
    NumRating = NumRatings[0].text
    AvgRating = NumRatings[1].text
    WAvgRating = NumRatings[2].text
    Seasonal= NumRatings[3].text
    Calories = NumRatings[4].text
    ABV = NumRatings[5].text   
    
    #Get commercial description
    ComDesc = soup.find_all("span", attrs = {"id":"_description3", "itemprop":"description"})[0].text
    
    #Get reviews
    Reviews = []
    GetReviews = soup.find_all("div", attrs = {"style":"padding: 20px 10px 20px 0px; border-bottom: 1px solid #e0e0e0; line-height: 1.5;"})
    for i in range(0, len(GetReviews)):
        Reviews.append(GetReviews[i].text)
    
    #Get ratings
    Ratings = []
    GetRatings = soup.find_all("div", attrs = {"style":"display:inline; padding: 0px 0px; font-size: 24px; font-weight: bold; color: #036;"})
    for i in range(0, len(GetRatings)):
        Ratings.append(GetRatings[i].text)
    
    numratings = len(Ratings)
    
    #Fill data frame
    df = pd.DataFrame(np.reshape([0]*14*numratings,(numratings,14)), \
                      columns = ["Beer", "Brewery" ,"City", "State", "NumRating", "AvgRating", "WAvg", "Seasonal", "Calories", "ABV", \
                                 "Reviews","Ratings","ComDesc", "DateCollected"])
    df["Beer"] = pd.DataFrame([BeerName]*numratings)
    df["Brewery"] = pd.DataFrame([BreweryName]*numratings)
    df["City"] = pd.DataFrame([CityName]*numratings)
    df["State"] = pd.DataFrame([StateName]*numratings)
    df["NumRating"] = pd.DataFrame([NumRating]*numratings)
    df["AvgRating"] = pd.DataFrame([AvgRating]*numratings)
    df["WAvg"] = pd.DataFrame([WAvgRating]*numratings)
    df["Seasonal"] = pd.DataFrame([Seasonal]*numratings)
    df["Calories"] = pd.DataFrame([Calories]*numratings)
    df["ABV"] = pd.DataFrame([ABV]*numratings)
    df["ComDesc"] = pd.DataFrame([ComDesc]*numratings)
    df["DateCollected"] = pd.DataFrame([datetime.date.today()]*numratings)
    
    for i in range(0, numratings):
        df["Reviews"][i] = Reviews[i]
        df["Ratings"][i] = Ratings[i]

    
    return(df)  