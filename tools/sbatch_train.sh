#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --time=$5:00:00
#SBATCH --mem-per-cpu=8G
#SBATCH --tmp=50000                        # per node!!
#SBATCH --job-name=$3
#SBATCH --output=$3.out
#SBATCH --gpus=$2
#SBATCH --gres=gpumem:10G

CONFIG=$1
GPUS=$2
NAME=$3
TIME=$4
WORKDIR=$5

tools/dist_train.sh $CONFIG $GPUS --work-dir $WORKDIR