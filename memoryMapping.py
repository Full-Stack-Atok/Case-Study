class MemoryMapping:
    def __init__(self, base, limit):
        """
        Initialize the memory mapping with the base and limit registers.
        
        :param base: The starting address of the process in physical memory.
        :param limit: The size of the process (maximum address the process can access).
        """
        
        self.base = base
        self.limit = limit
        
    def map_address(self, logical_address):
        """
        Map a logical address to a physical address using the base register.
        
        :param logical_address: The logical address the process is trying to access.
        :return Physical address if valid, or error message if out of bounds.
        """
        # Check if the logical address is within the allowed range (0 to limit-1)
        if logical_address < 0 or logical_address >= self.limit:
            return "Error: Address out of bounds"
        
        # Calculate physical address by adding base to logical address
        physical_address = self.base + logical_address
        return f"Physical Address: {physical_address}"
    

# Example usage
if __name__ == "__main__":
    # Example process with the base and limit register values
    base_register = 1000
    limit_register = 4000 # Starts with 0 index = 3999
    
    # Create memory mapping instance
    memory = MemoryMapping(base_register, limit_register)
    
    # Test with various logical addresses
    logical_addresses = [500, 1500, 3500, 3999, 5000, -100]
    
    print("Testing Memory Mapping:")
    for logical in logical_addresses:
        result = memory.map_address(logical)
        print(f"Logical Address: {logical} -> {result}")