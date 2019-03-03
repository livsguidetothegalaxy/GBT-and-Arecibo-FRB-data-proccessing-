#!/bin/bash


for d in ./*/*/; 

do

cd $d

filname=$(ls *.fil) 

newfilname=$(echo "$filname"_c2t5.fil)

sbatch  --job-name="decimate" -N1 -n1 --wrap="decimate -c 2 -t 5 $filname > $newfilname"

cd ../..

done 


