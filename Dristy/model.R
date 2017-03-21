d = read.table(file="experiment.txt",header = TRUE)
randomrows = sort(sample(nrow(d),size=15,replace=FALSE))
training = d[randomrows,]
test = d[-randomrows,]
model1=lm(y1~x1+x2+x3+x4+x5,d,randomrows)
model2=lm(y2~x1+x2+x3,d3,randomrows)

training_error_y1 = sqrt(mean((training$y1 - predict.lm(model1, training)) ^ 2))
test_error_y1 = sqrt(mean((test$y1 - predict.lm(model1, test)) ^ 2))

training_error_y2 = sqrt(mean((training$y2 - predict.lm(model2, training)) ^ 2))
test_error_y2 = sqrt(mean((test$y2 - predict.lm(model2, test)) ^ 2))


