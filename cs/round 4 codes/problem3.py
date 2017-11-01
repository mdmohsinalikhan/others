import numpy as np
import numpy.random as npr
import pandas as pd
import matplotlib.pyplot as plt
import scipy.special


data = pd.read_csv('http://www.helsinki.fi/~ahonkela/teaching/compstats1/toydata2.txt', sep='\t', header=None)
data = data.values
data = np.array(data[:,0])

def normal_pdf(x,mean,sd):
    return (1/(np.sqrt(2*3.14)*sd))*np.exp(-((x-mean)**2)/(2*sd**2))

def student_t_pdf(x,freedom):
    part1 = scipy.special.gamma((freedom+1)/2) 
    part2 = np.sqrt(freedom*3.14)*scipy.special.gamma(freedom/2)
    part3 = (1+((x)**2)/freedom)**(-(freedom+1)/2)
    return (part1/part2)*part3

def target(x,prior_sd):
    freedom = 5
    result = 1
    for i in data:
        result = result*student_t_pdf(i-x,freedom)*normal_pdf(x,0,prior_sd)
    return result

def drawproposal(x,sd):
    return npr.normal(x,sd)

def proposal(x,x_given,sd):
    return normal_pdf(x,x_given,sd)

def mhsample(x0, n, prior_sd, draw_sd):
    x = x0
    lp = target(x,prior_sd)
    xs = []
    for i in range(n):
        x_prop = drawproposal(x,draw_sd)
        l_prop = target(x_prop, prior_sd)
        if npr.rand() < (l_prop/lp)*(proposal(x, x_prop,draw_sd)/proposal(x_prop, x, draw_sd)):
            x = x_prop
            lp = l_prop
        xs.append(x)
    return xs

mean1 = []
prior_sd = 1
draw_sd = 3
sds = []
for j in range(0,10):
    x = mhsample(0,1000,prior_sd,draw_sd)
    mean1.append(np.mean(x))
    sds.append(np.std(x))
    #print(np.std(x))
    
print("mean of mu in the first part:")
print(np.mean(mean1))

print("sd of the mu in first part:")
print(np.mean(sds))

posterior = np.mean(mean1)
h = plt.hist(x, 50, normed=True)
h1 = plt.hist(data, 50, normed=True)
t1 = np.arange(-10, 10, 0.01)
plt.plot(t1+posterior,student_t_pdf(t1,5))
#plt.show()



mean1 = []
prior_sd = 10
draw_sd = 3
sds1 = []
for j in range(0,10):
    x = mhsample(0,1000,prior_sd,draw_sd)
    mean1.append(np.mean(x))
    sds1.append(np.std(x))
    #print(np.std(x))
    
print("mean of the second part:")
print(np.mean(mean1))

print("sd of the mu in second part:")
print(np.mean(sds1))

posterior = np.mean(mean1)
h = plt.hist(x, 50, normed=True)
h1 = plt.hist(data, 50, normed=True)
t1 = np.arange(-10, 10, 0.01)
plt.plot(t1+posterior,student_t_pdf(t1,5))
plt.show()

