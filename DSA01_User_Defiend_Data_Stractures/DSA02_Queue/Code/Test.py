

from QAlg import QueueAlg

# Creating algorithm obj.
# Now queue size is unlimited.
queue = QueueAlg(append_side = 'left')
queue1 = QueueAlg(append_side = 'right')
queue2 = QueueAlg(append_side = 'left', size= 5)
queue3 = QueueAlg(append_side = 'right', size= 5)

def queue_info(queue):

    # Checking all functions
    # print('\n###################################################\n')

    print('Is empty: ',queue.is_empty())
    print('View queue: ',queue.view())
    print('length of queue: ',queue.length())
    print('Is queue full: ',queue.is_full())
    print('\n###################################################\n')

def queue_operations(queue):

    queue_info(queue)

    queue.enqueue(3)
    queue.enqueue('rama')
    queue.enqueue(3.67)
    queue.enqueue(3)

    queue_info(queue)

    queue.dequeue()
    queue.dequeue()

    queue_info(queue)


list_objs = [queue, queue1, queue2, queue3]

for obj in list_objs:
    queue_operations(obj)
