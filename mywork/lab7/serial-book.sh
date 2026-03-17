#!/bin/bash
#SBATCH --account=ds2002
#SBATCH --job-name=serial-book-analysis
#SBATCH --output=serial-book-%j.out
#SBATCH --error=serial-book-%j.err
#SBATCH --time=00:10:00
#SBATCH --partition=standard
#SBATCH --mem=8G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1

# Navigate to the scratch working directory
cd /scratch/$USER/ds2002-jobruns/text-analysis

# Run the text processing script on book 1
python ~/ds2002-course/labs/07-hpc/process-book.py book-1.txt results-1.csv