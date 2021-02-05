
```{r,echo = FALSE}
data <- read.csv("mexico_youtube_21_24_.csv")
cat_id = data$categoryId
cat_data = aggregate(data.frame(count = cat_id),
                     list(value = cat_id),
                     length)
barplot(height = cat_data[,2],names.arg = cat_data[,1])
```