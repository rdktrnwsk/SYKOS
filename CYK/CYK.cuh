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

template //parallel j/k loop
__global__ void cykAlgorithm<101>(DeviceCYKData data, curandState* randGlobal);

//__global__ void cykAlgorithm(DeviceCYKData data, DeviceCultural cultural, curandState* randGlobal, int* solution, int** cykArray);


template<int action>
__global__ void cykAlgorithmCooperative(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int additionalVariable);

template // parallel j (block) m/n (threads) - block atomic synchronization
__global__ void cykAlgorithmCooperative<0>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int additionalVariable);

template // parallel j (block) m/n (threads) - fast barrier synchronization
__global__ void cykAlgorithmCooperative<1>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int additionalVariable);

template // parallel j (block) k/m/n (threads) - atomic synchro - !! k loop warning, too many threads (more than 1024)
__global__ void cykAlgorithmCooperative<2>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int additionalVariable);

template // parallel j (block) k/m(threads) - atomic synchro - k (index y), m (index x)
__global__ void cykAlgorithmCooperative<3>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int additionalVariable);

template // parallel j (block) k/m(threads) - atomic synchro - k (index y), m (index x)
__global__ void cykAlgorithmCooperative<4>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int additionalVariable);

template
__global__ void cykAlgorithmCooperative<5>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int additionalVariable);

template
__global__ void cykAlgorithmCooperative<6>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int additionalVariable);

template
__global__ void cykAlgorithmCooperative<7>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int additionalVariable);

template
__global__ void cykAlgorithmCooperative<8>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int additionalVariable);

template
__global__ void cykAlgorithmCooperative<9>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int additionalVariable);




template<int action>
__global__ void cykAlgorithmRules(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int** rulesArray, int rulesCount, int additionalVariable);


template // parallel j (block) - every rule = thread
__global__ void cykAlgorithmRules<0>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int** rulesArray, int rulesCount, int additionalVariable);


template // parallel j (block) - every rule = thread | i loop on host side EXTRA BLOCK LOOP
__global__ void cykAlgorithmRules<1>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int** rulesArray, int rulesCount, int additionalVariable);

template // parallel j (block) - every rule = thread 
__global__ void cykAlgorithmRules<2>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int** rulesArray, int rulesCount, int additionalVariable);


template // parallel j (block) Lrules (block) - every rule = thread | i loop on host side (host synchronization)  EXTRA BLOCK LOOP
__global__ void cykAlgorithmRules<3>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int** rulesArray, int rulesCount, int additionalVariable);

template // parallel j (block) Lrules (block) - every rule = thread, k loop idy| i loop on host side (host synchronization) 
__global__ void cykAlgorithmRules<4>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int** rulesArray, int rulesCount, int additionalVariable);


template // parallel j (block) Lrules (block) kLoop (z index) - every rule = thread | i loop on host side (host synchronization) 
__global__ void cykAlgorithmRules<5>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int** rulesArray, int rulesCount, int additionalVariable);


template // same as 3 but with  GPU synchronization
__global__ void cykAlgorithmRules<6>(DeviceCYKData data, curandState* randGlobal, volatile int* arrayIn, volatile int* arrayOut, int** rulesArray, int rulesCount, int additionalVariable);


#endif
