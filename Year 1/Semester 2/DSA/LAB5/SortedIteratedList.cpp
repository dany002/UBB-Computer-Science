#include "ListIterator.h"
#include "SortedIteratedList.h"
#include <iostream>
using namespace std;
#include <exception>


int SortedIteratedList::create_node(TComp elem, int left = -1, int right = -1){
    int i = allocate();

    nodes[i].value = elem;
    nodes[i].left = left;
    nodes[i].right = right;
    nodes[i].key = NULL_TCOMP;
    nodes[i].number_of_nodes = 1;
    nodes[i].father = -1;
    return i;
} // Theta(1)

SortedIteratedList::SortedIteratedList(Relation r) {
    this->relation = r;
    this->root = -1;
    this->_size = 0;
    this->cap = CAP;
    nodes = new bst_node[cap];
    for(int i = 0; i < cap; i++)
        this->nodes[i].key = NULL_TCOMP;
    this->sizee = 0;
} // Theta(n)



int SortedIteratedList::recursive_add(int root, TComp elem) {
    if(root == -1){
        root = create_node(elem);
        nodes[root].key = elem;
        nodes[root].value = elem;
        return root;
    }
    if(this->relation(elem, nodes[root].key))
        nodes[root].left = recursive_add(nodes[root].left, elem);
    else
        nodes[root].right = recursive_add(nodes[root].right, elem);
    recalculate(root);
    return root;
} // WC = AC = Theta(n) chain tree

void SortedIteratedList::add(TComp e) {
    this->root = recursive_add(this->root, e);
    this->_size++;
} //Theta(1)


int SortedIteratedList::size() const {
	return this->_size;
} // Theta(1)

bool SortedIteratedList::isEmpty() const {
	return this->_size == 0;
} // Theta(1)

ListIterator SortedIteratedList::first() const {
    ListIterator it{*this};
    return it;
} // Theta(1)

TComp SortedIteratedList::getElement(ListIterator poz) const {
	return poz.getCurrent();
} // Theta(1)

void SortedIteratedList::recalculate(int root) {
    nodes[root].number_of_nodes = 1;
    if(nodes[root].left != -1) {
        nodes[root].number_of_nodes += nodes[nodes[root].left].number_of_nodes;
        nodes[nodes[root].left].father = root;
    }
    if(nodes[root].right != -1) {
        nodes[root].number_of_nodes += nodes[nodes[root].right].number_of_nodes;
        nodes[nodes[root].right].father = root;
    }
} // Theta(1)

int SortedIteratedList::recursive_remove(int root, TComp elem) {
    if(root == -1)
        throw std::exception();
    if( nodes[root].key == elem) {
        int previous_father = -1;
        int previous = -1;
        int current = nodes[root].left;
        while(current != -1){
            previous_father = previous;
            previous = current;
            current = nodes[root].right;
        }
        if(previous == -1){
            int temp = nodes[root].right;
            deallocate(root);
            return temp;
        }
        nodes[previous].right = nodes[root].right;
        if(previous_father != -1)
            nodes[previous_father].right = -1;
        deallocate(root);
        return previous;
    }
    if(this->relation(elem, nodes[root].key))
        nodes[root].left = recursive_remove(nodes[root].left, elem);
    else
        nodes[root].right = recursive_remove(nodes[root].right, elem);
    recalculate(root);
    return root;
} // AC = Theta(log(n)). WC = Theta(n) chain tree

TComp SortedIteratedList::remove(ListIterator& poz) {
    TComp elem;
    try{
        elem = poz.getCurrent();
    }
    catch(exception& ex){
        throw std::exception();
    }
    try{
        this->root = recursive_remove(this->root, elem);
    }
    catch(exception& ex){
        throw std::exception();
    }
    this->_size--;
    return elem;
} // Theta(1)



ListIterator SortedIteratedList::search(TComp e) const{
    ListIterator it{*this};
    it.first();
    while(it.valid() && it.getCurrent() != e)
        it.next();
    return it;
} // Theta(n)


SortedIteratedList::~SortedIteratedList() {
    delete[] nodes;
} // Theta(1)


int SortedIteratedList::allocate() {
    if(this->sizee == cap){
        bst_node* temp = new bst_node[cap*2];
        for(int i = 0; i < this->sizee; i++)
            temp[i] = this->nodes[i];
        this->cap *= 2;
        for(int i = this->sizee; i < this->cap; i++)
            temp[i].key = NULL_TCOMP;
        delete[] this->nodes;
        this->nodes = temp;
    }
    for(int i = 0; i < this->cap; i++)
        if(this->nodes[i].key == NULL_TCOMP){
            this->sizee++;
            return i;
        }
} // WC = Theta(2*cap) BC=Theta(1) AC=Theta(n)

void SortedIteratedList::deallocate(int i) {
    this->nodes[i].key = NULL_TCOMP;
    this->sizee--;
} // Theta(1)
























