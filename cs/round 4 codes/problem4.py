import numpy as np
import pandas as pd
import scipy.special as scs
import numpy.random as npr
from scipy.stats import multivariate_normal


data1 = pd.read_csv('http://www.helsinki.fi/~ahonkela/teaching/compstats1/toydata.txt', sep='\t', header=None)
data1 = data1.values
data1 = np.array(data1[:,0])

rho = 0

def gamma_logpdf(x, alpha, beta):
    return (alpha*np.log(beta) - scs.gammaln(alpha) + (alpha-1) * np.log(x) - beta * x)

def pdf_ab(x):
    return -np.exp(x) + x

def target(a,b):
    result = 1
    for i in data1:
        result = result + gamma_logpdf(i,np.exp(a),np.exp(b))
    return result + pdf_ab(a) + pdf_ab(b)

def proposal(a,b,c,d):
    var = multivariate_normal(mean=[c,d], cov=[[1,rho],[rho,1]])
    return np.log(var.pdf([a,b]))
    
def drawproposal(a,b):
    x = []
    c,d = npr.multivariate_normal([a,b], [[1,rho],[rho,1]])
    x.append(c)
    x.append(d)
    return x


def mhsample(a0, b0, n):
    a = a0
    b = b0
    lp = target(a,b)
    as_bs = []
    for i in range(n):
        x = drawproposal(a,b)
        a_prop = x[0]
        b_prop = x[1]
        l_prop = target(a_prop, b_prop)
        if npr.rand() < np.exp(l_prop - lp + proposal(a, b, a_prop,b_prop) - proposal(a, b, a_prop,b_prop)):
            #print("i came here")
            a = a_prop
            b = b_prop
            lp = l_prop
        as_bs.append(a)
        as_bs.append(b)
    return as_bs

#print(scipy.integrate.quad(lambda x: np.exp(gamma_logpdf(x,1,1)), 0, 6))
n = 10000
x = mhsample(0,0,n)
#print(x)
a_s = []
b_s = []
for i in range(0,2*n):
    if i%2 == 0:
        a_s.append(np.exp(x[i]))
    else:
        b_s.append(np.exp(x[i]))
#print(a_s)

print("alpha mean:")
alpha = np.mean(a_s)
print(alpha)
print("beta mean:")
beta = np.mean(b_s)
print(beta)

print("alpha deviation:")
alpha_std = np.std(a_s)
print(alpha_std)
print("beta deviation:")
beta_std = np.std(b_s)
print(beta_std)

#print("length of x is:")
#print(len(x))
print("p(a):")
print(np.exp(pdf_ab(1)))

h = plt.hist(data1, 50, normed=True)
t1 = np.arange(-10, 10, 0.01)
plt.plot(t1,np.exp(pdf_ab(t1)))
plt.plot(t1,np.exp(gamma_logpdf(t1,alpha,beta)))
plt.show()

#print(data1)

