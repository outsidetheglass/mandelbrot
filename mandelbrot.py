
def mandel(c, maxiter):
    z = complex(0,0)
    for iteration in xrange(maxiter):
        z=(z*z)+c

        if abs(z) > 4:
            break
            pass
        pass
    return iteration+1
# set the location and size of the complex plane rectangle
xvalues = linspace(­2.25, 0.75, 1000)
yvalues = linspace(­1.5, 1.5, 1000)

# size of these lists of x and y values
xlen = len(xvalues)
ylen = len(yvalues)
atlas = empty((xlen,ylen))
for ix in xrange(xlen):
    for iy in xrange(ylen):


        cx = xvalues[ix]
        cy = yvalues[iy]
        c = complex(cx, cy)
        atlas[ix,iy] = mandel(c,40)

        pass
    pass
figsize(18,18)
imshow(atlas.T, interpolation="nearest")
