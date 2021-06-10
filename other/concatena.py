import pandas as pd

df1 = pd.read_csv("reviews.csv")
df2 = pd.read_csv("bad_reviews.csv")
frames = [df1, df2]
result = pd.concat(frames)


result.to_csv("final_movie_reviews.csv")