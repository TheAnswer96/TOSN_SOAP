##################IMPORT#######################
import subprocess
import time
import numpy as np
import copy
import csv
from math import *
import pandas as pd
import csv


##################FUNCTIONS####################

def orchard2csv(orchard, theta=0, sequence=1):
    r = len(orchard)
    c = len(orchard[0])
    l = len(orchard[0][0])
    path = "orchards/o_m" + str(r) + "_n" + str(c) + "_l" + str(l) + "_t" + str(theta) + "_s" + str(sequence)
    full_csv = []
    for i in range(r):
        rows = []
        for j in range(c):
            #list2string = np.array2string(np.array(orchard[i][j]), precision=2, separator=',', suppress_small=True)
            #rows.append(list2string)
            rows.append(orchard[i][j])
        full_csv.append(rows)
    df = pd.DataFrame(full_csv)
    df.to_csv(path, index=False, header=False, quoting = csv.QUOTE_NONE, quotechar='', escapechar = ' ')
    return


def opt_cpp(B, file="test", debug=False):
    e_time = 0

    index_alg = 0
    if file == "test":
        input = "orchards/o_m3_n4_l4_t0_s1"
    else:
        input = file
    budget = B

    # c++ call
    start = time.time()
    cmd = "cpp.exe %d %s %d" % (index_alg, input, budget)
    output_sb = subprocess.check_output(cmd, shell=True)
    output_sb = str(output_sb).split("\\")[0]
    cost = float(output_sb.strip().split(", ")[1].split("=")[1].split("'")[0])
    reward = float(output_sb.strip().split(", ")[0].split("=")[1].split("'")[0])
    end = time.time()
    e_time = end - start
    print(cost, reward, e_time)

    return reward, cost, e_time


def apx_cpp(B, file="test", debug=False):
    # Convert r to csv
    e_time = 0

    index_alg = 1
    if file == "test":
        input = "orchards/o_m3_n4_l4_t0_s1"
    else:
        input = file
    budget = B

    # c++ call
    start = time.time()
    cmd = "cpp.exe %d %s %d" % (index_alg, input, budget)
    output_sb = subprocess.check_output(cmd, shell=True)
    output_sb = str(output_sb).split("\\")[0]
    cost = float(output_sb.strip().split(", ")[1].split("=")[1].split("'")[0])
    reward = float(output_sb.strip().split(", ")[0].split("=")[1].split("'")[0])
    end = time.time()
    e_time = end - start
    print(cost, reward, e_time)

    return reward, cost, e_time

def heu_gba(B, file="test", debug=False):
    # Convert r to csv
    e_time = 0

    index_alg = 3
    if file == "test":
        input = "orchards/o_m3_n4_l4_t0_s1"
    else:
        input = file
    budget = B

    # c++ call
    start = time.time()
    cmd = "cpp.exe %d %s %d" % (index_alg, input, budget)
    output_sb = subprocess.check_output(cmd, shell=True)
    output_sb = str(output_sb).split("\\")[0]
    cost = float(output_sb.strip().split(", ")[1].split("=")[1].split("'")[0])
    reward = float(output_sb.strip().split(", ")[0].split("=")[1].split("'")[0])
    end = time.time()
    e_time = end - start
    print(cost, reward, e_time)

    return reward, cost, e_time

def heu_gbt(B, file="test", debug=False):
    # Convert r to csv
    e_time = 0

    index_alg = 4
    if file == "test":
        input = "orchards/o_m3_n4_l4_t0_s1"
    else:
        input = file
    budget = B

    # c++ call
    start = time.time()
    cmd = "cpp.exe %d %s %d" % (index_alg, input, budget)
    output_sb = subprocess.check_output(cmd, shell=True)
    output_sb = str(output_sb).split("\\")[0]
    cost = float(output_sb.strip().split(", ")[1].split("=")[1].split("'")[0])
    reward = float(output_sb.strip().split(", ")[0].split("=")[1].split("'")[0])
    end = time.time()
    e_time = end - start
    print(cost, reward, e_time)

    return reward, cost, e_time

def apx2_cpp(B, file="test", debug=False):
    # Convert r to csv
    e_time = 0

    index_alg = 2
    if file == "test":
        input = "orchards/o_m3_n4_l4_t0_s1"
    else:
        input = file
    budget = B

    # c++ call
    start = time.time()
    cmd = "cpp.exe %d %s %d" % (index_alg, input, budget)
    output_sb = subprocess.check_output(cmd, shell=True)
    output_sb = str(output_sb).split("\\")[0]
    cost = float(output_sb.strip().split(", ")[1].split("=")[1].split("'")[0])
    reward = float(output_sb.strip().split(", ")[0].split("=")[1].split("'")[0])
    end = time.time()
    e_time = end - start
    print(cost, reward, e_time)

    return reward, cost, e_time