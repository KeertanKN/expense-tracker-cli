import os
FILE_NAME = "expense.txt"
def main_menu():
    while True:
        print("---------Expense Tracker ---------")
        print("1.add new Expense")
        print("2.view Expense")
        print("3.Quit")
        n = input("Enter your choice(1-3): ")

        if n == '1':
            add_expense()
        elif n == '2':
            view_expense()
        elif n == '3':
            print("GoodBye......")
            return
        else:
            print("Invalid choice enter number btw (1 -- 3)")
def add_expense():
    item = input("What did you buy? ")
    price = input("How much did it cost?  ")
    with open(FILE_NAME, 'a') as f:
        f.write(f"{item} - {price}\n")
    print("Expense added succesfully ")
def view_expense():
    print("-----Your expenses-----")
    if not os.path.exists(FILE_NAME):
        print("No expense record yet!!")
        return
    with open(FILE_NAME, "r") as  r:
        lines = r.readlines()
        if len(lines) == 0:
            print("No Expense record yet!! ")
        else:
            for line in lines:
                print(line.strip())
if __name__ == "__main__":
    main_menu()