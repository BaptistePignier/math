from math import *
def fct(x):
	return (x**2)/6 + 1/2*x

intervalle = [1,2]
b = intervalle[-1]
a = intervalle[0]
n = int(1e8)
res = 0
for k in range(0,n-1):
	print(k,'/',n)
	ele1 = ((b-a)/n) **2
	ele2 = (fct( a+(k+1)*((b-a)/n))- fct(a+k*((b-a)/n)))**2
	ele3 = sqrt(ele1+ele2)
	res += ele3

print(res)