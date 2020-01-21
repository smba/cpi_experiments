import subprocess
import os
import sys
import time 
import statistics as stat


print("es flutet")

PROJECT = sys.argv[1]
REPETITIONS = int(sys.argv[2])
TIMEOUT = int(sys.argv[3])
ARRAY_ID = int(sys.argv[4])


# gehe zu tmp
os.chdir("/home/stefan/")

#os.system("rm -rf *")

if not "case_studies" in os.listdir("."):
	print("hier flutet es auch")
	os.system("git clone https://github.com/smba/cpi_experiments.git case_studies")
#print(os.listdir("."))
#print(os.getcwd())

print("jojojojojo")

# Obtain binaries
os.chdir("/home/stefan/case_studies")
os.system("git pull")

# get access to  binaries
os.chdir("{}".format(PROJECT))

print("flut flut mothafluters")

pwd = os.getcwd()
BINARIES = os.listdir(".")
BINARIES_ABSOLUTE = [pwd + "/" + binary for binary in BINARIES]
os.chdir("..")

# obtain config
configs = open("{}_configs.txt".format(PROJECT), "r").readlines()
config = configs[ARRAY_ID].replace("\n", "")
config_tail = config.split(" ")

fname = "perf_{}_{}.csv".format(PROJECT, ARRAY_ID)
os.system("rm -rf {}".format(fname))

for j, binary in enumerate(BINARIES):
	rev_index = int(binary.split("_")[0]) # revision id
	print("hier")	
	durations = []
	for i in range(REPETITIONS): 
		time.sleep(2)
		start = time.time()
		#print("timeout {} ./{}".format(TIMEOUT, BINARIES_ABSOLUTE[j]) + " ".join(config_tail))
		try:
			subprocess.run([
				"timeout", 
				"%d" % TIMEOUT, 
				".{}".format(BINARIES_ABSOLUTE[j])] + config_tail, check=True)
		except:
			time.sleep(3)

		end=time.time()
		duration = end - start
		durations.append(duration)
	   
	print(durations)
	median = stat.median(durations)
	
	#fname = "perf_{}_{}.csv".format(PROJECT, ARRAY_ID)
	f = open(fname, "a+")
	f.write("{},{}\n".format(rev_index, median))
	f.close()

os.system("cp {} /media/raid/stefan/case_studies/results/{}/{}".format(fname. PROJECT, fname))

