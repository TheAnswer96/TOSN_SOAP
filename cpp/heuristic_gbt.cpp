//
// Created by franc on 02/10/2022.
//

#include "heuristic_gbt.h"

tuple<int, int> gbt_algorithm(orchard3D orchard, int budget) {
    int sol_reward = 0;
    int sol_cost = 0;

    int m = orchard.size();
    int n = orchard[0].size();
    int l = orchard[0][0].size();

    int i_max = 0;
    vector<int> j_max(m);

    vector<vector<int>> trees(m, vector<int>(n));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int sum = 0;
            for (int k = 0; k < l; k++) {
                sum += orchard[i][j][k];
            }
            trees[i][j] = sum;
        }
    }

    while (budget > 0) {
        double best_ratio = -1.0;
        vector<int> best_selected(2);
        best_selected = {-1, -1};
        int best_reward = -1;
        int best_cost = -1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int reward = trees[i][j];
                int cost = 2 * (max(i - i_max, 0) + max(j-j_max[i], 0)) + (2*(l-1));
                double ratio = static_cast<double>(reward) / cost;
//                cout << "ratio=[" << ratio << "], reward=" << reward << ", cost=" << cost << endl;
                if (ratio > best_ratio) {
                    if (budget - cost >= 0) {
                        best_ratio = ratio;
                        best_reward = reward;
                        best_cost = cost;

                        best_selected = {i, j};
                    }
                }
            }
        }

//        cout << "  selected=[" << best_selected[0] << "," << best_selected[1] << "], reward=" << best_reward << ", cost=" << best_cost << ", res_budget=" << budget << endl;
        if (best_selected[0] == -1) {
            // Meaning that no tree can be selected with current budget

            best_ratio = -1.0;
            best_selected = {-1, -1};
            best_reward = -1;
//            int min_cost = l*2;

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    int reward = trees[i][j];
                    int cost = 2 * (max(i - i_max, 0) + max(j - j_max[i], 0)) + (2 * (l - 1));
                    double ratio = static_cast<double>(reward) / cost;
//                    cout << "ratio=[" << ratio << "], reward=" << reward << ", cost=" << cost << endl;
                    if (ratio > best_ratio) {
//                        if (cost < min_cost) {
                        best_ratio = ratio;
                        best_reward = reward;
//                            min_cost = cost;

                        best_selected = {i, j};
                    }
//                    }
                }
            }

//            cout << "  agument selected=[" << best_selected[0] << "," << best_selected[1] << "], reward=" << best_reward << ", cost=" << best_cost << ", res_budget=" << budget << endl;
            budget -= 2 * (max(best_selected[0] - i_max, 0) + max(best_selected[1]-j_max[best_selected[0]], 0));
            int budget_primo = (budget) / 2 + 1;
            for (int k=0; k < budget_primo; k++) {
                sol_reward += orchard[best_selected[0]][best_selected[1]][k];
            }
//            cout << budget_primo << endl;
//            cout << "selected=[" << best_selected_partial[0] << "," << best_selected_partial[1] << "]" << endl;
            sol_cost+= 2 * (max(best_selected[0] - i_max, 0) + max(best_selected[1]-j_max[best_selected[0]], 0)) + (budget_primo - 1) * 2;

            break;
        }

        sol_reward += best_reward;
        sol_cost += best_cost;
        i_max = max(best_selected[0], i_max);
        j_max[best_selected[0]] = max(best_selected[1],j_max[best_selected[0]]);
        budget -= best_cost;

        // Needed, otherwise the algorithm will consider it again
        trees[best_selected[0]][best_selected[1]] = 0;
//        cout << "    residual budget=" << budget << ", current total reward=" << sol_reward << endl;
    }

    return make_tuple(sol_reward, sol_cost);
}
