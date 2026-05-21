import numpy as np

ratings = np.random.randint(1,5,(100,20)) #Creating user reviews in range from 1 to 5

#The matrix/array is in integer format but ratings can be real!!

ratings = ratings.astype(float)  #hmm so we got the right format now what should we do??

#Notice that real datasets would not contain full data some cells should be empty(Not everyone watches every movie!!)
mask = np.random.choice([True,False], size = ratings.shape, p=[0.25,0.75])
ratings[mask] = np.nan

#Now we will calculate means etc but note that due to nan values we will have to use nan functions
mean_ratings = np.nanmean(ratings, axis = 0)
stdv = np.nanstd(ratings, axis = 0)
#To find the index of controversial movie
index = np.nanargmax(stdv)
print("The most controversial movie is ", index)

#We are finding scifi fans
scifi_fan = np.where(np.nanmean(ratings[:,:10], axis = 1) > 4)
print(scifi_fan)

#Now we want to find customer that have similar taste/exp to user 1 we will use euclidean distance formula
user_1 = ratings[0]
rest_users = ratings[1:100]
difference = np.sqrt(np.nansum((np.square((rest_users - user_1))), axis = 1))
index = np.nanargmin(difference)
index = index +1
print("The user similar to user 1 is ", index)

#Now to complete our project we want to recommend a movie using the similar user to user 1
index = index -1
similar_user = ratings[index]
movie_recommendation = np.where((similar_user>3) & (np.isnan(user_1)))

print("The movie recommended to user 1 is movie number", movie_recommendation)
