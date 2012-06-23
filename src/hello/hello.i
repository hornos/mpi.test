%module hello
%{
#include <mpi.h>
#include "hello.c"
%}
%include mpi4py/mpi4py.i
%mpi4py_typemap(Comm, MPI_Comm);
void sayhello(MPI_Comm comm);
