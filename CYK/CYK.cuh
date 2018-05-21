#include "Base.h"
#include "Cultural.cuh"
#include "Cultural.cu"

#ifndef CYK_CUH
#define CYK_CUH

template<int action>
__global__ void cykAlgorithm(DeviceCYKData data, curandState* randGlobal);

template
__global__ void cykAlgorithm<0>(DeviceCYKData data, curandState* randGlobal);

template
__global__ void cykAlgorithm<1>(DeviceCYKData data, curandState* randGlobal);

template
__global__ void cykAlgorithm<2>(DeviceCYKData data, curandState* randGlobal);

template
__global__ void cykAlgorithm<3>(DeviceCYKData data, curandState* randGlobal);

//__global__ void cykAlgorithm(DeviceCYKData data, DeviceCultural cultural, curandState* randGlobal, int* solution, int** cykArray);


template<int action>
__global__ void cykAlgorithmCooperative(DeviceCYKData data, curandState* randGlobal);

template
__global__ void cykAlgorithmCooperative<0>(DeviceCYKData data, curandState* randGlobal);


#endif
