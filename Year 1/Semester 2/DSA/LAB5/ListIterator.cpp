#include "ListIterator.h"
#include "SortedIteratedList.h"
#include <exception>
#include <iostream>
#include <algorithm>
using namespace std;

ListIterator::ListIterator(const SortedIteratedList &list) : list(list){
    this->current = 0;
    relation = list.relation;
    this->node_stack = std::vector<SortedIteratedList::bst_node*>();
    this->current_node.right = -1;
    this->current_node.left = -1;
    this->current_node.key = NULL_TCOMP;
    this->current_node.father = -1;
    //this->current = 0;


    if(list.root != -1) {

        this->node_stack.push_back(list.nodes);
        for(auto a : this->node_stack)
            cout << a->value << "    ";

        sort(this->node_stack.begin(), this->node_stack.end());

        /*
        SortedIteratedList::bst_node temp = this->node_stack.back();

        //cout << temp.key;
        while(temp.key != NULL_TCOMP){
            this->node_stack.push_back(temp);
            //cout << list.nodes[temp.left].key << endl;
            temp = list.nodes[temp.left];
        }
        current_node = this->node_stack.back();
        this->node_stack.pop_back();
        temp = list.nodes[current_node.right];


        while(temp.key != NULL_TCOMP){
            this->node_stack.push_back(temp);
            temp = list.nodes[temp.right];
        }
        */
    }

}
/*
ListIterator::ListIterator(const SortedIteratedList &list, int current) : list(list) {
    this->current = current;
}

 */



void ListIterator::first() {
    this->current = 0;
    /*
    if(list.root != -1) {
        this->node_stack.push_back(list.nodes);
        //for (auto a: this->node_stack)
        //    cout << a->value << "    ";
        sort(this->node_stack.begin(), this->node_stack.end());
    }
     */
}

void ListIterator::next() {
    if(!valid())
        throw std::exception();

    this->current++;

    //while(list.nodes[current].left != -1);
    /*
    if(list.nodes[current].right != -1 && list.relation(list.nodes[current].key, list.nodes[list.nodes[current].right].key) == 1){
        current = list.nodes[current].right;
    }
    else
    {
        int next = current;
        while (next != -1 && (list.nodes[next].right == -1 ||
                              list.nodes[list.nodes[next].right].key == this->list.nodes[current].key ||
                              this->list.relation(list.nodes[current].key, list.nodes[list.nodes[next].right].key) ==
                              0)) {
            next = list.nodes[next].father;
        }
        current = next;
    }
    if(current != -1){
        while(list.nodes[current].left != -1){
            current = list.nodes[current].left;
        }
    }
     */
}

bool ListIterator::valid() const {
    return this->current < list.size();
}

TComp ListIterator::getCurrent() const {
    if(!valid())
        throw std::exception();
    return list.nodes[this->current].value;
}
