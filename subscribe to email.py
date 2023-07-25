import boto3
#create a sns topic
sns = boto3.client('sns')
topicArn = 'arn:aws:sns:us-east-1:620227247341:black-message'
black_sub = sns.subscribe(
TopicArn= topicArn,
Protocol='email',
Endpoint='abiolamajekodunmi2011@gmail.com',
)
print('This is will subscriber ARN for SNS : ',black_sub['SubscriptionArn'])