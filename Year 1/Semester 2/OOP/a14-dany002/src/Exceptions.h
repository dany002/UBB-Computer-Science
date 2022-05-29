//
// Created by moldo on 3/19/2022.
//
#pragma once
#ifndef A5_6_DANY002_EXCEPTIONS_H
#define A5_6_DANY002_EXCEPTIONS_H

#include <exception>


class IndexGreaterThanSize: public std::exception{
public:
    const char* what() const throw() override;
    IndexGreaterThanSize();
    ~IndexGreaterThanSize() override;
};

class LengthIsZero: public std::exception{
public:
    const char* what() const throw() override;
    LengthIsZero();
    ~LengthIsZero() override;
};

class RepositoryException: public std::exception{
public:
    const char* what() const throw() override;
    RepositoryException();
    ~RepositoryException() override;
};



class MovieDoesntExist: public std::exception{
public:
    const char* what() const throw() override;
    MovieDoesntExist();
    ~MovieDoesntExist() override;
};

class IntegerError: public std::exception{
public:
    const char* what() const throw() override;
    IntegerError();
    ~IntegerError() override;
};

class MovieAlreadyExists: public std::exception{
public:
    const char* what() const throw() override;
    MovieAlreadyExists();
    ~MovieAlreadyExists() override;
};

class UndoException: public std::exception{
public:
    const char* what() const throw() override;
    UndoException();
    ~UndoException() override;
};

class RedoException: public std::exception{
public:
    const char* what() const throw() override;
    RedoException();
    ~RedoException() override;
};

#endif //A5_6_DANY002_EXCEPTIONS_H
