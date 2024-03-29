##################IMPORT#######################
import numpy as np
import pickle
import aisle
import algorithms
import time
import pandas as pd
import statistics


##################FUNCTIONS####################
def w1_reward_time():
    budgets = [0.05, 0.1, 0.15, 0.2, 0.4, 0.6, 0.8]
    thetas = [0, 0.8, 2.0]
    rows = [50, 25]
    columns = [25, 50]
    obs = [4, 6]
    sequences = 33

    print("w1 starting...")
    for theta in thetas:
        print("iteration with theta equals to ", theta)
        for i in range(len(rows)):
            print("orchard dimensions: ", rows[i], " x ", columns[i])
            for t in range(len(obs)):
                print("tree lenght: ", obs[t])
                df = pd.DataFrame()
                maxB = 2 * (rows[i] * (columns[i] - 1)) + 2 * (rows[i] - 1) + rows[i] * columns[i] * 2 * (obs[t]-1)
                #opt apx apx2
                total_rw_opt = []
                total_tm_opt = []
                total_rw_apx = []
                total_tm_apx = []
                total_rw_apx2 = []
                total_tm_apx2 = []
                total_rw_opt_std = []
                total_tm_opt_std = []
                total_rw_apx_std = []
                total_tm_apx_std = []
                total_rw_apx2_std = []
                total_tm_apx2_std = []
                total_ratio_rw_opt = []
                total_ratio_tm_opt = []
                total_ratio_rw_apx = []
                total_ratio_tm_apx = []
                total_ratio_rw_apx2 = []
                total_ratio_tm_apx2 = []
                total_ratio_rw_opt_std = []
                total_ratio_tm_opt_std = []
                total_ratio_rw_apx_std = []
                total_ratio_tm_apx_std = []
                total_ratio_rw_apx2_std = []
                total_ratio_tm_apx2_std = []
                #gba gbt
                total_rw_gba = []
                total_tm_gba = []
                total_rw_gbt = []
                total_tm_gbt = []
                total_rw_gba_std = []
                total_tm_gba_std = []
                total_rw_gbt_std = []
                total_tm_gbt_std = []

                total_ratio_rw_gba = []
                total_ratio_tm_gba = []
                total_ratio_rw_gbt = []
                total_ratio_tm_gbt = []
                total_ratio_rw_gba_std = []
                total_ratio_tm_gba_std = []
                total_ratio_rw_gbt_std = []
                total_ratio_tm_gbt_std = []

                for perc in budgets:
                    print("budget: ", perc * 100, "%")
                    opt_r = []
                    apx_r = []
                    apx2_r = []
                    opt_t = []
                    apx_t = []
                    apx2_t = []
                    opt_r_r = []
                    apx_r_r = []
                    apx2_r_r = []
                    opt_t_r = []
                    apx_t_r = []
                    apx2_t_r = []

                    gba_r = []
                    gbt_r = []
                    gba_t = []
                    gbt_t = []
                    gba_r_r = []
                    gbt_r_r = []
                    gba_t_r = []
                    gbt_t_r = []
                    for s in range(sequences):
                        print("#istance: ", s)
                        string = "orchards/wt1/o_m" + str(rows[i]) + "_n" + str(columns[i]) + "_l" + str(
                            obs[t]) + "_t" + str(
                            theta) + "_s" + str(s)
                        reward_opt, cost_opt, time_opt = algorithms.opt_cpp(int(maxB * perc) + 1, string)
                        reward_apx, cost_apx, time_apx = algorithms.apx_cpp(int(maxB * perc) + 1, string)
                        reward_apx2, cost_apx2, time_apx2 = algorithms.apx2_cpp(int(maxB * perc) + 1, string)
                        reward_gba, cost_gba, time_gba = algorithms.heu_gba(int(maxB * perc) + 1, string)
                        reward_gbt, cost_gbt, time_gbt = algorithms.heu_gbt(int(maxB * perc) + 1, string)
                        if reward_opt < reward_apx or reward_opt < reward_gbt or reward_opt < reward_gba or reward_opt < reward_apx2:
                            input()
                        opt_t.append(time_opt)
                        opt_r.append(reward_opt)
                        apx_t.append(time_apx)
                        apx_r.append(reward_apx)
                        apx2_t.append(time_apx2)
                        apx2_r.append(reward_apx2)

                        opt_t_r.append(1)
                        opt_r_r.append(1)
                        apx_t_r.append(time_opt / time_apx)
                        apx_r_r.append(reward_apx / reward_opt)
                        apx2_t_r.append(time_opt / time_apx2)
                        apx2_r_r.append(reward_apx2 / reward_opt)

                        gba_t.append(time_gba)
                        gba_r.append(reward_gba)
                        gbt_t.append(time_gbt)
                        gbt_r.append(reward_gbt)

                        gba_t_r.append(time_opt / time_gba)
                        gba_r_r.append(reward_gba / reward_opt)
                        gbt_t_r.append(time_opt / time_gbt)
                        gbt_r_r.append(reward_gbt / reward_opt)
                    #opt apx
                    total_tm_opt.append(statistics.mean(opt_t))
                    total_rw_opt.append(statistics.mean(opt_r))
                    total_tm_apx.append(statistics.mean(apx_t))
                    total_rw_apx.append(statistics.mean(apx_r))
                    total_tm_apx2.append(statistics.mean(apx2_t))
                    total_rw_apx2.append(statistics.mean(apx2_r))
                    total_tm_opt_std.append(statistics.stdev(opt_t))
                    total_rw_opt_std.append(statistics.stdev(opt_r))
                    total_tm_apx_std.append(statistics.stdev(apx_t))
                    total_rw_apx_std.append(statistics.stdev(apx_r))
                    total_tm_apx2_std.append(statistics.stdev(apx2_t))
                    total_rw_apx2_std.append(statistics.stdev(apx2_r))

                    total_ratio_tm_opt.append(statistics.mean(opt_t_r))
                    total_ratio_rw_opt.append(statistics.mean(opt_r_r))
                    total_ratio_tm_apx.append(statistics.mean(apx_t_r))
                    total_ratio_rw_apx.append(statistics.mean(apx_r_r))
                    total_ratio_tm_apx2.append(statistics.mean(apx2_t_r))
                    total_ratio_rw_apx2.append(statistics.mean(apx2_r_r))
                    total_ratio_tm_opt_std.append(statistics.stdev(opt_t_r))
                    total_ratio_rw_opt_std.append(statistics.stdev(opt_r_r))
                    total_ratio_tm_apx_std.append(statistics.stdev(apx_t_r))
                    total_ratio_rw_apx_std.append(statistics.stdev(apx_r_r))
                    total_ratio_tm_apx2_std.append(statistics.stdev(apx2_t_r))
                    total_ratio_rw_apx2_std.append(statistics.stdev(apx2_r_r))
                    #gba gbt
                    total_tm_gba.append(statistics.mean(gba_t))
                    total_rw_gba.append(statistics.mean(gba_r))
                    total_tm_gbt.append(statistics.mean(gbt_t))
                    total_rw_gbt.append(statistics.mean(gbt_r))
                    total_tm_gba_std.append(statistics.stdev(gba_t))
                    total_rw_gba_std.append(statistics.stdev(gba_r))
                    total_tm_gbt_std.append(statistics.stdev(gbt_t))
                    total_rw_gbt_std.append(statistics.stdev(gbt_r))

                    total_ratio_tm_gba.append(statistics.mean(gba_t_r))
                    total_ratio_rw_gba.append(statistics.mean(gba_r_r))
                    total_ratio_tm_gbt.append(statistics.mean(gbt_t_r))
                    total_ratio_rw_gbt.append(statistics.mean(gbt_r_r))
                    total_ratio_tm_gba_std.append(statistics.stdev(gba_t_r))
                    total_ratio_rw_gba_std.append(statistics.stdev(gba_r_r))
                    total_ratio_tm_gbt_std.append(statistics.stdev(gbt_t_r))
                    total_ratio_rw_gbt_std.append(statistics.stdev(gbt_r_r))
                #opt apx
                df['opt_reward'] = total_rw_opt
                df['opt_time'] = total_tm_opt
                df['opt_reward_std'] = total_rw_opt_std
                df['opt_time_std'] = total_tm_opt_std
                df['apx_reward'] = total_rw_apx
                df['apx_time'] = total_tm_apx
                df['apx_reward_std'] = total_rw_apx_std
                df['apx_time_std'] = total_tm_apx_std
                df['apx2_reward'] = total_rw_apx2
                df['apx2_time'] = total_tm_apx2
                df['apx2_reward_std'] = total_rw_apx2_std
                df['apx2_time_std'] = total_tm_apx2_std

                df['opt_ratio_reward'] = total_ratio_rw_opt
                df['opt_ratio_time'] = total_ratio_tm_opt
                df['opt_ratio_reward_std'] = total_ratio_rw_opt_std
                df['opt_ratio_time_std'] = total_ratio_tm_opt_std
                df['apx_ratio_reward'] = total_ratio_rw_apx
                df['apx_ratio_time'] = total_ratio_tm_apx
                df['apx_ratio_reward_std'] = total_ratio_rw_apx_std
                df['apx_ratio_time_std'] = total_ratio_tm_apx_std
                df['apx2_ratio_reward'] = total_ratio_rw_apx2
                df['apx2_ratio_time'] = total_ratio_tm_apx2
                df['apx2_ratio_reward_std'] = total_ratio_rw_apx2_std
                df['apx2_ratio_time_std'] = total_ratio_tm_apx2_std
                #gba gbt
                df['gba_reward'] = total_rw_gba
                df['gba_time'] = total_tm_gba
                df['gba_reward_std'] = total_rw_gba_std
                df['gba_time_std'] = total_tm_gba_std
                df['gbt_reward'] = total_rw_gbt
                df['gbt_time'] = total_tm_gbt
                df['gbt_reward_std'] = total_rw_gbt_std
                df['gbt_time_std'] = total_tm_gbt_std

                df['gba_ratio_reward'] = total_ratio_rw_gba
                df['gba_ratio_time'] = total_ratio_tm_gba
                df['gba_ratio_reward_std'] = total_ratio_rw_gba_std
                df['gba_ratio_time_std'] = total_ratio_tm_gba_std
                df['gbt_ratio_reward'] = total_ratio_rw_gbt
                df['gbt_ratio_time'] = total_ratio_tm_gbt
                df['gbt_ratio_reward_std'] = total_ratio_rw_gbt_std
                df['gbt_ratio_time_std'] = total_ratio_tm_gbt_std
                df['percentage'] = [5, 10, 15, 20, 40, 60, 80]
                name = "result/w1/w1_m" + str(rows[i]) + "_n" + str(columns[i]) + "_l" + str(obs[t]) + "_t" + str(
                    theta) + ".csv"
                df.to_csv(name)
    return


def w2_reward_time():
    start = 1110
    end = 1120
    budgets = [0.05, 0.1, 0.15, 0.2, 0.4, 0.6, 0.8]
    # budgets = [0.05, 0.1, 0.15]
    maxB = 2 * (106 * (137 - 1)) + 2 * (106 - 1) + 106 * 137 * 2 * 3

    # opt apx apx2
    total_rw_opt = []
    total_tm_opt = []
    total_rw_apx = []
    total_tm_apx = []
    total_rw_apx2 = []
    total_tm_apx2 = []
    total_rw_opt_std = []
    total_tm_opt_std = []
    total_rw_apx_std = []
    total_tm_apx_std = []
    total_rw_apx2_std = []
    total_tm_apx2_std = []
    total_ratio_rw_opt = []
    total_ratio_tm_opt = []
    total_ratio_rw_apx = []
    total_ratio_tm_apx = []
    total_ratio_rw_apx2 = []
    total_ratio_tm_apx2 = []
    total_ratio_rw_opt_std = []
    total_ratio_tm_opt_std = []
    total_ratio_rw_apx_std = []
    total_ratio_tm_apx_std = []
    total_ratio_rw_apx2_std = []
    total_ratio_tm_apx2_std = []
    # gba gbt
    total_rw_gba = []
    total_tm_gba = []
    total_rw_gbt = []
    total_tm_gbt = []
    total_rw_gba_std = []
    total_tm_gba_std = []
    total_rw_gbt_std = []
    total_tm_gbt_std = []

    total_ratio_rw_gba = []
    total_ratio_tm_gba = []
    total_ratio_rw_gbt = []
    total_ratio_tm_gbt = []
    total_ratio_rw_gba_std = []
    total_ratio_tm_gba_std = []
    total_ratio_rw_gbt_std = []
    total_ratio_tm_gbt_std = []

    df = pd.DataFrame()
    print("w2 starting...")
    for perc in budgets:
        print("percentage of budget: ", perc * 100, "%")
        opt_r = []
        apx_r = []
        apx2_r = []
        opt_t = []
        apx_t = []
        apx2_t = []
        opt_r_r = []
        apx_r_r = []
        apx2_r_r = []
        opt_t_r = []
        apx_t_r = []
        apx2_t_r = []

        gba_r = []
        gbt_r = []
        gba_t = []
        gbt_t = []
        gba_r_r = []
        gbt_r_r = []
        gba_t_r = []
        gbt_t_r = []
        for index in range(start, end):
            print("#irrigation instance: ", index)
            string = "orchards/wt2/o_m106_n137_l4_t0_s" + str(index)
            reward_opt, cost_opt, time_opt = algorithms.opt_cpp(int(maxB * perc) + 1, string)
            reward_apx, cost_apx, time_apx = algorithms.apx_cpp(int(maxB * perc) + 1, string)
            reward_apx2, cost_apx2, time_apx2 = algorithms.apx2_cpp(int(maxB * perc) + 1, string)
            reward_gba, cost_gba, time_gba = algorithms.heu_gba(int(maxB * perc) + 1, string)
            reward_gbt, cost_gbt, time_gbt = algorithms.heu_gbt(int(maxB * perc) + 1, string)
            if reward_opt < reward_apx or reward_opt < reward_gbt or reward_opt < reward_gba or reward_opt < reward_apx2:
                input()
            opt_t.append(time_opt)
            opt_r.append(reward_opt)
            apx_t.append(time_apx)
            apx_r.append(reward_apx)
            apx2_t.append(time_apx2)
            apx2_r.append(reward_apx2)

            opt_t_r.append(1)
            opt_r_r.append(1)
            apx_t_r.append(time_opt / time_apx)
            apx_r_r.append(reward_apx / reward_opt)
            apx2_t_r.append(time_opt / time_apx2)
            apx2_r_r.append(reward_apx2 / reward_opt)

            gba_t.append(time_gba)
            gba_r.append(reward_gba)
            gbt_t.append(time_gbt)
            gbt_r.append(reward_gbt)

            gba_t_r.append(time_opt / time_gba)
            gba_r_r.append(reward_gba / reward_opt)
            gbt_t_r.append(time_opt / time_gbt)
            gbt_r_r.append(reward_gbt / reward_opt)
            # opt apx
        total_tm_opt.append(statistics.mean(opt_t))
        total_rw_opt.append(statistics.mean(opt_r))
        total_tm_apx.append(statistics.mean(apx_t))
        total_rw_apx.append(statistics.mean(apx_r))
        total_tm_apx2.append(statistics.mean(apx2_t))
        total_rw_apx2.append(statistics.mean(apx2_r))
        total_tm_opt_std.append(statistics.stdev(opt_t))
        total_rw_opt_std.append(statistics.stdev(opt_r))
        total_tm_apx_std.append(statistics.stdev(apx_t))
        total_rw_apx_std.append(statistics.stdev(apx_r))
        total_tm_apx2_std.append(statistics.stdev(apx2_t))
        total_rw_apx2_std.append(statistics.stdev(apx2_r))

        total_ratio_tm_opt.append(statistics.mean(opt_t_r))
        total_ratio_rw_opt.append(statistics.mean(opt_r_r))
        total_ratio_tm_apx.append(statistics.mean(apx_t_r))
        total_ratio_rw_apx.append(statistics.mean(apx_r_r))
        total_ratio_tm_apx2.append(statistics.mean(apx2_t_r))
        total_ratio_rw_apx2.append(statistics.mean(apx2_r_r))
        total_ratio_tm_opt_std.append(statistics.stdev(opt_t_r))
        total_ratio_rw_opt_std.append(statistics.stdev(opt_r_r))
        total_ratio_tm_apx_std.append(statistics.stdev(apx_t_r))
        total_ratio_rw_apx_std.append(statistics.stdev(apx_r_r))
        total_ratio_tm_apx2_std.append(statistics.stdev(apx2_t_r))
        total_ratio_rw_apx2_std.append(statistics.stdev(apx2_r_r))
        # gba gbt
        total_tm_gba.append(statistics.mean(gba_t))
        total_rw_gba.append(statistics.mean(gba_r))
        total_tm_gbt.append(statistics.mean(gbt_t))
        total_rw_gbt.append(statistics.mean(gbt_r))
        total_tm_gba_std.append(statistics.stdev(gba_t))
        total_rw_gba_std.append(statistics.stdev(gba_r))
        total_tm_gbt_std.append(statistics.stdev(gbt_t))
        total_rw_gbt_std.append(statistics.stdev(gbt_r))

        total_ratio_tm_gba.append(statistics.mean(gba_t_r))
        total_ratio_rw_gba.append(statistics.mean(gba_r_r))
        total_ratio_tm_gbt.append(statistics.mean(gbt_t_r))
        total_ratio_rw_gbt.append(statistics.mean(gbt_r_r))
        total_ratio_tm_gba_std.append(statistics.stdev(gba_t_r))
        total_ratio_rw_gba_std.append(statistics.stdev(gba_r_r))
        total_ratio_tm_gbt_std.append(statistics.stdev(gbt_t_r))
        total_ratio_rw_gbt_std.append(statistics.stdev(gbt_r_r))
    # opt apx
    df['opt_reward'] = total_rw_opt
    df['opt_time'] = total_tm_opt
    df['opt_reward_std'] = total_rw_opt_std
    df['opt_time_std'] = total_tm_opt_std
    df['apx_reward'] = total_rw_apx
    df['apx_time'] = total_tm_apx
    df['apx_reward_std'] = total_rw_apx_std
    df['apx_time_std'] = total_tm_apx_std
    df['apx2_reward'] = total_rw_apx2
    df['apx2_time'] = total_tm_apx2
    df['apx2_reward_std'] = total_rw_apx2_std
    df['apx2_time_std'] = total_tm_apx2_std

    df['opt_ratio_reward'] = total_ratio_rw_opt
    df['opt_ratio_time'] = total_ratio_tm_opt
    df['opt_ratio_reward_std'] = total_ratio_rw_opt_std
    df['opt_ratio_time_std'] = total_ratio_tm_opt_std
    df['apx_ratio_reward'] = total_ratio_rw_apx
    df['apx_ratio_time'] = total_ratio_tm_apx
    df['apx_ratio_reward_std'] = total_ratio_rw_apx_std
    df['apx_ratio_time_std'] = total_ratio_tm_apx_std
    df['apx2_ratio_reward'] = total_ratio_rw_apx2
    df['apx2_ratio_time'] = total_ratio_tm_apx2
    df['apx2_ratio_reward_std'] = total_ratio_rw_apx2_std
    df['apx2_ratio_time_std'] = total_ratio_tm_apx2_std
    # gba gbt
    df['gba_reward'] = total_rw_gba
    df['gba_time'] = total_tm_gba
    df['gba_reward_std'] = total_rw_gba_std
    df['gba_time_std'] = total_tm_gba_std
    df['gbt_reward'] = total_rw_gbt
    df['gbt_time'] = total_tm_gbt
    df['gbt_reward_std'] = total_rw_gbt_std
    df['gbt_time_std'] = total_tm_gbt_std

    df['gba_ratio_reward'] = total_ratio_rw_gba
    df['gba_ratio_time'] = total_ratio_tm_gba
    df['gba_ratio_reward_std'] = total_ratio_rw_gba_std
    df['gba_ratio_time_std'] = total_ratio_tm_gba_std
    df['gbt_ratio_reward'] = total_ratio_rw_gbt
    df['gbt_ratio_time'] = total_ratio_tm_gbt
    df['gbt_ratio_reward_std'] = total_ratio_rw_gbt_std
    df['gbt_ratio_time_std'] = total_ratio_tm_gbt_std
    df['percentage'] = [5, 10, 15, 20, 40, 60, 80]
    name = "result/w2/w2.csv"
    df.to_csv(name)
    return


def w3_reward_time():
    file = ["orchards/wt3/o_m11_n15_l4_t0_s0", "orchards/wt3/o_m11_n15_l4_t0_s1"]
    budgets = [0.05, 0.1, 0.15, 0.2, 0.4, 0.6, 0.8]
    maxB = 2 * (11 * (15 - 1)) + 2 * (11 - 1) + 11 * 15 * 2 * 3

    df = pd.DataFrame()
    print("w3 starting...")
    for string in file:
        print("#irrigation instance: ", string)
        opt_r = []
        apx_r = []
        apx2_r = []
        opt_t = []
        apx_t = []
        apx2_t = []
        opt_r_r = []
        apx_r_r = []
        apx2_r_r = []
        opt_t_r = []
        apx_t_r = []
        apx2_t_r = []

        gba_r = []
        gbt_r = []
        gba_t = []
        gbt_t = []
        gba_r_r = []
        gbt_r_r = []
        gba_t_r = []
        gbt_t_r = []
        for perc in budgets:
            print("percentage of budget: ", perc * 100, "%")
            reward_opt, cost_opt, time_opt = algorithms.opt_cpp(int(maxB * perc) + 1, string)
            reward_apx, cost_apx, time_apx = algorithms.apx_cpp(int(maxB * perc) + 1, string)
            reward_apx2, cost_apx2, time_apx2 = algorithms.apx2_cpp(int(maxB * perc) + 1, string)
            reward_gba, cost_gba, time_gba = algorithms.heu_gba(int(maxB * perc) + 1, string)
            reward_gbt, cost_gbt, time_gbt = algorithms.heu_gbt(int(maxB * perc) + 1, string)
            if reward_opt < reward_apx or reward_opt < reward_gbt or reward_opt < reward_gba or reward_opt < reward_apx2:
                input()
            opt_t.append(time_opt)
            opt_r.append(reward_opt)
            apx_t.append(time_apx)
            apx_r.append(reward_apx)
            apx2_t.append(time_apx2)
            apx2_r.append(reward_apx2)

            opt_t_r.append(1)
            opt_r_r.append(1)
            apx_t_r.append(time_opt / time_apx)
            apx_r_r.append(reward_apx / reward_opt)
            apx2_t_r.append(time_opt / time_apx2)
            apx2_r_r.append(reward_apx2 / reward_opt)

            gba_t.append(time_gba)
            gba_r.append(reward_gba)
            gbt_t.append(time_gbt)
            gbt_r.append(reward_gbt)

            gba_t_r.append(time_opt / time_gba)
            gba_r_r.append(reward_gba / reward_opt)
            gbt_t_r.append(time_opt / time_gbt)
            gbt_r_r.append(reward_gbt / reward_opt)

        df['opt_reward'] = opt_r
        df['opt_time'] = opt_t
        df['apx_reward'] = apx_r
        df['apx_time'] = apx_t
        df['apx2_reward'] = apx2_r
        df['apx2_time'] = apx2_t
        df['opt_ratio_reward'] = opt_r_r
        df['opt_ratio_time'] = opt_t_r
        df['apx_ratio_reward'] = apx_r_r
        df['apx_ratio_time'] = apx_t_r
        df['apx2_ratio_reward'] = apx2_r_r
        df['apx2_ratio_time'] = apx2_t_r

        # gba gbt
        df['gba_reward'] = gba_r
        df['gba_time'] = gba_t
        df['gbt_reward'] = gbt_r
        df['gbt_time'] = gbt_t


        df['gba_ratio_reward'] = gba_r_r
        df['gba_ratio_time'] = gba_t_r
        df['gbt_ratio_reward'] = gbt_r_r
        df['gbt_ratio_time'] = gbt_t_r
        df['percentage'] = [5, 10, 15, 20, 40, 60, 80]
        name = "result/w3/wt3_" + str(file.index(string)) + ".csv"
        df.to_csv(name)
    return
