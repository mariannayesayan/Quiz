class Queue:
    def __init__(self):
        self.queue = []  # implementing array
        self.head = 0  # head is the first element
        self.tail = 0  # tail is the last element

    # checks whether it is empty or not
    def is_empty(self):
        if len(self.queue) == 0:
            return self.queue == []
        else:
            print("everything is ok")

    # adds from start
    def enqueue(self, item):
        if self.size() != self.is_empty():
            return ("it is full")
        self.queue.append(item)
        self.tail = -1
        return True

    # deletes from the end
    def dequeue(self):
        if self.size() == self.is_empty():
            return ("it is empty")
        data = self.queue[self.head]
        self.head = +1  # adds
        return data

    def size(self):
        return self.tail - self.head

    def delete(self):
        self.tail = 0
        self.head = 0
        self.queue = []


def main():
    q = Queue()
    print(q.enqueue(5))
    print(q.enqueue(4))
    print(q.enqueue(8))
    print(q.enqueue(10))

    print(q.size())


main()
