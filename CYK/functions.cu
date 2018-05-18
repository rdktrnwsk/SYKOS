#include "Ogolne.h"
#ifndef FUNCTIONS_CU
#define FUNCTIONS_CU

void initialPermutations(int** hostArray, int populationSize, int instanceSize) {

	const int maxInt = MAXINT;

	//initial permutations
	for(int i = 0; i < populationSize; i++) {	

		for(int j = 0; j < instanceSize; j++) {
			hostArray[i][j] = j;
		}		

		//hostArray[i][instanceSize] = maxInt; //poczatkowa inicjalizacja
		//hostArray[i][instanceSize + 1] = 0;

		// Fisher–Yates
		for(int j = instanceSize - 1; j > 0; j--) {
			int x = rand() % (j + 1);
			int tmp = hostArray[i][x];
			hostArray[i][x] = hostArray[i][j];
			hostArray[i][j] = tmp;
		}
	}

}

void createCuda2DArrayInt(int**& hostPtr, int**& devicePtr, int** data, int rows, int columns) {

	hostPtr = (int**)malloc((rows) * sizeof(int*));

	for(int i = 0; i < rows; i++) {
		cudaMalloc((void**)&hostPtr[i], columns  * sizeof(int));
		if(data != NULL) {
			cudaMemcpy(hostPtr[i], &data[i][0], columns * sizeof(int), cudaMemcpyHostToDevice);
		} 
	}

	cudaMalloc((void ***)&devicePtr, rows * sizeof(int*));
	cudaMemcpy(devicePtr, hostPtr, rows * sizeof(int*), cudaMemcpyHostToDevice);
}

void createCuda2DArrayFloat(float**& hostPtr, float**& devicePtr, float** data, int rows, int columns) {

	hostPtr = (float**)malloc((rows) * sizeof(float*));

	for(int i = 0; i < rows; i++) {
		cudaMalloc((void**)&hostPtr[i], columns * sizeof(float));
		if(data != NULL) {
			cudaMemcpy(hostPtr[i], &data[i][0], columns * sizeof(float), cudaMemcpyHostToDevice);
		} 
	}

	cudaMalloc((void ***)&devicePtr, rows * sizeof(float*));
	cudaMemcpy(devicePtr, hostPtr, rows * sizeof(float*), cudaMemcpyHostToDevice);
}

void destroyCuda2DArray(int**& hostPtr, int**& devicePtr, int rows) {

	for (int i = 0; i < rows; i++) {
		cudaFree(hostPtr[i]);
	}
	cudaFree(devicePtr);
	free(hostPtr);												
}


int testRouteArrayReversed(int** deviceArray, int rows, int columns, char* message) {
		
	bool* test = (bool*)malloc(rows * sizeof(bool));
	for(int i = 0 ; i < rows ; i++){
		test[i] = false;
	}

	int** hostArray = (int**)malloc(rows * sizeof(int*));
	for(int i = 0; i < rows; i++) {
		hostArray[i] = (int*)malloc(columns * sizeof(int));					
	}

	for(int i = 0; i < rows; i++) {
		cudaMemcpy(hostArray[i], deviceArray[i], columns * sizeof(int), cudaMemcpyDeviceToHost);
	}

	for(int i = 0 ; i < columns; i++) {
		/*printf( "\n\n");
		for(int k = 0; k < rows; k++) {
					printf( "%d -> ", hostArray[k][i]);
				}*/
		for(int j = 0 ; j < rows; j++) {
			/*if(test[hostArray[j][i]] == false) {
				test[hostArray[j][i]] = true;
			} else {
				fprintf(stderr, "\nRow: %d, Col: %d, Val: %d, Message: %s\n", j, i, hostArray[j][i], message);
				for(int k = 0; k < rows; k++) {
					fprintf(stderr, "%d -> ", hostArray[k][i]);
				}
				return 1;
			}*/
			printf("%d -> ", hostArray[j][i]);

		}
		return 1;
		printf("___________________________________\n\n");
		for(int i = 0 ; i < rows ; i++){
			test[i] = false;
		}
	}

				
	for(int i = 0; i < rows; i++) {
		free(hostArray[i]);				
	}
	free(hostArray);
	free(test);
	return 1;
}

int testRouteArray(int** deviceArray, int rows, int columns, char* message) {
		
	bool* test = (bool*)malloc(columns * sizeof(bool));
	for(int i = 0 ; i < columns ; i++){
		test[i] = false;
	}

	int** hostArray = (int**)malloc(rows * sizeof(int*));
	for(int i = 0; i < rows; i++) {
		hostArray[i] = (int*)malloc(columns * sizeof(int));					
	}

	for(int i = 0; i < rows; i++) {
		cudaMemcpy(hostArray[i], deviceArray[i], columns * sizeof(int), cudaMemcpyDeviceToHost);
	}


	for(int i = 0 ; i < rows; i++) {
		for(int j = 0 ; j < columns; j++) {
			if(test[hostArray[i][j]] == false) {
				test[hostArray[i][j]] = true;
			} else {
				fprintf(stderr, "\nRow: %d, Col: %d, Val: %d, Message: %s\n", i, j, hostArray[i][j], message);
				for(int k = 0; k < columns; k++) {
					fprintf(stderr, "%d -> ", hostArray[i][k]);
				}
				getchar();
				return 1;
			}

		}
		for(int i = 0 ; i < columns ; i++) {
			test[i] = false;
		}
	}

	free(test);

	for(int i = 0; i < rows; i++)  {
		free(hostArray[i]);				
	}
	free(hostArray);
}


#endif