#include "Base.h"
#include "Cultural.cuh"
#ifndef CULTURAL_CU
#define CULTURAL_CU

__forceinline__ __device__  void DeviceCultural::beforeOutput(int threadIndex) {
	__syncthreads();
	if(threadIndex == 0) {
		*_outputAllowed = 0;
		if(_numOfConnections > 1) {		
			int count = 0;
			for(int i = 0; i < _numOfConnections; i++) {
				if(_myVersionArray[0] == _myVersionArray[i] ) {
					count += 1;
				} else {
					break;
				}
			}	
			if(count == _numOfConnections) {
				*_outputAllowed = 1;
			}
		}
			__threadfence_system();
	}
	__syncthreads();
}

__forceinline__ __device__  void DeviceCultural::afterOutput(int threadIndex) {
	__syncthreads();
	if(threadIndex == 0 && *_outputAllowed != 0) {
		_myVersionArray[0] = _myVersionArray[0] + 1;
		*_outputAllowed = 0;
		__threadfence_system();
	}
	__syncthreads();
}

__forceinline__ __device__ void DeviceCultural::beforeInput(int threadIndex) {
	__syncthreads();
	if(threadIndex == 0) {
		*_inputAllowed = 0;
		if(_sbVersionArray[_ID] < _sbVersionArray[0]) {
			*_inputAllowed = 1;
			__threadfence_system();
		}
	}
	__syncthreads();
}

__forceinline__ __device__ void DeviceCultural::afterInput(int threadIndex) {
	__syncthreads();
	if(threadIndex == 0 && *_inputAllowed != 0) {
			_sbVersionArray[_ID] = _sbVersionArray[0];
			*_inputAllowed = 0;
			__threadfence_system();
	}
	__syncthreads();
	
}

__forceinline__ __device__ void DeviceCultural::setStatus(int num) {
	*_myStatus = num;
}

__forceinline__ __device__ void DeviceCultural::setResult(int num) {
	*_result = num;
}

#endif