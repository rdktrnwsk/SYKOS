#include "Ogolne.cuh"

__global__ void randInit(curandState* state, int seed) {
    int threadIndex = threadIdx.x;
    curand_init(seed, threadIndex, 0, &state[threadIndex]);
} 
