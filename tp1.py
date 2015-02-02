import numpy as np
import matplotlib.pyplot as plt

def chargement () :
	t = np.loadtxt("t.txt")
	y = np.loadtxt("p.txt")
	y = np.asmatrix(y).T
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
	N = x.shape[1]
	print N
	xT = x.T 
	#print theta
	tmp = np.dot(xT,theta)
	tmp = y - tmp
	#print tmp
	cumul = pow(np.linalg.norm(tmp),2) #pas de matrice carre
	cumul = cumul/N
	return cumul

def dessiner (x,y,theta) :
	reg = theta[0] * x + theta[1]
	print reg.T
	print x
	plt.plot(x,y,'b.')
	plt.plot(x,reg.T,'r-')
	plt.ylabel('position')
	plt.xlabel('temps')
	plt.show()

if __name__ == "__main__" :
	x,y = chargement()
	theta = calculTheta(x,y)
	print calculErreurQuadra (x,y,theta)
	print theta
	dessiner(x[0],y,theta)
