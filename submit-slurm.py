import os
import argparse
import time 
import itertools
import subprocess
import sys

# parse
PROJECT = sys.argv[1]
REPETITIONS = int(sys.argv[2])
TIMEOUT = int(sys.argv[3])
PARTITION = sys.argv[4]

# get configurations
configs = open("{}_configs.txt".format(PROJECT), "r").readlines()
configs = list(map(lambda s: s.replace("\n", ""), configs))

# sync benchmark

# construct tasks
n_tasks = len(configs - 1)

# submit tasks
# sbatch 
print("I'm about to submit %d tasks." % n_tasks)

subprocess.run([
	"sbatch", 
	"--array=0-%d" % n_tasks, 
	"--partition=%s" % PARTITION,
	"--job-name=%s" % PROJECT,
	"local-slurm.sh",
	PROJECT,
	str(REPETITIONS),
	str(TIMEOUT)
])

