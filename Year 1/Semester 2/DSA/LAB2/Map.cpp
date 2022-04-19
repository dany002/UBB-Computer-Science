#include "Map.h"
#include "MapIterator.h"
#include <iostream>


Map::Map::SLLNode::SLLNode(TElem e, Map::PNode n) {
    info = e;
    next = n;
}


Map::Map() {
	head = nullptr;
}

Map::~Map() {
	while ( head != nullptr ){
        PNode p = head;
        head = head->next;
        delete p;
    }
}

TValue Map::add(TKey c, TValue v){
    SLLNode* temp = head;
    TValue old;
    while(temp != nullptr){
        if(temp->info.first == c){
            old = temp->info.second;
            temp->info.second = v;
            return old;
        }
        temp = temp->next;
    }

    PNode pn = new SLLNode(TElem(c, v), nullptr);
    pn->next = head;
    head = pn;
    return NULL_TVALUE;
}

TValue Map::search(TKey c) const{
	PNode temp = head;
    while(temp != nullptr){
        if(temp->info.first == c)
            return temp->info.second;
        temp = temp->next;
    }
    return NULL_TVALUE;
}

TValue Map::remove(TKey c){
    TValue old;
    if(isEmpty())
        return NULL_TVALUE;

    if(head->info.first == c) // It means the head is the element.
    {
        old = head->info.second;
        PNode temp = head->next;
        delete head;
        head = temp;
        return old;
    }
    if(head->next == nullptr){ // It means there is only an element in the map.
        if(head->info.first == c){
            old = head->info.second;
            delete head;
            head = nullptr;
            return old;
        }
        else
            return NULL_TVALUE;
    }


    PNode temp = head;
    while(temp->next != nullptr){
        if(temp->next->info.first == c){
            PNode temp_ptr = temp->next->next;
            old = temp->next->info.second;

            delete temp->next;
            temp->next = temp_ptr;
            return old;
        }
        temp = temp->next;
    }
	return NULL_TVALUE;
}


int Map::size() const {
	int size = 0;
    PNode temp = head;
    while(temp != nullptr){
        size++;
        temp = temp->next;
    }
	return size;
}

bool Map::isEmpty() const{
    if(head == nullptr)
        return true;
	return false;
}

MapIterator Map::iterator() const {
	return MapIterator(*this);
}



