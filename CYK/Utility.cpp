#include "Utility.h"

int readGrammar(char fileName[50], char*& termsArray, int& terms, char*& nontermsArray, int& nonterms, int*& rulesArrayTerms, int& rulesTerms, int**& rulesArray, int& rulesNonterms)
{
	fstream file;
	file.open(fileName, ios::in);

	string row, name;
	terms = 0, nonterms = 0, rulesTerms = 0, rulesNonterms = 0;

	if(file.good())
	{
		getline(file, row);
		while(getline(file, row))
		{
			 // get the file row
			//cout << row << endl;

			if (isStringRule(row))
			{
				if (row.length() == 5) {
					rulesNonterms++;
				}
				else if (row.length() == 4) {
					rulesTerms++;
				}
				
			}
			else if (isStringLower(row)) //zgodnie z formatem pliku mamy dany opis
			{
				terms++;
			}
			else if (isStringUpper(row)) {
				nonterms++;
			}
		}

		/*cout << rules << endl;
		cout << terms << endl;
		cout << nonterms << endl;*/

		file.clear();
		file.seekg(0, ios::beg); // clear eof flag and go to the beginning of the file

		getline(file, row);

		// read all terminals
		termsArray = new char[terms];
		for (int i = 0; i < terms; i++) {
			getline(file, row);
			termsArray[i] = row[0];
		}

		// read all nonterminals
		nontermsArray = new char[nonterms];
		for (int i = 0; i < nonterms; i++) {
			getline(file, row);

			if (row[0] != 'S') {
				if (i == 0) {
					i++;
				}
				nontermsArray[i] = row[0];
			}
			else {
				nontermsArray[0] = row[0];
			}
			
		}

		// read all rules
		rulesArray = new int*[nonterms];
		for (int i = 0; i < nonterms; i++) {
			rulesArray[i] = new int[nonterms];
		}

		for (int i = 0; i < nonterms; i++) {
			for (int j = 0; j < nonterms; j++) {
				rulesArray[i][j] = -1;
			}
		}

		rulesArrayTerms = new int[terms];
		// tmp solution based on only correct data (single characters)
		for (int i = 0; i < rulesTerms + rulesNonterms; i++) {
			getline(file, row);
			
			int nontermIndex = -1, rowIndex = -1, columnIndex = -1;
			for (int j = 0; j < nonterms; j++) {
				
				if (row.length() == 5) {
					if (row[0] == nontermsArray[j]) {
						cout << nontermsArray[j] << endl;
						nontermIndex = j;
					}
					if (row[3] == nontermsArray[j]) {
						rowIndex = j;
					}
					if (row[4] == nontermsArray[j]) {
						columnIndex = j;
					}
				}
				else if (row.length() == 4) {
					
					if (row[0] == nontermsArray[j]) {
						nontermIndex = j;
						break;
					}
				}
				
			}

			if (row.length() == 5) {
				/*cout << row << endl;
				cout << rowIndex << endl;
				cout << columnIndex << endl;*/
				rulesArray[rowIndex][columnIndex] = nontermIndex;
			}
			else if (row.length() == 4) {

				for (int j = 0; j < terms; j++) {
					if (row[3] == termsArray[j]) {
						columnIndex = j;
						break;
					}
				}

				rulesArrayTerms[columnIndex] = nontermIndex;
			}

			

		}


		file.close();
		return 0;
	}
	else
	{
		file.close();
		printf("file problem");
		return -1;
	}

	return 0;
}


bool isStringLower(const string& inputString)
{
	for (char c : inputString)
	{
		if (!((c >= 'a' && c <= 'z')))
		{
			return false;
		}
		
	}

	return true;
}

bool isStringUpper(const string& inputString)
{
	for (char c : inputString)
	{
		if (!((c >= 'A' && c <= 'Z')))
		{
			return false;
		}

	}

	return true;
}

bool isStringRule(const string& inputString)
{
	bool ruleSet = false;
	for (char c : inputString)
	{
		if (c == '-')
		{
			ruleSet = true;
		}
		else if (c == '>') {
			if (ruleSet) {
				return true;
			}
			else {
				return false;
			}
		}
		else {
			ruleSet = false;
		}

	}
	return false;
}


