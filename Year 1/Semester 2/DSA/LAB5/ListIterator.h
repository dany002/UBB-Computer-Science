#pragma once
#include "SortedIteratedList.h"
#include <vector>
//DO NOT CHANGE THIS PART
class ListIterator{
	friend class SortedIteratedList;
private:
	const SortedIteratedList& list;
	ListIterator(const SortedIteratedList& list);
    int current_node;
    int previous_node;
    int* stack;
    int current_size;
    int capacity;
    void push(int data);
    int pop();
    int top();
    void resize();
    void empty();
    void previous();
	//TODO - Representation
public:
	void first();
	void next();
	bool valid() const;
    TComp getCurrent() const;

};


