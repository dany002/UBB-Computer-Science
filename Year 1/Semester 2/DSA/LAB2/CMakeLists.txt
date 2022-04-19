cmake_minimum_required(VERSION 3.21)
project(LAB2_DSA)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(LAB2_DSA
        App.cpp
        ExtendedTest.cpp
        ExtendedTest.h
        Map.cpp
        Map.h
        MapIterator.cpp
        MapIterator.h
        ShortTest.cpp
        ShortTest.h)
