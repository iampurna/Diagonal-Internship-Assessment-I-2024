
# The move_items function takes a list as input and creates a new list (moved_list) 
#where each item is moved one position to the right compared to its original position.
def move_items(lst):
    moved_list = []
    for i in range(len(lst)):
        new_position = (i + 1) % len(lst)  # Move each item one position to the right
        moved_list.insert(new_position, lst[i])
    return moved_list

if __name__ == "__main__":
    items = ['A', 'B', 'C', 'D', 'E']
    print("Original list:", items)
    
    moved_items = move_items(items)
    print("List after moving each item to a different position:", moved_items)
