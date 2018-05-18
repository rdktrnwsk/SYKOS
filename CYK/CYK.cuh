#include "Base.h"
#include "Cultural.cuh"
#include "Cultural.cu"

#ifndef CYK_CUH
#define CYK_CUH

template<int action>
__global__ void cykAlgorithm(curandState* randGlobal);

template
__global__ void cykAlgorithm<0>(curandState* randGlobal);

template
__global__ void cykAlgorithm<1>(curandState* randGlobal);

template
__global__ void cykAlgorithm<2>(curandState* randGlobal);

//__global__ void cykAlgorithm(DeviceCYKData data, DeviceCultural cultural, curandState* randGlobal, int* solution, int** cykArray);

#endif
