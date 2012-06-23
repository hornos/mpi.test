#!/bin/bash

INC=-I${MPI4PY_HOME}/mpi4py/include
LIB=-lmpi
PY_INC=$(python-config --includes)
PY_LIB=$(python-config --ldflags)

swig -Wall ${INC} -python hello.i
gcc -Wall ${PY_INC} ${INC} -c -fpic hello_wrap.c
gcc -Wall ${PY_LIB} ${LIB} -shared hello_wrap.o -o _hello.so
