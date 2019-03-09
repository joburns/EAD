#!/bin/bash

cnt=$1

for ((i=1; i<=$cnt; i++)); do
	echo "launching process $i..."
	python3 consumer_oos.py &
done

echo "All $cnt consumers ready" 
