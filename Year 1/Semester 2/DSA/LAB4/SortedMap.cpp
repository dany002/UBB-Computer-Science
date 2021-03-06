#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>
#include <vector>
#include <iostream>
using namespace std;

SortedMap::SortedMap(Relation r) {
    this->relation = r;
	this->set_sieve();
    this->TABLE_SIZE = 15001;
    this->PRIME = this->TABLE_SIZE - 1;
    while (this->is_prime[this->PRIME]) // The largest prime number smaller than hash table's size.
        this->PRIME--;
    this->keys_present = 0;
    this->hash_table = new TElem[this->TABLE_SIZE];
    for(int i = 0; i < this->TABLE_SIZE; i++)
        this->hash_table[i] = NULL_TPAIR;


}

TValue SortedMap::add(TKey k, TValue v) {

    if(v == NULL_TVALUE || v == NULL_TVALUE-1)
        throw std::exception();
    if(this->is_full()) {

        TElem* temp = new TElem[2*this->TABLE_SIZE];
        for(int i = 0; i < this->TABLE_SIZE * 2; i++)
            temp[i] = NULL_TPAIR;

        this->PRIME = 2 * this->TABLE_SIZE - 1;
        while (this->is_prime[this->PRIME]) // The largest prime number smaller than hash table's size.
            this->PRIME--;

        for(int i = 0; i < this->TABLE_SIZE; i++){ // Rehash !!!
            int probe = this->hash1(this->hash_table[i].first);
            int offset = this->hash2(this->hash_table[i].first);
            while(temp[probe].first != NULL_TVALUE){
                probe = (probe+offset) % TABLE_SIZE;
            }
            temp[probe] = this->hash_table[i];
        }
        delete[] this->hash_table;
        this->TABLE_SIZE *= 2;
        this->hash_table = temp;
    }
    int probe = this->hash1(k);
    int offset = this->hash2(k);



    while(this->hash_table[probe].first != NULL_TVALUE && this->hash_table[probe].first != k){

        probe = (probe+offset) % TABLE_SIZE;
    }

    if(this->hash_table[probe].first == k) // if the key exist.
    {

        int old = this->hash_table[probe].second;
        this->hash_table[probe].second = v;
        return old;
    }

    this->hash_table[probe].first = k;
    this->hash_table[probe].second = v;
    this->keys_present++;

	return NULL_TVALUE;
}

TValue SortedMap::search(TKey k) const {
	int probe = hash1(k), offset = hash2(k), initial_pos = probe;
    bool first_itr = true;
    while(true){
        if(hash_table[probe] == NULL_TPAIR)
            break;
        else if(hash_table[probe].first == k)
            return hash_table[probe].second;
        else if(probe == initial_pos && !first_itr)
            return NULL_TVALUE;
        else
            probe = ((probe+offset) % TABLE_SIZE);
        first_itr = false;
    }
	return NULL_TVALUE;
}

TValue SortedMap::remove(TKey k) {
	if(this->search(k) == NULL_TVALUE)
        return NULL_TVALUE;

    int probe = hash1(k), offset = hash2(k);

    while(hash_table[probe] != NULL_TPAIR)
        if(hash_table[probe].first == k){
            TValue old = hash_table[probe].second;
            hash_table[probe] = NULL_TPAIR;
            keys_present--;
            return old;
        }
        else
            probe = ((probe+offset) % TABLE_SIZE);

	return NULL_TVALUE;
}

int SortedMap::size() const {
	return keys_present;

}

bool SortedMap::isEmpty() const {
	return ( keys_present == 0 );
}

SMIterator SortedMap::iterator() const {
	return SMIterator(*this);
}

SortedMap::~SortedMap() {
    delete[] this->hash_table;

}

void SortedMap::set_sieve() {
    // It sets the sieve of Erathostene.
    this->is_prime[0] = this->is_prime[1] = true;
    for ( long long i = 2; i*i <= MAX_SIZE; i++)
        if(!this->is_prime[i])
            for ( long long j = i*i; j <= MAX_SIZE; j += i)
                this->is_prime = true;
}

int SortedMap::hash1(int value) const {
    return value % this->TABLE_SIZE;
}

int SortedMap::hash2(int value) const {
    return this->PRIME - ( value % this->PRIME);
}

bool inline SortedMap::is_full() const {
    return ( this->TABLE_SIZE - 1 == this->keys_present);
}
