#!/usr/bin/env python

import boto3
import urllib.request as urllib2

c = boto3.client('ec2', region_name='eu-west-1')

instanceid = urllib2.urlopen('http://169.254.169.254/latest/meta-data/instance-id').read()

instance_data = c.describe_instances(InstanceIds=[instanceid])

tags = instance_data['Reservations'][0]['Instances'][0]['Tags']

for tag in tags:

   if tag['Key'] == "Name":

    name=tag['Value']