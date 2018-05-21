from linkedstack import LinkedStack

def stack_to_queue(QueueObj):
    stk = LinkedQueue()
    for el in QueueObj:
        stk.add(el)
    return stk