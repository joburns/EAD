import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
req_queue = sqs.get_queue_by_name(QueueName='EAD-Request')

# Create a new message
print ('Non-Blocking send_message from response Q: ')
req_queue.send_message(MessageBody='message #1')

# now go into reading mode

resp_queue = sqs.get_queue_by_name(QueueName='EAD-Response')

print ('Blocking receive_message from response Q: ')

for response in resp_queue.receive_messages(WaitTimeSeconds=20):
    print ('Response Received from response Q: ')
    response.delete()

print ('Response deleted from response Q: ')
