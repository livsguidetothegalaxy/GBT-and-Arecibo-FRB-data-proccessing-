#!/bin/bash



for d in ./*/*/; 
do

cd $d

dir=$(pwd)
part=$( echo $dir | cut -d / -f 5-6)

sbatch --job-name="Fits2Fil" -N1 -n1 --wrap="yapp_fits2fil /hyrule/data/users/dmadison/trans_GRB/$part/*fits"


cd ../..

done 
