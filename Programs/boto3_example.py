#!/usr/bin/env python

import boto3

s3 = boto3.resource("s3")

bucket = s3.Bucket('mybucket')



# now bucket is "attached" the S3 bucket name "mybucket"

print(bucket)

# s3.Bucket(name='mybucket')



print(dir(bucket))

#show you all class method action you may perform