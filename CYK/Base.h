#ifndef BASE_H
#define BASE_H

#include <fstream>
#include <string>
#include <stdio.h>
#include <Windows.h>
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <curand.h>
#include <curand_kernel.h>
#include <iostream>
#include <time.h>
#include <assert.h>
#include <device_functions.h>
#include "functions.cuh"
#include "Ogolne.cuh"
using namespace std;

const int maxInt = 999999;


/******************************************************ACO DATA********************************************/

class AntData{
public:   
    AntData(float** instance, int instanceSize, int threadsNumber){

		instanceMatrix = instance;
		verticesNumber = instanceSize;

		//deafult values
		evaporationRate = 0.1f;
		tourNumber = 50;
		basePheromoneValue = 1000.0f;
		iterationNumber = 20;
		acceptRate = 20;

		createCuda2DArrayFloat(h_pheromoneMatrix, pheromoneMatrix, NULL, instanceSize , instanceSize);
		createCuda2DArrayInt(h_solutions, solutions, NULL, instanceSize + 2, threadsNumber); //additional space for metadata (e.g. route length)
		

		h_result = (int*)malloc(sizeof(int));
		*h_result = maxInt;	
		cudaMalloc((void**) &result, sizeof(int));
		cudaMemcpy(result, h_result, sizeof(int) ,cudaMemcpyHostToDevice);

		h_accExecutionNumber = (int*)malloc(sizeof(int));
		*h_accExecutionNumber = 0;	
		cudaMalloc((void**) &accExecutionNumber, sizeof(int));
		cudaMemcpy(accExecutionNumber, h_accExecutionNumber, sizeof(int) ,cudaMemcpyHostToDevice);

		h_accAllowNumber = (int*)malloc(sizeof(int));
		*h_accAllowNumber = 0;	
		cudaMalloc((void**) &accAllowNumber, sizeof(int));
		cudaMemcpy(accAllowNumber, h_accAllowNumber, sizeof(int) ,cudaMemcpyHostToDevice);
	};
    ~AntData(){
		for (int i = 0; i < verticesNumber; i++){
			cudaFree(h_pheromoneMatrix[i]);
			cudaFree(h_solutions[i]);
		}

		cudaFree(pheromoneMatrix);
		cudaFree(solutions);
		cudaFree(result);
		cudaFree(accAllowNumber);
		cudaFree(accExecutionNumber);

		free(h_pheromoneMatrix);
		free(h_result);
		free(h_accAllowNumber);
		free(h_accExecutionNumber);
		free(h_solutions);
	};

	float** getInstanceMatrix() { return instanceMatrix; };
	void setInstaneMatrix(float** ptr) { instanceMatrix = ptr; };

	float** getPheromoneMatrix() { return pheromoneMatrix; };
	void setPheromoneMatrix(float** ptr) { pheromoneMatrix = ptr; };

	int** getSolutions() { return solutions; };
	void setSolutions(int** ptr) { solutions = ptr; };

	int* getResult() { return result; };
	int  getResultValue() {
		cudaMemcpy(h_result, result, sizeof(int) ,cudaMemcpyDeviceToHost);
		return *h_result;
	};

	int* getAccExecutionNumber() { return accExecutionNumber; };
	int  getAccExecutionNumberValue() {
		cudaMemcpy(h_accExecutionNumber, accExecutionNumber, sizeof(int) ,cudaMemcpyDeviceToHost);
		return *h_accExecutionNumber;
	};

	int* getAccAllowNumber() { return accAllowNumber; };
	int  getAccAllowNumberValue() {
		cudaMemcpy(h_accAllowNumber, accAllowNumber, sizeof(int) ,cudaMemcpyDeviceToHost);
		return *h_accAllowNumber;
	};

	int getVerticesNumber() { return verticesNumber; };
	void setVerticesNumber(int num) { verticesNumber = num; };

	int getTourNumber() { return tourNumber; };
	void setTourNumber(int num) { tourNumber = num; };

	int getIterationNumber() { return iterationNumber; };
	void setIterationNumber(int num) { iterationNumber = num; };

	float getBasePheromoneValue() { return basePheromoneValue; };
	void setBasePheromoneValue(float num) { basePheromoneValue = num; };

	float getEvaporationRate() { return evaporationRate; };
	void setEvaporationRate(float num) { evaporationRate = num; };

	int getAcceptRate() { return acceptRate; };
	void setAcceptRate(int num) { acceptRate = num; };

private:


	float** instanceMatrix;

	float** h_pheromoneMatrix;
	float** pheromoneMatrix;

	int** h_solutions; //single ant best route
	int** solutions;

	int* h_result; // exchanging result point
	int* result;

	int* h_accExecutionNumber;
	int* accExecutionNumber;

	int* h_accAllowNumber;
	int* accAllowNumber;

	int verticesNumber;
	int tourNumber;
	int iterationNumber;
	float basePheromoneValue;
	float evaporationRate;
	int acceptRate;
};

class DeviceAntData{
public:
    __host__ DeviceAntData(AntData& device):
		instanceMatrix(device.getInstanceMatrix()),
		pheromoneMatrix(device.getPheromoneMatrix()),
        verticesNumber(device.getVerticesNumber()),
		tourNumber(device.getTourNumber()),
		iterationNumber(device.getIterationNumber()),
		basePheromoneValue(device.getBasePheromoneValue()),
		evaporationRate(device.getEvaporationRate()),
		acceptRate(device.getAcceptRate()),
		accAllowNumber(device.getAccAllowNumber()),
		accExecutionNumber(device.getAccExecutionNumber())
        {}

	__forceinline__ __device__ float** getInstanceMatrix() { return instanceMatrix;}
    __forceinline__ __device__ float** getPheromoneMatrix() { return pheromoneMatrix;}
	__forceinline__ __device__ int getVerticesNumber() { return verticesNumber;}
    __forceinline__ __device__ int getTourNumber() { return tourNumber;}
	__forceinline__ __device__ int getIterationNumber() { return iterationNumber;}
	__forceinline__ __device__ float getBasePheromoneValue() { return basePheromoneValue;}
	__forceinline__ __device__ float getEvaporationRate() { return evaporationRate;}
	__forceinline__ __device__ int getAcceptRate() { return acceptRate;}
	__forceinline__ __device__ int* getAccExecutionNumber() { return accExecutionNumber;}
	__forceinline__ __device__ int* getAccAllowNumber() { return accAllowNumber;}
private:
	float** instanceMatrix;
	float** pheromoneMatrix;

	int verticesNumber;
	int tourNumber;
	int iterationNumber;
	float basePheromoneValue;
	float evaporationRate;

	int* accExecutionNumber;
	int* accAllowNumber;

	int acceptRate;
};


/******************************************************CYK DATA********************************************/

class CYKData {
public:
	CYKData(int** cykArray, int inputStringLength, int** d_rulesNonTermsArray, int nonTerminalsCount ) {

		int cellWidth = ceil(((float)nonTerminalsCount / 32.0f));

		createCuda2DArrayInt(this->h_cykArray, this->cykArray, cykArray, inputStringLength, inputStringLength * cellWidth);
		
		rulesNonTermsArray = d_rulesNonTermsArray;

		nonTermsCount = nonTerminalsCount;
		inputCount = inputStringLength;

		h_result = (int*)malloc(sizeof(int));
		*h_result = 420;
		cudaMalloc((void**)&result, sizeof(int));
		cudaMemcpy(result, h_result, sizeof(int), cudaMemcpyHostToDevice);
	};
	~CYKData() {

		//TODO CHANGE
		for (int i = 0; i < this->inputCount; i++) {
			//free(this->cykArray[i]);
			cudaFree(this->h_cykArray[i]);
		}
		free(this->h_cykArray);

		free(h_result);
		cudaFree(result);
	};

	int** getCYKArray() { return cykArray; };
	void setCYKArray(int** ptr) { cykArray = ptr; };

	int** getRulesNonTermsArray() { return rulesNonTermsArray; };
	void setRulesNonTermsArray(int** ptr) { rulesNonTermsArray = ptr; };

	int getNonTermsCount() { return nonTermsCount; };
	void setNonTermsCount(int num) { nonTermsCount = num; };

	int getInputCount() { return inputCount; };
	void setInputCount(int num) { inputCount = num; };

	int* getResult() { return result; };
	int  getResultValue() {
		cudaMemcpy(h_result, result, sizeof(int), cudaMemcpyDeviceToHost);
		return *h_result;
	};

private:

	int** h_cykArray;
	int** cykArray;

	int** rulesNonTermsArray;
	int nonTermsCount;
	int inputCount;

	int* h_result; // exchanging result point
	int* result;

};

class DeviceCYKData {
public:
	__host__ DeviceCYKData(CYKData& device) :
		cykArray(device.getCYKArray()),
		rulesNonTermsArray(device.getRulesNonTermsArray()),
		nonTermsCount(device.getNonTermsCount()),
		inputCount(device.getInputCount()),
		result(device.getResult())
	{}

	__forceinline__ __device__ int** getCYKArray() { return cykArray; }
	__forceinline__ __device__ int** getRulesNonTermsArray() { return rulesNonTermsArray; }
	__forceinline__ __device__ int getInputCount() { return inputCount; }
	__forceinline__ __device__ int getNonTermsCount() { return nonTermsCount; }
	__forceinline__ __device__ int* getResult() { return result; }
	
private:

	int** cykArray;
	int** rulesNonTermsArray;
	int nonTermsCount;
	int inputCount;
	int* result;
	
};



#endif