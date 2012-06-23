#include <omp.h>
#include <stdio.h>
#ifdef MAIN
int main(void)  {
#else
int omp_kernel(void) {
#endif
  int nthreads;
  /* 0: mpi  1: omp */
  int rank[2];
  rank[0]=0;

  /* Fork a team of threads with each thread having a private rank variable */
  #pragma omp parallel private(rank)
  {
    /* Obtain and print thread id */
    rank[1] = omp_get_thread_num();
    printf("Hello World from thread = %d\n", rank[1]);
    /* Only master thread does this */
    if (rank[1] == 0) {
      nthreads = omp_get_num_threads();
      printf("Number of threads = %d\n", nthreads);
    }
  }  /* All threads join master thread and terminate */
  return 0;
}
