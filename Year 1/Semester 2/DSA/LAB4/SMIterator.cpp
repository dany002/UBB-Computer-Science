#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>

using namespace std;

SMIterator::SMIterator(const SortedMap& m) : map(m){
    this->arr = new TElem[MAX_SIZE];
	for(int i = 0; i < MAX_SIZE; i++){
        this->arr[i].first = m.hash_table[i].first;
        this->arr[i].second = m.hash_table[i].second;
    }

    for(int i = 0; i < MAX_SIZE - 1; i++)
        for(int j = i + 1; j < MAX_SIZE; j++)
            if(!map.relation(this->arr[i].first, this->arr[j].first)){
                TElem temp;
                temp.first = this->arr[i].first;
                temp.second = this->arr[i].second;
                this->arr[i] = this->arr[j];
                this->arr[j].first = temp.first;
                this->arr[j].second = temp.second;
            }
    this->current = 0;
}

void SMIterator::first(){
	this->current = 0;
}

void SMIterator::next(){
    if(this->valid())
        this->current++;
    else
        throw std::exception();
}

bool SMIterator::valid() const{
    if(this->current < this->map.size())
        return true;
	return false;
}

TElem SMIterator::getCurrent() const{
	if(this->valid())
        return this->arr[this->current];
	return NULL_TPAIR;
}


