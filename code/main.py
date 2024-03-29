##################IMPORT#######################
import aisle
import algorithms
import time
import test
import pickle

##################HYPER########################
m = 3  # NO. rows
n = 4  # NO. columns
t = 3  # NO. tree positions
B = 21
debug = False
##################MAIN#########################
if __name__ == '__main__':

	# inputs = aisle.generate_WT1_random_zipf()
	#start = time.time()
	# test.wt1_random_test_gap()
	#test.w1_reward_time()
	#test.w2_reward_time()
	test.w3_reward_time()
	#algorithms.orchard2csv(r)
	#algorithms.opt_big_aisle_dynamic_programming(r, B, True)
	#end = time.time()
	#print("time ", end - start)

	#aisle.wt2csv(2)
	# algorithms.apx_ccp(r, B, False)
	# algorithms.opt_ccp(r, B, False)
