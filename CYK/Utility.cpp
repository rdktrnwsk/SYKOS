#include "Utility.h"

int readGrammar(char fileName[50], char*& termsArray, int& terms, char*& nontermsArray, int& nonterms, int*& rulesArrayTerms, int& rulesTerms, int**& rulesArray, int& rulesNonterms, int**& onlyRulesArray, int& onlyRulesCount)
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

		onlyRulesCount = rulesNonterms;

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

			if (row[0] != '$') {
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


		//create new array containing only rules
		onlyRulesArray = new int*[3];
		for (int i = 0; i < 3; i++) {
			onlyRulesArray[i] = new int[rulesNonterms];
		}



		rulesArrayTerms = new int[terms];
		// tmp solution based on only correct data (single characters)
		int onlyRulesIndex = 0;
		for (int i = 0; i < rulesTerms + rulesNonterms; i++) {
			getline(file, row);
			
			int nontermIndex = -1, rowIndex = -1, columnIndex = -1;
			for (int j = 0; j < nonterms; j++) {
				
				if (row.length() == 5) {
					if (row[0] == nontermsArray[j]) {
						//cout << nontermsArray[j] << endl;
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
				else {
					cout << "bad row length:"  << row <<  endl;
				}
				
			}

			if (row.length() == 5) {
				/*cout << row << endl;
				cout << rowIndex << endl;
				cout << columnIndex << endl;*/
				rulesArray[rowIndex][columnIndex] = nontermIndex;

				onlyRulesArray[0][onlyRulesIndex] = rowIndex;
				onlyRulesArray[1][onlyRulesIndex] = columnIndex;
				onlyRulesArray[2][onlyRulesIndex] = nontermIndex;
				onlyRulesIndex++;
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

int readGrammarExtended(char fileName[50], char*& termsArray, int& terms, char*& nontermsArray, int& nonterms, int*& rulesArrayTerms, int& rulesTerms, int**& rulesArray, int& rulesNonterms, int**& onlyRulesArray, int& onlyRulesCount)
{
	fstream file;
	file.open(fileName, ios::in);

	string row, name;
	terms = 0, nonterms = 0, rulesTerms = 0, rulesNonterms = 0;

	if (file.good())
	{
		while (getline(file, row))
		{

			if (isStringRule(row)) //only rules there
			{
				/*if (row.length() == 5) {
					rulesNonterms++;
				}
				else if (row.length() == 4) {
					rulesTerms++;
				}*/
				if (countWordsInString(row) == 3) { // terminal or chain rule
					

					string word = getWordBetweenSymbols(row, "'");

					if (!word.empty()) { //terminal
						rulesTerms++;

						terms++;
					}
					else { //chain rule
						cout << "hehe" << endl;
					}
					
					
				}
				else if (countWordsInString(row) == 4) { // nonterminals
					rulesNonterms++;
				}

			}
			//else if (isStringLower(row)) //zgodnie z formatem pliku mamy dany opis
			//{
			//	terms++;
			//}
			//else if (isStringUpper(row)) {
			//	nonterms++;
			//}
		}
		getchar();

		onlyRulesCount = rulesNonterms;

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

			if (row[0] != '$') {
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


		//create new array containing only rules
		onlyRulesArray = new int*[3];
		for (int i = 0; i < 3; i++) {
			onlyRulesArray[i] = new int[rulesNonterms];
		}



		rulesArrayTerms = new int[terms];
		// tmp solution based on only correct data (single characters)
		int onlyRulesIndex = 0;
		for (int i = 0; i < rulesTerms + rulesNonterms; i++) {
			getline(file, row);

			int nontermIndex = -1, rowIndex = -1, columnIndex = -1;
			for (int j = 0; j < nonterms; j++) {

				if (row.length() == 5) {
					if (row[0] == nontermsArray[j]) {
						//cout << nontermsArray[j] << endl;
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
				else {
					cout << "bad row length:" << row << endl;
				}

			}

			if (row.length() == 5) {
				/*cout << row << endl;
				cout << rowIndex << endl;
				cout << columnIndex << endl;*/
				rulesArray[rowIndex][columnIndex] = nontermIndex;

				onlyRulesArray[0][onlyRulesIndex] = rowIndex;
				onlyRulesArray[1][onlyRulesIndex] = columnIndex;
				onlyRulesArray[2][onlyRulesIndex] = nontermIndex;
				onlyRulesIndex++;
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
		if (((c >= 'a' && c <= 'z')))
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

int countWordsInString(string const& str)
{
	stringstream stream(str);
	return distance(istream_iterator<string>(stream), istream_iterator<string>());
}

string getWordBetweenSymbols(string text, string symbol) {

	string::size_type start_position = 0;
	string::size_type end_position = 0;

	string word;

	start_position = text.find(symbol);
	if (start_position != std::string::npos)
	{
		start_position++; 

		end_position = text.find_last_of(symbol);
		if (end_position != std::string::npos)
		{
			word = text.substr(start_position, end_position - start_position);
		}
	}

	return word;
}


int saveData(string fileName, string separator, float time, int option, int value) {
	fstream score;
	score.open(fileName, ios::out | ios::app);
	if (score.good()) {
		score.setf(ios::showpoint);

		score << option << separator << value << separator << time << endl;

		score.close();
		return 0;
	}

	score.close();
	return -3;
}
