#!/usr/bin/python

from mpi4py import MPI
import numpy

def main():
  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  # pass explicit MPI datatypes
  if rank == 0:
    data = numpy.arange(10, dtype=numpy.int)
    print rank, "Master send (explicit): ", data
    comm.Send([data, MPI.INT], dest=1, tag=77)
  elif rank == 1:
    data = numpy.empty(10, dtype=numpy.int)
    comm.Recv([data, MPI.INT], source=0, tag=77)
    print rank, "Salve recv (explicit): ", data

  # automatic MPI datatype discovery
  if rank == 0:
    data = numpy.arange(10, dtype=numpy.float64)
    print rank, "Master send (discovery): ", data
    comm.Send(data, dest=1, tag=13)
  elif rank == 1:
    data = numpy.empty(10, dtype=numpy.float64)
    comm.Recv(data, source=0, tag=13)
    print rank, "Salve recv (discovery): ", data
# end def

if __name__ == '__main__':
  main()
