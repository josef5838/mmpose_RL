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
#SBATCH --time=7-24:00:00           # Wall time limit (D-HH:MM:SS)
#SBATCH --output=logs/output_%j.log    # Standard output and error log
#SBATCH --error=logs/error_%j.log      # Error log



PYTHONPATH="$(dirname $0)/..":$PYTHONPATH \

python tools/train.py --work-dir ${WORK_DIR} ${CONFIG} 
###${@:5} --job-name=${JOB_NAME} --gres=gpu:${GPUS_PER_NODE} ${SRUN_ARGS}
    
    
    #  \
    # --ntasks=${GPUS} \
    # --ntasks-per-node=${GPUS_PER_NODE} \
#    # --cpus-per-task=${CPUS_PER_TASK} \
    # --kill-on-bad-exit=1 \
    # ${SRUN_ARGS} \
    
