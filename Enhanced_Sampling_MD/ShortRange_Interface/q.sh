#!/bin/bash
#SBATCH -N 1
#SBATCH -n 6
#SBATCH -t 500:00:00
#SBATCH --gpus 3090:1
#SBATCH --job-name=025zd

cd $SLURM_SUBMIT_DIR

module load conda
conda activate dpmdkit_v2.1.5_0202

# Run the application - the line below is just a random example.
lmp -i in.glycine > glycine.out
