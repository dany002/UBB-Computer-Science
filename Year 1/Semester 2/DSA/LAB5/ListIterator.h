#pragma once
#include "SortedIteratedList.h"
#include <vector>
//DO NOT CHANGE THIS PART
class ListIterator{
	friend class SortedIteratedList;
private:
	const SortedIteratedList& list;
	ListIterator(const SortedIteratedList& list);
    //ListIterator(const SortedIteratedList& list, int current);
    int current;
    Relation relation;
    std::vector<SortedIteratedList::bst_node*> node_stack;
    SortedIteratedList::bst_node current_node;

	//TODO - Representation
public:
	void first();
	void next();
	bool valid() const;
    TComp getCurrent() const;

};


