# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Tuneski 

---

## 2. Intended Use  

 

This application offers song recommendations to a user based on preferences.  The recommendations are given in order of most to least recommended, along with details about why they are recommended to the degree they are based on each of the users' stated preferences.

## 3. How the Model Works  

The app works by comparing a dataset of songs and their given features, which each contain numerical or string values. These are compared to the values of a user's preferences and given significance according to predetermined "weights" which act as multipliers for a given score.  The app then returns a list of recommendations, starting with the most recommended, and then descending for a list of the top 5 recommended songs form the dataset.

## 4. Data  

Describe the dataset the model uses.  

This app uses 16 songs with the following features as attributes:
genre, artist, mood, energy, tempo, danceability, acousticnees, instrumentalness, speechiness, popularity, and valence.

## 5. Strengths  

It works best if the dataset is large, and if the user is ok with looking for recommendations within the same gnere.  When the genre is a mismatch, the usefulness drops sharply.

## 6. Limitations and Bias 

The dataset is very limited and not all genres or artists can be represented.

The fixed value for genre and artists mean only one value can ever be truly positive, so any songs that dont match automatically get bumped down.

The recommendations are less likely to help a user discover new artists or genres because there is no system to score a genre/artist relative to the users baseline 

## 7. Evaluation  

I added user profiles that fit the dataset well, as well as outlier profiles that did not.  It behaved as expected, and for the edge case profiles the results were correct or expected but much less useful because the most significant features did not influence the recommendations.
The neo classical correctly asserted a song in that genre as the top recommendation, and prioritized instrumental music after that. The classic country profile did not have much to work with at all, other than acousticness and energy which I think would be relevant.  High energy pop had a few gener matches as well as categories of signicance like danceability and energy.  

## 8. Future Work  

The first and most valuable addition would be a system to rank genres comparatively- a rock listener may prefer metal or country over EDM, for example.  A system for closeness of genres would be the first step for me.
I would also allow a user to provide more than one value for fixed categories like artist and genre- maybe top 3 or 5 in each of those. Similar to the genre ranking, artists would need to be compared in a way beyond basic collaborative filtering.

---

## 9. Personal Reflection  

This was eye opening as far as how music is recommended, I like many others use those streaming apps and have not thought much about how they recommend stuff.  It was cool to see "k most recommendations" as I just did a LeetCode chapter on heaps so I knew it right away.  
Also, reflecting on the limitations at the end was great because it forced me to think critically about how useful the model actually is, and what it would need ot do before it would be in a state worth shipping.
The AI tools did the heavy lifting but I was confidently able to steer and make the critical decisions. Only once or twice did I ask questions about the actual code- everything was self-explanatory once I saw it in the IDE.
What surprised me about the recommendations is how mysterious it still feels when you are not looking at the numbers, even knowing that it is all just a mathematical calculation based on pre-defined values.
