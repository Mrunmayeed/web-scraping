# Web Scraping Movie Review
In this project, the text and ratings of movie reviews was scraped from **Rotten Tomato**.

## Implementation:

1. First, in order to get a list of movies to get reviews, the 'essential-comedy-movies' list shared in editorial of rotten tomato was used.
2. The 'alinks' in class:article_movie_title were found and its 'href' extracted.
3. A list of these 'hrefs' was made and called in order.
4. For each link, a suffix was added to go to user review and then all the reviews in 'review_text_container' class were identified.
5. Then the text review as well as the ratings, given in the star format were extracted.
6. Only the first 20 reviews for each such movie were selected.
7. Finally, this formed a well distributed dataset of 1500 reviews.



