import numpy as np

t = np.loadtxt("t.txt")
y = np.loadtxt("p.txt")

o = np.ones((1,t.shape[0]))

x = np.vstack((t,o))
# teta = (XXt)**-1 * (XY)
tmp1 = np.asmatrix(np.dot(x,x.T))
tmp2 = np.dot(x,y)
teta = np.dot(tmp1.I, tmp2)

teta

	
