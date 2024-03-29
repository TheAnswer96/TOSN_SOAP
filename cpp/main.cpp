#include "definitions.h"
#include "util.h"
#include "optimal_alg.h"
#include "approximation_alg.h"
#include "approximation_alg2.h"
#include "heuristic_gba.h"
#include "heuristic_gbt.h"

/*
 * Example of parameters' execution: 0 orchards/o_m4_n3_l2_t0_s0 10
 *
 *      executable <function> <filename> <budget>
 *
 * The formal format of filename MUST BE as follows: o_m4_n3_l2_t0_s0
 *      m: number of rows (e.g., 4)
 *      n: number of columns (e.g., 3)
 *      l: number of observable positions (e.g., 2)
 *      t: ZipF theta (e.g., 0) (not used now)
 *      s: random instance (e.g., 0) (not used now)
 */
int main(int argc, char *argv[]) {

    int func = stoi(argv[1]);
    string input = argv[2];
    int budget = stoi(argv[3]);

    // It is a tree, therefore the path length must be even
    budget = (budget % 2 == 1 ? budget -1 : budget);

//    cout << "Function=" << (func == 0 ? "OPT" : "APX")  << ", Input=" << input << ", Budget=" << budget << endl;

    orchard3D orchard = read_input(input);
//    print_orchard(orchard);
    tuple<int, int> result;

    if (func == 0) {
        // OPT
        result = opt_algorithm(orchard, budget);
    } else if (func == 1) {
        // APX 0.32
        result = apx_algorithm(orchard, budget);
    } else if (func == 2) {
        // APX 1/m
        result = apx_algorithm2(orchard, budget);
    } else if (func == 3) {
        // GBA
        result = gba_algorithm(orchard, budget);
    } else if (func == 4) {
        // GBT
        result = gbt_algorithm(orchard, budget);
    }


    // Official output to be thrown...
    cout << "Reward=" << get<0>(result) << ", Cost=" << get<1>(result);

    return 0;
}
