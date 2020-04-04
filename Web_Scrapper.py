# WebScrapping means gathering data from a Website
# Project_Name = IMDB Top 100 Movies
# 1.Title
# 2.Release_Year
# 3.IMDB ratings
# 4.Metascore
# 5.Votes
# 6.US Gross Income

# Before Proceeding we need the URL = "https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"

# *.?- Acts as a separator
# count=It shows the number of movies in one page.
# groups=Its gives the idea about total phase.

# Inspecting HTML

# Tools Required:
# Repl--->Web programming environment
# Requests-->it will allow to send HTTP request to HTML page.
# BeautifulSoup--> will help us parse the HTML files
# Pandas--> will help us assemble the data into a DataFrame to clean and analyze it
# NumPy---> will add support for mathematical functions and tools for working with arrays

#Code:

import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# Movies in English

url = "https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"  # URL-The variable to store the Url
headers = {"Accept-Language": "en-US, en;q=0.5"}  # For english movies only
results = requests.get(url, headers=headers)
# results stores all the response from the URL
# requests.get(url, headers=headers)
# The headers part tells our scraper to bring us English, based on our previous line of code.

# Using of BeautifulSoup

soup = BeautifulSoup(results.text, "html.parser")
print(soup.prettify())

# soup==> is the variable we create to assign the method BeatifulSoup to, which specifies a desired format of results using the HTML parser — this allows Python to read the components of the page rather than treating it as one long string
# print(soup.prettify()) will print what we’ve grabbed in a more structured tree format, making it easier to read

# Intilize your storage

titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

# You‘ll notice the list of div elements to the right with a class attribute that has two values: lister-item and mode-advanced

# Find all lister-item mode-advanced

movie_div = soup.find_all('div', class_="lister-item mode-advanced")

# movie_div is the variable we’ll use to store all of the div containers with a class of lister-item mode-advanced
# the find_all() method extracts all the div containers that have a class attribute of lister-item mode-advanced from what we have stored in our variable soup.

for container in movie_div:
    # Titles
    name = container.h3.a.text
    titles.append(name)
    # name is the variable we’ll use to store the title data we find
    # container is what used in ourforloop — it’s used for iterating over each time.
    # h3 and .a is attribute notation and tells the scraper to access each of those tags
    # text tells the scraper to grab the text nested in the <a> tag
    # titles.append(name) tells the scraper to take what we found and stored in name and to add it into our empty list called titles, which we created in the beginning

    # Years
    year = container.h3.find('span', class_='lister-item-year text-muted unbold').text
    years.append(year)
    # year is the variable we’ll use to store the year data we find
    # container is what we used in our for loop — it’s used for iterating over each time.
    # h3 is attribute notation, which tells the scraper to access that tag.
    # (‘span’, class_ = ‘lister-item-year’) is the distinctive <span> tag we want
    # years.append(year) tells the scraper to take what we found and stored in year and to add it into our empty list called years (which we created in the beginning)

    # Runtime
    runtime = container.p.find('span', class_='runtime').text
    time.append(runtime)
    # runtime is the variable we’ll use to store the time data we find
    # container is what we used in our for loop — it’s used for iterating over each time.
    # find() is a method we’ll use to access this particular <span> tag
    # (‘span’, class_ = ‘runtime’) is the distinctive <span> tag we want
    # if container.p.find(‘span’, class_=’runtime’) else ‘-’ says if there’s data there, grab it — but if the data is missing, then put a dash there instead.
    # text tells the scraper to grab that text in the <span> tag
    # time.append(runtime) tells the scraper to take what we found and stored in runtime and to add it into our empty list called time (which we created in the beginning)

    # Ratings
    rating = float(container.strong.text)
    imdb_ratings.append(rating)
    # imdb is the variable we’ll use to store the IMDB ratings data it finds
    # container is what we used in our for loop — it’s used for iterating over each time.
    # strong is attribute notation that tells the scraper to access that tag.
    # text tells the scraper to grab that text
    # The float() method turns the text we find into a float — which is a decimal
    # imdb_ratings.append(imdb) tells the scraper to take what we found and stored in imdb and to add it into our empty list called imdb_ratings (which we created in the beginning).

    # Metascores
    #     score =container.find('span', class_='metascore').text if container.find('span',class_='metascore') else '-'
    #     metascores.append(score)
    # Metascore2
    try:
        score = container.find('span', class_='metascore').text
    except:
        score = '-'
    metascores.append(score)
    # m_score is the variable we’ll use to store the Metascore-rating data it finds
    # container is what we used in our for loop — it’s used for iterating over each time.
    # find() is a method we’ll use to access this particular <span> tag
    # (‘span’, class_ = ‘metascore’) is the distinctive <span> tag we want.
    # text tells the scraper to grab that text
    # if container.find(‘span’, class_=’metascore’) else ‘-’ says if there is data there, grab it — but if the data is missing, then put a dash there
    # The int() method turns the text we find into an integer
    # metascores.append(m_score) tells the scraper to take what we found and stored in m_score and to add it into our empty list called  metascores (which we created in the beginning)

    # Votes & Us_Grosses
    nv = container.find_all('span', attrs={'name': 'nv'})

    vote = nv[0].text
    votes.append(vote)

    gross = nv[1].text if len(nv) > 1 else "-"
    us_gross.append(gross)
    # nv is an entirely new variable we’ll use to hold both the votes and the gross <span> tags
    # container is what we used in our for loop for iterating over each time
    # find_all() is the method we’ll use to grab both of the <span> tags
    # (‘span’, attrs = ‘name’ : ’nv’) is how we can grab attributes of that specific tag.
    # vote is the variable we’ll use to store the votes we find in the nv tag
    # nv[0] tells the scraper to go into the nv tag and grab the first data in the list — which are the votes because votes comes first in our HTML code (computers count in binary — they start count at 0, not 1).
    # text tells the scraper to grab that text
    # votes.append(vote) tells the scraper to take what we found and stored in vote and to add it into our empty list called votes (which we created in the beginning)
    # grosses is the variable we’ll use to store the gross we find in the nv tag
    # nv[1] tells the scraper to go into the nv tag and grab the second data in the list — which is gross because gross comes second in our HTML code
    # nv[1].text if len(nv) > 1 else ‘-’ says if the length of nv is greater than one, then find the second datum that’s stored. But if the data that’s stored in nv isn’t greater than one — meaning if the gross is missing — then put a dash there.
    # us_gross.append(grosses) tells the scraper to take what we found and stored in grosses and to add it into our empty list called  us_grosses (which we created in the beginning)

# Print the data throught "Pandas Dataframe"
movies = pd.DataFrame({
    'Movie Name': titles,
    'Year of Release': years,
    'TimeLine': time,
    'Ratings': imdb_ratings,
    'metascore': metascores,
    'Votes': votes,
    'Earnings': us_gross
})

# Print the type of Data we have aquired:
print(movies.dtypes)

# Movie Name          object
# Year of Release     object
# TimeLine            object
# Ratings            float64
# metascore           object
# Votes               object
# Earnings            object
# dtype: object
# Hence here we need to convert the  object to its perfect datatypes

# Cleaning the data

# Cleaning the Mo
movies['Year of Release'] = movies['Year of Release'].str.extract('(\d+)').astype(int)
# movies[‘year’] tells pandas to go to the column year in our DataFrame
# .str.extract(‘(\d+’) this method: (‘(\d+’) says to extract all the digits in the string
# The .astype(int) method converts the result to an integer

# Clean teh TimeLine data
movies['TimeLine'] = movies['TimeLine'].str.extract('(\d+)').astype(int)

# Clean the Metascore data
movies['metascore'] = movies['metascore'].str.extract('(\d+)')
movies['metascore'] = pd.to_numeric(movies['metascore'], errors='coerce')

# Clean the votes
movies['Votes'] = movies['Votes'].str.replace(',', '').astype(int)
# movies[‘votes’] is our votes data in our movies DataFrame. We’re assigning our new cleaned up data to our votes DataFrame.
# .str.replace(‘ , ’ , ‘’) grabs the string and uses the replace method to replace the commas with an empty quote (nothing)
# The .astype(int) method converts the result into an integer

# Cleaning the us_gross data:
# movies['Earnings'] = movies['Earnings'].str.extract('(\d+)').astype(float)

# "or"

movies['Earnings'] = movies['Earnings'].map(lambda x: x.lstrip('$').rstrip('M'))  # ==>First Line
movies['Earnings'] = pd.to_numeric(movies['Earnings'], errors='coerce')  # ==>Second Line
# First line:
# movies[‘us_grossMillions’] is our gross data in our movies DataFrame. We’ll be assigning our new cleaned up data to our us_grossMillions column.
# movies[‘us_grossMillions’] tells pandas to go to thecolumn us_grossMillions in our DataFrame
# The .map() function calls the specified function for each item of an iterable
# lambda x: x is an anonymous functions in Python (one without a name). Normal functions are defined using the def keyword
# lstrip(‘$’).rstrip(‘M’) is our function arguments. This tells our function to strip the $ from the left side and strip the M from the right side

# Secondline
# movies[‘us_grossMillions’] is stripped of the elements we don’t need, and now we’ll assign the conversion code data to it to finish it up
# pd.to_numeric is a method we can use to change this column to a float. The reason we use this is because we have a lot of dashes in this column, and we can’t just convert it to a float using .astype(float) — this would catch an error.
# errors=’coerce’ will transform the nonnumeric values, our dashes, into NaN (not-a-number ) values because we have dashes in place of the data that’s missing

# Saving the data into CSV file

movies.to_csv('movie.csv')
print(movies)