#!/usr/bin/python

from mpi4py import MPI

def main():
  comm = MPI.COMM_WORLD
  size = comm.Get_size()
  rank = comm.Get_rank()
  if rank == 0:
    data = [(i+1)**2 for i in range(size)]
    print rank, 'Master data: ', data
  else:
    data = None
  data = comm.scatter(data, root=0)
  assert data == (rank+1)**2
  print rank, 'Slave data: ', data
# end def

if __name__ == '__main__':
  main()
