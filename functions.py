def addition  (x,y) :
    if(y>0 and x>0):
        z=x+y
    else:
        z=0
    return z

def substract (x,y) :
    if(x>0):
        z=x-y
    else:
        z=0
    return z

def mult (x, y, z) :
    return x*y*z

def customMult (x, y, z):
    if(z==1 or z==2):
        res = (x*y)**z
    else:
        res = 1
    return res
