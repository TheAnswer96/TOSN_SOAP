##################IMPORT#######################
import numpy as np
import random
import scipy.stats as stats
import pickle
import algorithms


##################FUNCTIONS####################
def print_aisle(a_reward, a_cost, check_0_rewards=False):
    print('- TEST GRAPH CREATION:\n\n')
    rows = len(a_reward)
    cols = len(a_reward[0])
    trees = len(a_reward[0][0])
    print('-- AISLE PROPERTIES: \n')
    print('--- rows: ', rows)
    print('--- columns: ', cols)
    print('--- tree observable point: ', trees, '\n')
    for r in range(rows):
        print("---- r: ", r)
        for c in range(cols):
            print("----- c: ", c)
            for t in range(trees):
                print("------ t: ", t, " cost: ", a_cost[r][c][t], " reward: ", a_reward[r][c][t])
    if (check_0_rewards):
        print('\n- CHECK 0 REWARDs \n')
        for r in range(rows):
            for c in range(cols):
                print("-- r: ", r, " c: ", c, " reward: ", a_reward[r][c][0])


def generate_aisle(rows, columns, trees):
    random.seed(1)
    np.random.seed(1)

    a_reward = []
    a_cost = []

    for r in range(rows):
        col_r = []
        col_c = []
        for c in range(columns):
            cumulative = 0
            tree_r = [cumulative]
            tree_c = [2]
            for t in range(trees):
                rnd_value = random.randint(1, 9)
                cumulative = rnd_value
                tree_r.append(cumulative)
                tree_c.append(2)
            col_r.append(tree_r)
            col_c.append(tree_c)
        a_reward.append(col_r)
        a_cost.append(col_c)
    a_cost[0][0][0] = 0
    return a_reward, a_cost


def generate_WT1_random_zipf():
    thetas = [2.0]
    rows = [25, 50]
    columns = [50, 25]
    observables = [3, 5]
    hmfi = 33

    rewards = 100
    x = np.arange(1, rewards + 1)
    inputs = []
    for i in range(len(thetas)):
        prob = x ** (-thetas[i])
        prob = prob / prob.sum()
        bounded_zipf = stats.rv_discrete(name='bounded_zipf', values=(x, prob))
        for tree in observables:
            for j in range(len(thetas)):
                wp = []
                for iteration in range(hmfi):
                    matrix = []
                    for r in range(rows[j]):
                        row = []
                        for c in range(columns[j]):
                            s = bounded_zipf.rvs(size=tree)
                            row.append([0] + list(s))
                        matrix.append(row)
                    wp.append(matrix)
                    print(wp)
                string = "dump/w1/wt" + str(i) + "_r" + str(rows[j]) + "_c" + str(columns[j]) + "_th" + str(
                    thetas[i]) + "_o" + str(tree) + "inputs.txt"
                with open(string, 'wb') as f:
                    pickle.dump(wp, f)
    return


def wt2csv(wt=1):
    if wt == 1:
        thetas = [0, 0.8,2.0]
        rows = [50, 25]
        columns = [25, 50]
        observables = [3, 5]

        for theta in thetas:
            for i in range(len(rows)):
                for t in range(len(observables)):
                    string = "dump/w1/wt_r" + str(rows[i]) + "_c" + str(columns[i]) + "_th" + str(theta) + "_o" + str(
                        observables[t]) + "input.txt"
                    with open(string, 'rb') as f:
                        inputs = pickle.load(f)
                    for k in range(len(inputs)):
                        algorithms.orchard2csv(inputs[k], theta, k)
    if wt == 2:
        start = 1110
        end = 1120

        for index in range(start, end):
            string = "dump/w2/dump" + str(index) + "inputs.txt"
            with open(string, 'rb') as f:
                G = pickle.load(f)
            rows = len(G)
            columns = len(G[0])
            observables = len(G[0][0])
            for i in range(rows):
                for j in range(columns):
                    for k in range(observables):
                        G[i][j][k] = G[i][j][k] * 100
            algorithms.orchard2csv(G, 0, index)

    if wt == 3:
        # index 0 carpi
        # inde 1 carpi inverted
        file = ["dump_carpi.txt", "dump_carpi_inverted.txt"]
        for index in range(len(file)):
            string = "dump/w3/"+file[index]
            with open(string, 'rb') as f:
                G = pickle.load(f)
            rows = len(G)
            columns = len(G[0])
            observables = len(G[0][0])
            algorithms.orchard2csv(G, rows, columns, observables, 0, index)
    return
