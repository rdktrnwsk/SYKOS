#include "Base.h"
#include "Cultural.cuh"
#include "Cultural.cu"

#ifndef CYK_CUH
#define CYK_CUH

template<int action> 
__global__ void cykAlgorithm(DeviceCYKData data, curandState* randGlobal);

template //single thread (TODO fix)
__global__ void cykAlgorithm<0>(DeviceCYKData data, curandState* randGlobal);

template // parallel n loop
__global__ void cykAlgorithm<1>(DeviceCYKData data, curandState* randGlobal);

template // parallel m loop
__global__ void cykAlgorithm<2>(DeviceCYKData data, curandState* randGlobal);

template // parallel m/n loop
__global__ void cykAlgorithm<3>(DeviceCYKData data, curandState* randGlobal);

template // parallel j loop
__global__ void cykAlgorithm<4>(DeviceCYKData data, curandState* randGlobal);

template //parallel j/k loop
__global__ void cykAlgorithm<5>(DeviceCYKData data, curandState* randGlobal);

//__global__ void cykAlgorithm(DeviceCYKData data, DeviceCultural cultural, curandState* randGlobal, int* solution, int** cykArray);


template<int action>
__global__ void cykAlgorithmCooperative(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut);

template // parallel j (block) m/n (threads) - block atomic synchronization
__global__ void cykAlgorithmCooperative<0>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut);

template // parallel j (block) m/n (threads) - fast barrier synchronization
__global__ void cykAlgorithmCooperative<1>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut);

template // parallel j (block) k/m/n (threads) - atomic synchro - !! k loop warning, too many threads (more than 1024)
__global__ void cykAlgorithmCooperative<2>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut);

template // parallel j (block) k/m(threads) - atomic synchro - k (index y), m (index x)
__global__ void cykAlgorithmCooperative<3>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut);




template<int action>
__global__ void cykAlgorithmRules(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int** rulesArray, int rulesCount);


template
__global__ void cykAlgorithmRules<0>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int** rulesArray, int rulesCount);


template
__global__ void cykAlgorithmRules<1>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int** rulesArray, int rulesCount);

template
__global__ void cykAlgorithmRules<2>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int** rulesArray, int rulesCount);


#endif
