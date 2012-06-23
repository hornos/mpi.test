# from mpi4py import MPI
import hello
hello.omp_kernel()

# mpirun -np 2 python test.py
# or
# mpipy 2 test.py
