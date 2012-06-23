#!/usr/bin/python

from mpi4py import MPI

def main():
  comm = MPI.COMM_WORLD
  size = comm.Get_size()
  rank = comm.Get_rank()
  data = (rank+1)**2

  print rank, "Node data before: ", data
  data = comm.gather(data, root=0)
  print rank, "Node data after: ", data

  if rank == 0:
    for i in range(size):
      assert data[i] == (i+1)**2
    print rank, "Master data: ", data
  else:
    assert data is None
    print rank, "Salve data: ", data

if __name__ == '__main__':
  main()
