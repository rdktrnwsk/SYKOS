#include "Utility.h"

int main()
{
	printf("working\n\n\n");

	char* termsArray;
	int termsCount;
	char* nonTermsArray;
	int nonTermsCount;
	int* rulesTermsArray;
	int rulesTermsCount;
	int** rulesNonTermsArray;
	int rulesNonTermsCount;

	char name[50] = "grammar.txt";

	readGrammar(name, termsArray, termsCount, nonTermsArray, nonTermsCount, rulesTermsArray, rulesTermsCount, rulesNonTermsArray, rulesNonTermsCount);

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
	string inputString = "abcabdcabe"; //example input string
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

								cout << rulesNonTermsArray[l][m] << endl;

								cykArray[i][j] |= bitValue;
							}

						}


					}
					//	cout << endl;
				}

				//cout << first << " | " << second << endl;

				//combinations of productions

				// for each production (rulesNonTerminals)

			}

		}

		//break; //only first line

	}

	for (int i = 0; i < nonTermsCount; i++) {

		cout << nonTermsArray[i] << " | ";
	}

	cout << endl;

	for (int j = 1; j < inputStringLength; j++){
		for (int i = 0; i < inputStringLength  -j; i++) {

			cout << cykArray[j][i] << " | ";
		}
		cout << endl;
	}
	



	

	

	getchar();
	return 0;

}