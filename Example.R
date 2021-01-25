cat_id = mexico_youtube_21_24_01$categoryId

cat_data = aggregate(data.frame(count = cat_id),
                     list(value = cat_id),
                     length)
barplot(height = cat_data[,2],names.arg = cat_data[,1])
mexico_youtube_21_24_01$view_count
cat_data
getwd()
