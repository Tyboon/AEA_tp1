import numpy as np

def chargement () :
	t = np.loadtxt("t.txt")
	y = np.loadtxt("p.txt")
	o = np.ones((1,t.shape[0]))
	x = np.vstack((t,o))
	return x,y

def calculTheta (x,y) :
	# teta = (XXt)**-1 * (XY)
	tmp1 = np.asmatrix(np.dot(x,x.T))
	tmp2 = np.dot(x,y)
	theta = np.dot(tmp1.I, tmp2)
	return theta

def calculErreurQuadra (x,y,theta) :
	N = x.shape[0]
	cumul = 0
	xT = x.T
	for i in range(1,N) :
		tmp = np.dot(xT[i],theta)
		cumul = (y[i] - tmp)**2
	cumul = cumul/N
	return cumul

if __name__ == "__main__" :
	x,y = chargement()
	theta = calculTheta(x,y)
	print calculErreurQuadra (x,y,theta)
