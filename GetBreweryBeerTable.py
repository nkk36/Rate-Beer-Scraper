"""
FUNCTION DESCRIPTION

Inputs: 
Outputs: 
"""

def GetBreweryBeerTable(links, numbeer):
    
    #Import packages
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import numpy as np
    import re

    #Get url and scrape data
    url = "https://www.ratebeer.com/brewers/avondale-brewing-company/12890/"#links#["links"][j] #Only for Avondale Brewing Company temporarily
    page = requests.get(url, verify = False)
    soup = BeautifulSoup(page.text, "lxml")
    
    #Get table in numpy array
    array_df = []
    for rows in soup.find_all("td"):
        array_df.append(rows.text)
    
    #Look for "alias" on website     
    aliasRegex = re.compile(r"(alias)")    
    delete = []
    L = len(array_df)
    for i in range(0, L, 1):
        if aliasRegex.search(array_df[i]) is not None:
            delete.append(i)
        else:
            pass
    
    #Find rows with 'alias" to delete
    deletearray = []
    index = 0
    for element in delete:
        deletearray.append(range(delete[index], element + 8,1))
        index += 1
    
    #Delete rows with "alias" and get number of active beers    
    array_df = np.delete(array_df, deletearray)
    numactive = numbeer - len(delete)
    
    #Fill dataframe
    df = pd.DataFrame(np.reshape(array_df[:numactive*7],(numactive,7)), columns = ["Beer", "ABV", "DateAdded", "Rate", "Score", "Style", "NumRating"])
    df["type"] = df["Beer"].apply(lambda x: x.split("%")[1] if "%" in x else x.split(" ")[len(x.split(" ")) - 1])
    
    #Search for links to reviews for each beer
    link_regex = re.compile(r"(/beer/)(.+)(/\d{1,6}/)")
    links = soup.find_all("a", href = True)
    
    tlinks = []
    for link in links:
        if link_regex.search(str(link)) is not None and "rate" != link_regex.search(str(link)).group(2):
            tlinks.append("https://www.ratebeer.com"+link_regex.search(str(link)).group())
        else:
            pass
        
    #Place link to individual beer reviews in dataframe
    df["link"] = pd.DataFrame(tlinks)
    
    return(df)

    #WORKING CODE THAT COULD BE USED
    #for i in range(0, len(df)):
     #   df["rname"][i] = df["Beer"][i].split(df["type"][i])[0]
    
    #Gets ABV 
    #abv_regex = re.compile(r"\d+(\.{0,1}\d{0,2})(\%)")
    #df["abv"] = df["Beer"].apply(lambda x: abv_regex.search(x).group() if abv_regex.search(x) is not None else "NA")
    
    #Gets type of beer
    #soup.find_all("span", attrs = {"class" : "real-small hidden-xs"}        