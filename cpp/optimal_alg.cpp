//
// Created by franc on 23/09/2022.
//

#include "optimal_alg.h"

tuple<int, int> opt_algorithm(orchard3D orchard3D, int B) {
    int reward = 12;
    int cost = 6;
    int nR = B/2;
    int m = orchard3D.size();
    int n = orchard3D[0].size();
    int l = orchard3D[0][0].size();
    tree1D res_single_opt(nR+1,0);
    aisle2D opt_aisles(m, vector<int>(nR+1));

//    for (int i= 0; i<m; i++){
//        cout << endl;
//        for(int j=0; j<n; j ++){
//            for(int k=0; k<l;k++){
//                cout << orchard3D[i][j][k] <<" ";
//            }
//        }
//    }

    for (int i = 0; i < m; i++) {
        // compute optimum for each aisle
        //res_single_opt = opt_single_aisle(orchard3D[i], B, n, l);
        //recover the solution which exceeded the budget by shifting i position the vector
        //opt_aisles[i] = shift_solution(res_single_opt,i);
        opt_aisles[i] = opt_single_aisle(orchard3D[i], B, n, l);
    }
//    for (int i = 0; i <m; i++){
//        for(int j = 0; j < nR+1; j++){
//            cout << opt_aisles[i][j] << " ";
//        }
//        cout << endl;
//    }
    //dynamic programming
    aisle2D Q(m, tree1D(nR + 1));
    aisle2D S(m, tree1D(nR + 1));

    //first row of the table Q is exactly the first A*'s row
    for (int b = 0; b < nR + 1; b++){
        Q[0][b] = opt_aisles[0][b];
        S[0][b] = b;
    }

    //recurrence
    int idx = 0;
    int r = 0;
    for (int row=1; row < m; row++){
//        cout << " up to aisle : "<< row << endl;
        for (int b = 0; b < nR + 1; b++){
//            cout << " budget: "<< b << endl;
            for(int b_prime = 0; b_prime <= b; b_prime++){
                idx = b - b_prime -1;
                if(idx > 0){
                    r = opt_aisles[row][idx] + Q[row - 1][b_prime];
//                    cout << "A*: " << idx << " Q: " << b_prime << " |";
                    if (Q[row][b] < r){
                        Q[row][b] = r;
                        S[row][b] = b_prime;
                    }
                } else {
                    r = Q[row - 1][b];
//                    cout << " oQ: " << b << " ";
                    if (Q[row][b] < r) {
                        Q[row][b] = r;
                        S[row][b] = -1;
                    }
                }
            }
//           cout << endl;
        }
    }

//    for (int i = 0; i < m; i++){
//       //cout << "row " << i << endl;
//        for (int j = 0; j < nR +1; j++){
//            cout << " " << S[i][j] ;
//       }
//        cout << endl;
//   }
//   cout << "REWARD: " <<endl;
//    for (int i = 0; i < m; i++){
//        cout << "row " << i << endl;
//        for (int j = 0; j < nR +1; j++){
//            cout << " " << Q[i][j] ;
//        }
//        cout << endl;
//    }

    int max_r = -1;
    for (int i = 0; i < m; i++){
        if (max_r < Q[i][nR])
            max_r = Q[i][nR];
    }
    return make_tuple(max_r, nR*2);
}

vector<int> shift_solution(vector<int> sol, int shift){
    int B = sol.size();
    vector<int> shifted(B,0);
    for (int i = 0; i < (B - shift); i++){
        shifted[i + shift] = sol[i];
    }
    return shifted;
}

vector<int> opt_single_aisle(aisle2D aisle, int B, int m, int n) {
    int nR = B/2 + 1; //budget
    aisle2D R(m, vector<int>(nR)); //reward matrix
    aisle2D S(m, vector<int>(nR)); //indexes matrix
    aisle2D T(m, vector<int>(nR)); //trees reward
//    cout << "n: " << m <<" l: " << n << endl;
//    for (int i = 0; i < m; i++){
//        cout << "tree " << i << endl;
//        for (int j = 0; j < n; j++){
//            cout << "pos " << j << " val " << aisle[i][j] << endl;
//        }
//    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (j == 0) {
                T[i][j] = aisle[i][j];
            } else {
                T[i][j] = aisle[i][j] + T[i][j-1];
            }
        }
    }

    for (int b = 0; b < nR; b++) {
        //cout << b << endl;
        if (b < n) {
            R[0][b] = T[0][b];
            S[0][b] = b;
        } else {
            R[0][b] = T[0][n-1];
            S[0][b] = n-1;
        }
    }

    for (int i = 1; i < m; i++) {
        for (int b = 0; b < nR; b++) {
            if (b < i) {
                R[i][b] = -1;
                S[i][b] = -1;
            } else if (b == i) {
                R[i][b] = 0;
                S[i][b] = 0;
            } else {
                int max_v = -100;
                int arg_v = -1;
                for (int j = 0; j < n; j++) {
                    int idx = b-j-1;
                    if (idx >= 0) {
                        if (R[i-1][idx] != -1) {
                            int v = R[i-1][idx] + T[i][j];
                            if (v > max_v) {
                                max_v = v;
                                arg_v = j;
                            }
                        }
                    }
                }

                R[i][b] = max_v;
                S[i][b] = arg_v;
            }
        }
    }

//    for (int i = 0; i < m; i++) {
//        for (int j = 0; j < nR; j++) {
//           cout << R[i][j] << " ";
//       }
//       cout << endl;
//    }
//    cout << "------" << endl;

    tree1D bestR (nR,0);
    int max_t = -1;
    for (int i = 0; i < nR; i++){
        for (int j = 0; j < m; j++){
            if (max_t < R[j][i]){
                max_t = R[j][i];
            }
        }
        bestR[i] = max_t;
    }

//    for (int i = 0; i < nR; i++)
//        cout << bestR[i] << " ";
//    cout << endl;

    return bestR;
}