from functions import addition, substract, mult, customMult

def test_addition():
    assert addition (3,4) == 7
    assert addition (-3,4)== 0

def test_substract():
    assert substract(4,3) == 1
    assert substract(-3,4) == 0
    assert substract(3,-4) == 7

def test_mult():
    assert mult(1,2,3) == 6
    assert mult(2,2,2) == 8
    assert mult(0,0,1) == 0
    assert mult(0,0,0) == 0
    assert mult(2,2,-2) == -8
    assert mult(2,-2,-2) == 8

def test_customMult():
    assert customMult(1,2,0)==1
    assert customMult(1,5,4)==1
    assert customMult(1,2,1)==2
    assert customMult(2,2,2)==16
