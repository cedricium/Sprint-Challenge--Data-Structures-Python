class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.pointer_index = 0

    def append(self, item):
        if (len(self.storage) < self.capacity):
            self.storage.append(item)
        else:
            curr_index = self.pointer_index % self.capacity
            self.storage[curr_index] = item
            self.pointer_index += 1

    def get(self):
        return self.storage
