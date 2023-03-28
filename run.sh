#!/bin/bash -l
#SBATCH --job-name="job_name"
#SBATCH --account="g34"
#SBATCH --time=01:00:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --constraint=gpu
#SBATCH --partition=amdv100
#SBATCH --mem=200G
#SBATCH --hint=nomultithread

# export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

module load cuda/10.1

export OMPI_COMM_WORLD_SIZE=$((SLURM_NTASKS * SLURM_NTASKS_PER_NODE))
export NCCL_DEBUG=INFO
export NCCL_IB_HCA=ipogif0
export NCCL_IB_CUDA_SUPPORT=1
export NCCL_SOCKET_IFNAME=ipogif0
export PYTHONPATH=$PYTHONPATH:/users/fscheidl/miniconda3/envs/cag3/lib/python3.6/site-packages

srun python gcn_distr_15d.py --dist_file="dist_file_x"