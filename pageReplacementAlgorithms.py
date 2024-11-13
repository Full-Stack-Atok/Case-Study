def fifo_page_replacement(capacity, page_requests):
    memory = [] # List to store pages in memory
    page_faults = 0
    
    for page in page_requests:
        # If the page is not in memory, we have a page fault
        if page not in memory:
            # If memory is full, remove the oldest page (first in the list) 
            if len(memory) == capacity:
                memory.pop # Remove the first page in memory (FIFO)
                
            # Add the new page to memory
            memory.append(page)
            page_faults += 1 # Increment page fault count
            print(f"Page {page} loaded, page fault occurred.")
        else:
            print(f"Page {page} hit, already in memory.")
    
    print(f"Total page faults: {page_faults}")
    
# Example usage
if __name__ == "__main__":
    capacity = 3 # Number of frames in memory
    page_requests = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    
    fifo_page_replacement(capacity, page_requests)