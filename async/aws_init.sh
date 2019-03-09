#!/bin/bash

# need to work as ec2-user
export PYTHONPATH=/home/ec2-user/.local/lib/python3.6/site-packages

# set up the AWS credentials
mkdir /root/.aws

echo "[default]" >> /root/.aws/config
echo "output = json" >> /root/.aws/config
echo "region = eu-west-1" >> /root/.aws/config

echo "[default]" >> /root/.aws/credentials
echo "aws_access_key_id = AKIAIRZQFRTMX2RZWA7A" >> /root/.aws/credentials
echo "aws_secret_access_key = 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" >> /root/.aws/credentials

chmod 600 /root/.aws/config
chmod 600 /root/.aws/credentials

# get the latest git repo
cd /home/ec2-user/EAD-Lab
git pull

# start the producer
cd async
python3 ./consumer_oos.py&
