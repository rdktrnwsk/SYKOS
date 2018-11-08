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

int readGrammarNew(char fileName[50], char*& termsArray, int& terms, char*& nontermsArray, int& nonterms, int*& rulesArrayTerms, int& rulesTerms, int**& rulesArray, int& rulesNonterms, int**& onlyRulesArray, int& onlyRulesCount, vector<string>& wordsArrayNew)
{
	fstream file;
	file.open(fileName, ios::in);

	string row, name;
	terms = 0, nonterms = 0, rulesTerms = 0, rulesNonterms = 0;

	onlyRulesCount = 0;

	if (file.good())
	{
		// all nonterminals
		//vector<string> words{ "car", "apple", "box", "car", "apple", "foo" };
		vector<string> words; //nonterms 
		vector<string> wordsTerms; //terms 

		getline(file, row);
		while (getline(file, row)) // pierwsze wczytanie pliku
		{
			// get the file row
			//cout << row << endl;

			int wordsNumber = countWordsInString(row); // ile slow ma dany wiersz?

			// nonterms rules
			if (wordsNumber == 4) { // jezeli natrafilismy na regule nieterminali to staramy sie je po prostu pozbierac (na razie zbieramy wszystkie)

				//count the rules number
				rulesNonterms++;
				onlyRulesCount++;

				//for every single word
				string word = "";
				for (auto x : row) {
					if (x == ' ') {
						//word = "";

						

						if (word.find("->") != std::string::npos) {
							// ignore that one
						}
						else {
							//we have got one nonterminal (could be a duplicate!)
							words.push_back(word);
							//cout << word << '\n';
						}

						word = "";

					} else {
						word = word + x;
					}
				}
				
				//last word
				//cout << word << '\n';
				words.push_back(word);

				//vector<string> words{ "car", "apple", "box", "car", "apple", "foo" };

			} 
			//terms rules
			else if (wordsNumber == 3) { // jezeli natrafilismy na regule z terminalem to zbieramy tez je
				//for every single word
				string word = "";
				for (auto x : row) {

					//just skip to the last word
					if (x == ' ') {
						word = "";
					}
					else {
						word = word + x;
					}
				}

				word.erase(remove(word.begin(), word.end(), '\''), word.end());

				wordsTerms.push_back(word);
			}

			//cout << "test" << wordsNumber << endl;
			//cout << "test        " << wordsNumber << "           "  << row << endl;
		}

		// sort nonterminals - remove all recalls
		distinct(words); // remember it is sorting!
		
		//find the selected starting symbol and move it to the first position
		string startingSymbol = "S"; //symbol startowy musi byc S!!
		auto itr = find(words.begin(), words.end(), startingSymbol);
		if (itr != words.end()) {
			words.erase(itr);
			words.insert(words.begin(), startingSymbol);
		}
		
		wordsArrayNew = wordsTerms;

		nonterms = words.size();   //zapisana liczba terminali i nieterminali
		terms = wordsTerms.size();
		cout << "------------------------" << endl;
		for (string word : wordsTerms) {
			cout << word << " | ";
		}
		cout << endl << "------------------------" << endl;
		
		file.clear();
		file.seekg(0, ios::beg); // clear eof flag and go to the beginning of the file


		
		// ALREADY GOT THAT
		// read all terminals 
		/*termsArray = new char[terms];
		for (int i = 0; i < terms; i++) {
			getline(file, row);
			termsArray[i] = row[0];
		}*/

		// ALREADY GOT THAT
		// read all nonterminals - The first one have to be S!
		/*nontermsArray = new char[nonterms];
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

		}*/

		// read all rules - Here just creating array
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

		
		
		int onlyRulesIndex = 0;
		getline(file, row);
		while (getline(file, row)) { // raz jeszcze wczytanie calego pliku

			//cout << row << endl;

			int wordsNumber = countWordsInString(row); 

			//cout << wordsNumber << endl;

			int nontermIndex = -1, rowIndex = -1, columnIndex = -1;

			if (wordsNumber == 4) { //ponownie - jezeli dotyczy regul z nieterminalami
				string word = "";
				int wordNum = 0;
				
				for (auto x : row) {
					//cout << "OKKKKK" << wordNum << word << endl;
					//just skip to the last word
					if (x == ' ') {
						if (word.find("->") != std::string::npos) {
							wordNum++;
						}
						else {

							if (wordNum == 0) {
								nontermIndex = distance(words.begin(), find(words.begin(), words.end(), word));
								wordNum++;
							}
							else if (wordNum == 2) { // one space...
								rowIndex = distance(words.begin(), find(words.begin(), words.end(), word));
								
							}
							/*else if (wordNum == 2) {
							columnIndex = distance(words.begin(), find(words.begin(), words.end(), word));
							}*/
						}
						word = "";
					}
					else {
						word = word + x;
					}


				}
				columnIndex = distance(words.begin(), find(words.begin(), words.end(), word)); // last word
																				// write something into table
				rulesArray[rowIndex][columnIndex] = nontermIndex;

				onlyRulesArray[0][onlyRulesIndex] = rowIndex;
				onlyRulesArray[1][onlyRulesIndex] = columnIndex;
				onlyRulesArray[2][onlyRulesIndex] = nontermIndex;
				onlyRulesIndex++;
			}
			else if (wordsNumber == 3) { //jezeli natrafilismy na wiersz z terminalami
				
				string word = "";
				string firstWord = "";
				for (auto x : row) {

					//just skip to the last word
					if (x == ' ') {

						if (firstWord.empty()) {
							//cout << "NIETERMINAL " << word << endl;
							firstWord = word;
							nontermIndex = distance(words.begin(), find(words.begin(), words.end(), firstWord));
						}

						// last word

						word = "";
					}
					else {
						word = word + x;
					}
				}
				word.erase(remove(word.begin(), word.end(), '\''), word.end());
				//cout << "Terminal  " << word << endl;
				columnIndex = distance(wordsTerms.begin(), find(wordsTerms.begin(), wordsTerms.end(), word));

				//cout << "TUTAJ: " << row << " INDEKS: " << columnIndex << endl;

				rulesArrayTerms[columnIndex] = nontermIndex;

			}
			
		}

		cout << "-----------------------------------" << endl;
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < rulesTerms; j++) {
				cout << rulesArrayTerms[j] << " | ";
			}
			cout << endl;
		}
		cout << endl << "-----------------------------------" << endl;

		/*cout << "read here";
		getchar();*/


		/*cout << "----------------RULES-------------------" << endl;
		for (int j = 0; j < terms; j++) {
			cout << rulesArrayTerms[j] << " | ";
		}
		cout << endl;
		cout << endl << "-----------------------------------" << endl;*/

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
	cout << "read here";
	string row, name;
	terms = 0, nonterms = 0, rulesTerms = 0, rulesNonterms = 0;

	if (file.good())
	{
		while (getline(file, row))
		{

			if (isStringRule(row)) //only rules there
			{

				rulesNonterms++;
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
				//else if (countWordsInString(row) == 4) { // nonterminals
				//	rulesNonterms++;
				//}

			}
			cout << "test" << 5 << endl;
			cout << "read here";
			getchar();
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


/*****************NOWE DANE ******************************/

void distinct(vector<string>& vec)
{
	// First sort words alphabetically so we can find the duplicates.
	sort(begin(vec), end(vec));

	// Unique algorithm rearranges the input range to "mark for deletion"
	// adjacent duplicated entries and return iterator that 
	// denotes the end of the range of the unique values
	auto end_unique = unique(begin(vec), end(vec));
	// then remove the nonunique elements
	vec.erase(end_unique, end(vec));
}