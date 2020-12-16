import numpy as np

def potential(x) :
  energy=0
  # Your code to calculate the potential goes here
  for i in range(1,7) :
      for j in range(i) :
          diff = x[i,:] - x[j,:]
          d2 = sum(diff*diff)
          d6 = d2*d2*d2
          energy = energy + 4/(d6*d6) - 4/d6   
  return energy
  
# This command reads in the positions that are contained in the file called positions.txt
pos = np.loadtxt( "positions.txt" )
# This calculates and prints the energy of the configuration in the input file.  If the 
# code has been implemented correct this energy should be equal to -11.4809
eng = potential( pos )
print( eng )
