########################################################

# 1. Back / Rear / Tail --------> Entering or adding side.

# 2. Frount / Head      --------> Leave or exit point.

# 3. We can add or remove one element at a time.

# 4. Queue follows FIFO or LILO rule to out the elements.

    # FIFO ------> First In First Out
    # LILO ------> Last In Last Out



########################################################
class QueueAlg:

    def __init__(self, append_side, size = 0):

        self.queue = []
        self.size = size
        if append_side in ['left', 'right']:
            self.append_side = append_side

        else:
            print(f'ERROR: append_side : {append_side} is invalid argument valuue. It should be "left" or "right"')

    def enqueue(self, val):

        if self.size == 0 or len(self.queue) < self.size:
            if self.append_side == 'right':
                self.queue.append(val)
            elif self.append_side == 'left':
                self.queue.insert(0, val)
        else:
            print('ERROR: Queue is Overfolw.')


    def dequeue(self):

        if len(self.queue) == 0:
            print('ERROR: Queue is Underflow')
        else:
            if self.append_side == 'right':
                self.queue.remove(self.queue[0])
            elif self.append_side == 'left':
                self.queue.remove(self.queue[-1])
    
    def is_empty(self):

        if len(self.queue) == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.size == 0 or len(self.queue) < self.size:
            return False
        else:
            return True

    def view(self):
        return self.queue

    def length(self):
        return len(self.queue)
    
