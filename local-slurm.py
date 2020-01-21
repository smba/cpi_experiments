import subprocess
import os
import sys
import time 
import statistics as stat

PROJECT = sys.argv[1]
REPETITIONS = int(sys.argv[2])
TIMEOUT = int(sys.argv[3])
ARRAY_ID = int(sys.argv[4])

HOME = "/home/stefan"
CHOME = "/media/raid/stefan"

# gehe zu tmp
os.chdir(HOME)

# mach ma sauber
os.system("rm -rf *")

if not "case_studies" in os.listdir("."):
	os.system("git clone https://github.com/smba/cpi_experiments.git case_studies")

# Obtain binaries
os.chdir(HOME + "/case_studies")
os.system("git pull")

# get access to  binaries
os.chdir("{}".format(PROJECT))

pwd = os.getcwd()
BINARIES = os.listdir(".")
BINARIES_ABSOLUTE = [pwd + "/" + binary for binary in BINARIES]
os.chdir("..")

# obtain configs
configs = open("{}_configs.txt".format(PROJECT), "r").readlines()
config = configs[ARRAY_ID].replace("\n", "")
config_tail = config.split(" ")

fname = "perf_{}_{}.csv".format(PROJECT, ARRAY_ID)
os.system("rm -rf {}".format(fname))

for j, binary in enumerate(BINARIES):
	rev_index = int(binary.split("_")[0]) # revision id
	durations = []
	for i in range(REPETITIONS): 
		time.sleep(2)
		start = time.time()
		try:
			subprocess.run([
				"timeout", 
				"%d" % TIMEOUT, 
				"{}".format(BINARIES_ABSOLUTE[j])] + config_tail, check=True)
		except:
			time.sleep(2)
			pass

		end=time.time()
		duration = end - start
		durations.append(duration)

	median = stat.median(durations)

	f = open(fname, "a+")
	f.write("{},{}\n".format(rev_index, median))
	f.close()

os.system("cp {} {}/case_studies/results/{}/{}".format(fname, CHOME, PROJECT, fname))

