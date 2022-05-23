#pragma once
//DO NOt INCLUDE LISTITERATOR

#include "ListIterator.h"

//DO NOT CHANGE THIS PART
class ListIterator;
typedef int TComp;
typedef bool (*Relation)(TComp, TComp);
#define NULL_TCOMP -11111
#define CAP 10000


class SortedIteratedList {
private:
	friend class ListIterator;
    Relation relation;
    struct bst_node{
        TComp value;
        int left;
        int right;
        TComp key;
        int number_of_nodes;
        int father;
    };
    int _size;
    bst_node* nodes;
    int sizee;
    int cap;
    int root;


    int create_node(TComp elem, int left, int right);

    int recursive_add(int root, TComp elem);

    int recursive_remove(int root, TComp elem);

    void recalculate(int root);

    int allocate();

    void deallocate(int i);

public:
	// constructor
	SortedIteratedList(Relation r);

	// returns the number of elements from the list
	int size() const;

	// verifies if the list is empty
	bool isEmpty() const;

	// returns the first position from the list
	ListIterator first() const;

	// returns the element from the given position
	//throws an exception if the position is not valid
	TComp getElement(ListIterator pos) const;

	// adds a new element to the list
	void add(TComp e);

	// removes the element from position pos
	//returns the removed element
	//after removal pos is positioned on the next element (the one after the removed one) or it is invalid if the last element was removed
	//throws an exception if the position is not valid
	TComp remove(ListIterator& poz);

	// searches for the first occurrence of an element 
	//returns an iterator that points to the element, if it appear in the list, or an invalid iterator if the element is not in the list
	ListIterator search(TComp e) const;

	//TODO elimina
	//void print();

	//destructor
	~SortedIteratedList();

};





