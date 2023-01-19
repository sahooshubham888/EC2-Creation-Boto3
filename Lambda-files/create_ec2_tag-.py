import boto3

client = boto3.client("ec2")

tags = [
    {"Key": "Owner", "Value": "shubham.sahoo.com"},
]

instance_ids = ["i-070a8ed2ff956a219"]

response = client.create_tags(DryRun=False, Resources=instance_ids, Tags=tags)

print(response)
