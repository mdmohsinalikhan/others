#import numpy as np
#import numpy.random as npr
import pandas as pd
import matplotlib.pyplot as plt
import scipy.special
from scipy.stats import multivariate_normal

import autograd.numpy as np
import autograd.numpy.random as npr
import autograd

import autograd.numpy.linalg as npl



mu1 = np.array([0.0,0.0])
mu2 = np.array([4.0,4.0])
mu3 = np.array([4.0,-4.0])
mu4 = np.array([-4.0,4.0])
mu5 = np.array([-4.0,-4.0])
Sigma = np.array([[1.0, .8],[.8, 1.0]])

def normal_pdf(x,mean,sd):
    return (1/(np.sqrt(2*3.14)*sd))*np.exp(-((x-mean)**2)/(2*sd**2))

def target(x):
    sum = 0
    
    x_minus_mu1 = np.array([x[0]-mu1[0],x[1]-mu1[1]])
    x_minus_mu2 = np.array([x[0]-mu2[0],x[1]-mu2[1]])
    x_minus_mu3 = np.array([x[0]-mu3[0],x[1]-mu3[1]])
    x_minus_mu4 = np.array([x[0]-mu4[0],x[1]-mu4[1]])
    x_minus_mu5 = np.array([x[0]-mu5[0],x[1]-mu5[1]])
    
    sum = sum + np.exp((-1/2)*1*(x_minus_mu1[0]*x_minus_mu1[0] + x_minus_mu1[1]*x_minus_mu1[1]))
    sum = sum + np.exp((-1/2)*2*(x_minus_mu2[0]*x_minus_mu2[0] + x_minus_mu2[1]*x_minus_mu2[1]))
    sum = sum + np.exp((-1/2)*3*(x_minus_mu3[0]*x_minus_mu3[0] + x_minus_mu3[1]*x_minus_mu3[1]))
    sum = sum + np.exp((-1/2)*4*(x_minus_mu4[0]*x_minus_mu4[0] + x_minus_mu4[1]*x_minus_mu4[1]))
    sum = sum + np.exp((-1/2)*5*(x_minus_mu5[0]*x_minus_mu5[0] + x_minus_mu5[1]*x_minus_mu5[1]))
    
    return np.log(sum)

def drawproposal(x,sd):
    return npr.normal(x,sd)

def proposal(x,x_given):
    var = multivariate_normal(mean=x_given, cov=Sigma)
    return var.pdf(x)

def mhsample(x0, n):
    x = x0
    lp = target(x)
    xs = []
    for i in range(n):
        x_prop = npr.multivariate_normal(x,Sigma)
        l_prop = target(x_prop)
        proposal(x, x_prop)
        if npr.rand() < (l_prop/lp)*(proposal(x, x_prop)/proposal(x_prop, x)):
            x = x_prop
            lp = l_prop
        xs.append(x)
    return xs

def compute_s_i_square(component,n,chainj,x_j_bar):
    sum = 0
    for i in chainj:
        sum = sum + (i[component]-x_j_bar)**2
    return (1/(n-1))*sum

def compute_x_j_bar(component,n,chainj):
    sum = 0
    for i in chainj:
        sum = sum + i[component]
    return (1/n)*sum

def compute_R_hat(component,n,chain1,chain2,chain3,chain4,chain5):
    x_1_bar = compute_x_j_bar(component,n,chain1)
    x_2_bar = compute_x_j_bar(component,n,chain2)
    x_3_bar = compute_x_j_bar(component,n,chain3)
    x_4_bar = compute_x_j_bar(component,n,chain4)
    x_5_bar = compute_x_j_bar(component,n,chain5)
    x_double_bar = (1/5)*(x_1_bar + x_2_bar + x_3_bar + x_4_bar + x_5_bar)
    #print(x_double_bar)
    B = (n/(5-1))*((x_1_bar-x_double_bar)**2 + (x_2_bar-x_double_bar)**2 + (x_3_bar-x_double_bar)**2 + (x_4_bar-x_double_bar)**2 + (x_5_bar-x_double_bar)**2)
    #print("Here is the value of B: " + str(B))
    s_1_square = compute_s_i_square(component,n,chain1,x_1_bar)
    s_2_square = compute_s_i_square(component,n,chain2,x_2_bar)
    s_3_square = compute_s_i_square(component,n,chain3,x_3_bar)
    s_4_square = compute_s_i_square(component,n,chain4,x_4_bar)
    s_5_square = compute_s_i_square(component,n,chain5,x_5_bar)
    W = (1/5)*(s_1_square + s_2_square + s_3_square + s_4_square + s_5_square )
    #print("Here is the value of W: " + str(W))
    var_x = (1-1/n)*W + (1/n)*B
    R_hat = var_x/W
    return R_hat

def hmc(x0, M, target, epsilon0, L):
    xs = np.zeros([M, len(x0)])
    gradF = autograd.grad(target)
    x = np.copy(x0)
    g = gradF(x)  # set gradient using initial x
    logP = target(x0)  # set objective function too
    accepts = 0
    for m in range(2*M): # draw M samples after M warm-up iterations
        p = npr.normal(size=x.shape)  # initial momentum is Normal(0,1)
        H = p.T @ p / 2 - logP   # evaluate H(x,p)
        xnew = np.copy(x)
        gnew = np.copy(g)
        for l in range(L): # make L ‘leapfrog’ steps
            epsilon = npr.uniform(0.8, 1.2) * epsilon0  # optional: randomise epsilon for improved theoretical convergence properties
            p = p + epsilon * gnew / 2   # make half-step in p
            xnew = xnew + epsilon * p    # make step in x
            gnew = gradF(xnew)           # find new gradient
            p = p + epsilon * gnew / 2   # make half-step in p
        logPnew = target(xnew)   # find new value of H
        Hnew = p.T @ p / 2 - logPnew
        dH = Hnew - H    # Decide whether to accept
        if dH < 0 or np.log(npr.rand()) < -dH:
            g = gnew
            x = xnew
            logP = logPnew
            accepts += 1
        if m >= M:
            xs[m-M,:] = x
    #print('Acceptance rate:', accepts/(2*M))
    return xs
    
def compute_expectations(chain1,chain2,chain3,chain4,chain5):
    x1 = []
    x2 = []
    for i in chain1:
        x1.append((i[0]-1)**2)
        x2.append((i[1]-1)**2)
    for i in chain2:
        x1.append((i[0]-1)**2)
        x2.append((i[1]-1)**2)
    for i in chain3:
        x1.append((i[0]-1)**2)
        x2.append((i[1]-1)**2)
    for i in chain4:
        x1.append((i[0]-1)**2)
        x2.append((i[1]-1)**2)
    for i in chain5:
        x1.append((i[0]-1)**2)
        x2.append((i[1]-1)**2)
        
    print("The square root of the mean of (x1-1)**2 is:")
    print(np.sqrt(np.mean(x1)))
    print("The square root of the mean of (x2-1)**2 is:")
    print(np.sqrt(np.mean(x2)))
    
n = 1
starting_point1 = np.array([0.0,0.0])
starting_point2 = np.array([4.0,4.0])
starting_point3 = np.array([4.0,-4.0])
starting_point4 = np.array([-4.0,4.0])
starting_point5 = np.array([-4.0,-4.0])
while True:
    n = 2*n
    chain1 = hmc(starting_point1, n, lambda x: target(x), 0.2, 10)
    chain2 = hmc(starting_point2, n, lambda x: target(x), 0.2, 10)
    chain3 = hmc(starting_point3, n, lambda x: target(x), 0.2, 10)
    chain4 = hmc(starting_point4, n, lambda x: target(x), 0.2, 10)
    chain5 = hmc(starting_point5, n, lambda x: target(x), 0.2, 10)
    print("the value of n is: " + str(n))
    R_hat_x1 = compute_R_hat(0,n,chain1,chain2,chain3,chain4,chain5)
    R_hat_x2 = compute_R_hat(1,n,chain1,chain2,chain3,chain4,chain5)
    
    
    #print("and the corresponding R_hat is:")
    if R_hat_x1 >= R_hat_x2:
        R_hat = R_hat_x1
    else:
        R_hat = R_hat_x2
        
    print("R_hat of x1: " + str(R_hat_x1))
    print("R_hat of x2: " + str(R_hat_x2))
    print("R_hat:" + str(R_hat))
    if R_hat <= 1.1:
    #if n == 256:
        print("program is ending.")
        compute_expectations(chain1,chain2,chain3,chain4,chain5)
        break

all_chain1_x = []
all_chain1_y = []
for i in range(0,n):
	all_chain1_x.append(chain1[i][0])
	all_chain1_y.append(chain1[i][1])

all_chain2_x = []
all_chain2_y = []
for i in range(0,n):
	all_chain2_x.append(chain2[i][0])
	all_chain2_y.append(chain2[i][1])

all_chain3_x = []
all_chain3_y = []
for i in range(0,n):
	all_chain3_x.append(chain3[i][0])
	all_chain3_y.append(chain3[i][1])

all_chain4_x = []
all_chain4_y = []
for i in range(0,n):
	all_chain4_x.append(chain4[i][0])
	all_chain4_y.append(chain4[i][1])

all_chain5_x = []
all_chain5_y = []
for i in range(0,n):
	all_chain5_x.append(chain5[i][0])
	all_chain5_y.append(chain5[i][1])
	



#all_x.append(chain2[i][0])
	#all_y.append(chain2[i][1])
	#all_x.append(chain3[i][0])
	#all_y.append(chain3[i][1])
	#all_x.append(chain4[i][0])
	#all_y.append(chain4[i][1])
	#all_x.append(chain5[i][0])
	#all_y.append(chain5[i][1])

plt.scatter(all_chain1_x,all_chain1_y,c='b')
plt.scatter(all_chain2_x,all_chain2_y,c='r')
plt.scatter(all_chain3_x,all_chain3_y,c='g')
plt.scatter(all_chain4_x,all_chain4_y,c='y')
plt.scatter(all_chain5_x,all_chain5_y,c='c')
plt.show()

#print(chain1[0][1])
        
#print("Here is chain1")
#print(chain1)
#print("Here is chain2")
#print(chain2)
#print("Here is chain3")
#print(chain3)
#print("Here is chain")
#print(chain4)
#print("Here is chain5")
#print(chain5)
#1.06826119571
