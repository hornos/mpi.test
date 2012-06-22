#!/usr/bin/python

from mpi4py import MPI

def main():
  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  if rank == 0:
    data = {'a': 7, 'b': 3.14}
    print rank, "Master send: ", data
    comm.send(data, dest=1, tag=11)
  elif rank == 1:
    data = comm.recv(source=0, tag=11)
    print rank, "Salve recv: ", data
# end def

if __name__ == '__main__':
  main()
