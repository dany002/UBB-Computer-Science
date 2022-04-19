//
// Created by SenZatIonALL on 3/18/2022.
//
#pragma once

#include "DynamicVector.h"
#include "Movie.h"
#include "Exceptions.h"


template<typename Telement>
DynamicVector<Telement>::DynamicVector() {
    /*
     * Default constructor. It allocates dynamically an element.
     */
    this->elems = new Telement[1];
    this->capacity = 1;
    this->size = 0;
}

template<typename Telement>
DynamicVector<Telement>::DynamicVector(const DynamicVector &v) {
    /*
     * Copy constructor.
     */
    this->size = v.size;
    this->capacity = v.capacity;
    this->elems = new Telement[this->capacity];
    for(int i = 0; i < v.size; i++)
        this->elems[i] = v.elems[i];

}

template<typename Telement>
void DynamicVector<Telement>::add(const Telement& data) {
    /*
     * It adds a new element in the end of the vector and if the size is the same as the capacity is going to reallocate memory.
     */
    if(this->size == this->capacity){
        Telement* temp = new Telement[2*this->capacity];
        for(int i = 0; i < this->size; i++)
            temp[i] = this->elems[i]; // Here we copy the elements from the old array!

        delete[] this->elems;
        this->capacity *= 2;
        this->elems = temp;
    }
    this->elems[this->size] = data;
    this->size++;
}

template<typename Telement>
Telement DynamicVector<Telement>::get_element(int index) {
    /*
     * It gets the element with the given index.
     */
    if(index >= this->size)
        throw IndexGreaterThanSize();

    return this->elems[index];

}

template<typename Telement>
void DynamicVector<Telement>::pop() {
    /*
     * It removes the last element.
     */
    if(this->size > 0)
        this->size--;
    else
        throw LengthIsZero();
}

template<typename Telement>
int DynamicVector<Telement>::get_size() {
    /*
     * It returns the size.
     */
    return this->size;
}

template<typename Telement>
int DynamicVector<Telement>::get_capacity() {
    /*
     * It returns the capacity.
     */
    return this->capacity;
}

template<typename Telement>
Telement *DynamicVector<Telement>::get_all_elems() {
    /*
     * It returns all the elements.
     */
    return this->elems;
}


template<typename Telement>
DynamicVector<Telement>::~DynamicVector(){
    /*
     * It frees the memory.
     */
    delete[] elems;
    this->size = 0;
    this->capacity = 0;
}

template<typename Telement>
void DynamicVector<Telement>::remove_element_from_a_specific_index(int index) {
    /*
     * It removes an element from a specific index.
     */
    if(index >= this->size)
        throw IndexGreaterThanSize();
    for(int i = index; i < this->size - 1; i++)
        this->elems[i] = this->elems[i+1];
    if(index < this->size)
        this->size--;
}

template<typename Telement>
void DynamicVector<Telement>::set_element(Telement elem, int i) {
    /*
     * It sets an element with a given index.
     */
    if(i >= this->size)
        throw IndexGreaterThanSize();
    this->elems[i] = elem;
}

template<typename Telement>
DynamicVector<Telement> &DynamicVector<Telement>::operator= (const DynamicVector &v) {
    this->size = v.size;
    this->capacity = v.capacity;
    this->elems = new Telement[this->capacity];
    for(int i = 0; i < v.size; i++)
        this->elems[i] = v.elems[i];
    return *this;
}


template class DynamicVector<Movie>;