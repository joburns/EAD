import boto3
import time

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
req_queue = sqs.get_queue_by_name(QueueName='EAD-Request')
resp_queue = sqs.get_queue_by_name(QueueName='EAD-Response')

# start the timer
t0 = time.time()

send_cntr = 0
# Create 100 new messages
for x in range(0, 100):
    print ('Q Send: ' + str(x))
    req_queue.send_message(MessageBody=str(x))
    send_cntr += 1

print('Sent ' + str(send_cntr))

# now go into reading mode
# until all the messages have been collected
recv_cntr = 0
while (True) :
    for response in resp_queue.receive_messages():
        print ('Q Read: ' + response.body)
        recv_cntr += 1
        response.delete()
    if recv_cntr == send_cntr:
       break
t1 = time.time()
print ('Elapsed time: ' + str(t1-t0))

