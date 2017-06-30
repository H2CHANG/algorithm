def Towers(disks, start='A', temp='B', to='C'):
  if disks>0:
    Towers(disks-1, start, to, temp)
    print("move disk {} from {} to {}".format(disks, start, to))
    Towers(disks-1, temp, start, to)
    
Towers(3)


