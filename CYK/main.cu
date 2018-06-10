#include "Utility.h"
#include "Ogolne.cuh"
#include "Ogolne.h"
#include "functions.cuh"
#include "Cultural.cuh"
#include "CYK.cuh"
#include <cooperative_groups.h>


int main(int argc, char** argv)
{
	printf("working\n\n\n");

	//printf("Grammar: %s\n", argv[1]);
	//printf("Input: %s\n", argv[2]);

	char* termsArray;
	int termsCount;
	char* nonTermsArray;
	int nonTermsCount;
	int* rulesTermsArray;
	int rulesTermsCount;
	int** rulesNonTermsArray;
	int rulesNonTermsCount;
	int** onlyRulesArray = NULL;
	int onlyRulesCount;

	char name[50] = "grammar.txt";

	int iterations = 3;
	//char* grammarFiles[5] = { "example1.bcfg", "g1_001.bcfg", "grammar5.txt", "grammar7.txt", "grammar7.txt" };
	char* grammarFiles[3] = { "grammar5.txt", "grammar7.txt", "grammar7.txt" };
	string inputStrings[3] = { "cababcabdcffabeedcababcabfffabeeecffabeeebdabfabebeb", "eeababkabdknteeababkabdtoc", "fdablsmteeababkabdtrfdablsmteeababkabdtrfdablsmabjrimabjrhmteeababkabdtreeababkabdhmabjreababhmabjreabab" };

	int cpuVersion = 0;


	for (int x = 0; x < iterations; x++) {

		string inputString = inputStrings[x];
		cout << "Grammar: " << grammarFiles[x] << endl << "Input string: " << inputString << endl;
		
		//readGrammar(argv[1], termsArray, termsCount, nonTermsArray, nonTermsCount, rulesTermsArray, rulesTermsCount, rulesNonTermsArray, rulesNonTermsCount, onlyRulesArray, onlyRulesCount);
		readGrammar(grammarFiles[x], termsArray, termsCount, nonTermsArray, nonTermsCount, rulesTermsArray, rulesTermsCount, rulesNonTermsArray, rulesNonTermsCount, onlyRulesArray, onlyRulesCount);
		
		// WSJ one
		/*readGrammarExtended(grammarFiles[0], termsArray, termsCount, nonTermsArray, nonTermsCount, rulesTermsArray, rulesTermsCount, rulesNonTermsArray, rulesNonTermsCount, onlyRulesArray, onlyRulesCount);
		for (int i = 0; i < nonTermsCount; i++) {
		for (int j = 0; j < nonTermsCount; j++) {
		cout << rulesNonTermsArray[i][j] << " | ";
		}
		cout << endl;
		}

		for (int i = 0; i < termsCount; i++) {
		cout << termsArray[i] << " | ";
		}
		cout << endl;

		for (int i = 0; i < termsCount; i++) {

		cout << rulesTermsArray[i] << " | ";
		}
		cout << endl;

		for (int i = 0; i < nonTermsCount; i++) {

		cout << nonTermsArray[i] << " | ";
		}
		cout << endl;


		getchar();*/
		

		/*ALGORITHM START*/

		// 1. First part

		// create CYK array of input string length

		int inputStringLength = inputString.length();

		int cellWidth = ceil(((float)nonTermsCount / 32.0f));
		//cellWidth = 1;

		int** cykArray = new int*[inputStringLength];
		for (int i = 0; i < inputStringLength; i++) {
			cykArray[i] = new int[inputStringLength * cellWidth]; // columns multiplied
		}
		// make array clear
		for (int i = 0; i < inputStringLength; i++) {
			for (int j = 0; j < inputStringLength * cellWidth; j++) {
				cykArray[i][j] = 0;
			}
		}

		// first phase, terminal rules array, for every input string character
		for (int i = 0; i < inputStringLength * cellWidth; i += cellWidth) {

			// find character (terminal index)
			int terminalIndex = -1;
			for (int j = 0; j < termsCount; j++) {
				if (inputString[i / cellWidth] == termsArray[j]) {
					terminalIndex = j;
					break;
				}
			}

			// TODO find out, if there is a possibility that one term is connected with many nonterms
			//for (int j = 0; j < rulesTermsCount; j++) {
			/*if (terminalIndex == rulesTermsArray[terminalIndex]) {
			cykArray[0][i] = j;
			}*/



			if (rulesTermsArray[terminalIndex] >= 0) {
				int shiftValue = rulesTermsArray[terminalIndex];

				int offset = (int)(shiftValue / 32); // shift by 32 is the next cell

				int base = 1;
				int bitValue = base << (shiftValue - (offset * 32));

				cykArray[0][i + offset] |= bitValue;
			}
		}

		// printing arrays and first row result - PRINTING PART

		// print rules 2D array
		/*for (int i = 0; i < nonTermsCount; i++) {
		for (int j = 0; j < nonTermsCount; j++) {
		cout << rulesNonTermsArray[i][j] << " | ";
		}
		cout << endl;
		}

		for (int i = 0; i < termsCount; i++) {
			cout << termsArray[i] << " | ";
		}
		cout << endl;

		for (int i = 0; i < termsCount; i++) {

			cout << rulesTermsArray[i] << " | ";
		}
		cout << endl;

		for (int i = 0; i < nonTermsCount; i++) {

			cout << nonTermsArray[i] << " | ";
		}
		cout << endl;

		for (int i = 0; i < inputStringLength * cellWidth; i++) {

			cout << cykArray[0][i] << " | ";
		}
		cout << endl;*/


		// 2. Second part

		// code input string to number
		int* inputNumber = new int[inputStringLength];
		for (int i = 0; i < inputStringLength; i++) {

			for (int j = 0; j < termsCount; j++) {
				if (inputString[i] == termsArray[j]) {
					inputNumber[i] = j;
					break;
				}
			}
		}

		// print coded input string
		//for (int i = 0; i < inputStringLength; i++) {

		//	cout << inputNumber[i] << " | ";
		//}
		//cout << endl;

		LARGE_INTEGER frequency;        // ticks per second
		LARGE_INTEGER t1, t2;           // ticks
		double elapsedTime;

		// get ticks per second
		QueryPerformanceFrequency(&frequency);
		// start timer
		QueryPerformanceCounter(&t1);

		if (cpuVersion == 0) {
			for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

				for (int j = 0; j < (inputStringLength - i) * cellWidth; j += cellWidth) { // every word <of given length: 5 words, 4 words, 3 words, 2, 1...> (2)

					for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

						//decode nonterminals (find out if bits are on a given positions)
						int base = 1;
						for (int m = 0; m < nonTermsCount; m++) {

							int offset = (int)(m / 32);
							int first = cykArray[k][j + offset];
							int bitMaskFirst = (base << (m - (offset * 32)));

							if (first & bitMaskFirst) {

								//all possibilities connected with rules
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
											//cout << "ok - " << i << " _ " <<  j << " | " << m << " - " << n << " - " << offset  << " - " << shiftValue << " - bitFirst " << bitMaskFirst << " value1 " << first <<" - bitSeconf " << bitMaskSecond << " val2 " << second << " WTF _  " << ((j + k + 1) * cellWidth) + offset2 << "A standardowo: " << j + k + 1 << endl;

											int bitValue = base << (shiftValue - (offset * 32));

											cykArray[i][j + offset] |= bitValue;
										}

									}

								} // end n loop

							} //first condition

						} // end m loop

					} // end k loop

				} // end j loop

			} // end i loop
		} else if (cpuVersion == 1) {
			
			for (int i = 1; i < inputStringLength; i++) { // for every row (starting from second one) (word length of 2, 3, 4 etc.) (1)

				for (int j = 0; j < (inputStringLength - i) * cellWidth; j += cellWidth) { // every word of given length 5, 4, 3, 2, 1... (2)

					for (int r = 0; r < onlyRulesCount; r++) { //for each production (each rule)

						for (int k = 0; k < i; k++) { // for each neighbour (split points number of a word) 2| 1_2 - 2_1| 3_1 - 2_2 - 1_3| 4_1 - 3_2 - 2_3 - 1_4 (3)

							int offset = (int)(onlyRulesArray[0][r] / 32);
							int first = cykArray[k][j + offset];
							
							int offset2 = (int)(onlyRulesArray[1][r] / 32); // shift by 32 is the next cell
							int second = cykArray[i - k - 1][(((j / cellWidth) + k + 1) * cellWidth) + offset2];

							//decode nonterminals (find out if bits are on a given positions)
							int base = 1;
							//int bitMaskFirst = base << onlyRulesArray[0][r];
							int bitMaskFirst = (base << (onlyRulesArray[0][r] - (offset * 32)));
							//int bitMaskSecond = base << onlyRulesArray[1][r];
							int bitMaskSecond = (base << (onlyRulesArray[1][r] - (offset2 * 32)));
							if (first & bitMaskFirst && second & bitMaskSecond) {

								int shiftValue = onlyRulesArray[2][r];
								int offset = (int)(shiftValue / 32);
								int bitValue = base << (shiftValue - (offset * 32));
								//TODO - tutaj może być problem

								cykArray[i][j + offset] |= bitValue;
								
							}

						} // k loop

					} // r loop 

				} //end j loop

			} // end i loop

		}


		// stop timer
		QueryPerformanceCounter(&t2);

		elapsedTime = (t2.QuadPart - t1.QuadPart) * 1000.0 / frequency.QuadPart;
		std::cout << "CPU time: " << elapsedTime / 1000.0 << " ms\n";
		cout << "CPU result: " << cykArray[inputStringLength -1][0] << endl;

/*
		for (int j = 1; j < inputStringLength; j++) {
		for (int i = 0; i < inputStringLength - j; i++) {
		for (int c = 0; c < cellWidth; c++) {
		cout << cykArray[j][i + c] << " - ";
		}
		cout <<  " | ";
		}
		cout << endl;
		}*/

		/******************************************************************CUDA PART*********************************************************************/

		// variables
		int deviceNumber = 1;

		//select device number
		cudaSetDevice(deviceNumber);

		// time measure
		cudaEvent_t cudaStartTime, cudaStopTime;
		cudaEventCreate(&cudaStartTime);
		cudaEventCreate(&cudaStopTime);
		//default stream (time)
		cudaStream_t defStream;
		cudaStreamCreate(&defStream);



		// GPU Array Copy
		int** h_rulesNonTermsArray; //redundant
		int** d_rulesNonTermsArray;
		createCuda2DArrayInt(h_rulesNonTermsArray, d_rulesNonTermsArray, rulesNonTermsArray, nonTermsCount, nonTermsCount);

		// initial
		int threadsNumber = nonTermsCount; //TODO zmieniaj to odpowiednio - teraz jest to liczba nieterminali

										   // TODO remove that
		curandState * randState;
		cudaMalloc(&randState, threadsNumber * sizeof(curandState)); //warning! look size
		randInit << <1, threadsNumber >> > (randState, time(NULL)); //ustawienie ziaren

		int instanceSize = 5;


		CulturalData culturalData(instanceSize + 2, threadsNumber);
		// make array clear
		for (int i = 2; i < inputStringLength; i++) {
			for (int j = 0; j < inputStringLength * cellWidth; j++) {
				cykArray[i][j] = 0;
			}
		}

		CYKData cykData(cykArray, inputStringLength, d_rulesNonTermsArray, nonTermsCount);


		int blockNumber = 16;
		int* h_array_in;
		int* array_in;
		int* h_array_out;
		int* array_out;
		int** h_onlyRulesArray;
		int** d_onlyRulesArray;
		int nonTermsWithRulesCount;
		int** devicePtr;
		int** hostPtr;

		int algorithmChoice = 36; // TODO REPLACE IT
// ----------------------
		if (algorithmChoice >= 20 && algorithmChoice <= 29) {
			h_array_in = (int*)malloc(sizeof(int) * blockNumber);
			for (int i = 0; i < blockNumber; i++) { h_array_in[i] = 0; }
			cudaMalloc((void**)&array_in, sizeof(int) * blockNumber);
			cudaMemcpy(array_in, h_array_in, sizeof(int) * blockNumber, cudaMemcpyHostToDevice);

			h_array_out = (int*)malloc(sizeof(int) * blockNumber);
			for (int i = 0; i < blockNumber; i++) { h_array_out[i] = 0; }
			cudaMalloc((void**)&array_out, sizeof(int) * blockNumber);
			cudaMemcpy(array_out, h_array_out, sizeof(int) * blockNumber, cudaMemcpyHostToDevice);
		}
		else if (algorithmChoice >= 30 && algorithmChoice <= 39) {

			createCuda2DArrayInt(h_onlyRulesArray, d_onlyRulesArray, onlyRulesArray, 3, onlyRulesCount); // standard array (3 rows)

			// fancy array (every row each possible symbol (existing), first cell symbol index, second cell number of rules [ech 2 cell pair])
			int* nonTermsWithRules = new int[nonTermsCount];
			for (int i = 0; i < nonTermsCount; i++) {
				nonTermsWithRules[i] = 0;
			}
			for (int i = 0; i < onlyRulesCount; i++) {
				//cout << onlyRulesCount << " : " << i << ": " << onlyRulesArray[2][i] << endl;
				nonTermsWithRules[onlyRulesArray[2][i]]++;
			}
			// to create array (row) of proper size
			nonTermsWithRulesCount = 0;
			for (int i = 0; i < nonTermsCount; i++) {
				if (nonTermsWithRules[i] > 0) {
					nonTermsWithRulesCount++;
				}
			}

			int** onlyRulesArraySplitted = new int*[nonTermsWithRulesCount];
			int* nonTermsToRules = new int[nonTermsCount]; // to project indexes
			int projectionNumber = 0;
			for (int i = 0; i < nonTermsCount; i++) {
				// create rows of given length (2 + 2 * productions)
				if (nonTermsWithRules[i] > 0) {

					onlyRulesArraySplitted[projectionNumber] = new int[(nonTermsWithRules[i] * 2) + 2]; // additional 2 positions, first for the left nonterminal, second for row length
																										// initial setup
					onlyRulesArraySplitted[projectionNumber][1] = 0;
					onlyRulesArraySplitted[projectionNumber][0] = -1; //initial value - empty row

					nonTermsToRules[i] = projectionNumber;
					projectionNumber++;
				}
				else {
					nonTermsToRules[i] = -1;
				}

			}


			for (int i = 0; i < onlyRulesCount; i++) {

				int leftSymbol = onlyRulesArray[2][i]; //left symbol numeric value
				int leftSymbolPr = nonTermsToRules[leftSymbol]; // left symbol projection to new array row
				int offset = onlyRulesArraySplitted[leftSymbolPr][1]++; //get current productions number and increment it!

				onlyRulesArraySplitted[leftSymbolPr][2 + (offset * 2)] = onlyRulesArray[0][i];
				onlyRulesArraySplitted[leftSymbolPr][3 + (offset * 2)] = onlyRulesArray[1][i];
				onlyRulesArraySplitted[leftSymbolPr][0] = leftSymbol;
			}

			//for (int i = 0; i < nonTermsWithRulesCount; i++) { //rows

			//	for (int j = 0; j < onlyRulesArraySplitted[i][1] * 2 + 2; j+=2) {
			//		cout << onlyRulesArraySplitted[i][j] << " - " << onlyRulesArraySplitted[i][j + 1] << " | ";
			//	}
			//	cout << endl;

			//}

			//create device array copy
			hostPtr = (int**)malloc((nonTermsWithRulesCount) * sizeof(int*));

			for (int i = 0; i < nonTermsWithRulesCount; i++) {
				int columns = (onlyRulesArraySplitted[i][1] * 2 + 2);
				cudaMalloc((void**)&hostPtr[i], columns * sizeof(int));
				cudaMemcpy(hostPtr[i], &onlyRulesArraySplitted[i][0], columns * sizeof(int), cudaMemcpyHostToDevice);
			}

			cudaMalloc((void ***)&devicePtr, nonTermsWithRulesCount * sizeof(int*));
			cudaMemcpy(devicePtr, hostPtr, nonTermsWithRulesCount * sizeof(int*), cudaMemcpyHostToDevice);

		}
		cudaEventRecord(cudaStartTime, defStream); //start counting time
/////////////////////////////////////////////////////////////////////////////////////////////////
		algorithmChoice = 37;
		if (algorithmChoice == 10) {
			// TODO pamiętaj o wejściowej liczbie wątków
			// no restrictions
			cykAlgorithm<0> << <1, 1, 0, culturalData.getStream() >> >(cykData, randState);
		}
		else if (algorithmChoice == 11) {
			// noTermsCount < 1024
			cykAlgorithm<1> << <1, nonTermsCount, 0, culturalData.getStream() >> >(cykData, randState);
		}
		else if (algorithmChoice == 12) {
			// noTermsCount < 1024
			cykAlgorithm<2> << <1, nonTermsCount, 0, culturalData.getStream() >> >(cykData, randState);
		}
		else if (algorithmChoice == 13) {
			// noTermsCount < 32
			dim3 dimBlock(32, 32, 1);
			cykAlgorithm<3> << <1, dimBlock, 0, culturalData.getStream() >> >(cykData, randState);
		}
		else if (algorithmChoice == 14) {
			// dimension equals input string length
			// inputStringLength < 1024
			dim3 dimBlock(inputStringLength, 1, 1); //j - cells
			cykAlgorithm<4> << <1, dimBlock, 0, culturalData.getStream() >> >(cykData, randState);
		}
		else if (algorithmChoice == 15) {
			// block dimensions - max 1024 -> 32x32
			int tDimX = 32;
			int tDimY = 32;
			dim3 dimBlock(tDimX, tDimY, 1); //j - cells, k -> split points
			cykAlgorithm<5> << <1, dimBlock, 0, culturalData.getStream() >> >(cykData, randState);
		}
		else if (algorithmChoice == 101) {
			blockNumber = 16;
			dim3 dimBlock5(onlyRulesCount, 1, 1);

			//with local synchronisation
			for (int i = 1; i < inputStringLength; i++) {

				cykAlgorithmRules<2> << <inputStringLength - i, dimBlock5, 0 >> >(cykData, randState, array_in, array_out, d_onlyRulesArray, onlyRulesCount, i);
				//cudaDeviceSynchronize();
				cudaError_t cudaState;
				if (i < inputStringLength - 1) {
					cudaState = cudaDeviceSynchronize();

					if (cudaState != cudaSuccess) {
						fprintf(stderr, "\ncudaGetLastError: %s\n", cudaGetErrorString(cudaState));
						cudaGetLastError();
					}
				}
			}
		}
		else if (algorithmChoice == 20) {

			// TODO values -> now word cant be larger than 32 letters!!!! (bcs m is up to 32)
			dim3 dimBlock(32, 32, 1);
			int blockNumber = 8; // TODO and number of blocks with connection to number of threads

			cykAlgorithmCooperative<0> << <blockNumber, dimBlock, 0, culturalData.getStream() >> >(cykData, randState, array_in, array_out, 0);

		}
		else if (algorithmChoice == 21) {

			//TODO to samo co wyzej
			dim3 dimBlock(32, 32, 1);
			int blockNumber = 8;

			cykAlgorithmCooperative<1> << <blockNumber, dimBlock, 0, culturalData.getStream() >> >(cykData, randState, array_in, array_out, 0);

		}
		else if (algorithmChoice == 22) {

			//TODO to samo co wyzej
			dim3 dimBlock(16, 16, 1);
			int blockNumber = 8;

			cykAlgorithmCooperative<2> << <blockNumber, dimBlock, 0, culturalData.getStream() >> >(cykData, randState, array_in, array_out, 0);

		}
		else if (algorithmChoice == 23) {

			//TODO to samo co wyzej
			// x - m
			// y - k
			dim3 dimBlock(threadsNumber, 16, 1);
			int blockNumber = 8;

			cykAlgorithmCooperative<3> << <blockNumber, dimBlock, 0, culturalData.getStream() >> >(cykData, randState, array_in, array_out, 0);

		}
		else if (algorithmChoice == 24) {

			//TODO to samo co wyzej
			// x - m
			// y - k
			dim3 dimBlock(16, 16, 1);
			int blockNumber = 8;

			cykAlgorithmCooperative<4> << <blockNumber, dimBlock, 0, culturalData.getStream() >> >(cykData, randState, array_in, array_out, 0);

		} else if (algorithmChoice == 25) {

			

			dim3 dimBlock(32, 32, 1);

			//with local synchronisation
			for (int i = 1; i < inputStringLength; i++) {
				cykAlgorithmCooperative<5> <<<1, dimBlock, 0, culturalData.getStream() >>>(cykData, randState, array_in, array_out, i);

				//cudaDeviceSynchronize();
				cudaError_t cudaState;
				if (i < inputStringLength - 1) {
					cudaState = cudaDeviceSynchronize();

					if (cudaState != cudaSuccess) {
						fprintf(stderr, "\ncudaGetLastError: %s\n", cudaGetErrorString(cudaState));
						cudaGetLastError();
					}
				}
			}

		}
		else if (algorithmChoice == 26) {

			dim3 dimBlock(32, 1, 1);

			//with local synchronisation
			for (int i = 1; i < inputStringLength; i++) {
				cykAlgorithmCooperative<6> <<<inputStringLength - i, dimBlock, 0, culturalData.getStream() >> >(cykData, randState, array_in, array_out, i);

				//cudaDeviceSynchronize();
				cudaError_t cudaState;
				if (i < inputStringLength - 1) {
					cudaState = cudaDeviceSynchronize();

					if (cudaState != cudaSuccess) {
						fprintf(stderr, "\ncudaGetLastError: %s\n", cudaGetErrorString(cudaState));
						cudaGetLastError();
					}
				}
			}

		}
		else if (algorithmChoice == 27) {

			dim3 dimBlock(32, 32, 1);

			//with local synchronisation
			for (int i = 1; i < inputStringLength; i++) {
				cykAlgorithmCooperative<7> << <inputStringLength - i, dimBlock, 0, culturalData.getStream() >> >(cykData, randState, array_in, array_out, i);

				//cudaDeviceSynchronize();
				cudaError_t cudaState;
				if (i < inputStringLength - 1) {
					cudaState = cudaDeviceSynchronize();

					if (cudaState != cudaSuccess) {
						fprintf(stderr, "\ncudaGetLastError: %s\n", cudaGetErrorString(cudaState));
						cudaGetLastError();
					}
				}
			}

		}
		else if (algorithmChoice == 28) {

			dim3 dimBlock(128, 1, 1);

			//with local synchronisation

			for (int i = 1; i < inputStringLength; i++) {

				dim3 dimGrid(inputStringLength - i, 32, 1);

				cykAlgorithmCooperative<8> << <dimGrid, dimBlock, 0, culturalData.getStream() >> >(cykData, randState, array_in, array_out, i);

				//cudaDeviceSynchronize();
				cudaError_t cudaState;
				if (i < inputStringLength - 1) {
					cudaState = cudaDeviceSynchronize();

					if (cudaState != cudaSuccess) {
						fprintf(stderr, "\ncudaGetLastError: %s\n", cudaGetErrorString(cudaState));
						cudaGetLastError();
					}
				}
			}

		}
		else if (algorithmChoice == 29) {

			dim3 dimBlock(16, 2, 1);

			//with local synchronisation

			for (int i = 1; i < inputStringLength; i++) {

				dim3 dimGrid(inputStringLength - i, 32, 1);

				cykAlgorithmCooperative<9> << <dimGrid, dimBlock, 0, culturalData.getStream() >> >(cykData, randState, array_in, array_out, i);

				//cudaDeviceSynchronize();
				cudaError_t cudaState;
				if (i < inputStringLength - 1) {
					cudaState = cudaDeviceSynchronize();

					if (cudaState != cudaSuccess) {
						fprintf(stderr, "\ncudaGetLastError: %s\n", cudaGetErrorString(cudaState));
						cudaGetLastError();
					}
				}
			}

		}

		else if (algorithmChoice == 30) {

			blockNumber = 4;
			dim3 dimBlock5(onlyRulesCount, 1, 1); // every rule  = thread, blocks j loop
			cykAlgorithmRules<0> << <blockNumber, dimBlock5, 0, culturalData.getStream() >> >(cykData, randState, array_in, array_out, d_onlyRulesArray, onlyRulesCount, 0);

		}
		else if (algorithmChoice == 31) { //remember 32!!!!!!!

			dim3 dimBlock5(onlyRulesCount, 1, 1);

			//with local synchronisation
			for (int i = 1; i < inputStringLength; i++) {

				cykAlgorithmRules<2> << <inputStringLength - i, dimBlock5, 0 >> >(cykData, randState, array_in, array_out, d_onlyRulesArray, onlyRulesCount, i);
				cudaError_t cudaState;
				if (i < inputStringLength - 1) {
					cudaState = cudaDeviceSynchronize();

					if (cudaState != cudaSuccess) {
						fprintf(stderr, "\ncudaGetLastError: %s\n", cudaGetErrorString(cudaState));
						cudaGetLastError();
					}
				}
			}
		}
		else if (algorithmChoice == 32) {

			dim3 dimBlock5(onlyRulesCount, 1, 1);

			//with local synchronisation
			for (int i = 1; i < inputStringLength; i++) {
				dim3 dimGrid(inputStringLength - i, 2, 1);
				cykAlgorithmRules<2> << <dimGrid, dimBlock5, 0 >> >(cykData, randState, array_in, array_out, d_onlyRulesArray, onlyRulesCount, i);
				cudaError_t cudaState;
				if (i < inputStringLength - 1) {
					cudaState = cudaDeviceSynchronize();

					if (cudaState != cudaSuccess) {
						fprintf(stderr, "\ncudaGetLastError: %s\n", cudaGetErrorString(cudaState));
						cudaGetLastError();
					}
				}
			}
		}
		else if (algorithmChoice == 33) {
			//blockNumber = nonTermsWithRulesCount;
			dim3 dimBlock(64, 1, 1); //TODO change number of threads, number of rules -> x
			
														//with local synchronisation
			for (int i = 1; i < inputStringLength; i++) {
				dim3 dimGrid(inputStringLength - i, nonTermsWithRulesCount, 1); // y - left symbol, x - j loop
				cykAlgorithmRules<3> <<<dimGrid, dimBlock, 0, culturalData.getStream() >> >(cykData, randState, array_in, array_out, devicePtr, nonTermsWithRulesCount, i);

				//cudaDeviceSynchronize();
				cudaError_t cudaState;
				if (i < inputStringLength - 1) {
					cudaState = cudaDeviceSynchronize();

					if (cudaState != cudaSuccess) {
						fprintf(stderr, "\ncudaGetLastError: %s\n", cudaGetErrorString(cudaState));
						cudaGetLastError();
					}
				}
			}

			
		} else if (algorithmChoice == 34) {
			//blockNumber = nonTermsWithRulesCount;
			dim3 dimBlock(32, 4, 1); //TODO change number of threads, number of rules -> x

									 //with local synchronisation
			for (int i = 1; i < inputStringLength; i++) {
				dim3 dimGrid(inputStringLength - i, nonTermsWithRulesCount, 1); // y - left symbol, x - j loop
				cykAlgorithmRules<4> << <dimGrid, dimBlock, 0, culturalData.getStream() >> >(cykData, randState, array_in, array_out, devicePtr, nonTermsWithRulesCount, i);

				//cudaDeviceSynchronize();
				cudaError_t cudaState;
				if (i < inputStringLength - 1) {
					cudaState = cudaDeviceSynchronize();

					if (cudaState != cudaSuccess) {
						fprintf(stderr, "\ncudaGetLastError: %s\n", cudaGetErrorString(cudaState));
						cudaGetLastError();
					}
				}
			}


		} else if (algorithmChoice == 35) {
			//blockNumber = nonTermsWithRulesCount;
			dim3 dimBlock(32, 1, 1); //TODO change number of threads, number of rules -> x

									  //with local synchronisation
			for (int i = 1; i < inputStringLength; i++) {
				dim3 dimGrid(inputStringLength - i, nonTermsWithRulesCount, 8); // y - left symbol, x - j loop
				cykAlgorithmRules<5> << <dimGrid, dimBlock, 0, culturalData.getStream() >> >(cykData, randState, array_in, array_out, devicePtr, nonTermsWithRulesCount, i);

				//cudaDeviceSynchronize();
				cudaError_t cudaState;
				if (i < inputStringLength - 1) {
					cudaState = cudaDeviceSynchronize();

					if (cudaState != cudaSuccess) {
						fprintf(stderr, "\ncudaGetLastError: %s\n", cudaGetErrorString(cudaState));
						cudaGetLastError();
					}
				}
			}


		} else if (algorithmChoice == 36) {
			dim3 dimBlock5(32, 32, 1);

			//with local synchronisation
			for (int i = 1; i < inputStringLength; i++) {
				dim3 dimGrid(inputStringLength - i, 1, 1);
				cykAlgorithmRules<2> << <dimGrid, dimBlock5, 0 >> >(cykData, randState, array_in, array_out, d_onlyRulesArray, onlyRulesCount, i);
				cudaError_t cudaState;
				if (i < inputStringLength - 1) {
					cudaState = cudaDeviceSynchronize();

					if (cudaState != cudaSuccess) {
						fprintf(stderr, "\ncudaGetLastError: %s\n", cudaGetErrorString(cudaState));
						cudaGetLastError();
					}
				}
			}
		}
		else if (algorithmChoice == 37) {
			dim3 dimBlock5(1, 32, 1);

			//with local synchronisation
			for (int i = 1; i < inputStringLength; i++) {
				dim3 dimGrid(inputStringLength - i, onlyRulesCount, 1);
				cykAlgorithmRules<2> << <dimGrid, dimBlock5, 0 >> >(cykData, randState, array_in, array_out, d_onlyRulesArray, onlyRulesCount, i);
				cudaError_t cudaState;
				if (i < inputStringLength - 1) {
					cudaState = cudaDeviceSynchronize();

					if (cudaState != cudaSuccess) {
						fprintf(stderr, "\ncudaGetLastError: %s\n", cudaGetErrorString(cudaState));
						cudaGetLastError();
					}
				}
			}
		}
		else {

			/*void* params1[2];
			params1[0] = (void*)&cykData;
			params1[1] = (void*)&randState;*/

			//cudaLaunchCooperativeKernel((void*)cykAlgorithmCooperative<0>, 1, dimBlock, params1, 0, culturalData.getStream());
			//cudaStreamSynchronize(culturalData.getStream());

			//TODO Linux
			/*cudaError_t cudaState2;
			cudaState2 = cudaLaunchCooperativeKernel((void*)cykTest, 1, dimBlock, 0, 0, culturalData.getStream());

			cout << cudaGetErrorString(cudaState2);*/


			// Reversed Loop CYK part


			//getchar();

			blockNumber = nonTermsWithRulesCount;
			dim3 dimBlock6(16, 1, 1); //TODO change number of threads
			dim3 dimBl(2, nonTermsWithRulesCount, 1);
			//cykAlgorithmRules<1> << <dimBl, dimBlock6, 0, culturalData.getStream() >> >(cykData, randState, array_in, array_out, devicePtr, nonTermsWithRulesCount);



		}


		


		cudaError_t cudaState;
		cudaState = cudaDeviceSynchronize();

		if (cudaState != cudaSuccess) {
			fprintf(stderr, "\ncudaGetLastError: %s\n", cudaGetErrorString(cudaState));
			cudaGetLastError();
		}
		else {
			float hTimeValue = -1.0;
			cudaEventRecord(cudaStopTime, defStream); //stop counting time
			cudaEventSynchronize(cudaStopTime);
			cudaEventElapsedTime(&hTimeValue, cudaStartTime, cudaStopTime);
			printf("CUDA time: %f\n", hTimeValue / 1000.0f);
			printf("Result: %d\n", cykData.getResultValue());

		}

		//cuda memory
		cudaStreamDestroy(defStream);
		cudaFree(randState);

		if (algorithmChoice >= 20 && algorithmChoice <= 29) {
			cudaFree(h_array_in);
			cudaFree(h_array_out);
			cudaFree(array_out);
			cudaFree(array_in);
		}
		if (algorithmChoice >= 30 && algorithmChoice <= 39) {
			for (int i = 0; i < nonTermsWithRulesCount; i++) {
				cudaFree(hostPtr[i]);
			}
			free(hostPtr);
			cudaFree(devicePtr);
		}

		for (int i = 0; i < nonTermsCount; i++) {
			cudaFree(h_rulesNonTermsArray[i]);
		}
		free(h_rulesNonTermsArray);
		cudaFree(d_rulesNonTermsArray);

		getchar();
	}

	

	getchar();
	return 0;

}