#!/usr/bin/python

from mpi4py import MPI

def main():
  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  if rank == 0:
    data = {'key1' : [7, 2.72, 2+3j], 'key2' : ( 'abc', 'xyz')}
    print rank, 'Master bcast: ', data
  else:
    data = None

  data = comm.bcast(data, root=0)
  print rank, 'Slave bcast: ', data

if __name__ == '__main__':
  main()
