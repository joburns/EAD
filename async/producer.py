import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
req_queue = sqs.get_queue_by_name(QueueName='EAD-Request')
resp_queue = sqs.get_queue_by_name(QueueName='EAD-Response')

# Create a new message
print ('Non-Blocking send_message from response Q: ')
req_queue.send_message(MessageBody='This is a request')

# now go into reading mode
while (True) :
    print ('Blocking receive_message from response Q: ')
    for response in resp_queue.receive_messages(WaitTimeSeconds=3):
        print ('Response Received from response Q: ' + response.body)
        response.delete()
        print ('Response deleted from response Q: ')
