#include "Ogolne.h"

int readInstance(string fileName, float**& instanceMatrix, int& instanceSize) // wczytanie pliku z danymi
{
	fstream file;
	file.open(fileName + ".atsp", ios::in);
	string line, key, value;
	
	int i;
	if(file.good())  {
		do {
			getline(file, line); 
			i = line.find(':'); 

			if (i > 0) {
				key = line.substr(0, i);
				value = line.substr(i + 1);

				if(!key.compare("DIMENSION")) {
					sscanf_s(value.c_str(), "%d", &instanceSize);
				}
			}	
		}
		while(line.compare("EDGE_WEIGHT_SECTION"));

		instanceMatrix = (float**)malloc(instanceSize * sizeof(float*));
	
		for (int i = 0; i < instanceSize; i++) {
			instanceMatrix[i] = (float*)malloc(instanceSize * sizeof(float));
			for (int j = 0; j < instanceSize; j++) {
				file >> instanceMatrix[i][j];
				if(instanceMatrix[i][j] == 0) { //ants do not accept zero length route
					instanceMatrix[i][j] = 0.00001f;
				}
			}		
		}
		file.close();
		return 0;
	}
	else {
		file.close();
		return -2;
	}
} 


int readParameters(char* fileName, int& threadsNumber, int& tourNumber, int& iterationsNumber, float& basePheromoneValue, float& evaporationRate, int& populationSize, int& generationsNumber, char save[100]) {
	fstream file;
	file.open(fileName, ios::in);
	string line, key, value, saveName;
	
	int i;
	if(file.good())  {
		do {
			getline(file, line); //single row
			i = line.find(':'); //colon position

			if (i > 0) {

				key = line.substr(0, i);
				value = line.substr(i + 1);

				if(!key.compare("NUM_OF_THREADS"))  {
					sscanf_s(value.c_str(), "%d", &threadsNumber); 
					saveName += value;
					saveName += "_";
				}
				else if(!key.compare("NUM_OF_TOURS")) {
					sscanf_s(value.c_str(), "%d", &tourNumber); 
					saveName += value;
					saveName += "_";
				}
				else if(!key.compare("NUM_OF_ITERATIONS")) {
					sscanf_s(value.c_str(), "%d", &iterationsNumber); 
					saveName += value;
					saveName += "_";
				}
				else if(!key.compare("BASE_PHEROMONE_VAL")) {
					sscanf_s(value.c_str(), "%f", &basePheromoneValue); 
				}
				else if(!key.compare("EVAPORATION_RATE")) {
					sscanf_s(value.c_str(), "%f", &evaporationRate); 
				}
				else if(!key.compare("POPULATION_SIZE")) {
					sscanf_s(value.c_str(), "%d", &populationSize); 
					saveName += value;
					saveName += "_";
				}
				else if(!key.compare("NUM_OF_GENERATIONS")) {
					sscanf_s(value.c_str(), "%d", &generationsNumber); 
					saveName += value;
					saveName += "_";
				}
			}	
		}
		while(line.compare("EOF"));
		saveName = saveName.substr(0, saveName.size() -1);
		saveName += ".csv"; //default .csv
		sscanf_s(saveName.c_str(), "%s", &save[0]); 

		file.close();
		return 0;
	} else {
		file.close();
		return -1;
	}
}


int saveData(string fileName, string separator, float time, int best, int value1, int value2, int value3, int value4) {
	fstream score;
	score.open(fileName, ios::out | ios::app);
	if(score.good()) {
		score.setf( ios::showpoint );

		score << time <<separator << best <<separator << value1 << separator << value2 << separator << value3 << separator << value4  << endl;

		score.close();
		return 0;
	}
	
	score.close();
	return -3;
}

int saveData2(string fileName, string separator, float time, int best, int value1, int value2, int value3, int value4, int value5, int value6) {
	fstream score;
	score.open(fileName, ios::out | ios::app);
	if(score.good()) {
		score.setf( ios::showpoint );

		score << time <<separator << best <<separator << value1 << separator << value2 << separator << value3 << separator << value4 << separator << value5 << separator << value6 << endl;

		score.close();
		return 0;
	}
	
	score.close();
	return -3;
}