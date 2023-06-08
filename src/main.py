from space_manager.space_manager import SpaceManager
from in_memory_grid.in_memory_grid import InMemoryGrid

# Usage example
if __name__ == '__main__':
    # Create and start the Space Manager
    space_manager = SpaceManager()
    space_manager.start()

    # Create and initialize the In-Memory Grid
    in_memory_grid = InMemoryGrid()
    in_memory_grid.initialize()

    # Perform necessary operations with the space-based architecture
    # ...

    # Stop the Space Manager and In-Memory Grid
    space_manager.stop()
    in_memory_grid.stop()
