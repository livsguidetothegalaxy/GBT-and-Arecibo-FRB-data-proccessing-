#!/bin/bash


for d in A*/*/; 
do

	cd $d
	echo $d
	decimatename=$( ls *c2t5.fil)
	out_cands=$(echo $d | cut -d / -f 2)
	rm -rf slurm *.out
	mkdir -p $out_cands
	rm -rf $out_cands/2*cand
	sbatch  --job-name="$decimatename" -N1 -n1 --gres=gpu:1 --partition=gpu --nodelist=gpu01 --wrap="heimdall -f $decimatename -dm 20 10000 -boxcar_max 128 -output_dir ${out_cands} -rfi_tol 3 -cand_sep_time 8 -cand_sep_filter 8"
	cd ../../
done 


