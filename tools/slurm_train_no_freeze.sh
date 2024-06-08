#!/usr/bin/env bash
# Copyright (c) OpenMMLab. All rights reserved.

set -x

PARTITION=$1
JOB_NAME=$2
CONFIG=$3
WORK_DIR=$4

#SBATCH --job-name=human_pose_job         # Job name
#SBATCH --nodes=1                 # Number of nodes
#SBATCH --ntasks-per-node=1       # Number of tasks per node
#SBATCH --cpus-per-task=4         # Number of CPU cores per task
#SBATCH --gres=gpu:1             # Number of GPUs per node
#SBATCH --time=7-00:00:00           # Wall time limit (D-HH:MM:SS)



PYTHONPATH="$(dirname $0)/..":$PYTHONPATH \

python tools/train_no_freeze.py --work-dir ${WORK_DIR} ${CONFIG} 

    
