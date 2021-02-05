import pandas as pd
cat_name = ["Film & Animation","Autos & Vehicles","Music","Pets & Animals","Sports","Short Movies","Travel & Events","Gaming","Videoblogging","People & Blogs","Comedy","Entertainment","News & Politics","Howto & Style","Education","Science & Technology","Movies","Anime/Animation","Action/Adventure","Classics","Comedy","Documentary","Drama","Family","Foreign","Horror","Sci-Fi/Fantasy","Thriller","Shorts","Shows","Trailers"]
cat_id=[1,2,10,15,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43]
df = pd.read_csv("/home/hasser/ProyecEsta/mexico_youtube_21_24_01.csv")

dic_cat = dict(zip(cat_id,cat_name))
for c_id in dic_cat:
    df.loc[df["categoryId"] == c_id,"categoryId"] = dic_cat[c_id]
df.to_csv("/home/hasser/ProyecEsta/mexico_youtube.csv",index = False)
