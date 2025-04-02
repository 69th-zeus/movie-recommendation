# Movie Recommendation System

Recommendation System are of two types - 

- Content Based - Based Current Content you are watching

- Collaborative Based - Based on what users like you watch

- Hybrid - Mix of Both

In this Project, we will be using content based recommendation system.

# Project Flow (Overview of Things)

 - Data which we will preprocess to minimise error
 - Building Model by Training and Testing
 - Converting to a website
 - Deploying it on Heroku

 Dataset Used - TMDB 5000 Movie Dataset

 # Building Model

Approaches -

- Find Similar words and sort with highest
- Text Vectorization and finding similar (closest) vectors

We will go with Text Vectorization here

# Text Vectorization

We will use bag of words technique here

Bag of words Basic Algorithm -

- combine all tags
- find most common words (excluding stop words*, and stemming these words**)
- find frequency of all those words in all movies and create a dataframe
- find closest vectors which will be our recommended movies (Instead of Euclidean*** distance, we will calculate cosine**** distance)

*stop words - words like in, are, a, we, it etc as they do not contribute much to the meaning of sentences

**stemming - combining words like 'action', 'actions' which would be considered as different into one to improve efficiency. will be done before Vectorizing

***Euclidan = Normal Distance. Not reliable in higher dimensions

****Cosine Distance = Distance in terms of angles

# Frontend code 

Front code was written using the streamlit library and the pickle files were pushed using git LFS so cloning them directly might not work that efficiently. 

# *Proceed at your own risk*
