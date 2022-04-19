cmake_minimum_required(VERSION 3.21)
project(a8_9_dany002)




#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")


set(CMAKE_CXX_STANDARD 14)

include_directories(src)

add_executable(a8_9_dany002
        src/Controller.cpp
        src/Controller.h
        src/DynamicVector.cpp
        src/DynamicVector.h
        src/Exceptions.cpp
        src/Exceptions.h
        src/main.cpp
        src/Movie.cpp
        src/Movie.h
        src/Repository.cpp
        src/Repository.h
        src/Tests.cpp
        src/UI.cpp
        src/UI.h
        src/WatchList.cpp
        src/WatchList.h
        src/TextFiles.cpp
        src/TextFiles.h
        src/HtmlFile.cpp
        src/HtmlFile.h
        src/CsvFiles.cpp
        src/CsvFiles.h)
