#!/usr/bin/env bash

CONFIG=$1
GPUS=$2
NAME=$3
WORKDIR=$4

#SBATCH --job-name=human_pose_job         # Job name
#SBATCH --account=rl              # Account name
#SBATCH --nodes=1                 # Number of nodes
#SBATCH --ntasks-per-node=1       # Number of tasks per node
#SBATCH --cpus-per-task=4         # Number of CPU cores per task
#SBATCH --gres=gpu:$GPUS              # Number of GPUs per node
#SBATCH --time=24:00:00           # Wall time limit (D-HH:MM:SS)
#SBATCH --output=logs/output_%j.log    # Standard output and error log
#SBATCH --error=logs/error_%j.log      # Error log
 





tools/dist_train.sh $CONFIG $GPUS --work-dir $WORKDIR