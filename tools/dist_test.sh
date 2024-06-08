#!/usr/bin/env bash
# Copyright (c) OpenMMLab. All rights reserved.

# Check if the correct number of arguments is provided
if [ "$#" -lt 3 ]; then
    echo "Usage: $0 <config> <checkpoint> <gpus> [extra_args...]"
    exit 1
fi

CONFIG=$1
CHECKPOINT=$2
GPUS=$3
NNODES=${NNODES:-1}
NODE_RANK=${NODE_RANK:-0}
PORT=${PORT:-29500}
MASTER_ADDR=${MASTER_ADDR:-"127.0.0.1"}

# Debugging outputs
echo "CONFIG: $CONFIG"
echo "CHECKPOINT: $CHECKPOINT"
echo "GPUS: $GPUS"
echo "NNODES: $NNODES"
echo "NODE_RANK: $NODE_RANK"
echo "PORT: $PORT"
echo "MASTER_ADDR: $MASTER_ADDR"
echo "PYTHONPATH: $(dirname $0)/..:$PYTHONPATH"

PYTHONPATH="$(dirname $0)/..":$PYTHONPATH \

torchrun \
    --nnodes=$NNODES \
    --node_rank=$NODE_RANK \
    --nproc_per_node=$GPUS \
    --rdzv_backend=c10d \
    --rdzv_endpoint=$MASTER_ADDR:$PORT \
    $(dirname "$0")/test.py \
    $CONFIG \
    $CHECKPOINT \
    --launcher pytorch \
    ${@:4}
