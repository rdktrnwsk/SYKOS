#include "Base.h"
#ifndef CULTURAL_CUH
#define CULTURAL_CUH

class CulturalData{
public:   

	CulturalData(int instanceSize, int numberOfSolutions) {

		_numOfConnections = 0;

		_h_inputAllowed = (int*)malloc(sizeof(int)); 
		_h_inputAllowed = 0;	
		cudaMalloc((void**) &_inputAllowed, sizeof(int));
		cudaMemcpy(_inputAllowed, _h_inputAllowed, sizeof(int), cudaMemcpyHostToDevice);

		_h_outputAllowed = (int*)malloc(sizeof(int)); 
		_h_outputAllowed = 0;	
		cudaMalloc((void**) &_outputAllowed, sizeof(int));
		cudaMemcpy(_outputAllowed, _h_outputAllowed, sizeof(int), cudaMemcpyHostToDevice);

		_h_myStatus = (int*)malloc(sizeof(int)); 
		_h_myStatus = 0;	
		cudaMalloc((void**) &_myStatus, sizeof(int));
		cudaMemcpy(_myStatus, _h_myStatus, sizeof(int), cudaMemcpyHostToDevice);

		/*_h_myVersionArray = (int*)malloc(sizeof(int) * numOfConnectedToUs); 
		for(int i = 0; i < numOfConnectedToUs; i++) {
			_h_myVersionArray[i] = 0;
		}
		cudaMalloc((void**) &_myVersionArray, numOfConnectedToUs *sizeof(int));
		cudaMemcpy(_myVersionArray, _h_myVersionArray, sizeof(int) * numOfConnectedToUs, cudaMemcpyHostToDevice);*/
		_h_myVersionArray = NULL;
		_myVersionArray = NULL;
		createVersionArray();

		solutionNumber = numberOfSolutions;
		createCuda2DArrayInt(_h_myData, _myData, NULL, instanceSize, numberOfSolutions);

		_h_result = (int*)malloc(sizeof(int));
		*_h_result = maxInt;	
		cudaMalloc((void**) &_result, sizeof(int));
		cudaMemcpy(_result, _h_result, sizeof(int) ,cudaMemcpyHostToDevice);

		cudaStreamCreate(&_myStream);

	};

    ~CulturalData(){
		for (int i = 0; i < solutionNumber; i++) {
			cudaFree(_h_myData[i]);
		}
		free(_h_myData);
		free(_h_inputAllowed);
		free(_h_outputAllowed);
		free(_h_myVersionArray);
		free(_h_myStatus);
		free(_h_result);

		cudaFree(_inputAllowed);
		cudaFree(_outputAllowed);
		cudaFree(_myStatus);
		cudaFree(_myVersionArray);
		cudaFree(_myData);
		cudaFree(_result);

		cudaStreamDestroy(_myStream);
		
	};

	int ID() {return _ID;};
	void ID(int num) {_ID = num;};

	int numOfConnections() {return _numOfConnections;};
	void numOfConnections(int num) {_numOfConnections = num;};

	int* outputAllowed() {return _outputAllowed;};
	void outputAllowed(int* ptr) {_outputAllowed = ptr;};
	int isOutputAllowed() {return *_outputAllowed;};

	int* inputAllowed() {return _inputAllowed;};
	void inputAllowed(int* ptr) {_inputAllowed = ptr;};
	int isInputAllowed() {return *_inputAllowed;};

	int* myVersionArray() {return _myVersionArray;};
	void myVersionArray(int* ptr) {_myVersionArray = ptr;};
	int* sbVersionArray() {return _sbVersionArray;};
	void sbVersionArray(int* ptr) {_sbVersionArray = ptr;};

	int* myStatus() {return _myStatus;};
	void myStatus(int* ptr) {_myStatus = ptr;};

	int* sbStatus() {return _sbStatus;};
	void sbStatus(int* ptr) {_sbStatus = ptr;};

	int** myData() {return _myData;};
	void myData(int** ptr) {_myData = ptr;};

	int** sbData() {return _sbData;};
	void sbData(int** ptr) {_sbData = ptr;};

	int* result() {return _result;};
	void result(int* ptr) {_result = ptr;};
	int getResultValue() {
		cudaMemcpy(_h_result, _result, sizeof(int) ,cudaMemcpyDeviceToHost);
		return *_h_result;
	}

	cudaStream_t getStream() { return _myStream;};

	void setup(CulturalData& sbCultural) {
		_sbVersionArray = sbCultural.myVersionArray();
		_sbStatus = sbCultural.myStatus();
		_sbData = sbCultural.myData();

		_ID = sbCultural.createVersionArray();
	}

	int createVersionArray() {

		if(_myVersionArray != NULL && _h_myVersionArray != NULL) {
			free(_h_myVersionArray);
			cudaFree(_myVersionArray);
		}

		_numOfConnections++;
		_h_myVersionArray = (int*)malloc(sizeof(int) * _numOfConnections); 
		for(int i = 0; i < _numOfConnections; i++) {
			_h_myVersionArray[i] = 0;
		}
		cudaMalloc((void**) &_myVersionArray, _numOfConnections *sizeof(int));
		cudaMemcpy(_myVersionArray, _h_myVersionArray, sizeof(int) * _numOfConnections, cudaMemcpyHostToDevice);
		return _numOfConnections - 1;
	}

private:

	int _ID; //ID of a Cultural component (have to be unique)
	int _numOfConnections; //number of Cultural components connected to us
	int* _outputAllowed; //output allowed code number (default 0 is not allowed)
	int* _inputAllowed; //input allowed code number (default 0 is not allowed)
	int* _myVersionArray; //my version array
	int* _sbVersionArray; //version array to which we are connected
	
	int** _myData; //my Data Array (data output)
	int** _sbData; //somebody Data Array (data input)

	int* _myStatus; //algorithm status (e.g. to comunnicate others our work is done)
	int* _sbStatus; //connected algorithm status (e.g. to know when end algorithm)

	int* _result; //result (number) in relation to whole algorithm (e.g. length of TSP path)

	cudaStream_t _myStream; //my cuda stream (m-heuristic)
	curandState* _randState; //random state

	int** _h_myData;
	int* _h_inputAllowed;
	int* _h_outputAllowed;
	int* _h_myStatus;
	int* _h_myVersionArray;
	int* _h_result;

	int solutionNumber;
};



class DeviceCultural {
public:
    __host__ DeviceCultural(CulturalData& device):
		_ID(device.ID()),
		_numOfConnections(device.numOfConnections()),
		_myVersionArray(device.myVersionArray()),
		_sbVersionArray(device.sbVersionArray()),
		_outputAllowed(device.outputAllowed()),
		_inputAllowed(device.inputAllowed()),
		_myStatus(device.myStatus()),
		_sbStatus(device.sbStatus()),
		_myData(device.myData()),
		_sbData(device.sbData()),
		_result(device.result())
        {}

	__forceinline__ __device__ int ID(){return _ID;}
	__forceinline__ __device__ int* outputAllowed(){return _outputAllowed;}
	__forceinline__ __device__ int isOutputAllowed(){return *_outputAllowed;}
	__forceinline__ __device__ int* inputAllowed(){return _inputAllowed;}
	__forceinline__ __device__ int isInputAllowed(){return *_inputAllowed;}
	__forceinline__ __device__ int numOfConnections(){return _numOfConnections;}
	__forceinline__ __device__ int* myVersionArray(){return _myVersionArray;}
	__forceinline__ __device__ int* sbVersionArray(){return _sbVersionArray;}
	__forceinline__ __device__ int* myStatus(){return _myStatus;}
	__forceinline__ __device__ int* sbStatus(){return _sbStatus;}
	__forceinline__ __device__ int** myData(){return _myData;}
	__forceinline__ __device__ int** sbData(){return _sbData;}
	__forceinline__ __device__ int* result(){return _result;}

	__forceinline__ __device__ void beforeOutput(int threadIndex);
	__forceinline__ __device__ void afterOutput(int threadIndex);

	__forceinline__ __device__ void beforeInput(int threadIndex);
	__forceinline__ __device__ void afterInput(int threadIndex);

	__forceinline__ __device__ void setStatus(int num);

	__forceinline__ __device__ void setResult(int num);

private:
	int _ID; //ID of a Cultural component (have to be unique)
	int _numOfConnections; //number of Cultural components connected to us
	int* _outputAllowed;
	int* _inputAllowed;

	int* _myVersionArray; //my version array
	int* _sbVersionArray; //version array to which we are connected

	int* _myStatus;
	int* _sbStatus;

	int** _myData;
	int** _sbData;

	int* _result;
};
#endif