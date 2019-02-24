import boto3

# Get the service resource
sqs = boto3.resource('sqs')

req_queue = sqs.get_queue_by_name(QueueName='EAD-Request.fifo')
resp_queue = sqs.get_queue_by_name(QueueName='EAD-Response.fifo')

print ('Blocking receive_message from request from Q: ')

while (True) :
    for request in req_queue.receive_messages(WaitTimeSeconds=3):
        print ('Q Read: ' + request.body)
        resp_queue.send_message(MessageBody=request.body, MessageDeduplicationId=request.body, MessageGroupId='EAD-FIFO-DEMO')
        # now comment this out and study what happens
        request.delete()

