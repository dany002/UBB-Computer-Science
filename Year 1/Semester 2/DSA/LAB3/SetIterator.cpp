#include "SetIterator.h"
#include "Set.h"
#include <exception>
#include <iostream>

SetIterator::SetIterator(const Set& m) : set(m)
{
	current = m.head;
}


void SetIterator::first() {
	current = set.head;
}


void SetIterator::next() {
	if(current == -1)
        throw std::exception();
    //std::cout << "Current in next: " << current << std::endl;
    current = set.next[current];
}


TElem SetIterator::getCurrent()
{
    if(current == -1)
	    throw std::exception();
    return set.elems[current];
}

bool SetIterator::valid() const {
	return current != -1;
}



