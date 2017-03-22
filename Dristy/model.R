d = read.table(file="experiment.txt",header = TRUE)
#randomrows = sort(sample(nrow(d),size=15,replace=FALSE))
#training = d[randomrows,]
#test = d[-randomrows,]
model1=lm(y1~x1+x2+x3+x4+x5,d)
model2=lm(y2~x1+x2+x3,d)

#error_y1 = sqrt(mean((d$y1 - predict.lm(model1, d)) ^ 2))
#error_y2 = sqrt(mean((d$y2 - predict.lm(model2, d)) ^ 2))

mean_error_y1 = mean((abs(d$y1 - predict.lm(model1, d))/d$y1)*100)
sd_error_y1 = sd((abs(d$y1 - predict.lm(model1, d))/d$y1)*100)
minimum_error_y1 = min((abs(d$y1 - predict.lm(model1, d))/d$y1)*100)
maximum_error_y1 = max((abs(d$y1 - predict.lm(model1, d))/d$y1)*100)



mean_error_y2 = mean((abs(d$y2 - predict.lm(model2, d))/d$y2)*100)
sd_error_y2 = sd((abs(d$y2 - predict.lm(model2, d))/d$y2)*100)
minimum_error_y2 = min((abs(d$y2 - predict.lm(model2, d))/d$y2)*100)
maximum_error_y2 = max((abs(d$y2 - predict.lm(model2, d))/d$y2)*100)
