#!/bin/bash

id=$SLURM_ARRAY_TASK_ID
python3 local-slurm.py $1 $2 $3 $id

