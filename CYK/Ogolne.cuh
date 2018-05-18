#include "Base.h"
#ifndef OGOLNE_CUH
#define OGOLNE_CUH

//inicjowanie stanu losowania dla ka¿dego w¹tka
__global__ void randInit(curandState* stan, int ziarno);

#endif