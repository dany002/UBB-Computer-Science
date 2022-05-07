#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>
#include <iostream>
using namespace std;

SMIterator::SMIterator(const SortedMap& m) : map(m){
    this->arr = new TElem[m.TABLE_SIZE];

	for(int i = 0; i < m.TABLE_SIZE; i++){
        this->arr[i] = m.hash_table[i];
    }

    for(int i = 0; i < m.TABLE_SIZE - 1; i++)
        for(int j = i + 1; j < m.TABLE_SIZE; j++)
            if(!map.relation(this->arr[i].first, this->arr[j].first)){
                TElem temp;
                temp = this->arr[i];
                this->arr[i] = this->arr[j];
                this->arr[j] = temp;
            }



    this->capacity = m.TABLE_SIZE;
    this->current = 0;
    this->total = m.keys_present;
    this->size = 0;
}

void SMIterator::first(){

    this->current = 0;
    while(!this->valid())
        this->current++;
    if(this->valid())
        this->size = 1;

}

void SMIterator::next(){

    if(!this->valid())
        throw std::exception();
    this->current++;
    this->size++;
}

bool SMIterator::valid(){
    if(this->arr[this->current] != NULL_TPAIR && this->size <= this->total) {
        return true;
    }
	return false;
}

TElem SMIterator::getCurrent() {
	if(this->valid()) {

        return this->arr[this->current];
    }
    throw std::exception();


}

SMIterator::~SMIterator() {
    delete[] this->arr;
}


