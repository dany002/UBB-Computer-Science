#pragma once
#include "SortedBag.h"

class SortedBag;

class SortedBagIterator
{
	friend class SortedBag;

private:
	const SortedBag& bag;
    int current;
	SortedBagIterator(const SortedBag& b);


public:
	TComp getCurrent();
	bool valid() const;
	void next();
	void first();
};

