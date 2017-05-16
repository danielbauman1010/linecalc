from math import sqrt
#print 'First point is the one with the smaller x value'
fx = raw_input('First point X:\t')
fy = raw_input('First point Y:\t')
sx = raw_input('Second point X:\t')
sy = raw_input('Second point Y:\t')
fx = float(fx)
fy = float(fy)
sx = float(sx)
sy = float(sy)
m = (sy-fy)/(sx-fx)
b = sy - sx*m

result = 'Full line:\n y = {}x + {}'.format(m,b)
print result
print 'Specific line:'
minx = 0
maxx = 0
if fx >= sx:
	maxx=fx
	minx=sx
else:
	maxx=sx
	minx=fx
result = 'y = ( ({}x + {}) * sqrt(x - {}) * sqrt({} - x) )/( sqrt(x-{}) * sqrt({} - x)  )'.format(m,b,minx,maxx,minx,maxx)
print result
