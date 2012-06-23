from mpi4py import MPI
import hello
hello.sayhello(MPI.COMM_WORLD)

# mpirun -np 2 python test.py
# or
# mpipy 2 test.py
