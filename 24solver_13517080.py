# Name      : Mgs. Muhammad Riandi Ramadhan
# NIM       : 13517080
# Class     : 02
# Lesson    : Algorithm Strategy

# Dictionary and initialization
operators = ['+', '-', '*', '/']
n_permutation = []
o_permutation = []
solutions = []
temp_score = 0
count_solution = 0
valid = False

# Asking for input in the type of char and putted them into a list
print('24 GAME SOLVER')
print('Input 4 numbers below')
numbers = input().split()

# Import a library for getting execution time
import time
# Starting point for calculating time
start_time = time.time()

# Validating user input, must be 4 positive integers 
while not(valid):
    # Checking how many numbers in list
    if len(numbers) == 4:
        # Checking whether negative number exists or not
        count_negative = 0
        for number in numbers:
            if int(number) < 0:
                count_negative += 1
        # User input is correct
        if count_negative == 0:
            valid = True
    # User input is still wrong
    if not(valid):
        print("Wrong input, try again")
        # Re-asking user input
        numbers = input().split()
        # Renewing starting point for calculating time
        start_time = time.time()

# Generating all permutations of numbers and putting them into a list without same indexes
for i in range(len(numbers)):
    for j in range(len(numbers)):
        for k in range(len(numbers)):
            for l in range(len(numbers)):
                # Preventing a number from being used more than once
                if (i != j) and (i != k) and (i != l) and (j != k) and (j != l) and (k != l):
                    # Making an empty temporary list
                    n_temp = []
                    # Appending into a temporary list
                    n_temp.append(numbers[i])
                    n_temp.append(numbers[j])
                    n_temp.append(numbers[k])
                    n_temp.append(numbers[l])
                    # Appending the temporary list into list of operators permutation
                    n_permutation.append(n_temp)

# Generating all permutations of operators and putting them into a list
for i in operators:
    for j in operators:
        for k in operators:
            # Making an empty temporary list
            o_temp = []
            # Appending into a temporary list
            o_temp.append(i)
            o_temp.append(j)
            o_temp.append(k)
            # Appending the temporary list into list of operators permutation
            o_permutation.append(o_temp)

# Generating all possible solutions
for n in n_permutation:
    for o in o_permutation:
        # First pattern of solution is ((ab)c)d
        solution_1 = '((' + n[0] + o[0] + n[1] + ')' + o[1] + n[2] + ')' + o[2] + n[3]
        # Second pattern of solution is (a(bc))d
        solution_2 = '(' + n[0] + o[0] + '(' + n[1] + o[1] + n[2] + '))' + o[2] + n[3]
        # Third pattern of solution is a((bc)d)
        solution_3 = n[0] + o[0] + '((' + n[1] + o[1] + n[2] + ')' + o[2] + n[3] + ')'
        # Fourth pattern of solution is (ab)(cd)
        solution_4 = '(' + n[0] + o[0] + n[1] + ')' + o[1] + '(' + n[2] + o[2] + n[3] + ')'
        try:
            # Appending the solution into a list if it's equal to 24 and hasn't been existed
            if eval(solution_1) == 24 and solution_1 not in solutions:
                solutions.append(solution_1)
                # Counting numbers of solution
                count_solution += 1
            if eval(solution_2) == 24 and solution_2 not in solutions:
                solutions.append(solution_2)
                # Counting numbers of solution
                count_solution += 1
            if eval(solution_3) == 24 and solution_3 not in solutions:
                solutions.append(solution_3)
                # Counting numbers of solution
                count_solution += 1
            if eval(solution_4) == 24 and solution_4 not in solutions:
                solutions.append(solution_4)
                # Counting numbers of solution
                count_solution += 1
        except:
            # Handling error cases
            pass
        
# Printing the numbers of solution
print(count_solution, "solutions found")

# Printing all possible solutions
for solution in solutions:
    temp_score = 0
    for s in solution:
        if (s == '+'):
            temp_score += 5
        elif (s == '-'):
            temp_score += 4
        elif (s == '*'):
            temp_score += 3
        elif (s == '/'):
            temp_score += 2
        elif (s == '('):
            temp_score -= 1
        temp_score -= abs(24 - eval(solution))
    print(solution + ' ' + str(temp_score))

# Ending point for calculating time
end_time = time.time()

# Printing execution time in seconds
print(end_time-start_time, "seconds time taken")