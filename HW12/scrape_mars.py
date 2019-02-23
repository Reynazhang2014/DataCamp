#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup as bs
import requests
import pymongo 
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    opts = webdriver.ChromeOptions()
    opts.headless = True
    return webdriver.Chrome(**executable_path,options = opts)

def scrape():
    final_mars = {}
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    response = requests.get(url)
    soup = bs(response.text,'html.parser')

    result_title = soup.find(class_ = 'content_title')
    title = result_title.a.text.strip()
    result_des = soup.find(class_ = 'rollover_description_inner')
    description = result_des.text.strip()

    top_story = {
        'title':title,
        'description':description
    }

    ## Use Selenium to get Mars Image
    #executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    #opts = webdriver.ChromeOptions()
    #opts.headless = True
    browser = init_browser() #webdriver.Chrome(**executable_path,options = opts)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.get(url)
    browser.find_element_by_partial_link_text('FULL IMAGE').click()
    browser.implicitly_wait(10)
    browser.find_element_by_partial_link_text('more info').click()


    html = browser.execute_script("return document.body.outerHTML;")
    soup = bs(html, 'html.parser')
    soup.body()
    figure = soup.find(class_ = 'lede')
    #get the image url
    img_url = 'https://www.jpl.nasa.gov/' + figure.find('a').attrs['href'].strip()


    #get Mars weather
    url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)
    soup = bs(response.text,'html.parser')
    latest_tweets = soup.find_all('p',class_ = 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    for tweet_html in latest_tweets:
        tweet = tweet_html.text
        if tweet.strip().startswith('Sol'): 
            weather = tweet
            break

    #get Mars fact
    url = 'http://space-facts.com/mars/'
    table = pd.read_html(url)[0]
    table.columns = ['Attribute','Value']
    table.set_index('Attribute',inplace= True)


    # Get Mars' images and URL's
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    response = requests.get(url)
    soup = bs(response.text,'html.parser')



    hemisphere_image_urls = []
    items = soup.find_all(class_ = 'item')
    for i in items:
        image_url = {}
        image_url['title'] = i.find('h3').text
        new_url = 'https://astrogeology.usgs.gov' + i.find('a',class_ = 'itemLink product-item').attrs['href']
        new_response = requests.get(new_url)
        new_soup = bs(new_response.text,'html.parser')
        image_url['img_url'] = 'https://astrogeology.usgs.gov' + new_soup.find(class_ = 'wide-image').attrs['src']
        hemisphere_image_urls.append(image_url)
    
    final_mars = {'story':top_story,'featured_img':img_url,'weather':weather,'table':table.to_json(),'mars_image':hemisphere_image_urls}
    print(final_mars)
    return final_mars


    
        


