//
// Created by franc on 23/09/2022.
//

#include "approximation_alg.h"

tuple<int, int> apx_algorithm(orchard3D orchard, int budget) {
    int sol_reward = 0;
    int sol_cost = 0;

    int m = orchard.size();
    int n = orchard[0].size();
    int l = orchard[0][0].size();

    int i_max = 0;
    vector<int> j_max(m);
    vector<vector<int>> k_max(m, vector<int>(n));
//    int total = 0;

    while (budget > 0) {
        double best_ratio = -1.0;
        vector<int> best_selected(3);
        int best_reward = -1;
        int best_cost = -1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = k_max[i][j]+1; k < l; k++) {
                    int reward = orchard[i][j][k];
                    int cost = 2*(max(i-i_max, 0) + max(j-j_max[i], 0) + max(k-k_max[i][j], 0));
                    double ratio = static_cast<double>(reward) / cost;
//                    cout << "i: "<<i << " j: " << j << " k: " << k <<" cost: " << cost << " reward: "<< reward<< " ratio: " << ratio << endl;
                    if ((ratio > best_ratio) && (budget >= cost)) {
                        best_ratio = ratio;
                        best_reward = reward;
                        best_cost = cost;
//                        cout << "aa " << best_ratio << endl;

                        best_selected = {i, j, k};
                    }
                }
            }
        }

//        cout << "selected=[" << best_selected[0] << "," << best_selected[1] << "," << best_selected[2] << "], ratio=" << best_ratio << ", cost=" << best_cost << ", reward=" << best_reward << endl;
        if (best_ratio != -1){
            sol_cost += best_cost;
            i_max = max(best_selected[0], i_max);
            j_max[best_selected[0]] = max(best_selected[1],j_max[best_selected[0]]);
            k_max[best_selected[0]][best_selected[1]] = max(best_selected[2],k_max[best_selected[0]][best_selected[1]]);
//        total += best_reward;
            budget -= best_cost;
        }
        else{
            budget = 0;
        }
        //        cout << "remained budget: "<< budget << " total reward: "<< total << endl;
//        int a;
//        cin >>a;
    }
//    cout << "selected=[" << i_max << "," << j_max[i_max] << "," << k_max[i_max][j_max[i_max]] << "]" << endl;
    // Cumulative reward
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < k_max[i][j]+1; k++) {
                sol_reward += orchard[i][j][k];
            }
        }
    }


    return make_tuple(sol_reward, sol_cost);
}