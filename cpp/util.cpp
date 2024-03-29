//
// Created by franc on 26/09/2022.
//

#include "util.h"

orchard3D read_input(string input_file_name) {
    // Example: "orchards/o_m4_n3_l2_t0_s0"

    stringstream ss(input_file_name);
    string segment;
    vector<int> parameters;

    int i = 0;
    while(getline(ss, segment, '_')) {
        // Ignores the shit "orchards/o"
        if (i++ > 0) {
            // Remove the first char, and convert it to int
            int value = stoi(segment.erase(0, 1));
            parameters.push_back(value);
        }
    }

    int m = parameters[0];
    int n = parameters[1];
    int l = parameters[2];
    orchard3D orchard(m, aisle2D(n, tree1D(l)));

    i = 0;
    ifstream data(input_file_name);
    string line;
    while(getline(data, line)) {
        int j = 0;
        stringstream ss_1(line);
        string cell_1;
        while(getline(ss_1, cell_1, ']')) {
            int k = 0;
            if (j > 0) {
                // Remove the useless comma
                cell_1 = cell_1.erase(0, 1);
            }
            // Remove the "["
            cell_1 = cell_1.erase(0, 1);
            stringstream ss_2(cell_1);
            string cell_2;
            while(getline(ss_2, cell_2, ',')) {
                int value = stoi(cell_2);
//                cout << i << ", " << j << ", " << k << ": -> " << value << endl;
                orchard[i][j][k] = value;
                k++;
            }
            j++;
        }
        i++;
    }

    return orchard;
}

void print_orchard(orchard3D orchard) {
    cout << "m=" << orchard.size() << ", n=" << orchard[0].size() << ", l=" << orchard[0][0].size() << endl;
    for (aisle2D aisle : orchard) {
        for (tree1D tree : aisle) {
            cout << "[";
            for (int position : tree) {
                cout << position << ",";
            }
            cout << "]";
        }
        cout << endl;
    }
}
