#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --account=rl
#SBATCH --cpus-per-task=4
#SBATCH -t 6:00:00
#SBATCH --mem-per-cpu=8G
#SBATCH --job-name=$3
#SBATCH --output=$3.out
#SBATCH --gres=gpu:$2  




CONFIG=$1
GPUS=$2
NAME=$3
WORKDIR=$4

tools/dist_train.sh $CONFIG $GPUS --work-dir $WORKDIR