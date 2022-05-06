#pragma once
//DO NOT INCLUDE SORTEDMAPITERATOR

//DO NOT CHANGE THIS PART
typedef int TKey;
typedef int TValue;
#include <utility>
typedef std::pair<TKey, TValue> TElem;
#define NULL_TVALUE -111111
#define NULL_TPAIR pair<TKey, TValue>(-111111, -111111)
class SMIterator;
typedef bool(*Relation)(TKey, TKey);

#include <vector>
#include <bitset>
#define MAX_SIZE 100

template <typename TKey, typename TValue >
class HashNode {
public:
    TKey k;
    TValue v;

    HashNode(TKey k, TValue v): k(k), v(v){};
};


class SortedMap {
	friend class SMIterator;
private:
    HashNode<TKey, TValue>* aux;
    TElem* hash_table;
    int TABLE_SIZE, keys_present, PRIME;
    std::bitset<MAX_SIZE> is_prime;
    Relation relation;

    void set_sieve();
    int hash1(int value) const;
    int hash2(int value) const;
    bool inline is_full();

public:

    // implicit constructor
    SortedMap(Relation r);


	// adds a pair (key,value) to the map
	//if the key already exists in the map, then the value associated to the key is replaced by the new value and the old value is returned
	//if the key SMes not exist, a new pair is added and the value null is returned
	TValue add(TKey c, TValue v);

	//searches for the key and returns the value associated with the key if the map contains the key or null: NULL_TVALUE otherwise
	TValue search(TKey c) const;


	//removes a key from the map and returns the value associated with the key if the key existed ot null: NULL_TVALUE otherwise
	TValue remove(TKey c);

	//returns the number of pairs (key,value) from the map
	int size() const;

	//checks whether the map is empty or not
	bool isEmpty() const;

    // return the iterator for the map
    // the iterator will return the keys following the order given by the relation
    SMIterator iterator() const;

    // destructor
    ~SortedMap();
};
