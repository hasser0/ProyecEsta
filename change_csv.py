import pandas as pd
cat_name=["FilmAnimation","AutosVehicles","Music","PetsAnimals","Sports","ShortMovies","TravelEvents","Gaming","Videoblogging","PeopleBlogs","Comedy","Entertainment","NewsPolitics","HowtoStyle","Education","ScienceTechnology","Movies","AnimeAnimation","ActionAdventure","Classics","Comedy","Documentary","Drama","Family","Foreign","Horror","Sci-FiFantasy","Thriller","Shorts","Shows","Trailers"]
cat_id=[1,2,10,15,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43]


df = pd.read_csv("/home/hasser/ProyecEsta/mexico_youtube_21_24_01.csv")
dic_cat = dict(zip(cat_id,cat_name))

df.astype({'categoryId':'string'})
for c_id in dic_cat:
    df.loc[df['categoryId']==c_id,'categoryId'] = dic_cat[c_id]
df.to_csv("/home/hasser/ProyecEsta/mexico_youtube.csv",index = False)
