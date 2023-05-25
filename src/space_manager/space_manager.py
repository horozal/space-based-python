from multiprocessing import Process, Queue

# Define the space-based architecture manager
class SpaceManager:
    def __init__(self):
        self.queue = Queue()
      
