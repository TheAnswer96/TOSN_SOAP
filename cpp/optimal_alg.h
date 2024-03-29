//
// Created by franc on 23/09/2022.
//

#ifndef CPP_OPTIMAL_ALG_H
#define CPP_OPTIMAL_ALG_H

#include "definitions.h"

tuple<int, int> opt_algorithm(orchard3D, int);
vector<int> opt_single_aisle(aisle2D aisle, int B, int m, int n);
vector<int> shift_solution(vector<int> sol, int shift);

#endif //CPP_OPTIMAL_ALG_H