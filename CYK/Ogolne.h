#include "Base.h"
#ifndef OGOLNE_H
#define OGOLNE_H

int readInstance(string fileName, float**& instanceMatrix, int& instanceSize); 

int readParameters(char* fileName, int& threadsNumber, int& roundsNumber, int& iterationsNumber, float& basePheromoneValue, float& evaporationRate, int& populationSize, int& generationsNumber, char save[100]);

int saveData(string fileName, string separator, float time, int best, int value1, int value2, int value3, int value4) ;

int saveData2(string fileName, string separator, float time, int best, int value1, int value2, int value3, int value4 , int value5 , int value6) ;
#endif