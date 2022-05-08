//
// Created by moldo on 3/19/2022.
//

#include "Exceptions.h"

const char *IndexGreaterThanSize::what() const throw() {
    return "The index that u gave is greater than the size of the array.";
}

IndexGreaterThanSize::~IndexGreaterThanSize(){}

IndexGreaterThanSize::IndexGreaterThanSize(){}

const char *LengthIsZero::what() const throw() {
    return "The length is zero.";
}

LengthIsZero::~LengthIsZero() {}

LengthIsZero::LengthIsZero() {}

const char *RepositoryException::what() const throw() {
    return "Repository exception.";
}

RepositoryException::~RepositoryException() {}

RepositoryException::RepositoryException() {}



const char *MovieDoesntExist::what() const throw() {
    return "Movie doesn't exist.";
}

MovieDoesntExist::MovieDoesntExist() {}

MovieDoesntExist::~MovieDoesntExist() {}

const char *IntegerError::what() const throw() {
    return "The year and the number of likes must be > 0.";
}

IntegerError::IntegerError() {}

IntegerError::~IntegerError() {}

const char *MovieAlreadyExists::what() const throw() {
    return "Movie already exists.";
}

MovieAlreadyExists::MovieAlreadyExists() {}

MovieAlreadyExists::~MovieAlreadyExists() {}
