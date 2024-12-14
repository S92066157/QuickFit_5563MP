import random

# Lists to store available memory blocks of each size, process sizes,
# and errors encountered during memory allocation

list_8kb = []
list_16kb = []
list_32kb = []
errors = []
process_size = []


def memory_block_init():
    # This function initializes random numbers of 8KB, 16KB, and 32KB memory blocks (1 to 5 blocks each).
    size_8kb = random.randint(1, 5)
    size_16kb = random.randint(1, 5)
    size_32kb = random.randint(1, 5)

    print("----- Number of Memory Block Available -------\n")

    # Print the initialized memory block names and add them to lists for each block size.
    for x in range(size_8kb):
        memory_block_name = f"B{x}_8KB"
        list_8kb.append(memory_block_name)

    for x in range(size_16kb):
        memory_block_name = f"B{x}_16KB"
        list_16kb.append(memory_block_name)

    for x in range(size_32kb):
        memory_block_name = f"B{x}_32KB"
        list_32kb.append(memory_block_name)

    # Print a summary of the available memory blocks for 8KB, 16KB, and 32KB.
    print("Block size - (number of Block)  => names of memory blocks")

    print(f"8KB ({size_8kb}) => {list_8kb}")
    print(f"16KB ({size_16kb}) => {list_16kb}")
    print(f"32KB ({size_32kb})=> {list_32kb}")


# function of assign process to memory
def assign_process_to_memory(process_sizes, arg_list_8kb, arg_list_16kb, arg_list_32kb ):
    num_of_process = len(process_sizes)

    # initiate assigned memory lists
    assigned_all = []

    # Check the required memory size for each process and assign it to the first available memory block.
    for num in range(num_of_process):

        balance_8kb = len(arg_list_8kb)
        balance_16kb = len(arg_list_16kb)
        balance_32kb = len(arg_list_32kb)

        process_name = f"P{num + 1}"

        if process_sizes[num] <= 8:

            if balance_8kb > 0:
                first = arg_list_8kb.pop(0)
                first = first, process_name, process_sizes[num]
                assigned_all.append(first)

            elif balance_16kb > 0:
                first = arg_list_16kb.pop(0)
                first = first, process_name, process_sizes[num]
                assigned_all.append(first)

            elif balance_32kb > 0:
                first = arg_list_32kb.pop(0)
                first = first, process_name, process_sizes[num]
                assigned_all.append(first)

            else:
                errors.append(
                    f" There is no free memory space to assign process {num + 1} (Process Size : {process_sizes[num]}KB)")

        elif 8 < process_sizes[num] <= 16:

            if balance_16kb > 0:
                first = arg_list_16kb.pop(0)
                first = first, process_name, process_sizes[num]
                assigned_all.append(first)

            elif balance_32kb > 0:
                first = arg_list_32kb.pop(0)
                first = first, process_name, process_sizes[num]
                assigned_all.append(first)

            else:
                errors.append(
                    f" There is no free memory space to assign process {num + 1} (Process Size : {process_sizes[num]}KB)")

        elif 16 < process_sizes[num] <= 32:

            if balance_32kb > 0:
                first = arg_list_32kb.pop(0)
                first = first, process_name, process_sizes[num]
                assigned_all.append(first)
            else:
                errors.append(
                    f" There is no free memory space to assign process {num + 1} (Process Size : {process_sizes[num]}KB)")

        else:
            errors.append(
                f" There is no free memory space to assign process {num + 1} (Process Size : {process_sizes[num]}KB)")

    print("\n\n--- Memory Allocation ---")
    print("Process ID --- Memory Block ID --- (Size)")

    for [block_id, process_id, process_size] in assigned_all:
        print(f"{process_id} --- {block_id} --- (size: {process_size}KB)")


# Print a list of any unused memory blocks remaining at the end of the program.
def print_free_memory():
    print("\n--- Free Memory Blocks ---")

    # check and print if there is any free memory blocks at the end of the program.
    if len(list_8kb) == 0:
        print("No free memory space in 8KB Blocks")
    else:
        print(f"free memory space in 8KB Blocks : {list_8kb} ")

    if len(list_16kb) == 0:
        print("No free memory space in 16KB Blocks")
    else:
        print(f"free memory space in 16KB Blocks : {list_16kb} ")

    if len(list_32kb) == 0:
        print("No free memory space in 32KB Blocks")
    else:
        print(f"free memory space in 32KB Blocks : {list_32kb} ")


# function for get user input for size for each process
def enter_process_size(process_count):
    print("\n--- Process Size Entry : ---")
    for x in range(1, process_count + 1):
        process_size_int = int(input(f"Size for P{x} : "))
        process_size.append(process_size_int)


# function to print the errors which had occurred during the memory allocation process
def print_errors():
    if len(errors) == 0:
        print("\nThere are no errors during the allocation of memory blocks")

    else:
        print("\n--- Error/s during the allocation of memory blocks ---")
        for error in errors:
            print(error)


def enter_process_count():
    global count
    try:
        count = int(input(f"\nEnter the number of processes  : "))

        if count == 0:
            print("Process count cannot be zero. Please Retry")
            enter_process_count()

    except Exception as e:
        print(f"Exception Occurred : {e}  ")
        print("Please Retry")
        enter_process_count()

    finally:
        return count


# Main execution of the program begins here.
memory_block_init()
process_count = enter_process_count()
enter_process_size(process_count)
assign_process_to_memory(process_size, list_8kb, list_16kb, list_32kb)
print_errors()
print_free_memory()
