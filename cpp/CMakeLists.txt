cmake_minimum_required(VERSION 3.23)
project(cpp)

set(CMAKE_CXX_STANDARD 14)

add_executable(cpp main.cpp optimal_alg.cpp optimal_alg.h approximation_alg.cpp approximation_alg.h definitions.h util.cpp util.h heuristic_gba.cpp heuristic_gba.h heuristic_gbt.cpp heuristic_gbt.h approximation_alg2.cpp approximation_alg2.h)

