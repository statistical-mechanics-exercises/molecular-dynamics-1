import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_energy(self) : 
        pp = pos
        N = len(pos)
        for i in range(8) :
            if i>0 : 
              pp[i-1][0] = pp[i-1][0] - 0.25 + 0.5*np.random.uniform(0,1)
              pp[i-1][1] = pp[i-1][1] - 0.25 + 0.5*np.random.uniform(0,1)
            eng = 0
            for j in range(1,7) :
               for k in range(j) :
                  xdiff = pp[j][0] - pp[k][0]
                  ydiff = pp[j][1] - pp[k][1]
                  r2 = xdiff*xdiff + ydiff*ydiff
                  r6 = r2*r2*r2
                  eng = eng + 4*( 1/(r6*r6) - 1 /r6 )
            self.assertTrue( np.abs( eng - potential(pp))<1e-6, "The function you have written for calculating the potential outputs the wrong value" )
