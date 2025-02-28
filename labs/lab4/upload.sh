#!/bin/bash

FILE_NAME=$1
BUCKET_NAME=$2
EXPIRATION=$3

aws s3 cp FILE_NAME s3://$BUCKET_NAME/

aws s3 presign --expires-in $EXPIRATION ://$BUCKET_NAME/$FILE_NAME
