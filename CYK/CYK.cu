#include "CYK.cuh"

template<int action>
__global__ void cykAlgorithm(DeviceCYKData data, curandState * randGlobal) {

	__shared__ int** cykArray;
	__shared__ int inputStringLength;
	__shared__ int** rulesNonTermsArray;
	__shared__ int nonTermsCount;
	__shared__ int cellWidth;

	if (threadIdx.x == 0 && threadIdx.y == 0) {
		cykArray = data.getCYKArray();
		inputStringLength = data.getInputCount();
		rulesNonTermsArray = data.getRulesNonTermsArray();
		nonTermsCount = data.getNonTermsCount();
		cellWidth = (int)(ceilf(((float)nonTermsCount / 32.0f)));
	}

	__syncthreads();

	if (action == 0) {
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


							if (first & bitMaskFirst) {

								// all possibilities connected with rules
								for (int m = 0; m < nonTermsCount; m++) {
									int bitMaskSecond = base << m;

									// if rule with 'l' index and 'm' index is created and ready to be found if corrrect X ->lm (does X exist in a grammar?)
									if (second & bitMaskSecond) {

										//rule exists
										if (rulesNonTermsArray[l][m] != -1) {
											int shiftValue = rulesNonTermsArray[l][m];
											int bitValue = base << shiftValue;

											cykArray[i][j] |= bitValue;
										}

									}

								}
							}

						} // l loop end

					}

				}

				//break; //only first line

			}
		}
	} else if (action == 1) {

		int idx = threadIdx.x;

		if (idx < nonTermsCount) {
			
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

							if (first & bitMaskFirst) {
								// all possibilities connected with rules
								//for (int m = 0; m < nonTermsCount; m++) {
								int m = idx;

								int bitMaskSecond = base << m;

								// if rule with 'l' index and 'm' index is created and ready to be found if corrrect X ->lm (does X exist in a grammar?)
								//if (first & bitMaskFirst && second & bitMaskSecond) {
								if (second & bitMaskSecond) {

									//rule exists
									if (rulesNonTermsArray[l][m] != -1) {
										int shiftValue = rulesNonTermsArray[l][m];
										int bitValue = base << shiftValue;

										cykArray[i][j] |= bitValue;
									}

								}

								//}
							}

						} // l loop end

					}

				}

				//break; //only first line

			}
		} 
	} else if (action == 2) { //////////////////////////////////////////////////////////////// each entry 1D threads (last loop 1)

		int idx = threadIdx.x;

		if (idx < nonTermsCount) {
			for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

				for (int j = 0; j < inputStringLength - i; j++) { // every word of given length 5, 4, 3, 2, 1... (2)

					for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

												  //TODO correct split points!
						int first = cykArray[k][j];
						int second = cykArray[i - k - 1][j + k + 1];

						//decode nonterminals (find out if bits are on a given positions)
						int base = 1;
						//for (int m = 0; m < nonTermsCount; m++) {
						int m = idx;
						int bitMaskFirst = base << m;
						//all possibilities connected with rules
						if (first & bitMaskFirst) {

					
							for (int n = 0; n < nonTermsCount; n++) {
								int bitMaskSecond = base << n;

								// if rule with 'm' index and 'n' index is created and ready to be found if corrrect X ->mn (does X exist in a grammar?)
								if (second & bitMaskSecond) {
									//cout << bitMaskFirst << ", " << bitMaskSecond << " | ";

									//rule exists
									if (rulesNonTermsArray[m][n] != -1) {
										int shiftValue = rulesNonTermsArray[m][n];
										int bitValue = base << shiftValue;

										//TODO - tutaj może być problem
										atomicOr(&cykArray[i][j], bitValue);
										//cykArray[i][j] |= bitValue;
									}

								}

							}
						}


					}

				}

			}
		}

		
	} else if (action == 3) { //////////////////////////////////////////////////////////////// each entry 2D threads (last loop 1)

	 if (threadIdx.x < nonTermsCount && threadIdx.y < nonTermsCount) {
		 int idx = threadIdx.x;
		 int idy = threadIdx.y;

		 //for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

			// for (int j = 0; j < inputStringLength - i; j++) { // every word of given length 5, 4, 3, 2, 1... (2)

			//	 for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

			//								   //TODO correct split points!
			//		 int first = cykArray[k][j];
			//		 int second = cykArray[i - k - 1][j + k + 1];

			//		 //decode nonterminals (find out if bits are on a given positions)
			//		 int base = 1;

			//		 int l = idx;
			//		 int bitMaskFirst = base << l;



			//			 int m = idy;

			//			 int bitMaskSecond = base << m;

			//			 // if rule with 'l' index and 'm' index is created and ready to be found if corrrect X ->lm (does X exist in a grammar?)
			//			 if (first & bitMaskFirst && second & bitMaskSecond) {
			//				 //cout << bitMaskFirst << ", " << bitMaskSecond << " | ";

			//				 //rule exists
			//				 if (rulesNonTermsArray[l][m] != -1) {
			//					 int shiftValue = rulesNonTermsArray[l][m];
			//					 int bitValue = base << shiftValue;

			//					 //TODO - tutaj może być problem
			//					 atomicOr(&cykArray[i][j], bitValue);

			//					 //cykArray[i][j] |= bitValue;
			//				 }

			//			 }

			//	 }

			// }

		 //}
		 for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

			 for (int j = 0; j < (inputStringLength - i) * cellWidth; j += cellWidth) { // every word <of given length: 5 words, 4 words, 3 words, 2, 1...> (2)

				 for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

											   //decode nonterminals (find out if bits are on a given positions)
					 int base = 1;
					 float iterM = ceilf((float)(nonTermsCount) / (float)blockDim.x);
					 //for (int m = 0; m < nonTermsCount; m++) {
					 for (int md = 0; md < (int)iterM; md++) {

						int temp_idx = idx + (md * blockDim.x);
					 
						int m = temp_idx;

						 int offset = (int)(m / 32);
						 int first = cykArray[k][j + offset];
						 int bitMaskFirst = (base << (m - (offset * 32)));

						 if (first & bitMaskFirst) {

							 float iterN = ceilf((float)(nonTermsCount) / (float)blockDim.y);
							 // for (int n = 0; n < nonTermsCount; n++) {
							 for (int nd = 0; nd < (int)iterN; nd++) {

								 int temp_idy = idy + (nd * blockDim.y);
							 //all possibilities connected with rules
							
								int n = temp_idy;

								 int offset2 = (int)(n / 32); // shift by 32 is the next cell
								 int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];
								 int bitMaskSecond = (base << (n - (offset2 * 32)));

								 if (second & bitMaskSecond) {

									 //rule exists
									 if (rulesNonTermsArray[m][n] != -1) {
										 int shiftValue = rulesNonTermsArray[m][n];
										 //int bitValue = base << shiftValue;

										 int offset = (int)(shiftValue / 32); // shift by 32 is the next cell
										 int base = 1;
										 int bitValue = base << (shiftValue - (offset * 32));

										 cykArray[i][j + offset] |= bitValue;
									 }

								 }

							 } // end n loop
						 }

					 } // end m loop

				 } // end k loop

			 } // end j loop

		 } // end i loop
	 }
 }	else if (action == 4) { //////////////////////////////////////////////////////////////// magisterka rozwiazanie pierwsze

	 //int idx = threadIdx.x;

	 ////if (idx < inputStringLength) {
		//
		// for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

		//	 //for (int j = 0; j < inputStringLength - i; j++) { // every word of given length 5, 4, 3, 2, 1... (2)

		//	 if (threadIdx.x < inputStringLength - i) {
		//		 int j = threadIdx.x;

		//		 for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

		//									   //TODO correct split points!
		//			 int first = cykArray[k][j];
		//			 int second = cykArray[i - k - 1][j + k + 1];

		//			 //decode nonterminals (find out if bits are on a given positions)
		//			 int base = 1;
		//			 for (int l = 0; l < nonTermsCount; l++) {

		//				 int bitMaskFirst = base << l;
		//				 if (first & bitMaskFirst) {

		//					 // all possibilities connected with rules
		//					 for (int m = 0; m < nonTermsCount; m++) {
		//						 int bitMaskSecond = base << m;

		//						 // if rule with 'l' index and 'm' index is created and ready to be found if corrrect X ->lm (does X exist in a grammar?)
		//						 if (second & bitMaskSecond) {

		//							 //rule exists
		//							 if (rulesNonTermsArray[l][m] != -1) {
		//								 int shiftValue = rulesNonTermsArray[l][m];
		//								 int bitValue = base << shiftValue;

		//								 cykArray[i][j] |= bitValue;
		//							 }

		//						 }

		//					 } // m loop
		//				 }

		//			 } // l loop end

		//		 } // k loop

		//	 }

		//	 __syncthreads();

		//	 //break; //only first line

		//	}
		////}
	 int idx = threadIdx.x;

	 int base = 1;
	 for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

		 float iterJ = ceilf((float)(inputStringLength - i) / (float)blockDim.x);
		 for (int jd = 0; jd < (int)iterJ; jd++) { // every word <of given length: 5 words, 4 words, 3 words, 2, 1...> (2)
												   ////TODO!!!!
			 int temp_idx = idx + (jd * blockDim.x);

			 if (temp_idx < inputStringLength - i) {

				 for (int k = 0; k < i; k++) {
	
					 //printf("%d - %d \n", temp_idx, temp_idy);

					 int j = temp_idx * cellWidth;

					 for (int m = 0; m < nonTermsCount; m++) {

						 int offset = (int)(m / 32);
						 int first = cykArray[k][j + offset];
						 int bitMaskFirst = (base << (m - (offset * 32)));

						 //if (first & bitMaskFirst) {
						 if (first & bitMaskFirst) {

							 for (int n = 0; n < nonTermsCount; n++) {

								 int offset2 = (int)(n / 32); // shift by 32 is the next cell
								 int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];
								 int bitMaskSecond = (base << (n - (offset2 * 32)));

								 if (second & bitMaskSecond) {

									 //rule exists
									 if (rulesNonTermsArray[m][n] != -1) {

										 int shiftValue = rulesNonTermsArray[m][n];
										 //int bitValue = base << shiftValue;

										 int offset = (int)(shiftValue / 32); // shift by 32 is the next cell
										 int base = 1;
										 int bitValue = base << (shiftValue - (offset * 32));

										 //cykArray[i][j + offset] |= bitValue;

										 atomicOr(&cykArray[i][j + offset], bitValue);
									 }

								 }

							 } // end n loop
						 }

					 } // end m loop

				 } // end k loop

			 } 

		 } // end j loop

		 __syncthreads();

	 } // end i loop
	}
 else if (action == 5) { //////////////////////////////////////////////////////////////// magisterka rozwiazanie drugie

	 int idx = threadIdx.x;
	 int idy = threadIdx.y;

		 //for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

			// /*int pidx = i - idy - 1;
			// int pidy = idx + idy + 1;*/

			// //for (int j = 0; j < inputStringLength - i; j++) { // every word of given length 5, 4, 3, 2, 1... (2)

			// float iter = ceilf((float)(inputStringLength - i) / (float)blockDim.x);
			// //iter = 2.0f;

			// for (int r = 0; r < (int)iter; r++) {

			//	 int temp_idx = idx + (r * blockDim.x);

			//	 float iter2 = ceilf((float)(i) / (float)blockDim.y);

			//	 for (int s = 0; s < (int)iter2; s++) {

			//		 int temp_idy = idy + (s * blockDim.y);

			//	 if (temp_idx < inputStringLength - i && temp_idy < i) {
			//		 int j = temp_idx;
			//		 int k = temp_idy;

			//		 //for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

			//			 //TODO correct split points!
			//			 int first = cykArray[k][j];
			//			 int second = cykArray[i - k - 1][j + k + 1];

			//			 //decode nonterminals (find out if bits are on a given positions)
			//			 int base = 1;
			//			 for (int l = 0; l < nonTermsCount; l++) {

			//				 int bitMaskFirst = base << l;

			//				 // all possibilities connected with rules
			//				 for (int m = 0; m < nonTermsCount; m++) {
			//					 int bitMaskSecond = base << m;

			//					 // if rule with 'l' index and 'm' index is created and ready to be found if corrrect X ->lm (does X exist in a grammar?)
			//					 if (first & bitMaskFirst && second & bitMaskSecond) {

			//						 //rule exists
			//						 if (rulesNonTermsArray[l][m] != -1) {
			//							 int shiftValue = rulesNonTermsArray[l][m];
			//							 int bitValue = base << shiftValue;

			//							 cykArray[i][j] |= bitValue;
			//						 }

			//					 }

			//				 }

			//			 } // l loop end
			//	 

			//		 //} // k loop

			//		 }
			//	 } // end s loop

		 //} // r loop

			// __syncthreads();

			// //break; //only first line

		 //} // l loop
		 
	 //if (idx < inputStringLength && idy < inputStringLength) {
	 if (true) {
	 
	 int base = 1;
	 for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

		 float iterJ = ceilf((float)(inputStringLength - i) / (float)blockDim.x);
		 for (int jd = 0; jd < (int)iterJ; jd++) { // every word <of given length: 5 words, 4 words, 3 words, 2, 1...> (2)
																////TODO!!!!
			 int temp_idx = idx + (jd * blockDim.x);

			 float iterK = ceilf((float)(i) / (float)blockDim.y);
			 for (int kd = 0; kd < (int)iterK; kd++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

				 int temp_idy = idy + (kd * blockDim.y);

				 if (temp_idx < inputStringLength - i && temp_idy < i) {

					 //printf("%d - %d \n", temp_idx, temp_idy);

					 int j = temp_idx * cellWidth;
					 int k = temp_idy;
					
					 for (int m = 0; m < nonTermsCount; m++) {

						 int offset = (int)(m / 32);
						 int first = cykArray[k][j + offset];
						 int bitMaskFirst = (base << (m - (offset * 32)));

						 //if (first & bitMaskFirst) {
						 if (first & bitMaskFirst) {
							 
							 for (int n = 0; n < nonTermsCount; n++) {

								 int offset2 = (int)(n / 32); // shift by 32 is the next cell
								 int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];
								 int bitMaskSecond = (base << (n - (offset2 * 32)));

								 if (second & bitMaskSecond) {
									 
									 //rule exists
									 if (rulesNonTermsArray[m][n] != -1) {
										 
										 int shiftValue = rulesNonTermsArray[m][n];
										 //int bitValue = base << shiftValue;

										 int offset = (int)(shiftValue / 32); // shift by 32 is the next cell
										 int base = 1;
										 int bitValue = base << (shiftValue - (offset * 32));

										 //cykArray[i][j + offset] |= bitValue;

										 atomicOr(&cykArray[i][j + offset], bitValue);
									 }

								 }

							 } // end n loop
						 }

					 } // end m loop

				 }

			 } // end k loop

		 } // end j loop

		 __syncthreads();

	 } // end i loop


 }
	 } else if (action == 101) { //////////////////////////////////////////////////////////////// magisterka rozwiazanie drugie

		 int idx = threadIdx.x;
		 int idy = threadIdx.y;

			int base = 1;
			for (int i = 1; i < inputStringLength; i++) {

				float iterJ = ceilf((float)(inputStringLength - i) / (float)blockDim.x);
				for (int jd = 0; jd < (int)iterJ; jd++) { 
														
					int temp_idx = idx + (jd * blockDim.x);

					float iterK = ceilf((float)(i) / (float)blockDim.y);
					for (int kd = 0; kd < (int)iterK; kd++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

						int temp_idy = idy + (kd * blockDim.y);

						if (temp_idx < inputStringLength - i && temp_idy < i) {

							//printf("%d - %d \n", temp_idx, temp_idy);

							int j = temp_idx * cellWidth;
							int k = temp_idy;

							for (int m = 0; m < nonTermsCount; m++) {

								int offset = (int)(m / 32);
								int first = cykArray[k][j + offset];
								int bitMaskFirst = (base << (m - (offset * 32)));

								//if (first & bitMaskFirst) {
								if (first & bitMaskFirst) {

									for (int n = 0; n < nonTermsCount; n++) {

										int offset2 = (int)(n / 32); // shift by 32 is the next cell
										int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];
										int bitMaskSecond = (base << (n - (offset2 * 32)));

										if (second & bitMaskSecond) {

											//rule exists
											if (rulesNonTermsArray[m][n] != -1) {

												int shiftValue = rulesNonTermsArray[m][n];
												//int bitValue = base << shiftValue;

												int offset = (int)(shiftValue / 32); // shift by 32 is the next cell
												int base = 1;
												int bitValue = base << (shiftValue - (offset * 32));

												//cykArray[i][j + offset] |= bitValue;

												atomicOr(&cykArray[i][j + offset], bitValue);
											}

										}

									} // end n loop
								}

							} // end m loop

						}

					} // end k loop

				} // end j loop

				__syncthreads();

			} // end i loop

	 }

	
	__syncthreads();
	
	if (threadIdx.x == 0 && threadIdx.y == 0) {

		/*for (int i = 0; i < nonTermsCount; i++) {
			for (int j = 0; j < nonTermsCount; j++) {

				printf("%d | ", rulesNonTermsArray[i][j]);
			}

			printf("\n");
		}*/

		/*for (int j = 1; j < inputStringLength; j++) {
			for (int i = 0; i < inputStringLength - j; i++) {
				printf("%d | ", cykArray[j][i]);
			}
			printf("\n");
		}*/

		int* result = data.getResult();
		//printf("RESUUUULt: %d | ", result[0]);
		result[0] = cykArray[inputStringLength - 1][0];
		//printf("JEST? %d \n", cykArray[inputStringLength -1][0]);
	}

	__syncthreads();

	return;
}

/*                                                                                      GLOBAL FUNCTION                                                                     */

__device__ volatile int g_mutex;

template<int action>
__global__ void cykAlgorithmCooperative(DeviceCYKData data, curandState * randGlobal, volatile int* arrayIn, volatile int* arrayOut, int additionalVariable) {
	__shared__ int** cykArray;
	__shared__ int inputStringLength;
	__shared__ int** rulesNonTermsArray;
	__shared__ int nonTermsCount;
	__shared__ int cellWidth;

	int bidx = blockIdx.x;
	int bidy = blockIdx.y;
	int idx = threadIdx.x;
	int idy = threadIdx.y;

	if (threadIdx.x == 0 && threadIdx.y == 0) {
		g_mutex = 0;
		cykArray = data.getCYKArray();
		inputStringLength = data.getInputCount();
		rulesNonTermsArray = data.getRulesNonTermsArray();
		nonTermsCount = data.getNonTermsCount();
		//printf("Dim %d\n", gridDim.x);
		cellWidth = (int)(ceilf(((float)nonTermsCount / 32.0f)));
	}


	__syncthreads();

	if (action == 0) { //////////////////////////////////////////////////////////////// entry = block, block used are decremented, threads 2D

		if (threadIdx.x < nonTermsCount && threadIdx.y < nonTermsCount ) {
		
			for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)
				
				//for (int j = 0; j < inputStringLength - i; j++) { // every word of given length 5, 4, 3, 2, 1... (2)

				float iter = ceilf((float)(inputStringLength - i) / (float)gridDim.x);
				//iter = 2.0f;
				//if (iter < 1.0f) iter = 1.0f;
				

				for (int r = 0; r < (int)iter ; r++) {

					int temp_bidx = bidx + (r * gridDim.x);

					
					if (temp_bidx < inputStringLength - i) {
						int j = temp_bidx;

						

						for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

													  //TODO correct split points!
							//int first = cykArray[k][j];
							//int second = cykArray[i - k - 1][j + k + 1];

							////decode nonterminals (find out if bits are on a given positions)
							//int base = 1;
							////for (int l = 0; l < nonTermsCount; l++) {
							//int l = idx;
							//int bitMaskFirst = base << l;
							////all possibilities connected with rules

							////for (int m = 0; m < nonTermsCount; m++) {

							//int m = idy;

							//int bitMaskSecond = base << m;

							//// if rule with 'l' index and 'm' index is created and ready to be found if corrrect X ->lm (does X exist in a grammar?)
							//if (first & bitMaskFirst && second & bitMaskSecond) {
							//	//cout << bitMaskFirst << ", " << bitMaskSecond << " | ";

							//	//rule exists
							//	if (rulesNonTermsArray[l][m] != -1) {
							//		int shiftValue = rulesNonTermsArray[l][m];
							//		int bitValue = base << shiftValue;

							//		//TODO - tutaj może być problem
							//		atomicOr(&cykArray[i][j], bitValue);

							//		//cykArray[i][j] |= bitValue;
							//	}

							//}
							int base = 1;
							float iterM = ceilf((float)(nonTermsCount) / (float)blockDim.x);
							//for (int m = 0; m < nonTermsCount; m++) {
							for (int md = 0; md < (int)iterM; md++) {

								int temp_idx = idx + (md * blockDim.x);

								int m = temp_idx;

								int offset = (int)(m / 32);
								int first = cykArray[k][j + offset];
								int bitMaskFirst = (base << (m - (offset * 32)));

								if (first & bitMaskFirst) {

									float iterN = ceilf((float)(nonTermsCount) / (float)blockDim.y);
									// for (int n = 0; n < nonTermsCount; n++) {
									for (int nd = 0; nd < (int)iterN; nd++) {

										int temp_idy = idy + (nd * blockDim.y);
										//all possibilities connected with rules

										int n = temp_idy;

										int offset2 = (int)(n / 32); // shift by 32 is the next cell
										int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];
										int bitMaskSecond = (base << (n - (offset2 * 32)));

										if (second & bitMaskSecond) {

											//rule exists
											if (rulesNonTermsArray[m][n] != -1) {
												int shiftValue = rulesNonTermsArray[m][n];
												//int bitValue = base << shiftValue;

												int offset = (int)(shiftValue / 32); // shift by 32 is the next cell
												int base = 1;
												int bitValue = base << (shiftValue - (offset * 32));

												//cykArray[i][j + offset] |= bitValue;
												atomicOr(&cykArray[i][j + offset], bitValue);
											}

										}

									} // end n loop
								}

							} // end m loop

						}

					}
				}

				//break; //only first line
				if (idx == 0 && idy == 0) {
					//printf("%d | ", g_mutex);
					atomicAdd((int *)&g_mutex, 1);
					//only when all blocks add 1 to g_mutex
					//will g_mutex equal to goalVal
					while (g_mutex != (gridDim.x * i)) {
						//Do nothing here
					}
					
				}
				__syncthreads();

			}
		}

		// only thread 0 is used for synchronization

		//int base = 1;
	 //for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

		// float iterJ = ceilf((float)(inputStringLength - i) / (float)blockDim.x);
		// for (int jd = 0; jd < (int)iterJ; jd++) { // every word <of given length: 5 words, 4 words, 3 words, 2, 1...> (2)
		//														////TODO!!!!
		//	 int temp_idx = idx + (jd * blockDim.x);

		//	 float iterK = ceilf((float)(i) / (float)blockDim.y);
		//	 for (int kd = 0; kd < (int)iterK; kd++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

		//		 int temp_idy = idy + (kd * blockDim.y);

		//		 if (temp_idx < inputStringLength - i && temp_idy < i) {

		//			 //printf("%d - %d \n", temp_idx, temp_idy);

		//			 int j = temp_idx * cellWidth;
		//			 int k = temp_idy;

		//			 

		//			 for (int m = 0; m < nonTermsCount; m++) {

		//				 int offset = (int)(m / 32);
		//				 int first = cykArray[k][j + offset];
		//				 int bitMaskFirst = (base << (m - (offset * 32)));

		//				 //if (first & bitMaskFirst) {
		//				 if (first & bitMaskFirst) {
		//					 
		//					 for (int n = 0; n < nonTermsCount; n++) {

		//						 int offset2 = (int)(n / 32); // shift by 32 is the next cell
		//						 int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];
		//						 int bitMaskSecond = (base << (n - (offset2 * 32)));

		//						 if (second & bitMaskSecond) {
		//							 
		//							 //rule exists
		//							 if (rulesNonTermsArray[m][n] != -1) {
		//								 
		//								 int shiftValue = rulesNonTermsArray[m][n];
		//								 //int bitValue = base << shiftValue;

		//								 int offset = (int)(shiftValue / 32); // shift by 32 is the next cell
		//								 int base = 1;
		//								 int bitValue = base << (shiftValue - (offset * 32));

		//								 cykArray[i][j + offset] |= bitValue;
		//							 }

		//						 }

		//					 } // end n loop
		//				 }

		//			 } // end m loop

		//		 }

		//	 } // end k loop

		// } // end j loop

		// __syncthreads();

	 //} // end i loop


	} else if (action == 1) { //////////////////////////////////////////////////////////////// entry = block, block used are decremented, threads 2D + FAST BARIER SYNCHRONISATION

		if (threadIdx.x <= nonTermsCount && threadIdx.y <= nonTermsCount) {


			for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

				__syncthreads();
														  //for (int j = 0; j < inputStringLength - i; j++) { // every word of given length 5, 4, 3, 2, 1... (2)

				float iter = ceilf((float)(inputStringLength - i) / (float)gridDim.x);
				//iter = 2.0f;

				for (int j = 0; j < (int)iter; j++) {

					int temp_bidx = bidx + (j * gridDim.x);

					if (temp_bidx < inputStringLength - i) {
						int j = temp_bidx;

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
				}

				if (idx == 0 && idy == 0) {
					arrayIn[bidx] = i;
				}

				if (bidx == 1) {

					if (idx < gridDim.x && idy == 0) {
						while (arrayIn[idx] != i) {

						}
					}

					__syncthreads();

					if (idx < gridDim.x && idy == 0) {
						arrayOut[idx] = i;
					}

				}

				//break; //only first line
				if (idx == 0 && idy == 0) {
					while (arrayOut[bidx] != i) {

					}
				}
				__syncthreads();

			}
		}

		// only thread 0 is used for synchronization


	} else if (action == 2) { //////////////////////////////////////////////////////////////// entry = block, block used are decremented, threads 2D + FAST BARIER SYNCHRONISATION

		if (threadIdx.x <= nonTermsCount && threadIdx.y <= nonTermsCount) {

			for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

														  //for (int j = 0; j < inputStringLength - i; j++) { // every word of given length 5, 4, 3, 2, 1... (2)

				float iter = ceilf((float)(inputStringLength - i) / (float)gridDim.x);
				//iter = 2.0f;

				for (int r = 0; r < (int)iter; r++) {

					int temp_bidx = bidx + (r * gridDim.x);

					if (temp_bidx < inputStringLength - i) {
						int j = temp_bidx;

						int idz = threadIdx.z;

						float iter2 = ceilf((float)(i) / (float)blockDim.z);

						for (int s = 0; s < (int)iter2; s++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

							int temp_idz = idz + (s * blockDim.z);

							if (temp_idz < i) {

								int k = temp_idz;

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

						} //end s loop
					}

					}
				}

				//break; //only first line
				if (idx == 0 && idy == 0) {
					//printf("%d | ", g_mutex);
					atomicAdd((int *)&g_mutex, 1);
					//only when all blocks add 1 to g_mutex
					//will g_mutex equal to goalVal
					while (g_mutex != (gridDim.x * i)) {
						//Do nothing here
					}

				}
				__syncthreads();

			}
		}

	 } else if (action == 3) { //////////////////////////////////////////////////////////////// entry = block, block used are decremented, threads 2D + FAST BARIER SYNCHRONISATION

		if (threadIdx.x <= nonTermsCount) {

			for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

														  //for (int j = 0; j < inputStringLength - i; j++) { // every word of given length 5, 4, 3, 2, 1... (2)

				float iter = ceilf((float)(inputStringLength - i) / (float)gridDim.x);
				//iter = 2.0f;

				for (int r = 0; r < (int)iter; r++) {

					int temp_bidx = bidx + (r * gridDim.x);

					if (temp_bidx < inputStringLength - i) {
						int j = temp_bidx;

						int idy = threadIdx.y;

						float iter2 = ceilf((float)(i) / (float)blockDim.y);

						for (int s = 0; s < (int)iter2; s++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

							int temp_idy = idy + (s * blockDim.y);

							if (temp_idy < i) {

								int k = temp_idy;

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

							} //end s loop
						}

					}
				}

				//break; //only first line
				if (idx == 0 && idy == 0) {
					//printf("%d | ", g_mutex);
					atomicAdd((int *)&g_mutex, 1);
					//only when all blocks add 1 to g_mutex
					//will g_mutex equal to goalVal
					while (g_mutex != (gridDim.x * i)) {
						//Do nothing here
					}

				}
				__syncthreads();

			}
		}

	}
	 else if (action == 4) { //////////////////////////////////////////////////////////////// entry = block, block used are decremented, threads 2D + FAST BARIER SYNCHRONISATION

		 if (threadIdx.x < nonTermsCount) {

			 for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

														   //for (int j = 0; j < inputStringLength - i; j++) { // every word of given length 5, 4, 3, 2, 1... (2)

				 float iter = ceilf((float)(inputStringLength - i) / (float)gridDim.x);
				 //iter = 2.0f;

				 for (int r = 0; r < (int)iter; r++) {

					 int temp_bidx = bidx + (r * gridDim.x);

					 if (temp_bidx < inputStringLength - i) {
						 int j = temp_bidx * cellWidth;

						 int idy = threadIdx.y;

						 float iter2 = ceilf((float)(i) / (float)blockDim.y);

						 for (int s = 0; s < (int)iter2; s++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

							 int temp_idy = idy + (s * blockDim.y);

							 if (temp_idy < i) {

								 int k = temp_idy;

								 //TODO correct split points!
								 int first = cykArray[k][j];
								 int second = cykArray[i - k - 1][j + k + 1];

								 //decode nonterminals (find out if bits are on a given positions)
								 int base = 1;
								 //for (int l = 0; l < nonTermsCount; l++) {
								 //int l = idx;
								 //int bitMaskFirst = base << l;
								 ////all possibilities connected with rules

								 //for (int m = 0; m < nonTermsCount; m++) {
									// int bitMaskSecond = base << m;

									// // if rule with 'l' index and 'm' index is created and ready to be found if corrrect X ->lm (does X exist in a grammar?)
									// if (first & bitMaskFirst && second & bitMaskSecond) {
									//	 //cout << bitMaskFirst << ", " << bitMaskSecond << " | ";

									//	 //rule exists
									//	 if (rulesNonTermsArray[l][m] != -1) {
									//		 int shiftValue = rulesNonTermsArray[l][m];
									//		 int bitValue = base << shiftValue;

									//		 //TODO - tutaj może być problem
									//		 atomicOr(&cykArray[i][j], bitValue);

									//		 //cykArray[i][j] |= bitValue;
									//	 }

									// }


								 //}
								 

								 float iterM = ceilf((float)(nonTermsCount) / (float)blockDim.x);
								 for (int md = 0; md < (int)iterM; md++) {

									 int temp_idx = idy + (md * blockDim.x); 

									 if (temp_idx < nonTermsCount) {

										 int m = temp_idx;

										 int offset = (int)(m / 32);
										 int first = cykArray[k][j + offset];
										 int bitMaskFirst = (base << (m - (offset * 32)));

										 //if (first & bitMaskFirst) {
										 if (first & bitMaskFirst) {

											 for (int n = 0; n < nonTermsCount; n++) {

												 int offset2 = (int)(n / 32); // shift by 32 is the next cell
												 int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];
												 int bitMaskSecond = (base << (n - (offset2 * 32)));

												 if (second & bitMaskSecond) {

													 //rule exists
													 if (rulesNonTermsArray[m][n] != -1) {

														 int shiftValue = rulesNonTermsArray[m][n];
														 //int bitValue = base << shiftValue;

														 int offset = (int)(shiftValue / 32); // shift by 32 is the next cell
														 int base = 1;
														 int bitValue = base << (shiftValue - (offset * 32));

														 cykArray[i][j + offset] |= bitValue;
													 }

												 }

											 } // end n loop
										 }
									 }

									 

								 } // end m loop

							 } //end s loop
						 }

					 }
				 }

				 //break; //only first line
				 if (idx == 0 && idy == 0) {
					 //printf("%d | ", g_mutex);
					 atomicAdd((int *)&g_mutex, 1);
					 //only when all blocks add 1 to g_mutex
					 //will g_mutex equal to goalVal
					 while (g_mutex != (gridDim.x * i)) {
						 //Do nothing here
					 }

				 }
				 __syncthreads();

			 }
		 }

		 //start
		 int base = 1;
		 for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

			 float iterJ = ceilf((float)(inputStringLength - i) / (float)blockDim.x);
			 for (int jd = 0; jd < (int)iterJ; jd++) { // every word <of given length: 5 words, 4 words, 3 words, 2, 1...> (2)
													   ////TODO!!!!
				 int temp_idx = idx + (jd * blockDim.x);

				 float iterK = ceilf((float)(i) / (float)blockDim.y);
				 for (int kd = 0; kd < (int)iterK; kd++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

					 int temp_idy = idy + (kd * blockDim.y);

					 if (temp_idx < inputStringLength - i && temp_idy < i) {

						 //printf("%d - %d \n", temp_idx, temp_idy);

						 int j = temp_idx * cellWidth;
						 int k = temp_idy;


						 for (int m = 0; m < nonTermsCount; m++) {

							 int offset = (int)(m / 32);
							 int first = cykArray[k][j + offset];
							 int bitMaskFirst = (base << (m - (offset * 32)));

							 //if (first & bitMaskFirst) {
							 if (first & bitMaskFirst) {

								 for (int n = 0; n < nonTermsCount; n++) {

									 int offset2 = (int)(n / 32); // shift by 32 is the next cell
									 int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];
									 int bitMaskSecond = (base << (n - (offset2 * 32)));

									 if (second & bitMaskSecond) {

										 //rule exists
										 if (rulesNonTermsArray[m][n] != -1) {

											 int shiftValue = rulesNonTermsArray[m][n];
											 //int bitValue = base << shiftValue;

											 int offset = (int)(shiftValue / 32); // shift by 32 is the next cell
											 int base = 1;
											 int bitValue = base << (shiftValue - (offset * 32));

											 cykArray[i][j + offset] |= bitValue;
										 }

									 }

								 } // end n loop
							 }

						 } // end m loop

					 }

				 } // end k loop

			 } // end j loop

			 __syncthreads();

		 } // end i loop
		 //end

	 } else if (action == 5) { //////////////////////////////////////////////////////////////// entry = block, block used are decremented, threads 2D

				 int base = 1;

				 int i = additionalVariable;

					 float iterJ = ceilf((float)(inputStringLength - i) / (float)blockDim.x);
					 for (int jd = 0; jd < (int)iterJ; jd++) { // every word <of given length: 5 words, 4 words, 3 words, 2, 1...> (2)
															   ////TODO!!!!
						 int temp_idx = idx + (jd * blockDim.x);

						 float iterK = ceilf((float)(i) / (float)blockDim.y);
						 for (int kd = 0; kd < (int)iterK; kd++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

							 int temp_idy = idy + (kd * blockDim.y);

							 if (temp_idx < inputStringLength - i && temp_idy < i) {

								 //printf("%d - %d \n", temp_idx, temp_idy);

								 int j = temp_idx * cellWidth;
								 int k = temp_idy;

								 for (int m = 0; m < nonTermsCount; m++) {

									 int offset = (int)(m / 32);
									 int first = cykArray[k][j + offset];
									 int bitMaskFirst = (base << (m - (offset * 32)));

									 //if (first & bitMaskFirst) {
									 if (first & bitMaskFirst) {

										 for (int n = 0; n < nonTermsCount; n++) {

											 int offset2 = (int)(n / 32); // shift by 32 is the next cell
											 int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];
											 int bitMaskSecond = (base << (n - (offset2 * 32)));

											 if (second & bitMaskSecond) {

												 //rule exists
												 if (rulesNonTermsArray[m][n] != -1) {

													 int shiftValue = rulesNonTermsArray[m][n];
													 //int bitValue = base << shiftValue;

													 int offset = (int)(shiftValue / 32); // shift by 32 is the next cell
													 int base = 1;
													 int bitValue = base << (shiftValue - (offset * 32));

													 //cykArray[i][j + offset] |= bitValue;

													 atomicOr(&cykArray[i][j + offset], bitValue);
												 }

											 }

										 } // end n loop
									 }

								 } // end m loop

							 }

						 } // end k loop

					 } // end j loop

	 }
	 else if (action == 6) { //////////////////////////////////////////////////////////////// entry = block, block used are decremented, threads 2D

		 int base = 1;

		 int i = additionalVariable;

		 float iterJ = ceilf((float)(inputStringLength - i) / (float)gridDim.x);
		 for (int jd = 0; jd < (int)iterJ; jd++) { // every word <of given length: 5 words, 4 words, 3 words, 2, 1...> (2)
												   ////TODO!!!!
			 int temp_bidx = bidx + (jd * gridDim.x);

			 float iterK = ceilf((float)(i) / (float)blockDim.x);
			 for (int kd = 0; kd < (int)iterK; kd++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

				 int temp_idx = idx + (kd * blockDim.x);

				 if (temp_bidx < inputStringLength - i && temp_idx < i) {

					 //printf("%d - %d \n", temp_idx, temp_idy);

					 int j = temp_bidx * cellWidth;
					 int k = temp_idx;

					 for (int m = 0; m < nonTermsCount; m++) {

						 int offset = (int)(m / 32);
						 int first = cykArray[k][j + offset];
						 int bitMaskFirst = (base << (m - (offset * 32)));

						 //if (first & bitMaskFirst) {
						 if (first & bitMaskFirst) {

							 for (int n = 0; n < nonTermsCount; n++) {

								 int offset2 = (int)(n / 32); // shift by 32 is the next cell
								 int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];
								 int bitMaskSecond = (base << (n - (offset2 * 32)));

								 if (second & bitMaskSecond) {

									 //rule exists
									 if (rulesNonTermsArray[m][n] != -1) {

										 int shiftValue = rulesNonTermsArray[m][n];
										 //int bitValue = base << shiftValue;

										 int offset = (int)(shiftValue / 32); // shift by 32 is the next cell
										 int base = 1;
										 int bitValue = base << (shiftValue - (offset * 32));

										 //cykArray[i][j + offset] |= bitValue;

										 atomicOr(&cykArray[i][j + offset], bitValue);
									 }

								 }

							 } // end n loop
						 }

					 } // end m loop

				 }

			 } // end k loop

		 } // end j loop

	 }
	 else if (action == 7) { //////////////////////////////////////////////////////////////// entry = block, block used are decremented, threads 2D

		 int base = 1;

		 int i = additionalVariable;

		 float iterJ = ceilf((float)(inputStringLength - i) / (float)gridDim.x);
		 for (int jd = 0; jd < (int)iterJ; jd++) { // every word <of given length: 5 words, 4 words, 3 words, 2, 1...> (2)
												   ////TODO!!!!
			 int temp_bidx = bidx + (jd * gridDim.x);

			 float iterK = ceilf((float)(i) / (float)blockDim.x);
			 for (int kd = 0; kd < (int)iterK; kd++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

				 int temp_idx = idx + (kd * blockDim.x);

				 if (temp_bidx < inputStringLength - i && temp_idx < i) {

					 //printf("%d - %d \n", temp_idx, temp_idy);

					 int j = temp_bidx * cellWidth;
					 int k = temp_idx;


					 float iterM = ceilf((float)(nonTermsCount) / (float)blockDim.y);
					 for (int km = 0; km < (int)iterM; km++) {

						 int temp_idy = idy + (km * blockDim.y);

						 if (temp_idy < nonTermsCount) {

							 int m = temp_idy;


							 int offset = (int)(m / 32);
							 int first = cykArray[k][j + offset];
							 int bitMaskFirst = (base << (m - (offset * 32)));

							 //if (first & bitMaskFirst) {
							 if (first & bitMaskFirst) {

								 for (int n = 0; n < nonTermsCount; n++) {

									 int offset2 = (int)(n / 32); // shift by 32 is the next cell
									 int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];
									 int bitMaskSecond = (base << (n - (offset2 * 32)));

									 if (second & bitMaskSecond) {

										 //rule exists
										 if (rulesNonTermsArray[m][n] != -1) {

											 int shiftValue = rulesNonTermsArray[m][n];
											 //int bitValue = base << shiftValue;

											 int offset = (int)(shiftValue / 32); // shift by 32 is the next cell
											 int base = 1;
											 int bitValue = base << (shiftValue - (offset * 32));

											 //cykArray[i][j + offset] |= bitValue;

											 atomicOr(&cykArray[i][j + offset], bitValue);
										 }

									 }

								 } // end n loop
							 }

						 } // end m loop
					 }

				 }

			 } // end k loop

		 } // end j loop

	 }
	 else if (action == 8) { //////////////////////////////////////////////////////////////// entry = block, block used are decremented, threads 2D

		 int base = 1;

		 int i = additionalVariable;

		 float iterJ = ceilf((float)(inputStringLength - i) / (float)gridDim.x);
		 for (int jd = 0; jd < (int)iterJ; jd++) { // every word <of given length: 5 words, 4 words, 3 words, 2, 1...> (2)
												   ////TODO!!!!
			 int temp_bidx = bidx + (jd * gridDim.x);

			 float iterK = ceilf((float)(i) / (float)gridDim.y);
			 for (int kd = 0; kd < (int)iterK; kd++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

				 int temp_bidy = bidy + (kd * gridDim.y);

				 if (temp_bidx < inputStringLength - i && temp_bidy < i) {

					 //printf("%d - %d \n", temp_idx, temp_idy);

					 int j = temp_bidx * cellWidth;
					 int k = temp_bidy;


					 float iterM = ceilf((float)(nonTermsCount) / (float)blockDim.x);
					 for (int km = 0; km < (int)iterM; km++) {

						 int temp_idx = idx + (km * blockDim.x);

						 if (temp_idx < nonTermsCount) {

							 int m = temp_idx;


							 int offset = (int)(m / 32);
							 int first = cykArray[k][j + offset];
							 int bitMaskFirst = (base << (m - (offset * 32)));

							 //if (first & bitMaskFirst) {
							 if (first & bitMaskFirst) {

								 for (int n = 0; n < nonTermsCount; n++) {

									 int offset2 = (int)(n / 32); // shift by 32 is the next cell
									 int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];
									 int bitMaskSecond = (base << (n - (offset2 * 32)));

									 if (second & bitMaskSecond) {

										 //rule exists
										 if (rulesNonTermsArray[m][n] != -1) {

											 int shiftValue = rulesNonTermsArray[m][n];
											 //int bitValue = base << shiftValue;

											 int offset = (int)(shiftValue / 32); // shift by 32 is the next cell
											 int base = 1;
											 int bitValue = base << (shiftValue - (offset * 32));

											 //cykArray[i][j + offset] |= bitValue;

											 atomicOr(&cykArray[i][j + offset], bitValue);
										 }

									 }

								 } // end n loop
							 }

						 } // end m loop
					 }

				 }

			 } // end k loop

		 } // end j loop

	 }
	 else if (action == 9) { //////////////////////////////////////////////////////////////// entry = block, block used are decremented, threads 2D

		 int base = 1;

		 int i = additionalVariable;

		 float iterJ = ceilf((float)(inputStringLength - i) / (float)gridDim.x);
		 for (int jd = 0; jd < (int)iterJ; jd++) { // every word <of given length: 5 words, 4 words, 3 words, 2, 1...> (2)
												   ////TODO!!!!
			 int temp_bidx = bidx + (jd * gridDim.x);

			 float iterK = ceilf((float)(i) / (float)gridDim.y);
			 for (int kd = 0; kd < (int)iterK; kd++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

				 int temp_bidy = bidy + (kd * gridDim.y);

				 if (temp_bidx < inputStringLength - i && temp_bidy < i) {

					 //printf("%d - %d \n", temp_idx, temp_idy);

					 int j = temp_bidx * cellWidth;
					 int k = temp_bidy;


					 float iterM = ceilf((float)(nonTermsCount) / (float)blockDim.x);
					 for (int km = 0; km < (int)iterM; km++) {

						 int temp_idx = idx + (km * blockDim.x);

						 if (temp_idx < nonTermsCount) {

							 int m = temp_idx;


							 int offset = (int)(m / 32);
							 int first = cykArray[k][j + offset];
							 int bitMaskFirst = (base << (m - (offset * 32)));

							 //if (first & bitMaskFirst) {
							 if (first & bitMaskFirst) {


								 float iterN = ceilf((float)(nonTermsCount) / (float)blockDim.y);
								 for (int nd = 0; nd < nonTermsCount; nd++) {

									 int temp_idy = idy + (nd * blockDim.y);

									 if (temp_idy < nonTermsCount) {

										 int n = temp_idy;

										 int offset2 = (int)(n / 32); // shift by 32 is the next cell
										 int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];
										 int bitMaskSecond = (base << (n - (offset2 * 32)));

										 if (second & bitMaskSecond) {

											 //rule exists
											 if (rulesNonTermsArray[m][n] != -1) {

												 int shiftValue = rulesNonTermsArray[m][n];
												 //int bitValue = base << shiftValue;

												 int offset = (int)(shiftValue / 32); // shift by 32 is the next cell
												 int base = 1;
												 int bitValue = base << (shiftValue - (offset * 32));

												 //cykArray[i][j + offset] |= bitValue;

												 atomicOr(&cykArray[i][j + offset], bitValue);
											 }

										 }

									 } // end n loop
								 }
							 }

						 } // end m loop
					 }

				 }

			 } // end k loop

		 } // end j loop

	 }

	

	__syncthreads();

	if (threadIdx.x == 0 && threadIdx.y == 0 && bidx == 0) {
		
		//for (int i = 0; i < nonTermsCount; i++) {
		//	for (int j = 0; j < nonTermsCount; j++) {
		//		//cout << rulesNonTermsArray[i][j] << " | ";

		//		printf("%d | ", rulesNonTermsArray[i][j]);
		//	}
		//	//cout << endl;

		//	printf("\n");
		//}

		//for (int j = 1; j < inputStringLength; j++) {
		//	for (int i = 0; i < inputStringLength - j; i++) {
		//		printf("%d | ", cykArray[j][i]);
		//	}
		//	printf("\n");
		//}

		//int* result = data.getResult();
		//printf("RESUUUULt: %d | ", result[0]);
		//result[0] = 1337;
		int* result = data.getResult();
		//printf("RESUUUULt: %d | ", result[0]);
		result[0] = cykArray[inputStringLength - 1][0];
	}

	__syncthreads();

	return;
}



template<int action>
__global__ void cykAlgorithmRules(DeviceCYKData data, curandState * randGlobal, volatile int * arrayIn, volatile int * arrayOut, int** rulesArray, int rulesCount, int additionalVariable)
{
	__shared__ int** cykArray;
	__shared__ int inputStringLength;
	__shared__ int** rulesNonTermsArray;
	__shared__ int nonTermsCount;
	__shared__ int cellWidth;

	int bidx = blockIdx.x;
	int bidy = blockIdx.y;
	int bidz = blockIdx.z;
	int idx = threadIdx.x;
	int idy = threadIdx.y;
	int idz = threadIdx.z;

	if (threadIdx.x == 0 && threadIdx.y == 0) {
		g_mutex = 0;
		cykArray = data.getCYKArray();
		inputStringLength = data.getInputCount();
		rulesNonTermsArray = data.getRulesNonTermsArray();
		nonTermsCount = data.getNonTermsCount();
		//printf("Dim %d\n", gridDim.x);
		cellWidth = (int)(ceilf(((float)nonTermsCount / 32.0f)));
	}


	__syncthreads();

	if (action == 0) { //////////////////////////////////////////////////////////////// only threads

		if (threadIdx.x <= nonTermsCount && threadIdx.y <= nonTermsCount) {

			for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

														
				float iter = ceilf((float)(inputStringLength - i) / (float)gridDim.x);
				//iter = 2.0f;

				for (int r = 0; r < (int)iter; r++) {

					int temp_bidx = bidx + (r * gridDim.x);

					if (temp_bidx < inputStringLength - i) {
						int j = temp_bidx; //J

						//for (int p = 0; p < rulesCount; p++) { //for each production (each rule)
						if (idx < rulesCount) {

							int p = idx;

							for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

														  //TODO correct split points!
								int first = cykArray[k][j];
								int second = cykArray[i - k - 1][j + k + 1];

								//decode nonterminals (find out if bits are on a given positions)
								int base = 1;
								int bitMaskFirst = base << rulesArray[0][p];
								int bitMaskSecond = base << rulesArray[1][p];
								if (first & bitMaskFirst && second & bitMaskSecond) {

									int shiftValue = rulesArray[2][p];
									int bitValue = base << shiftValue;
									//TODO - tutaj może być problem
									atomicOr(&cykArray[i][j], bitValue);
								}

							}
						}

					}
				}

				//break; //only first line
				if (idx == 0 && idy == 0) {
					//printf("%d | ", g_mutex);
					atomicAdd((int *)&g_mutex, 1);
					//only when all blocks add 1 to g_mutex
					//will g_mutex equal to goalVal
					while (g_mutex != (gridDim.x * i)) {
						//Do nothing here
					}

				}
				__syncthreads();

			}
		}

		// only thread 0 is used for synchronization


	} if (action == 2) { //////////////////////////////////////////////////////////////// only threads


			int i = additionalVariable;

			//float iter = ceilf((float)(inputStringLength - i) / (float)gridDim.x);
			////iter = 2.0f;

			////for (int r = 0; r < (int)iter; r++) {


			//int temp_bidx = bidx;// +(r * gridDim.x);

			//if (temp_bidx < inputStringLength - i) {
			//	int j = temp_bidx; //J
			float iterJ = ceilf((float)(inputStringLength - i) / (float)gridDim.x);

			for (int jd = 0; jd < (int)iterJ; jd++) {
				
				int temp_bidx = bidx + (jd * gridDim.x);

				if (temp_bidx < inputStringLength - i) {

					int j = temp_bidx * cellWidth;

					float iterP = ceilf((float)(rulesCount) / (float)blockDim.x);

					for (int pd = 0; pd < (int)iterP; pd++) {

						int temp_idx = idx + (pd * blockDim.x);
						
						if (temp_idx < rulesCount) { //TODO wtf?

							int p = temp_idx;

							for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

														  //TODO correct split points!
								//int first = cykArray[k][j];
								//int second = cykArray[i - k - 1][j + k + 1];

								////decode nonterminals (find out if bits are on a given positions)
								//int base = 1;
								int rule1 = rulesArray[0][p];
								int rule2 = rulesArray[1][p];

								int offset = (int)(rule1 / 32);
								int first = cykArray[k][j + offset];

								int offset2 = (int)(rule2 / 32);
								int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];

								int base = 1;

								/*int bitMaskFirst = base << rulesArray[0][p];
								int bitMaskSecond = base << rulesArray[1][p];*/
								

								int bitMaskFirst = (base << (rule1 - (offset * 32)));
								int bitMaskSecond = (base << (rule2 - (offset2 * 32)));


								if (first & bitMaskFirst && second & bitMaskSecond) {

									//int shiftValue = rulesArray[2][p];
									//int bitValue = base << shiftValue;
									////TODO - tutaj może być problem
									//atomicOr(&cykArray[i][j], bitValue);

									int shiftValue = rulesArray[2][p];
									int offset = (int)(shiftValue / 32);
									int bitValue = base << (shiftValue - (offset * 32));

									atomicOr(&cykArray[i][j + offset], bitValue);
								}

							}
						}
					}

				}
			}

			__syncthreads();


	} else if (action == 1) { //////////////////////////////////////////////////////////////// blocks + threads

		int i = additionalVariable;

		float iterJ = ceilf((float)(inputStringLength - i) / (float)gridDim.x);

		for (int jd = 0; jd < (int)iterJ; jd++) {

			int temp_bidx = bidx + (jd * gridDim.x);

			if (temp_bidx < inputStringLength - i) {

				int j = temp_bidx * cellWidth;

				float iterP = ceilf((float)(rulesCount) / (float)blockDim.x);

				for (int pd = 0; pd < (int)iterP; pd++) {

					int temp_idx = idx + (pd * blockDim.x);

					if (temp_idx < rulesCount) { //TODO wtf?

						int p = temp_idx;

						float iterk = ceilf((float)(i) / (float)gridDim.y);

						for (int kd = 0; kd < (int)iterk; kd++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

							int temp_bidy = bidy + (kd * gridDim.y);

							if (temp_bidy < i) {

								int k = temp_bidy;

								int rule1 = rulesArray[0][p];
								int rule2 = rulesArray[1][p];

								int offset = (int)(rule1 / 32);
								int first = cykArray[k][j + offset];

								int offset2 = (int)(rule2 / 32);
								int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];

								int base = 1;

								int bitMaskFirst = (base << (rule1 - (offset * 32)));
								int bitMaskSecond = (base << (rule2 - (offset2 * 32)));


								if (first & bitMaskFirst && second & bitMaskSecond) {

									int shiftValue = rulesArray[2][p];
									int offset = (int)(shiftValue / 32);
									int bitValue = base << (shiftValue - (offset * 32));

									atomicOr(&cykArray[i][j + offset], bitValue);
								}
							}
						}
					}
				}

			}
		}

		__syncthreads();

	} else if (action == 3) { //////////////////////////////////////////////////////////////// blocks + threads

							// bidx - i loop, bidy - each left symbol, idx - left symbol connected rules
							// block dim y - number of unique left symbols

		int numberOfProductions = rulesArray[bidy][1];

		int i =  additionalVariable;

			float iterJ = ceilf((float)(inputStringLength - i) / (float)gridDim.x);

			for (int jd = 0; jd < (int)iterJ; jd++) {

				int temp_bidx = bidx + (jd * gridDim.x);

				if (temp_bidx < inputStringLength - i) {

					int j = temp_bidx * cellWidth;

					//for (int p = 0; p < rulesCount; p++) { //for each production (each rule)

					float iterP = ceilf((float)(numberOfProductions) / (float)(blockDim.x));

						for (int pd = 0; pd < (int)iterP; pd++) {

							int temp_idx = idx + (pd * blockDim.x);

							if (temp_idx < numberOfProductions) {

								int p = temp_idx;

								for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

									int rule1 = rulesArray[blockIdx.y][(p + 1) * 2];
									int rule2 = rulesArray[blockIdx.y][(p + 1) * 2 + 1];

									int offset = (int)(rule1 / 32);
									int first = cykArray[k][j + offset];

									int offset2 = (int)(rule2 / 32);
									int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];

									//decode nonterminals (find out if bits are on a given positions)
									int base = 1;
									int bitMaskFirst = (base << (rule1 - (offset * 32)));
									int bitMaskSecond = (base << (rule2 - (offset2 * 32)));

									if (first & bitMaskFirst && second & bitMaskSecond) {

										int shiftValue = rulesArray[blockIdx.y][0];
										int offset = (int)(shiftValue / 32);
										int bitValue = base << (shiftValue - (offset * 32));

										atomicOr(&cykArray[i][j + offset], bitValue);

									}

								}
							} //pd if

						} // pd loop

				} //jd if 

			} // jd loop

			__syncthreads();


	} else if (action == 4) { //////////////////////////////////////////////////////////////// blocks + threads

							// bidx - i loop, bidy - each left symbol, idx - left symbol connected rules
							// block dim y - number of unique left symbols

		int numberOfProductions = rulesArray[bidy][1];

		int i = additionalVariable;

		float iterJ = ceilf((float)(inputStringLength - i) / (float)gridDim.x);

		for (int jd = 0; jd < (int)iterJ; jd++) {

			int temp_bidx = bidx + (jd * gridDim.x);

			if (temp_bidx < inputStringLength - i) {

				int j = temp_bidx * cellWidth;

				//for (int p = 0; p < rulesCount; p++) { //for each production (each rule)

				float iterP = ceilf((float)(numberOfProductions) / (float)(blockDim.x));

				for (int pd = 0; pd < (int)iterP; pd++) {

					int temp_idx = idx + (pd * blockDim.x);

					if (temp_idx < numberOfProductions) {

						int p = temp_idx;

						float iterK = ceilf((float)(i) / (float)(blockDim.y));

						//for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)
						for (int kd = 0; kd < (int)iterK; kd++) {

							int temp_idy = idy + (kd * blockDim.y);
							
							if (temp_idy < i) {

								int k = temp_idy;

								int rule1 = rulesArray[blockIdx.y][(p + 1) * 2];
								int rule2 = rulesArray[blockIdx.y][(p + 1) * 2 + 1];

								int offset = (int)(rule1 / 32);
								int first = cykArray[k][j + offset];

								int offset2 = (int)(rule2 / 32);
								int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];

								//decode nonterminals (find out if bits are on a given positions)
								int base = 1;
								int bitMaskFirst = (base << (rule1 - (offset * 32)));
								int bitMaskSecond = (base << (rule2 - (offset2 * 32)));

								if (first & bitMaskFirst && second & bitMaskSecond) {

									int shiftValue = rulesArray[blockIdx.y][0];
									int offset = (int)(shiftValue / 32);
									int bitValue = base << (shiftValue - (offset * 32));

									atomicOr(&cykArray[i][j + offset], bitValue);

								}
							} //kd if

						} // kd loop

					} //pd if

				} // pd loop

			} //jd if 

		} // jd loop

		__syncthreads();


	} else if (action == 5) { //////////////////////////////////////////////////////////////// blocks + threads

							// bidx - i loop, bidy - each left symbol, idx - left symbol connected rules
							// block dim y - number of unique left symbols

		int numberOfProductions = rulesArray[bidy][1];

		int i = additionalVariable;

		float iterJ = ceilf((float)(inputStringLength - i) / (float)gridDim.x);

		for (int jd = 0; jd < (int)iterJ; jd++) {

			int temp_bidx = bidx + (jd * gridDim.x);

			if (temp_bidx < inputStringLength - i) {

				int j = temp_bidx * cellWidth;

				//for (int p = 0; p < rulesCount; p++) { //for each production (each rule)

				float iterP = ceilf((float)(numberOfProductions) / (float)(blockDim.x));

				for (int pd = 0; pd < (int)iterP; pd++) {

					int temp_idx = idx + (pd * blockDim.x);

					if (temp_idx < numberOfProductions) {

						int p = temp_idx;

						float iterK = ceilf((float)(i) / (float)(gridDim.z));

						//for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)
						for (int kd = 0; kd < (int)iterK; kd++) {

							int temp_idy = bidz + (kd * gridDim.z);

							if (temp_idy < i) {

								int k = temp_idy;

								int rule1 = rulesArray[blockIdx.y][(p + 1) * 2];
								int rule2 = rulesArray[blockIdx.y][(p + 1) * 2 + 1];

								int offset = (int)(rule1 / 32);
								int first = cykArray[k][j + offset];

								int offset2 = (int)(rule2 / 32);
								int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];

								//decode nonterminals (find out if bits are on a given positions)
								int base = 1;
								int bitMaskFirst = (base << (rule1 - (offset * 32)));
								int bitMaskSecond = (base << (rule2 - (offset2 * 32)));

								if (first & bitMaskFirst && second & bitMaskSecond) {

									int shiftValue = rulesArray[blockIdx.y][0];
									int offset = (int)(shiftValue / 32);
									int bitValue = base << (shiftValue - (offset * 32));

									atomicOr(&cykArray[i][j + offset], bitValue);

								}
							} //kd if

						} // kd loop

					} //pd if

				} // pd loop

			} //jd if 

		} // jd loop

		__syncthreads();


	}
	else if (action == 6) { //////////////////////////////////////////////////////////////// blocks + threads

		int i = additionalVariable;

		float iterJ = ceilf((float)(inputStringLength - i) / (float)gridDim.x);

		for (int jd = 0; jd < (int)iterJ; jd++) {

			int temp_bidx = bidx + (jd * gridDim.x);

			if (temp_bidx < inputStringLength - i) {

				int j = temp_bidx * cellWidth;

				float iterP = ceilf((float)(rulesCount) / (float)blockDim.x);

				for (int pd = 0; pd < (int)iterP; pd++) {

					int temp_idx = idx + (pd * blockDim.x);

					if (temp_idx < rulesCount) { //TODO wtf?

						int p = temp_idx;

						float iterk = ceilf((float)(i) / (float)blockDim.y);

						for (int kd = 0; kd < (int)iterk; kd++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

							int temp_idy = idy + (kd * blockDim.y);

							if (temp_idy < i) {

								int k = temp_idy;

								int rule1 = rulesArray[0][p];
								int rule2 = rulesArray[1][p];

								int offset = (int)(rule1 / 32);
								int first = cykArray[k][j + offset];

								int offset2 = (int)(rule2 / 32);
								int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];

								int base = 1;

								int bitMaskFirst = (base << (rule1 - (offset * 32)));
								int bitMaskSecond = (base << (rule2 - (offset2 * 32)));


								if (first & bitMaskFirst && second & bitMaskSecond) {

									int shiftValue = rulesArray[2][p];
									int offset = (int)(shiftValue / 32);
									int bitValue = base << (shiftValue - (offset * 32));

									atomicOr(&cykArray[i][j + offset], bitValue);
								}
							}
						}
					}
				}

			}
		}

		__syncthreads();

	}
	else if (action == 7) { //////////////////////////////////////////////////////////////// blocks + threads

		int i = additionalVariable;

		float iterJ = ceilf((float)(inputStringLength - i) / (float)gridDim.x);

		for (int jd = 0; jd < (int)iterJ; jd++) {

			int temp_bidx = bidx + (jd * gridDim.x);

			if (temp_bidx < inputStringLength - i) {

				int j = temp_bidx * cellWidth;

				float iterP = ceilf((float)(rulesCount) / (float)gridDim.y);

				for (int pd = 0; pd < (int)iterP; pd++) {

					int temp_bidy = bidy + (pd * gridDim.y);

					if (temp_bidy < rulesCount) { //TODO wtf?

						int p = temp_bidy;

						float iterk = ceilf((float)(i) / (float)blockDim.y);

						for (int kd = 0; kd < (int)iterk; kd++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

							int temp_idy = idy + (kd * blockDim.y);

							if (temp_idy < i) {

								int k = temp_idy;

								int rule1 = rulesArray[0][p];
								int rule2 = rulesArray[1][p];

								int offset = (int)(rule1 / 32);
								int first = cykArray[k][j + offset];

								int offset2 = (int)(rule2 / 32);
								int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];

								int base = 1;

								int bitMaskFirst = (base << (rule1 - (offset * 32)));
								int bitMaskSecond = (base << (rule2 - (offset2 * 32)));


								if (first & bitMaskFirst && second & bitMaskSecond) {

									int shiftValue = rulesArray[2][p];
									int offset = (int)(shiftValue / 32);
									int bitValue = base << (shiftValue - (offset * 32));

									atomicOr(&cykArray[i][j + offset], bitValue);
								}
							}
						}
					}
				}

			}
		}

		__syncthreads();

	}

	__syncthreads();
	//&& rulesCount == inputStringLength
	if (threadIdx.x == 0 && threadIdx.y == 0 && blockIdx.y == 0 && blockIdx.x == 0 ) {
		if (action != 2 || additionalVariable == inputStringLength -1) {
			//for (int i = 0; i < nonTermsCount; i++) {
			//	for (int j = 0; j < nonTermsCount; j++) {
			//		//cout << rulesNonTermsArray[i][j] << " | ";

			//		printf("%d | ", rulesNonTermsArray[i][j]);
			//	}
			//	//cout << endl;

			//	printf("\n");
			//}

			//for (int j = 1; j < inputStringLength; j++) {
			//	for (int i = 0; i < inputStringLength - j; i++) {
			//		for (int c = 0; c < cellWidth; c++) {
			//			//cout << cykArray[j][i + c] << " - ";

			//			printf("%d -  ", cykArray[j][i + c]);
			//		}
			//		printf(" | ");
			//	}
			//	printf("\n");
			//}

			//int* result = data.getResult();
			//printf("RESUUUULt: %d | ", result[0]);
			//result[0] = cykArray[j][i];

			int* result = data.getResult();
			//printf("RESUUUULt: %d | ", result[0]);
			result[0] = cykArray[inputStringLength - 1][0];

		}
		
	}

	__syncthreads();

	return;
}


