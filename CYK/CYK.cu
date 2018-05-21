#include "CYK.cuh"

template<int action>
__global__ void cykAlgorithm(DeviceCYKData data, curandState * randGlobal)
{
	/*if (action == 1 || action == 2) {
		printf("%d", threadIdx.x);
	}*/

	__shared__ int** cykArray;
	__shared__ int inputStringLength;
	__shared__ int** rulesNonTermsArray;
	__shared__ int nonTermsCount;

	if (threadIdx.x == 0 && threadIdx.y == 0) {
		cykArray = data.getCYKArray();
		inputStringLength = data.getInputCount();
		rulesNonTermsArray = data.getRulesNonTermsArray();
		nonTermsCount = data.getNonTermsCount();
	}

	__syncthreads();

	if (action == 1) {
		if (threadIdx.x == 0) {
			int idx = threadIdx.x;

			for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)
				
				for (int j = 0; j < inputStringLength - i; j++) { // every word of given length 5, 4, 3, 2, 1... (2)

					for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

												  //TODO correct split points!
						int first = cykArray[k][j];
						int second = cykArray[i - k - 1][j + k + 1];

						//decode nonterminals (find out if bits are on a given positions)
						int base = 1;
						for (int l = 0; l < nonTermsCount; l++) {
						
							int bitMaskFirst = base << l;

							// all possibilities connected with rules
							for (int m = 0; m < nonTermsCount; m++) {
								int bitMaskSecond = base << m;

								// if rule with 'l' index and 'm' index is created and ready to be found if corrrect X ->lm (does X exist in a grammar?)
								if (first & bitMaskFirst && second & bitMaskSecond) {

									//rule exists
									if (rulesNonTermsArray[l][m] != -1) {
										int shiftValue = rulesNonTermsArray[l][m];
										int bitValue = base << shiftValue;

										cykArray[i][j] |= bitValue;
									}

								}

							}

						} // l loop end

					}

				}

				//break; //only first line

			}
		} 
	} else if (action == 2) { //////////////////////////////////////////////////////////////// each entry 1D threads (last loop 1)

		if (threadIdx.x <= 32) {
			int idx = threadIdx.x;

			for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

				for (int j = 0; j < inputStringLength - i; j++) { // every word of given length 5, 4, 3, 2, 1... (2)

					for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

												  //TODO correct split points!
						int first = cykArray[k][j];
						int second = cykArray[i - k - 1][j + k + 1];

						//decode nonterminals (find out if bits are on a given positions)
						int base = 1;
						//for (int l = 0; l < nonTermsCount; l++) {
						int l = idx;
						int bitMaskFirst = base << l;
						//all possibilities connected with rules

						for (int m = 0; m < nonTermsCount; m++) {
							int bitMaskSecond = base << m;

							// if rule with 'l' index and 'm' index is created and ready to be found if corrrect X ->lm (does X exist in a grammar?)
							if (first & bitMaskFirst && second & bitMaskSecond) {
								//cout << bitMaskFirst << ", " << bitMaskSecond << " | ";

								//rule exists
								if (rulesNonTermsArray[l][m] != -1) {
									int shiftValue = rulesNonTermsArray[l][m];
									int bitValue = base << shiftValue;

									//TODO - tutaj może być problem
									atomicOr(&cykArray[i][j], bitValue);

									//cykArray[i][j] |= bitValue;
								}

							}


						}

						//} // l loop end

						//cout << first << " | " << second << endl;

						//combinations of productions

						// for each production (rulesNonTerminals)

					}

				}

				//break; //only first line

			}
		}
	} else if (action == 3) { //////////////////////////////////////////////////////////////// each entry 2D threads (last loop 1)

	 if (threadIdx.x <= nonTermsCount && threadIdx.y <= nonTermsCount) {
		 int idx = threadIdx.x;
		 int idy = threadIdx.y;

		 for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

			 for (int j = 0; j < inputStringLength - i; j++) { // every word of given length 5, 4, 3, 2, 1... (2)

				 for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

											   //TODO correct split points!
					 int first = cykArray[k][j];
					 int second = cykArray[i - k - 1][j + k + 1];

					 //decode nonterminals (find out if bits are on a given positions)
					 int base = 1;
					 //for (int l = 0; l < nonTermsCount; l++) {
					 int l = idx;
					 int bitMaskFirst = base << l;
					 //all possibilities connected with rules

					 //for (int m = 0; m < nonTermsCount; m++) {

						 int m = idy;

						 int bitMaskSecond = base << m;

						 // if rule with 'l' index and 'm' index is created and ready to be found if corrrect X ->lm (does X exist in a grammar?)
						 if (first & bitMaskFirst && second & bitMaskSecond) {
							 //cout << bitMaskFirst << ", " << bitMaskSecond << " | ";

							 //rule exists
							 if (rulesNonTermsArray[l][m] != -1) {
								 int shiftValue = rulesNonTermsArray[l][m];
								 int bitValue = base << shiftValue;

								 //TODO - tutaj może być problem
								 atomicOr(&cykArray[i][j], bitValue);

								 //cykArray[i][j] |= bitValue;
							 }

						 }


					// }

					 //} // l loop end

					 //cout << first << " | " << second << endl;

					 //combinations of productions

					 // for each production (rulesNonTerminals)

				 }

			 }

			 //break; //only first line

		 }
	 }
 }

	
	
	__syncthreads();
	
	if (threadIdx.x == 0 && threadIdx.y == 0) {

		for (int i = 0; i < nonTermsCount; i++) {
			for (int j = 0; j < nonTermsCount; j++) {
				//cout << rulesNonTermsArray[i][j] << " | ";

				printf("%d | ", rulesNonTermsArray[i][j]);
			}
			//cout << endl;

			printf("\n");
		}

		for (int j = 1; j < inputStringLength; j++) {
			for (int i = 0; i < inputStringLength - j; i++) {
				printf("%d | ", cykArray[j][i]);
			}
			printf("\n");
		}

		int* result = data.getResult();
		printf("RESUUUULt: %d | ", result[0]);
		result[0] = 1337;
	}

	__syncthreads();

	return;
}

/*                                                                                      GLOBAL FUNCTION                                                                     */

__device__ volatile int g_mutex;

template<int action>
__global__ void cykAlgorithmCooperative(DeviceCYKData data, curandState * randGlobal)
{
	__shared__ int** cykArray;
	__shared__ int inputStringLength;
	__shared__ int** rulesNonTermsArray;
	__shared__ int nonTermsCount;

	int bidx = blockIdx.x;
	int idx = threadIdx.x;
	int idy = threadIdx.y;

	if (threadIdx.x == 0 && threadIdx.y == 0) {
		g_mutex = 0;
		cykArray = data.getCYKArray();
		inputStringLength = data.getInputCount();
		rulesNonTermsArray = data.getRulesNonTermsArray();
		nonTermsCount = data.getNonTermsCount();
		//printf("HEHEHEHEHEHHE:%d | ", bidx);
	}


	__syncthreads();

	if (action == 0) { //////////////////////////////////////////////////////////////// entry = block, block used are decremented, threads 2D

		if (threadIdx.x <= nonTermsCount && threadIdx.y <= nonTermsCount) {
		

			for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

				//for (int j = 0; j < inputStringLength - i; j++) { // every word of given length 5, 4, 3, 2, 1... (2)
				if (bidx < inputStringLength - i) {
					int j = bidx;

					for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

												  //TODO correct split points!
						int first = cykArray[k][j];
						int second = cykArray[i - k - 1][j + k + 1];

						//decode nonterminals (find out if bits are on a given positions)
						int base = 1;
						//for (int l = 0; l < nonTermsCount; l++) {
						int l = idx;
						int bitMaskFirst = base << l;
						//all possibilities connected with rules

						//for (int m = 0; m < nonTermsCount; m++) {

						int m = idy;

						int bitMaskSecond = base << m;

						// if rule with 'l' index and 'm' index is created and ready to be found if corrrect X ->lm (does X exist in a grammar?)
						if (first & bitMaskFirst && second & bitMaskSecond) {
							//cout << bitMaskFirst << ", " << bitMaskSecond << " | ";

							//rule exists
							if (rulesNonTermsArray[l][m] != -1) {
								int shiftValue = rulesNonTermsArray[l][m];
								int bitValue = base << shiftValue;

								//TODO - tutaj może być problem
								atomicOr(&cykArray[i][j], bitValue);

								//cykArray[i][j] |= bitValue;
							}

						}


						// }

						//} // l loop end

						//cout << first << " | " << second << endl;

						//combinations of productions

						// for each production (rulesNonTerminals)

					}

				}

				//break; //only first line
				if (idx == 0 && idy == 0) {
					atomicAdd((int *)&g_mutex, 1);
					//only when all blocks add 1 to g_mutex
					//will g_mutex equal to goalVal
					while (g_mutex != (10 * i)) {
						//Do nothing here
					}
				}
				__syncthreads();

			}
		}

		// only thread 0 is used for synchronization


	}

	


	__syncthreads();

	if (threadIdx.x == 0 && threadIdx.y == 0 && bidx == 0) {

		for (int i = 0; i < nonTermsCount; i++) {
			for (int j = 0; j < nonTermsCount; j++) {
				//cout << rulesNonTermsArray[i][j] << " | ";

				printf("%d | ", rulesNonTermsArray[i][j]);
			}
			//cout << endl;

			printf("\n");
		}

		for (int j = 1; j < inputStringLength; j++) {
			for (int i = 0; i < inputStringLength - j; i++) {
				printf("%d | ", cykArray[j][i]);
			}
			printf("\n");
		}

		int* result = data.getResult();
		printf("RESUUUULt: %d | ", result[0]);
		result[0] = 1337;
	}

	__syncthreads();

	return;
}


