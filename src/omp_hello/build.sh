
# gcc -D MAIN -Wall -fopenmp -o hello.exe hello.c
# OMP_NUM_THREADS=4 ./hello.exe

# INC=-I${MPI4PY_HOME}/mpi4py/include
# LIB=-lmpi
PY_INC=$(python-config --includes)
PY_LIB=$(python-config --ldflags)

swig -Wall ${INC} -python hello.i
gcc -Wall ${PY_INC} ${INC} -fopenmp -c -fpic hello_wrap.c
gcc -Wall ${PY_LIB} ${LIB} -fopenmp -shared hello_wrap.o -o _hello.so
