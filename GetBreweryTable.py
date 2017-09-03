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
    #brewT = soup.find_all('table', attrs = {"id": "brewerTable"})

    #Get table in numpy array
    array_df = []
    for rows in soup.find_all("td"):
        array_df.append(rows.text)

    #Get number of breweries
    numRegex = re.compile(r"\d{1,4}")
    numactive = int(numRegex.search(soup.find_all("a", href = "#active")[0].text).group())

    #Initialize data frame and fill with data. Drop MyCount column
    df = pd.DataFrame(np.reshape(array_df[:numactive*5],(numactive,5)), columns = ["Brewery", "Type", "NumBeer", "MyCount", "Est"])
    df.drop("MyCount", axis = 1, inplace = True)

    
    #Split brewery name from city location and put into main dataframe
    split_brewery_city = df["Brewery"].apply(lambda x: x.split("-"))
    df_sbc = pd.DataFrame(np.concatenate(split_brewery_city, axis = 0).reshape(numactive,2), columns = ["Brewery","City"])
    df["Brewery"] = df_sbc["Brewery"]
    df.insert(1, "City", df_sbc["City"])
    
    #Place state name in main dataframe
    state = ["Alabama"]*numactive #Only for state of Alabama currently
    df_state = pd.DataFrame(state, columns = ["State"])
    df.insert(2, "State", df_state)

    #Put date collected into main dataframe
    today = [datetime.date.today()]*numactive
    df_today = pd.DataFrame(today, columns = ["Date"])
    df = pd.concat([df, df_today], axis = 1)


    return(df)
