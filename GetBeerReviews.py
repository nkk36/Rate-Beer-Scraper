"""
FUNCTION DESCRIPTION

Inputs: 
Outputs: 
"""

def GetBeerReviews(link, beer, brewery, city, state):
    
    #Import packages
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import numpy as np
    import datetime


    #Get url and scrape data
    url = link #https://www.ratebeer.com/beer/founders-porter/3173/"
    page = requests.get(url, verify = False)
    soup = BeautifulSoup(page.text, "lxml")
    
    #Get beer, brewery, city, and state
    BeerName = beer
    BreweryName = brewery
    CityName = city
    StateName = state
    
    #Get number of ratings, average, weighted average, seasonal, calories, ABV
#    BeerReviewInfo = soup.find_all("big", attrs = {"style":"color: #777;"})
#    NumRating = BeerReviewInfo[0].text
#    WAvgRating = BeerReviewInfo[1].text
#    IBU = BeerReviewInfo[2].text
#    Calories = BeerReviewInfo[3].text
#    ABV = BeerReviewInfo[4].text   
    
#    #Get commercial description
#    if soup.find_all("span", attrs = {"id":"_description3", "itemprop":"description"}) != []:
#        ComDesc = soup.find_all("span", attrs = {"id":"_description3", "itemprop":"description"})[0].text
#    else:
#        ComDesc = "N/A"
    
    #Get number of pages of reviews
    ExtraReviews = soup.find_all("a", attrs = {"class":"ballno"})
    if ExtraReviews != []:
        NumPages = int(ExtraReviews[len(ExtraReviews) - 1].text)
    else:
        NumPages = 1
        
    #Create data frame
    df = pd.DataFrame(columns = ["User", "Review"])
        
    ReviewsContainer = soup.find_all("div", attrs = {"class":"reviews-container"})
    if ReviewsContainer == []:
        return("No")
    NReviews = len(ReviewsContainer[0].find_all("div", attrs = {"style":"padding: 20px 10px 20px 0px; border-bottom: 1px solid #e0e0e0; line-height: 1.5;"}))
    for i in range(0, NReviews):
        user = soup.find_all("div", attrs = {"style":"padding: 0px 0px 0px 0px;"})[i].find_all("img")[0]["src"]
        IndividualReviews = ReviewsContainer[0].find_all("div", attrs = {"style":"padding: 20px 10px 20px 0px; border-bottom: 1px solid #e0e0e0; line-height: 1.5;"})[i].text
        df = df.append(pd.DataFrame(np.reshape([user, IndividualReviews],(1,2)), columns = ["User", "Review"]))                                    
    if NumPages > 1:
        for i in range(0, NumPages - 2):
            url = "https://ratebeer.com"+ExtraReviews[0]["href"][0:len(ExtraReviews[0]["href"]) - 2]+str(i + 2)+"/"
            page = requests.get(url, verify = False)
            soup = BeautifulSoup(page.text, "lxml")
            ReviewsContainer = soup.find_all("div", attrs = {"class":"reviews-container"})
            NReviews = len(ReviewsContainer[0].find_all("div", attrs = {"style":"padding: 20px 10px 20px 0px; border-bottom: 1px solid #e0e0e0; line-height: 1.5;"}))
            for j in range(0, NReviews):
                user = soup.find_all("div", attrs = {"style":"padding: 0px 0px 0px 0px;"})[j].find_all("img")[0]["src"]
                IndividualReviews = ReviewsContainer[0].find_all("div", attrs = {"style":"padding: 20px 10px 20px 0px; border-bottom: 1px solid #e0e0e0; line-height: 1.5;"})[j].text
                df = df.append(pd.DataFrame(np.reshape([user, IndividualReviews],(1,2)), columns = ["User", "Review"]))  
    
    df["Beer"] = [BeerName]*len(df)
    df["Brewery"] = [BreweryName]*len(df)
    df["City"] = [CityName]*len(df)
    df["State"] = [StateName]*len(df)
    
#    #Get reviews
#    Reviews = []
#    GetReviews = soup.find_all("div", attrs = {"style":"padding: 20px 10px 20px 0px; border-bottom: 1px solid #e0e0e0; line-height: 1.5;"})
#    for i in range(0, len(GetReviews)):
#        Reviews.append(GetReviews[i].text)
#    
#    #Get ratings
#    Ratings = []
#    GetRatings = soup.find_all("div", attrs = {"style":"display:inline; padding: 0px 0px; font-size: 24px; font-weight: bold; color: #036;"})
#    for i in range(0, len(GetRatings)):
#        Ratings.append(GetRatings[i].text)
#    
#    numratings = len(Ratings)
    
    #Fill data frame
#    df = pd.DataFrame(np.reshape([0]*6,(1,6)), \
#                      columns = ["Beer", "Brewery" ,"City", "State","ComDesc","User","Review", "DateCollected"])
#    df["Beer"] = pd.DataFrame([BeerName])
#    df["Brewery"] = pd.DataFrame([BreweryName])
#    df["City"] = pd.DataFrame([CityName])
#    df["State"] = pd.DataFrame([StateName])
##    df["NumRating"] = pd.DataFrame([NumRating])
##    df["WAvg"] = pd.DataFrame([WAvgRating])
##    df["IBU"] = pd.DataFrame([IBU])
##    df["Calories"] = pd.DataFrame([Calories])
##    df["ABV"] = pd.DataFrame([ABV])
##    df["NumPages"] = pd.DataFrame([NumPages])
#    df["ComDesc"] = pd.DataFrame([ComDesc])
#    df["User"] = pd.DataFrame([ComDesc])
#    df["Review"] = pd.DataFrame([ComDesc])
#    df["DateCollected"] = pd.DataFrame([datetime.date.today()])

    return(df)
    
    
    #Gets username, and ratings
    #test = soup.find_all("div", attrs = {"style":"padding: 0px 0px 0px 0px;"})
    
    #Better way to get reviews
    #ReviewsContainer = soup.find_all("div", attrs = {"class":"reviews-container"})
    #IndividualReviews = ReviewsContainer[0].find_all("div", attrs = {"style":"padding: 20px 10px 20px 0px; border-bottom: 1px solid #e0e0e0; line-height: 1.5;"})[1].text

    
    #Get additional review pages
    #ExtraReviews = soup.find_all("a", attrs = {"class":"ballno"})
    #len(ExtraReviews) will give the additional pages of reviews
    