# Create EC2 instance from boto3
import boto3

def create_ec2_instance():
    try:
       print("Creating EC2 Instance From Boto3")
       resource_ec2 = boto3.client("ec2")
       resource_ec2.run_instances(
           ImageId="ami-0b5eea76982371e91",
           MinCount=1,
           MaxCount=1,
           InstanceType="t2.micro",
           KeyName="lambda-function"

       )
    except Exception as e:
        print(e)

def describe_ec2_instance():
    try:
        print ("Describing EC2 Instance")
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instances(InstanceIds=['i-06310c84eccb7da5f']))
    except Exception as e:
        print(e)

#create_ec2_instance()
describe_ec2_instance()
