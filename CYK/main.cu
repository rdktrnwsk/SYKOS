#include "Utility.h"
#include "Ogolne.cuh"
#include "Ogolne.h"
#include "functions.cuh"
#include "Cultural.cuh"
#include "CYK.cuh"


int main(int argc, char** argv)
{
	printf("working\n\n\n");

	printf("Grammar: %s\n", argv[1]);
	printf("Input: %s\n", argv[2]);

	char* termsArray;
	int termsCount;
	char* nonTermsArray;
	int nonTermsCount;
	int* rulesTermsArray;
	int rulesTermsCount;
	int** rulesNonTermsArray;
	int rulesNonTermsCount;

	char name[50] = "grammar.txt";

	readGrammar(argv[1], termsArray, termsCount, nonTermsArray, nonTermsCount, rulesTermsArray, rulesTermsCount, rulesNonTermsArray, rulesNonTermsCount);

	//for (int i = 0; i < terms; i++) {
	//	for (int j = 0; j < rules; j++) {

	//		//cout << rulesArray[i][j] << " | ";

	//	}
	//	cout << rulesTerms[i] << " | ";
	//	//cout << endl;
	//}

	for (int i = 0; i < nonTermsCount; i++) {
		for (int j = 0; j < nonTermsCount; j++) {
			cout << rulesNonTermsArray[i][j] << " | ";
		}
		cout << endl;
	}

	/*ALGORITHM START*/

	// 1. First part

	// create CYK array of input string length
	//string inputString = "abcabdcabe"; //example input string
	string inputString = argv[2];
	int inputStringLength = inputString.length();
	int** cykArray = new int*[inputStringLength];
	for (int i = 0; i < inputStringLength; i++) {
		cykArray[i] = new int[inputStringLength];
	}
	// make array clear
	for (int i = 0; i < inputStringLength; i++) {
		for (int j = 0; j < inputStringLength; j++) {
			cykArray[i][j] = 0;
		}
	}

	// first phase, terminal rules array, for every input string character
	for (int i = 0; i < inputStringLength; i++) {

		// find character (terminal index)
		int terminalIndex = -1;
		for (int j = 0; j < termsCount; j++) {
			if (inputString[i] == termsArray[j]) {
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

			int base = 1;
			int bitValue = base << shiftValue;

			cykArray[0][i] |= bitValue;
		}
		//}
	}

	// printing arrays and first row result
	/*for (int i = 0; i < termsCount; i++) {

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

	for (int i = 0; i < inputStringLength; i++) {

		cout << cykArray[0][i] << " | ";
	}*/

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

								cykArray[i][j] |= bitValue;
							}

						}


					}

				}

				//cout << first << " | " << second << endl;

				//combinations of productions

				// for each production (rulesNonTerminals)

			}

		}

		//break; //only first line

	}

	for (int j = 1; j < inputStringLength; j++) {
		for (int i = 0; i < inputStringLength - j; i++) {

			cout << cykArray[j][i] << " | ";
		}
		cout << endl;
	}


	/******************************************************************CUDA PART*********************************************************************/

	// initial
	int threadsNumber = 8;

	//
	curandState * randState;
	cudaMalloc(&randState, threadsNumber * sizeof(curandState)); //warning! look size
	randInit <<<1, threadsNumber >>> (randState, time(NULL)); //ustawienie ziaren

	int instanceSize = 5;


	CulturalData culturalData(instanceSize + 2, threadsNumber);
	float** d_instanceMatrix;
	//CYKData cykData(d_instanceMatrix);


	cykAlgorithm<1><<<1, threadsNumber, 0, culturalData.getStream()>>>(randState);
	
	//cuda memory
	cudaFree(randState);

	getchar();
	return 0;

}