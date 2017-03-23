d = read.table(file="experiment.txt",header = TRUE)
#randomrows = sort(sample(nrow(d),size=15,replace=FALSE))
#training = d[randomrows,]
#test = d[-randomrows,]
model_f=lm(y1~x1+x2+x3+x4+x5,d)
model_g=lm(y2~x1+x2+x3,d)

mean_error_y1 = mean((abs(d$y1 - predict.lm(model_f, d))/d$y1)*100)
sd_error_y1 = sd((abs(d$y1 - predict.lm(model_f, d))/d$y1)*100)
minimum_error_y1 = min((abs(d$y1 - predict.lm(model_f, d))/d$y1)*100)
maximum_error_y1 = max((abs(d$y1 - predict.lm(model_f, d))/d$y1)*100)



mean_error_y2 = mean((abs(d$y2 - predict.lm(model_g, d))/d$y2)*100)
sd_error_y2 = sd((abs(d$y2 - predict.lm(model_g, d))/d$y2)*100)
minimum_error_y2 = min((abs(d$y2 - predict.lm(model_g, d))/d$y2)*100)
maximum_error_y2 = max((abs(d$y2 - predict.lm(model_g, d))/d$y2)*100)
