# concept learned loop, 
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'\
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'\
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'\
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_rand(num, target):
    rand = ''
    for i in range(0, num + 1):
        rand_num = random.randint(0, len(target) - 1)
        rand += target[rand_num]
    print(rand)
    return rand

def generate_pass(num_letters, num_symbols, num_numbers):
    rand_letters = generate_rand(num_letters, letters)
    rand_symbols = generate_rand(num_symbols, symbols)
    rand_numbers = generate_rand(num_numbers, numbers)

    password = f"{rand_letters}{rand_symbols}{rand_numbers}"
    return password

def main():
    print("Welcome to the PyPassword Generator!")
    num_letters = int(input("How many letters would you like in your password?\n"))
    num_symbols = int(input("How many symbols would you like?\n"))
    num_numbers = int(input("How many numbers would you like?\n"))
    password = generate_pass(num_letters, num_symbols, num_numbers)
    password = ''.join(random.sample(password, len(password)))
    
    print(f"Here is your password: {password}")

# for loop practise
def loop():
    fruits = ["Apple", "Peach", "Pear"]
    for fruit in fruits:
        print(fruit)


def cal_avg_height():
    student_heights = input("Input a list of student heights ").split()
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])
    print(student_heights)

    sum = 0
    num_students = 0
    for height in student_heights:
        sum += height
        num_students += 1
    print(f"Average hieght is {sum // num_students}")

if __name__ == "__main__":
    #loop()
    #cal_avg_height()
    main()