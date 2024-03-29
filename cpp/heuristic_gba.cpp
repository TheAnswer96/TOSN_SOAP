//
// Created by franc on 02/10/2022.
//

#include "heuristic_gba.h"

tuple<int, int> gba_algorithm(orchard3D orchard, int budget) {
    int sol_reward = 0;
    int sol_cost = 0;

    int m = orchard.size();
    int n = orchard[0].size();
    int l = orchard[0][0].size();

    int i_max = 0;

    vector<int> aisles(m);
    for (int i = 0; i < m; i++) {
        int sum = 0;
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < l; k++) {
                sum += orchard[i][j][k];
            }
        }
        aisles[i] = sum;
    }

    while (budget > 0) {
        double best_ratio = -1.0;
        int best_selected = -1;
        int best_reward = -1;
        int best_cost = -1;

        for (int i = 0; i < m; i++) {
            int reward = aisles[i];
            int cost = 2*(max(i-i_max, 0)) + (2*(l-1)*n + 2*(n-1));
            double ratio = static_cast<double>(reward) / cost;
//            cout << "ratio=[" << ratio << "], reward=" << reward << ", cost=" << cost << endl;
            if (ratio > best_ratio) {
                if (budget - cost >= 0) {
                    best_ratio = ratio;
                    best_reward = reward;
                    best_cost = cost;

                    best_selected = i;
                }
            }
        }

//        cout << "selected=[" << best_selected << "], reward=" << best_reward << ", cost=" << best_cost << endl;
        if (best_selected == -1) {
            // Meaning that no aisle can be selected with current budget

            best_ratio = -1.0;
            best_selected = -1;
            best_reward = -1;
//            int min_cost = 100*(2*(l-1)*n + 2*(n-1));

            for (int i = 0; i < m; i++) {
                int reward = aisles[i];
                int cost = 2*(max(i-i_max, 0)) + (2*(l-1)*n + 2*(n-1));
                double ratio = static_cast<double>(reward) / cost;
//                cout << "ratio=[" << ratio << "], reward=" << reward << ", cost=" << cost << endl;
                if (ratio > best_ratio) {
//                    if (cost < min_cost) {
                    best_ratio = ratio;
                    best_reward = reward;
//                        min_cost = cost;

                    best_selected = i;
//                    }
                }
            }

            budget -= 2*(max(best_selected-i_max, 0));
            int budget_primo = (budget)/2 + 1;
            int t = budget_primo / l;
            int l_primo = budget_primo % l;
//            cout << "selected=[" << best_selected << "], reward=" << best_reward << ", cost=" << best_cost << endl;
            for (int j = 0; j < t; j++){
                for (int node : orchard[best_selected][j]) {
                    sol_reward += node;
                }
            }

            for(int k = 0; k < l_primo; k++) {
                sol_reward += orchard[best_selected][t][k];
            }
            sol_cost += 2*(max(best_selected-i_max, 0)) + (budget_primo - 1) * 2;
            break;
        }

        sol_reward += best_reward;
        sol_cost += best_cost;
        i_max = max(best_selected, i_max);
        budget -= best_cost;

        // Needed, otherwise the algorithm will consider it again
        aisles[best_selected] = 0;
    }

    return make_tuple(sol_reward, sol_cost);
}
