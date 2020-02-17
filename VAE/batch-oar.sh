#!/bin/bash
#OAR -n VAE with CelebA
#OAR -t gpu
#OAR -l /nodes=1/gpudevice=1,walltime=01:00:00
#OAR --stdout _batch/VAE_CelebA_%jobid%.out
#OAR --stderr _batch/VAE_CelebA_%jobid%.err
#OAR --project fidle

#---- For cpu
# use :
# OAR -l /nodes=1/core=32,walltime=01:00:00
# and add a 2>/dev/null to ipython xxx

# -----------------------------------------------
#         _           _       _
#        | |__   __ _| |_ ___| |__
#        | '_ \ / _` | __/ __| '_ \
#        | |_) | (_| | || (__| | | |
#        |_.__/ \__,_|\__\___|_| |_|
#                       VAE CelebA at GRICAD
# -----------------------------------------------
#

CONDA_ENV=deeplearning2
RUN_DIR=~/fidle/VAE
RUN_IPYNB=05.1-Batch-01.ipynb

# ---- Cuda Conda initialization
#
echo '------------------------------------------------------------'
echo "Start : $0"
echo '------------------------------------------------------------'
#
source /applis/environments/cuda_env.sh dahu 10.0
source /applis/environments/conda.sh
#
conda activate "$CONDA_ENV"

# ---- Run it...
#
cd $RUN_DIR

jupyter nbconvert --to notebook --execute "$RUN_IPYNB"