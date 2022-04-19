//
// Created by SenZatIonALL on 3/18/2022.
//
#pragma once

#ifndef A5_6_DANY002_DYNAMICVECTOR_H
#define A5_6_DANY002_DYNAMICVECTOR_H



template <typename Telement>
class DynamicVector {

private:
    Telement* elems;
    int size;
    int capacity;

public:
    DynamicVector();
    DynamicVector(const DynamicVector& v);
    ~DynamicVector();
    void add(const Telement& data);
    Telement get_element(int index);
    void set_element(Telement elem, int i);
    void pop();
    int get_size();
    int get_capacity();
    Telement* get_all_elems();
    void remove_element_from_a_specific_index(int index);
    DynamicVector& operator= (const DynamicVector& v);
};




#endif //A5_6_DANY002_DYNAMICVECTOR_H
