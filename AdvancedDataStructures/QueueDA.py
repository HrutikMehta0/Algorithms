from AdvancedDataStructures.DynamicArray import DynamicArray


class QueueDA(object):
    queue = DynamicArray()

    def enqueue(self, value):
        self.queue.append(value)  # Adds an element to the end of the array
        return None

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.removeAt(0)  # Removes element from the top of the array

    def read(self, index):
        if index > len(self.queue):
            return None
        return self.queue.__getitem__(index)  # Returns element at the index

    def reserve(self):
        self.queue[::-1]  # Not Graded for 4101 but my attempt at Reserve
        if len(self.queue) == 0:
            return None
