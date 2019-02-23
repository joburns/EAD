import boto3

# Get the service resource
sqs = boto3.resource('sqs')

req_queue = sqs.get_queue_by_name(QueueName='EAD-Request')
resp_queue = sqs.get_queue_by_name(QueueName='EAD-Response')

print ('Blocking receive_message from request from Q: ')

while (True) :
    print ('Blocking for 20 seconds waiting for message')
    for request in req_queue.receive_messages(WaitTimeSeconds=20):
        print ('Request Received from request Q: ' + request.body)
        print ('Non-Blocking send_message from response Q: ')
        resp_queue.send_message(MessageBody='This is a response')

        request.delete()

