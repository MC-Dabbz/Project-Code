# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:33:09 20244

@author: Mumba Chinyanwa
"""

# import pandas
import pandas as pd

# read file
movies_df = pd.read_csv("movie_dataset.csv")
movies_df.info()

"""
First Clean The Data to Make Work Easy
"""

# fix column names
movies_df.columns = movies_df.columns.str.replace(' ', '_')
movies_df.columns = movies_df.columns.str.lower()
movies_df.info()

# delete unuseful columns
movies_df.drop(["rank", "description", "runtime_(minutes)", "votes", "metascore"], inplace = True, axis = 1)
movies_df.info()

# replace missing revenue_(millions) values with mean values
movies_df['revenue_(millions)'].fillna(movies_df['revenue_(millions)'].mean(), inplace=True)
movies_df.info()

# remove any duplicates if present
duplicates = movies_df.duplicated()

if sum(duplicates) > 0:
    print(f'There are {sum(duplicates)} duplicate rows')
    movies_df.drop_duplicates(inplace = True)
    print("Duplicate rows have been removed")
else:
    print("No duplicate rows found")
    
"""
Answer Quiz Questions
"""
# Find the highest rated movie in the data set

highest_rated_movie_name = movies_df.loc[movies_df['rating'] == movies_df['rating'].max(), 'title']
print(f'The Highest Rated Movie is {highest_rated_movie_name.iloc[0]}.') 

# Find the average revenue 
mean_revenue = movies_df["revenue_(millions)"].mean()
print(f'The Mean Revenue of all the movies is {mean_revenue:.2f} million.')

# Find the average revenue of all the movies between 2015 and 2017
filtered_movies = movies_df[(movies_df["year"] >= 2015) & (movies_df["year"] <= 2017)]
average_revenue_2015_2017 = filtered_movies["revenue_(millions)"].mean()
print(f'The Average revenue of movies between 2015 and 2017 is {average_revenue_2015_2017:.2f} Million.')

# Movies released in 2016

movies2016 = movies_df["year"] == 2016
number_of_movies_2016 = len(movies_df[movies2016])
print(f'The Total number of movies released in 2016 is {number_of_movies_2016}.')

# Movies Directed by Christopher Nolan
cn_moviesbool = movies_df["director"] == "Christopher Nolan"
cn_movies = movies_df[cn_moviesbool]
num_cnmovies = len(cn_movies)
print(f'The Total number of Christopher Nolan Movies is {num_cnmovies}.')

# Movies in the dataset with a rating of at least 8.0
movies_ratedbool = movies_df["rating"] >= 8.0
movies_rated = movies_df[movies_ratedbool]
print(f'There are {len(movies_rated)} Movies with a rating of at least 8.0')

# median rating of movies directed by Christopher Nolan
nolan_movies = movies_df[movies_df["director"] == "Christopher Nolan"]
median_rating = nolan_movies["rating"].median()
print(f'The median rating of movies directed by Christopher Nolan is {median_rating}')

# Year with the highest average rating
average_rating = movies_df.groupby('year')["rating"].mean()
highest_average_year = average_rating.idxmax()
highest_average_rating = average_rating.max()
print(f'The year with the highest average rating is {highest_average_year}.')

# Percentage increase in number of movies made between 2006 and 2016?
sliced_years_min = movies_df[(movies_df["year"] == 2006)]
sliced_years_max = movies_df[(movies_df["year"] == 2016)]

Percentage_increase = ((len(sliced_years_max) - len(sliced_years_min))/ len(sliced_years_min))*100
print(f'Percentage increase in number of movies made between 2006 and 2016 = {Percentage_increase}%')

# Find the most common actor in all the movies

most_common_actor = movies_df['actors'].str.split(',').explode().str.strip().str.lower().value_counts().idxmax()
print(f"The most common actor is {most_common_actor.title()}.")

# unique genres are there in the dataset
unique_genre = movies_df["genre"].str.split(",", expand = True).stack().value_counts().count()
print(f'Number of unique_genres = {unique_genre} genres')

