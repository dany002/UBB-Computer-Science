#include "Map.h"
#include "MapIterator.h"
#include <exception>
using namespace std;


MapIterator::MapIterator(const Map& d) : map(d)
{
	currentElement = d.head;
}


void MapIterator::first() {
	currentElement = map.head;
}


void MapIterator::next() {
	if (currentElement == nullptr)
        throw exception();
    currentElement = currentElement->next;

}


TElem MapIterator::getCurrent(){
	if(currentElement == nullptr)
        throw exception();
	return currentElement->info;
}


bool MapIterator::valid() const {
	return currentElement != nullptr;
}



