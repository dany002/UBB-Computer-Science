#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <iostream>


SortedBag::SortedBag(Relation r) {
    this->relation = r;
	this->elements = new TComp[1];
    this->capacity = 1;
    this->length = 0;

}

void SortedBag::add(TComp e) {
	if(this->capacity == this->length){
        TComp* temp = new TComp[2*this->capacity];
        for(int i = 0; i < this->length; i++)
            temp[i] = this->elements[i];
        delete[] this->elements;
        this->capacity *= 2;
        this->elements = temp;
    }
    this->elements[this->length] = e;
    this->length++;
    int i = 1;
    while(i < this->length){ // SELECTION SORT.
        TComp x = this->elements[i];
        int j = i - 1;
        while(j >= 0 && this->relation(x, this->elements[j])){
            this->elements[j+1] = this->elements[j];
            j--;
        }
        this->elements[j+1] = x;
        i++;
    }

}//WC ( when capacity == length ) Theta(this->length) + Theta(this->length*2) = Theta(this->length*2). BC = Theta(1).


bool SortedBag::remove(TComp e) {

	for(int i = 0; i < this->length; i++){
        if(this->elements[i] == e){
            for(int j = i; j < this->length - 1; j++)
                this->elements[j] = this->elements[j+1];
            this->length--;
            return true;
        }
    }
    return false;
}//BC = AC = WC = Theta(this->length)


bool SortedBag::search(TComp elem) const {
	for(int i = 0; i < this->length; i++){
        if(this->elements[i] == elem)
            return true;
    }
	return false;
} // BC = AC = WC = Theta(this->length)


int SortedBag::nrOccurrences(TComp elem) const {
	int count = 0;
    for(int i = 0; i < this->length; i++)
        if(this->elements[i] == elem)
            count++;
	return count;
} // BC = AC = WC = Theta(this->length)



int SortedBag::size() const {
	return this->length;
} // Theta(1)


bool SortedBag::isEmpty() const {
	if(this->size() == 0)
        return true;
    return false;
} // Theta(1)


SortedBagIterator SortedBag::iterator() const {
	return SortedBagIterator(*this);
}


SortedBag::~SortedBag() {
	delete[] elements;
}
