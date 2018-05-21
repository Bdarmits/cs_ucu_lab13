from linkedqueue import LinkedQueue

def stack_to_queue(StackObj):
    queue = LinkedQueue()
    for el in StackObj:
        queue.add(el)
    return queue