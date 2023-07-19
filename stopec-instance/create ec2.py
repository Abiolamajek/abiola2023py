import boto3
ec2 = boto3.client('ec2')
response = ec2.run_instances(ImageId='ami-087f66943bdcbaed2',
    InstanceType='t2.micro',
    KeyName='black_keypair',
    MaxCount=4,
    MinCount=4,
TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Developer Environment'
                },
                {
                    'Key': 'Name1',
                    'Value': 'Developer1 Environment'
                },
                {
                    'Key': 'Name2',
                    'Value': 'Developer2 Environment'
                },
                {
                    'Key': 'Production',
                    'Value': 'Production Environment'
                },
            ]
        },
    ], 
)

for i in response ['Instances']:
    print('Instance ID Created is :{} Instance Type Created is :{}' .format(i['InstanceId'],i['InstanceType']))
 