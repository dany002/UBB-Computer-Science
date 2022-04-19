#include "Set.h"
#include "SetIterator.h"
#include <iostream>

Set::Set() {
    this->head = -1;

    for(int i = 0; i < Set::cap - 1; i++){
        this->next[i] = i + 1;
        this->prev[i+1] = i;
        this->elems[i] = 0;
    }
    this->elems[Set::cap - 1] = 0;
    this->prev[0] = -1;
    this->next[cap-1] = -1;

    firstFree = 0;
}


bool Set::add(TElem elem) {

    for(int node = head; node != -1; node=next[node])
        if(this->elems[node] == elem){
            return false;
        }

    int n = this->allocateP();
    if(n == -1) // it s full.
        return false;


    this->elems[n] = elem;
    next[n] = head;
    prev[head] = n;
    head = n;

    //std::cout << "n = " << n << " " << elem << " " <<"HEAD = " << head << std::endl;
    return true;
}


bool Set::remove(TElem elem) {

    if(head == -1)
        return false;
	if(elems[head] == elem) {
        int tmp = next[head];
        FreeP(head);
        head = tmp;
        if(head != -1)
            prev[head] = -1;
        return true;
    }
    for(int node = head; node != -1; node=next[node])
        if(elems[node] == elem){
            if(next[node] == -1 && prev[node] == -1);
            else if(next[node] == -1)
                next[prev[node]] = -1;
            else if(prev[node] == -1)
                prev[next[node]] = -1;
            else{
                prev[next[node]] = prev[node];
                next[prev[node]] = next[node];
            }

            FreeP(node);

            return true;
        }
	return false;
}

bool Set::search(TElem elem) const {
    for(int node = head; node != -1; node=next[node])
        if(elems[node] == elem)
            return true;
	return false;
}


int Set::size() const {
    int count = 0;
    for(int node = head; node != -1; node=next[node])
        count++;
    return count;
}


bool Set::isEmpty() const {
	if(head == -1)
	    return true;
    return false;
}


Set::~Set() {

}


SetIterator Set::iterator() const {
	return SetIterator(*this);
}

int Set::allocateP() {

    if(firstFree == -1)
        return -1;
    int new_free_pos = firstFree;
    firstFree = next[firstFree];
    if(firstFree != -1)
        prev[firstFree] = -1;
    return new_free_pos;
}

void Set::FreeP(int i) {
    next[i] = firstFree;
    if(firstFree != -1)
        prev[firstFree] = i;
    firstFree = i;

}

Set &Set::operator=(const Set &set) {

    for(int i = 0; i < Set::cap; i++){
        this->elems[i] = set.elems[i];
        this->next[i] = set.next[i];
        this->prev[i] = set.prev[i];
    }
    this->head = set.head;
    this->firstFree = set.head;
    return *this;
}

Set::Set(const Set &set) {

    for(int i = 0; i < Set::cap; i++){
        this->elems[i] = set.elems[i];
        this->next[i] = set.next[i];
        this->prev[i] = set.prev[i];
    }
    this->head = set.head;
    this->firstFree = set.head;
}




