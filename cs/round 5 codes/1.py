import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

def laplacetarget(x,mu,b):
    return (1/(2*b))*np.exp(-np.abs(x-mu)/b)

def normaltarget(x,pi1,pi2,mu1,mu2,sigma1,sigma2):
    n1 = pi1*1/(np.sqrt(2*3.14)*sigma1)*np.exp(-((x-mu1)**2)/(2*sigma1**2))
    n2 = pi2*1/(np.sqrt(2*3.14)*sigma2)*np.exp(-((x-mu2)**2)/(2*sigma2**2))
    return n1 + n2

#npr.seed(44)
x = npr.laplace(size=1000000)

pi1 = .5
pi2 = .5
mu1 = -1
mu2 = 1
sigma1 = np.sqrt(0.5)
sigma2 = np.sqrt(0.5)

print('E[(x-1)^2] =', np.mean(((x-1)**2)* normaltarget(x,pi1, pi2,mu1,mu2,sigma1,sigma2)/laplacetarget(x,0,1)))
t1 = np.arange(-10, 10, 0.01)
plt.plot(t1,normaltarget(t1,0.5,0.5,-1,1,0.5,0.5))

sigma1 = np.sqrt(0.1)
sigma2 = np.sqrt(0.1)

print('E[(x-1)^2] =', np.mean(((x-1)**2)* normaltarget(x,pi1, pi2,mu1,mu2,sigma1,sigma2)/laplacetarget(x,0,1)))
t1 = np.arange(-10, 10, 0.01)
plt.plot(t1,normaltarget(t1,0.5,0.5,-1,1,0.1,0.1))

plt.show()
