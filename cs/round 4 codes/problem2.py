%matplotlib inline
import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

rho = 0.0

def p(x1,x2,y1,y2):
    d = 2
    mu = np.array([[y1, y2]]).transpose()
    x = np.array([[x1, x2]]).transpose()
    S = np.array([[1.0, rho], [rho, 1.0]])
    A = np.linalg.cholesky(S)

    log_det_S = 2*np.log(np.linalg.det(A))

    y = np.linalg.solve(A, x - mu)
    third_term = .5*np.dot(y.transpose(),y)

    log_density = -.5*d*np.log(2*np.pi) - .5*log_det_S - third_term

    return np.exp(log_density)

def mhsample(x0,y0, n, target, proposal, drawproposal):
    x = x0
    y = y0
    accepts = 0
    lp = target(x,y)
    #xs = np.zeros(n)
    xs = []
    ys = []
    for i in range(n):
        x_prop,y_prop = drawproposal(x,y)
        l_prop = target(x_prop,y_prop)
        #if npr.rand() < np.exp(l_prop - lp + proposal(x_prop, x) - proposal(x, x_prop)):
        if npr.rand() < (l_prop/lp)*(proposal(x,y,x_prop, y_prop)/proposal(x_prop,y_prop,x,y)):
            x = x_prop
            y = y_prop
            lp = l_prop
            accepts += 1
        #xs[i] = x
        xs.append(x)
        ys.append(y)
    #print('Acceptance rate:', accepts/n)
    return xs,ys

x_square = []

sd = 3
mean1 = []
for j in range(0,10):
    # Note that now Q(x',x^(t)) = Q(x^(t), x') so we do not need to include Q(x'; x) term for the acceptance probability
    x,y = mhsample(0.0, 0.0, 10000, lambda x, y: np.exp(-3*(np.sqrt(x**2+y**2)-2)**2) , lambda x_new,y_new,x_old,y_old : p(x_new,y_new,x_old,y_old), lambda x,y: npr.multivariate_normal([x,y],[[1,rho],[rho,1]]))
    del x_square[:]
    for i in x:
        x_square.append(i*i)
    mean1.append(np.mean(x_square))
    
print("mean of the first part:")
print(np.mean(mean1))

plt.scatter(x,y)
#plt.contour(x,y,-3*(np.sqrt(x**2+y**2)-2)**2)
#h = plt.hist(x, 50, normed=True)
#x = np.arange(-10, 10, 0.01)
#plt.plot(x,np.exp(-3*(np.sqrt(x**2+y**2)-2)**2))
plt.show()



sd = 3
mean1 = []
for j in range(0,10):
    # Note that now Q(x',x^(t)) = Q(x^(t), x') so we do not need to include Q(x'; x) term for the acceptance probability
    x,y = mhsample(0.0, 0.0, 10000, lambda x, y: np.exp(-3*(np.sqrt(x**2+y**2)-2)**2 + np.absolute(2*x - y)) , lambda x_new,y_new,x_old,y_old : p(x_new,y_new,x_old,y_old), lambda x,y: npr.multivariate_normal([x,y],[[1,rho],[rho,1]]))
    del x_square[:]
    for i in x:
        x_square.append((i-1)*(i-1))
    mean1.append(np.mean(x_square))
    
print("mean of the second part:")
print(np.mean(mean1))

#h = plt.hist(x, 50, normed=True)
plt.scatter(x,y)
#x = np.arange(-10, 10, 0.01)
#plt.plot(x,np.exp(-3*(np.sqrt(x**2+y**2)-2)**2))
plt.show()
