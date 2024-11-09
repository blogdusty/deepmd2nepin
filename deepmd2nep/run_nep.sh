#!/bin/bash
#SBATCH --job-name=AlLiOSi_nep1
#SBATCH --account=gpu-general-users
#SBATCH --partition=gpu-general       # Partition name
#SBATCH --nodelist=compute-0-390
#SBATCH --time=7-00:00:00             # Time allotted for the job (hh:mm:ss)
#SBATCH --ntasks=1                    # Number of tasks (processes)
#SBATCH --cpus-per-task=1             # Number of CPU cores per task
#SBATCH --gres=gpu:1                 # number of GPU's to use in the job
#SBATCH --mem-per-cpu=20G              # Memory per CPU core
#SBATCH --output=my_job_%j.out        # Standard output and error log (%j expands to jobId)
#SBATCH --error=my_job_%j.err         # Separate file for standard error

module load CUDA/CUDA-11.8

cd $SLURM_SUBMIT_DIR

/locationofNEP/GPUMD/src/nep
