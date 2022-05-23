#include "ListIterator.h"
#include "SortedIteratedList.h"
#include <exception>
#include <iostream>
#include <algorithm>
using namespace std;

ListIterator::ListIterator(const SortedIteratedList &list) : list(list){
    this->stack = new int[10000];
    this->capacity = 10000;
    this->current_size = 0;
    this->first();
} //Theta(1)



void ListIterator::first() {
    this->empty();
    this->current_node = this->list.root;
    while(this->current_node != -1){
        this->push(this->current_node);
        this->current_node = this->list.nodes[current_node].left;
    }
    if(this->current_size != 0){
        this->current_node = this->top();
    }
    else
        this->current_node = -1;
} // Theta(n)

void ListIterator::next() {
    if(!valid())
        throw std::exception();
    int node = this->pop();
    previous_node = node;
    if(this->list.nodes[node].right != -1){
        node = this->list.nodes[node].right;
        while(node != -1){
            this->push(node);
            node = this->list.nodes[node].left;
        }
    }
    if(this->current_size != 0){
        this->current_node = this->top();
    }
    else
        this->current_node = -1;

} // Theta(n)

bool ListIterator::valid() const {
    return this->current_node != -1;
} // Theta(1)

TComp ListIterator::getCurrent() const {
    if(!valid())
        throw std::exception();
    return list.nodes[current_node].value;
} // Theta(1)

void ListIterator::push(int data) {
    if(this->current_size == this->capacity)
        this->resize();
    this->stack[this->current_size] = data;
    this->current_size++;
} //Theta(1)

int ListIterator::pop() {
    if(this->current_size > 0){
        int elem = this->stack[this->current_size - 1];
        this->current_size--;
        return elem;
    }
} //Theta(1)

int ListIterator::top() {
    if(this->current_size > 0){
        return this->stack[this->current_size - 1];
    }
} //Theta(1)

void ListIterator::resize() {
    this->capacity *= 2;
    int* temp = new int[this->capacity];
    for(int i = 0; i < this->current_size; i++)
        temp[i] = this->stack[i];
    delete[] this->stack;
    this->stack = temp;
} //Theta(n)

void ListIterator::empty() {
    this->current_size = 0;
} //Theta(1)

void ListIterator::previous() {
    if(previous_node == -1)
        throw std::exception();
    current_node = previous_node;
    previous_node = list.nodes[current_node].father;
} //Theta(1)
