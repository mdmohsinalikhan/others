import numpy as np
import numpy.random as npr

def target(x,gamma):
    return np.exp(-gamma*(x**2 - 1)**2)

def proposal(x,y,b):
    return (1/(2*b))*np.exp(-np.abs(x-y)/b)

def drawproposal(x,b):
    return npr.laplace(x,b)

def mhsample(a0, gamma, b, n):
    a = a0
    lp = target(a,gamma)
    accepted = []
    for i in range(n):
        x = drawproposal(a,b)
        a_prop = x
        if npr.rand() < (target(a_prop,gamma)*proposal(a,a_prop,b))/(target(a,gamma)*proposal(a_prop,a,b)):    
            #print("i came here")
            a = a_prop
        accepted.append(a)
    return accepted


b = 2
n = 1000000


gamma = 8
x = mhsample(0,gamma,b,n)
h = plt.hist(x, 50, normed=True)
t1 = np.arange(-2, 2, 0.01)
plt.plot(t1,target(t1,gamma))

result = []
for i in x:
    result.append((i-1)**2)

print("the mean of (x-1)**2 is:")
print(np.mean(result))

gamma = 64
x = mhsample(0,gamma,b,n)
h = plt.hist(x, 50, normed=True)
t1 = np.arange(-2, 2, 0.01)
plt.plot(t1,target(t1,gamma))

result2 = []
for i in x:
    result2.append((i-1)**2)

print("the mean of (x-1)**2 is:")
print(np.mean(result2))

plt.show()
