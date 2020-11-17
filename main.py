import numpy as np

def potential(x) :
  energy=0
  # Your code to calculate the potential goes here
  
  return energy
  
# This command reads in the positions that are contained in the file called positions.txt
pos = np.loadtxt( "positions.txt" )
# This calculates and prints the energy of the configuration in the input file.  If the 
# code has been implemented correct this energy should be equal to -11.4809
eng = potential( pos )
print( eng )
