class  ContiguousMemoryAllocator:
    def __init__(self, ram_size):
        self.ram_size = ram_size
        self.memory = [(0, ram_size)] # Start with one big free block: (start_address, size)
        
    def allocate(self, process_id, process_size):
        # First-fit: Find the first free block that fits the process
        for i, (start, size) in enumerate(self.memory):
            if size >= process_size:
                # Allocate memory for the process
                self.memory[i] = (start + process_size, size - process_size) # Update remaining block
                if self.memory[i][1] == 0: # Remove block if it's fully used
                    self.memory.pop(i)
                print(f"Process {process_id} allocated at address {start}")
                return start # Return the starting address for the process
        
        print(f"Process {process_id} cannot be allocated. Not enough contiguous memory.")
        return None
    
    def deallocate(self, process_id, start_address, process_size):
        # Add the freed memory back into the list
        self.memory.append((start_address, process_size))
        self.memory = sorted(self.memory) # Keep blocks sorted by address
        
        # Merge adjacent free blocks to avoid fragmentation
        merged_memory = []
        for start, size in self.memory:
            if merged_memory and merged_memory[-1][0] + merged_memory[-1][1] == start:
                # Merged with the last block
                merged_memory[-1] = (merged_memory[-1][0], merged_memory[-1][1] + size)
            else:
                # No Adjacent block, add a new entry
                merged_memory.append((start, size))
        
        self.memory = merged_memory
        print(f"Process {process_id} deallocated from address {start_address}")
        
    def display_memory(self):
        print("Current memory layout:")
        for start, size in self.memory:
            print(f"Free block starts at {start} with size {size}")

# Example usage
if __name__ == "__main__":
    allocator = ContiguousMemoryAllocator(ram_size=20)
    
    # Allocate processes
    allocator.allocate(1, 5) # Process 1 requires 5 units
    allocator.allocate(2, 8) # Process 2 requires 8 units
    allocator.display_memory()
    
    # Deallocate Process 1 to create space  
    allocator.deallocate(1, 0, 5)
    allocator.display_memory()
    
    # Try to allocate a process that requires 10 units
    allocator.allocate(3, 10)
    allocator.display_memory() 
   