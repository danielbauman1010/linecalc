from math import sqrt
#print('First point is the one with the smaller x value'
fx = input('First point X:\t')
fy = input('First point Y:\t')
sx = input('Second point X:\t')
sy = input('Second point Y:\t')
fx = float(fx)
fy = float(fy)
sx = float(sx)
sy = float(sy)
m = (sy-fy)/(sx-fx)
b = sy - sx*m

result = 'Full line:\n y = {}x + {}'.format(m,b)
print(result)
print('Specific line:’)
minx = 0
maxx = 0
if fx >= sx:
	maxx=fx
	minx=sax
else:
	maxx=sx
	minx=fx
result = 'y = ( ({}x + {}) * sqrt(x - {}) * sqrt({} - x) )/( sqrt(x-{}) * sqrt({} - x)  )'.format(m,b,minx,maxx,minx,maxx)
print(result)
