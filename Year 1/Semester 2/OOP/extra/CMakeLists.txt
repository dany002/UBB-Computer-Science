cmake_minimum_required(VERSION 3.21)
project(extra)

set(CMAKE_CXX_STANDARD 17)

add_executable(extra main.cpp Aircraft.cpp Aircraft.h Helicopter.cpp Helicopter.h Plane.cpp Plane.h Balloon.cpp Balloon.h Repo.cpp Repo.h UI.cpp UI.h Service.cpp Service.h)
