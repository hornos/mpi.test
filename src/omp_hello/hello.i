%module hello
%{
#include <omp.h>
#include "hello.c"
%}
void omp_kernel(void);
