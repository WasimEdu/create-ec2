import boto3

aws_console = boto3.session.Session(profile_name = "default", region_name = "us-east-1")
ec2 = aws_console.client('ec2')

ami_id = 'ami-0e86e20dae9224db8'
instance_type = 't2.micro'
max_count = 1
min_count = 1

# Launch an EC2 instance
response = ec2.run_instances(
    ImageId = ami_id,
    InstanceType = instance_type,
    MaxCount = max_count,
    MinCount = min_count
)

# Geting the Instance ID of the newly launched instance
instance_id = response['Instances'][0]['InstanceId']
print(f"Instance ID: {instance_id}")

# Wait for the instance to be in running state
print("Waiting for instance to be in running state....")
ec2.get_waiter('instance_running').wait(InstanceIds = [instance_id])


# describing the instance
instant_info = ec2.describe_instances(InstanceIds=[instance_id])
instant = instant_info['Reservations'][0]['Instances'][0]

# Printing the public IP address
print(f"Public Ip Address: {instant.get("PublicIpAddress", "N/A")}")
print(f"Private Ip Address: {instant.get("PrivateIpAddress", "N/A")}")



