# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 14:08:13 2018

@author: asus
"""
from os import path
import requests as re
from bs4 import BeautifulSoup
from PIL import Image
import numpy as np
import os
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def getText():
    page = re.get('https://www.rottentomatoes.com/m/andhadhun')
    soup = BeautifulSoup(page.content,'html.parser')
    text = soup.find_all('p')              
    total_text = ""
    for i in range(12,22):
        review = text[i].get_text().strip()
        total_text += review + " "
    return total_text

def word_cloud():
    text = getText()
    mask = np.array(Image.open(path.join("cat_mask.png")))
    stopwords = set(STOPWORDS)
    stopwords.add("said")
    wc = WordCloud(background_color="black", max_words=20000, mask=mask,
                 stopwords=stopwords, contour_width=1, contour_color='white')
    
    wc.generate(text)
    wc.to_file(path.join("wordcloudpic.png"))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.figure()
    plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    word_cloud()