#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_rating(rating_score):
    star = 0
    for i in enumerate(rating_score.findAll('span',attrs={'class':'star-display__filled'})):
          star +=1
    half_star = rating_score.find('span',attrs={'class':'star-display__half'})
    if half_star:
        star += 0.5
    return star


def fetch_reviews(url):    
    reviews = []
    ratings = []
    r = requests.get(url+'/reviews?type=user')
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    # table = soup.find('table', attrs = {'align':'center', 'width':'100%'}) 
    for _,review in enumerate(soup.findAll('div',attrs={'class':'review-text-container'})):
        rating = get_rating(review.find('span',attrs={'class':'audience-reviews__score'}))
        review_text = review.find('p',attrs={'class':'audience-reviews__review js-review-text'}).text
        if review_text and rating:
            reviews.append(review_text.strip())
            ratings.append(rating)
    return reviews,ratings


def get_movies(url):
    r = requests.get(url)
    movie_df = pd.DataFrame(columns=['name','reviews','ratings'])   
    soup = BeautifulSoup(r.content, 'html5lib') 
    for _,movie_tab in enumerate(soup.findAll('div',attrs={'class':'article_movie_title'})):
        movie = movie_tab.find('a')
        reviews,ratings = fetch_reviews(movie['href'])
        df = pd.DataFrame({'reviews':reviews, 'ratings':ratings})
        df['name'] = movie.text
        movie_df = pd.concat([movie_df,df])
        
    return movie_df


movie_df = get_movies('https://editorial.rottentomatoes.com/guide/essential-comedy-movies/')

movie_df.to_csv('movie_reviews.csv', index=False)




        
