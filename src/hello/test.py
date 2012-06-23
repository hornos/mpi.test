from mpi4py import MPI
import hello
hello.sayhello(MPI.COMM_WORLD)

# mpirun -np 4 python test.py
