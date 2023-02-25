"""
CMPS 2200  Recitation 3.
See recitation-03.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    n = len(x)
    if n==1:
        return[x[0]*y[0]
    x0 = x[:n//2]
    x1 = x[n//2:]
    y0 = y[:n//2]
    y1 = y[n//2:]
    
              
    z0 = _quadratic_multiply(x0, y0)
    z1 = _quadratic_multiply(x1,y1)
    z2 = _quadratic_multiply[x0[i]+x1[i] for i in range(n//2)], [y0[i]+ y1[i] for i in range(n//2)])
    
    result = [0] * (2*n - 1)
    for i in range(n-1):
        result[i] += z0[i]
        result[i+n]+= z1[i]
        result[i+(n//2)] += z2[i] - z0[i] - z1[i]
    result[2*n-2] += z2[n//2-1]
    return result
               
    pass
    ###



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    
    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000


    
    

