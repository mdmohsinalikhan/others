
import numpy as np
import numpy.random as npr
import pandas as pd
import scipy.special as scs
import matplotlib.pyplot as plt
import scipy.stats as ss
import datetime

data = pd.read_csv('http://www.helsinki.fi/~ahonkela/teaching/compstats1/toydata.txt', sep='\t', header=None)
data = data.values
data = np.array(data[:,0])

def draw_z(x,pi1,mu1,mu2,sigma):
    #c1 = pi1*(1/(np.sqrt(2*3.14)*sigma))*np.exp(-(1-mu1)**2/(2*sigma**2))
    c1 = pi1*ss.norm(mu1,sigma).pdf(x)
    #c2 = (1-pi1)*(1/(np.sqrt(2*3.14)*sigma))*np.exp(-(2-mu2)**2/(2*sigma**2))
    c2 = (1-pi1)*ss.norm(mu2,sigma).pdf(x)
    c = 1/(c1+c2)
    if npr.rand() < c1*c:
        return 1
    else:
        return 2
    
def draw_Z(pi1,mu1,mu2,sigma):
    Z = []
    for i in data:
        Z.append(draw_z(i,pi1,mu1,mu2,sigma))
    return Z

def draw_PI(alpha_pi,beta_pi,n1,n2):
    return npr.beta(alpha_pi+n1,beta_pi+n2)

def compute_n1_n2(Z):
    n1 = 0
    n2 = 0
    n = []
    for i in Z:
        if i == 1:
            n1 = n1 + 1
        elif i == 2:
            n2 = n2 + 1
    n.append(n1)
    n.append(n2)
    return n

def draw_mu(m,nu):
    return npr.normal(m,nu)

def compute_mk(k,Z,nu,mu0,sigma,sigma0):
    summation = 0
    for i in range(0,len(Z)):
        if Z[i] == k:
            summation = summation + data[i]
    m = nu*(summation/sigma**2 + mu0/sigma0**2)
    return m


def gibbs_sampling(chain_size,mu1,mu2,pi1,sigma,alpha_pi,beta_pi,mu0,sigma0):
    pis_mus = []
    for i in range(0,chain_size):
	print("Hello")
    return pis_mus
    
    
mu1 = 0
mu2 = 1
pi1 = .5
sigma = 1
alpha_pi = 1
beta_pi = 1
mu0 = 4
sigma0 = np.sqrt(100)
    
chain_size = 10
pis_mus = gibbs_sampling(chain_size,mu1,mu2,pi1,sigma,alpha_pi,beta_pi,mu0,sigma0)

pis = []
mu1s = []
mu2s = []
length = len(pis_mus)
for i in range(0,length):
    if i%3 == 0:
        pis.append(pis_mus[i])
    elif i%3 == 1:
        mu1s.append(pis_mus[i])
    elif i%3 == 2:
        mu2s.append(pis_mus[i])
        
print("Mean of posterior pi:")
print(np.mean(pis))
print("standard deviation of posterior pi")
print(np.std(pis))
print("Mean of posterior mu1:")
print(np.mean(mu1s))
print("standard deviation of posterior mu1")
print(np.std(mu1s))
print("Mean of posterior mu2:")
print(np.mean(mu2s))
print("standard deviation of posterior mu2")
print(np.std(mu2s))
