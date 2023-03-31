#!/bin/bash -l
#SBATCH --job-name="job_name"
#SBATCH --account="g34"
#SBATCH --time=2:00:00
#SBATCH --nodes=16
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --constraint=gpu
#SBATCH --partition=normal
#SBATCH --mem=50G
#SBATCH --hint=nomultithread

module load daint-gpu
module swap PrgEnv-cray PrgEnv-gnu
module load cudatoolkit/10.2.89_3.28-2.1__g52c0314
module load cray-mpich/7.7.18
module load cray-libsci/20.09.1
conda activate cag3

export OMPI_COMM_WORLD_SIZE=$((SLURM_NTASKS * SLURM_NTASKS_PER_NODE))
export CUDA_LAUNCH_BLOCKING=1
export TORCH_DISTRIBUTED_DEBUG=DETAIL
export TORCH_SHOW_CPP_STACKTRACES=1

export MASTER_ADDR=$(srun --ntasks=1 hostname 2>&1 | tail -n1)
echo $MASTER_ADDR

srun python3.6 gcn_distr_15d.py --graphname=Amazon