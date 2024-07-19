#!/usr/bin/env bash

set -x

PARTITION=$1
JOB_NAME=$2
CONFIG=$3
WORK_DIR=$4

#SBATCH --job-name=human_pose_job        # Job name
#SBATCH --nodes=1                        # Number of nodes
#SBATCH --ntasks=2                       # Total number of tasks (processes)
#SBATCH --cpus-per-task=4                # Number of CPU cores per task
#SBATCH --gres=gpu:2                     # Number of GPUs per node
#SBATCH --time=7-00:00:00                # Wall time limit (D-HH:MM:SS)

# Set up environment variables
MASTER_ADDR=${MASTER_ADDR:-"127.0.0.1"}
MASTER_PORT=12355
WORLD_SIZE=$SLURM_NTASKS

# Print out the configuration for debugging
echo "MASTER_ADDR=$MASTER_ADDR"
echo "MASTER_PORT=$MASTER_PORT"
echo "WORLD_SIZE=$WORLD_SIZE"

# Run the training script for each task
srun --mpi=pmi2 bash -c '
export RANK=$SLURM_PROCID
export WORLD_SIZE=$SLURM_NTASKS
export MASTER_ADDR='"$MASTER_ADDR"'
export MASTER_PORT='"$MASTER_PORT"'
export PYTHONPATH="$(dirname $0)/..":$PYTHONPATH

echo "Starting training on rank $RANK/$WORLD_SIZE"
python tools/train_no_freeze.py --work-dir '"${WORK_DIR}"' '"${CONFIG}"' --launcher slurm --local_rank=$SLURM_LOCALID
'
