#!/usr/bin/python

from mpi4py import MPI
import numpy
import sys

def main():
  comm = MPI.COMM_SELF.Spawn(sys.executable, args=['dynslave.py'],maxprocs=4)
  N = numpy.array(100, 'int')
  comm.Bcast([N, MPI.INT], root=MPI.ROOT)
  PI = numpy.array(0.0, 'double')
  comm.Reduce(None, [PI, MPI.DOUBLE],op=MPI.SUM, root=MPI.ROOT)
  print(PI)
  comm.Disconnect()
# end def

if __name__ == '__main__':
  main()
