import boto3
import time

# Get the service resource
sqs = boto3.resource('sqs')

req_queue = sqs.get_queue_by_name(QueueName='EAD-Request')
resp_queue = sqs.get_queue_by_name(QueueName='EAD-Response')

print ('Blocking receive_message from request from Q: ')

while (True) :
    for request in req_queue.receive_messages(WaitTimeSeconds=3):
        print ('Q Read: ' + request.body)
        resp_queue.send_message(MessageBody=request.body)
        # now comment this out and study what happens
        time.sleep(0.25)
        request.delete()

