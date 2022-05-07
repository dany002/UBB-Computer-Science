#pragma once
#include "SortedMap.h"

//DO NOT CHANGE THIS PART
class SMIterator{
	friend class SortedMap;
private:
	const SortedMap& map;
	SMIterator(const SortedMap& mapionar);

	//TODO - Representation
    int current;
    TElem* arr;
    int total;
    int size;
    int capacity;


public:
	void first();
	void next();
	bool valid();
    TElem getCurrent();
    ~SMIterator();
};

