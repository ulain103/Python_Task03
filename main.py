import random

ROWS = 3
COLS = 300  # Adjust the size based on your actual data size

# Function to display the student's ID
def display_student_id(student_id):
    print(f"Student ID: {student_id}")

# Function to calculate and display the cost for slab 1
def cost_slab1(source_data):
    total_units = sum(source_data[0][:100])
    total_cost = total_units * 10
    print(f"Total cost for slab 1: Rs. {total_cost}")

# Function to calculate and display the cost for slab 2
def cost_slab2(source_data):
    total_units = sum(source_data[1][100:200])
    total_cost = total_units * 15
    print(f"Total cost for slab 2: Rs. {total_cost}")

# Function to calculate and display the cost for slab 3
def cost_slab3(source_data):
    total_units = sum(source_data[2][200:300])
    total_cost = total_units * 20
    print(f"Total cost for slab 3: Rs. {total_cost}")

def main():
    student_id = 12345  # Replace with the actual student ID

    # Generate random values for source_data matrix
    source_data = [[random.randint(0, 100) for _ in range(COLS)] for _ in range(ROWS)]

    while True:
        print("------------------------------")
        display_student_id(student_id)
        print("1. Display the bill of slab 1 and slab 2")
        print("2. Display the bill of slab 3")
        print("Press any other key to exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            cost_slab1(source_data)
            cost_slab2(source_data)
        elif choice == '2':
            cost_slab3(source_data)
        else:
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()

