#ifndef FUNCTIONS_CUH
#define FUNCTIONS_CUH

/**
 * Creates initial permutations for
 * 
 * @param filename GIF File name to be loaded
 * @return Inited GIF Handler or NULL for error
 */
void initialPermutations(int** parent, int populationSize, int instanceSize);


/**
 * create arrays on the host (CPU) and the device (GPU) of size rows/columns, optionally sending data to device
 * 
 * @param (hostPtr) pointer to an array on the host (CPU) side, every elements points to the device array (single row)!
 * @param (devicePtr) pointer to an array on the device (GPU) side (two dimensional)
 * @param (data) optional pointer to data which will be send to the device (structure size indicated by rows/columns)
 * @param (rows) number of rows to be created (first index)
 * @param (columns) number of columns to be created (second index)
 */
void createCuda2DArrayInt(int**& hostPtr, int**& devicePtr, int** data, int rows, int columns);
void createCuda2DArrayFloat(float**& hostPtr, float**& devicePtr, float** data, int rows, int columns);

int testRouteArray(int** deviceArray, int rows, int columns, char* message);
int testRouteArrayReversed(int** deviceArray, int rows, int columns, char* message);

#endif