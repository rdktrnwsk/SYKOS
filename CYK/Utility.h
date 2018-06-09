#include "Header.h"
#ifndef UTILITY_H
#define UTILITY_H


int readGrammar(char fileName[50], char*& termsArray, int& terms, char*& nontermsArray, int& nonterms, int*& rulesArrayTerms, int& rulesTerms, int**& rulesArray, int& rulesNonterms, int**& onlyRulesArray, int& onlyRulesCount);

int readGrammarExtended(char fileName[50], char*& termsArray, int& terms, char*& nontermsArray, int& nonterms, int*& rulesArrayTerms, int& rulesTerms, int**& rulesArray, int& rulesNonterms, int**& onlyRulesArray, int& onlyRulesCount);


bool isStringLower(const string & inputString);

bool isStringUpper(const string & inputString);

bool isStringRule(const string & inputString);

int countWordsInString(string const& str);

string getWordBetweenSymbols(string text, string symbol);

#endif
