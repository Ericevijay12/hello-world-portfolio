"""
CSE 310 - Hello World
Author: Eric Evijay Ohiani
"""

def main():
    # Greeting the world with a bit of personality as requested in the instructions
    name = "Eric"
    print(f"Hello World! My name is {name} and I am excited to start CSE 310.")
    
    # Adding a simple loop to demonstrate basic syntax
    print("\nStarting the semester with 3 core goals:")
    goals = ["Mastering Kotlin", "Building Mobile Apps", "Learning Cloud Databases"]
    for goal in goals:
        print(f"- {goal}")

if __name__ == "__main__":
    main()
