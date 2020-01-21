import subprocess
import os
import sys

print("es flutet")

PROJECT = sys.argv[1]
REPETITIONS = int(sys.argv[2])
TIMEOUT = int(sys.argv[3])
ARRAY_ID = int(sys.argv[4])

# gehe zu tmp
os.chdir("/home/stefan/")
if not os.path.exists("./case_studies"):
	os.system("git clone https://github.com/smba/cpi.git /home/stefan/case_studies")
print(os.listdir("."))
print(os.getcwd())

# Obtain binaries
os.chdir("case_studies/%s" % PROJECT)
os.system("git pull")


#pwd = os.getcwd()
BINARIES = os.listdir(".")
BINARIES_ABSOLUTE = [pwd + "/" + binary for binary in BINARIES]
os.chdir("../..")

# obtain config
configs = open("{}_configs.txt".format(PROJECT), "r").readlines()
config = configs[ARRAY_ID].replace("\n", "")
config_tail = config.split(" ")

for j, binary in enumerate(BINARIES):
	rev_index = int(binary.split("_")[0]) # revision id
	
	for i in range(REPETITIONS): 
		time.sleep(2)
		start = time.time()
		try:
			subprocess.run([
				"timeout", 
				"%d" % TIMEOUT, 
				".{}".format(BINARIES_ABSOLUTE[i])] + config_tail, check=True)
		except:
			time.sleep(5)
			
		end=time.time()
		duration = end - start
		durations.append(duration)
	   
	median = stat.median(durations)
	fname = "perf_{}_{}.csv".format(PROJECT, ARRAY_ID)
	f = open(fname, "a+")
	f.write("{},{}\n".format(rev_index, median))
	f.close()

os.system("cp {} /media/raid/stefan/case_studies/results/{}/{}".format(fname. PROJECT, fname))

