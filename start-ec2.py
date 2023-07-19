import boto3
ec2 = boto3.client ('ec2')
response = ec2.start_instances(
    InstanceIds=[
        'i-03b4f6fa75e5c4006','i-0b85b05870e480b5a','i-0f264250358099bb4'
    ]
)
print (response)