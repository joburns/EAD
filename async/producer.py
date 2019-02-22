import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='EAD-Q')

# Create a new message
response = queue.send_message(MessageBody='message #1')
queue.send_message(MessageBody='message #2')

# The response is NOT a resource, but gives you a message ID and MD5
# print(response.get('MessageId'))
# print(response.get('MD5OfMessageBody'))


