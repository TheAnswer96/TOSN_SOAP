//
// Created by franc on 02/10/2022.
//

#include "approximation_alg2.h"
#include "optimal_alg.h"

tuple<int, int> apx_algorithm2(orchard3D orchard, int budget) {
    int sol_reward = 0;
    int sol_cost = 0;

    int m = orchard.size();
    int n = orchard[0].size();
    int l = orchard[0][0].size();
    int max_budget_aisle =  2*(l-1)*n + 2*(n-1);
    int nR = budget/2;
    int aisle_max = 0;
    set<int> aisles;

    aisle2D opt_aisles(m, vector<int>(nR+1));
    for (int i = 0; i < m; i++) {
        // compute optimum for each aisle
        aisles.insert(i);
        opt_aisles[i] = opt_single_aisle(orchard[i], max_budget_aisle, n, l);
    }

    while (nR > 0){
        double best_ratio = -1.0;
        int best_selected = 0;
        int best_reward = -1;
        int best_cost = 0;
        for (int aisle : aisles) {
            int reward = 0;
            int cost = 0;
            double ratio = 0.0;
            if ((nR - max(aisle - aisle_max, 0)) >= (max_budget_aisle / 2)) {
                reward = opt_aisles[aisle][max_budget_aisle / 2];
                cost = (max_budget_aisle / 2) + max(aisle - aisle_max, 0);
                ratio = static_cast<double>(reward) / cost;
//                cout << "selected=[" << aisle << "], ratio=" << ratio << ", cost=" << cost*2 << ", reward=" << reward << endl;
//                cout << "BIG" <<endl;
            } else {
                reward = opt_aisles[aisle][max_budget_aisle / 2];
                cost = (max_budget_aisle / 2) + max(aisle - aisle_max, 0);
                ratio = static_cast<double>(reward) / cost;
//                cout << "was selected=[" << aisle << "], ratio=" << ratio << ", cost=" << cost*2 << ", reward=" << reward << endl;
                if (nR - max(aisle - aisle_max, 0) >= 0){
                    reward = opt_aisles[aisle][nR - max(aisle - aisle_max, 0)];
//                    cout << (nR - max(aisle - aisle_max, 0))*2 << endl;
                    cost = nR;
                    ratio = static_cast<double>(reward) / cost;
//                   cout << "frac selected=[" << aisle << "], ratio=" << ratio << ", cost=" << cost*2 << ", reward=" << reward << endl;
                }
//                cout << "LITTLE" <<endl;
            }
//            cout << "aisle: " << aisle <<" ratio: " << ratio << " reward: "<< reward << " cost: " << cost << " nR: "<< nR <<  endl;
            if (best_ratio < ratio && nR - cost >= 0) {
                best_ratio = ratio;
                best_reward = reward;
                best_selected = aisle;
                best_cost = cost;
            }
        }
        sol_reward = sol_reward + best_reward;
        nR = nR - best_cost;
        sol_cost = sol_cost + (best_cost * 2);
        aisles.erase(best_selected);
        if(aisles.empty())
            break;
        aisle_max = max(aisle_max, best_selected);
//        cout << "nR: " << nR << " cost: " << sol_cost << " reward: " << sol_reward << " aisle: " << best_selected << endl;
    }

    return make_tuple(sol_reward, sol_cost);
}
