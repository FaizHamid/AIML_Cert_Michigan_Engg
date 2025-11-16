# Conditional Statements in Python  
# Conditional statements are used to perform different actions based on certain conditions.
# The main conditional statements in Python are:
# 1. if statement - Used to execute a block of code if a specified condition is true.
# 2. elif statement - Short for "else if", used to check multiple conditions.
# 3. else statement - Used to execute a block of code if none of the previous conditions are true. 
# 4. Nested if statements - if statements inside other if statements to check multiple levels of conditions.
# 5. Conditional Expressions (Ternary Operator) - A shorthand way of writing an if-else statement in a single line. 

# Examples of Conditional Statements:   

# if statement
age = 18
if age >= 18:
    print("You are an adult.")               # Output: You are an adult.            

inp = input("Nationality ? ")
if inp == "French":
    print("Bonjour!")                         # Output: Bonjour! (if input is French)
elif inp == "Spanish":
    print("Hola!")                            # Output: Hola! (if input is Spanish)
else:
    print("Hello!")                           # Output: Hello! (for any other input)

# if-else statement
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")                # Output: You are a minor.

# if-elif-else statement
score = 85          
if score >= 90:
    print("Grade: A")
elif score >= 80:               
    print("Grade: B")                      # Output: Grade: B
elif score >= 70:             
    print("Grade: C")                      # Output: Grade: C                   
else:
    print("Grade: F")                      # Output: Grade: F                   

# Nested if statement                           
num = 10
if num > 0:             
    if num % 2 == 0:
        print("The number is positive and even.")  # Output: The number is positive and even.              
    else:
        print("The number is positive and odd.")                
else:             
    print("The number is non-positive.")                    

# Conditional Expressions (Ternary Operator)        
is_even = "Even" if num % 2 == 0 else "Odd"             
print("The number is", is_even)               # Output: The number is Even          

# End of Conditional Statements in Python   
