#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:03:11 2017

@author: nicholaskallfa
"""

def scrape2(links):
    
    #Get number of links
    L = len(links)
    
    #Join prefix to url
    for i in range(0,L,1):
        links["links"][i] = "https://www.ratebeer.com" + links["links"][i]

    url = links["links"][0]
    page = requests.get(url, verify = False)
    soup = BeautifulSoup(page.text, "lxml")
    return(links)