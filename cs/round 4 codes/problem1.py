%matplotlib inline
import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

def mhsample(x0, n, target, proposal, drawproposal):
    x = x0
    accepts = 0
    lp = target(x)
    #xs = np.zeros(n)
    xs = []
    for i in range(n):
        x_prop = drawproposal(x)
        l_prop = target(x_prop)
        #if npr.rand() < np.exp(l_prop - lp + proposal(x_prop, x) - proposal(x, x_prop)):
        if npr.rand() < (l_prop/lp)*(proposal(x, x_prop)/proposal(x_prop, x)):
            x = x_prop
            lp = l_prop
            accepts += 1
        #xs[i] = x
        xs.append(x)
    #print('Acceptance rate:', accepts/n)
    return xs

x_square = []

sd = 3
mean1 = []
for j in range(0,100):
    # Note that now Q(x',x^(t)) = Q(x^(t), x') so we do not need to include Q(x'; x) term for the acceptance probability
    x = mhsample(0.0, 10000, lambda x: (np.sin(x)**2)*(np.exp(-np.absolute(x))) , lambda y, x: np.exp(-((y-x)**2)/(2*sd**sd)), lambda x: npr.normal(x,sd))
    del x_square[:]
    for i in x:
        x_square.append(i*i)
    mean1.append(np.mean(x_square))
    
print("mean of the first part:")
print(np.mean(mean1))

h = plt.hist(x, 50, normed=True)
t1 = np.arange(-10, 10, 0.01)
plt.plot(t1,(np.sin(t1)**2)*(np.exp(-np.absolute(t1))))
plt.show()



sd = 3
mean2 = []
for j in range(0,100):
    # Note that now Q(x',x^(t)) = Q(x^(t), x') so we do not need to include Q(x'; x) term for the acceptance probability
    x = mhsample(0.0, 10000, lambda x: (np.sin(x)**2)*(np.exp(-3*np.sqrt(np.absolute(x)))) , lambda y, x: np.exp(-((y-x)**2)/(2*sd**sd)), lambda x: npr.normal(x,sd))
    x_square = []
    del x_square[:]
    for i in x:
        x_square.append(i*i)
    mean2.append(np.mean(x_square))

print("mean of the second part:")
print(np.mean(mean2))

h = plt.hist(x, 50, normed=True)
t1 = np.arange(-10, 10, 0.01)
plt.plot(t1,(np.sin(t1)**2)*(np.exp(-np.absolute(t1))))
plt.show()
