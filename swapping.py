class MemoryManager:
    def __init__(self, ram_size, swap_space_size):
        self.ram_size = ram_size
        self.swap_space_size = swap_space_size
        self.ram = []
        self.swap_space = []
        
    def load_process(self, process_id, process_size):
        if process_size <= self.ram_size - sum([p[1] for p in self.ram]):
            self.ram.append((process_id , process_size))
            print(f"Process {process_id} loaded into RAM.")
        elif process_size <= self.swap_space_size - sum([p[1] for p in  self.swap_space]):
            self.swap(process_id, process_size)
        else:
            print(f"Not enough space for Process {process_id}")

    def swap(self, process_id, process_size):
        if len(self.ram) > 0:
            # Swap out the first process in RAM
            swapped_process = self.ram.pop(0)
            self.swap_space.append(swapped_process)
            print(f"Process {swapped_process[0]} swapped out to swap space.")
        
        # Load the new process into RAM 
        self.ram.append((process_id, process_size))
        print(f"Process {process_id} loaded into RAM.")
    
    def display_memory(self):
        print("Current RAM processes:", [p[0] for p in self.ram])
        print("Swap space processes:", [p[0] for p in self.swap_space])
        

# Example usage
if __name__ == "__main__":
    memory_manager = MemoryManager(ram_size=10, swap_space_size=10)
    
    
    # Simulate loading processes
    memory_manager.load_process(1, 4) # Load process 1 (size 4) 
    memory_manager.load_process(2, 6) # Load process 2 (size 6)
    memory_manager.load_process(3, 3) # Load process 3 (size 3)
    
    # Display current memory status
    memory_manager.display_memory()
    
    # Load a new process and trigger swapping
    memory_manager.load_process(4, 5) # Load process 4 (size 5)
    
    # Display memory after swapping
    memory_manager.display_memory()   