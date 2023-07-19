import boto3
ec2 = boto3.client('ec2')
response = ec2.create_image(

    InstanceId='i-0b97ddb10ebe1f922 ',
    Name='black-image'
    )

print(response)