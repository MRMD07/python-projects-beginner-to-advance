import numpy as np

ratings = np.random.randint(1,5,(100,20)) #Creating user reviews in range from 1 to 5

#The matrix/array is in integer format but ratings can be real!!

ratings = ratings.astype(float)  #hmm so we got the right format now what should we do??

#Notice that real datasets would not contain full data some cells should be empty(Not everyone watches every movie!!)
mask = np.random.choice([True,False], size = ratings.shape, p=[0.25,0.75])
ratings[mask] = np.nan