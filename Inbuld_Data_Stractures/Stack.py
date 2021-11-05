######### STACK ###########
# 1. Stack is a user defiend data structure
# 2. We can add element at last in stack
# 3. Add and Remove of elements in stack worked in two ways:
    # 1. Last In First Out (LIFO)
    # 2. First In Last Out (FILO)
# 4. In a stack, you can store elements of the same type or different types.
# 5. Operation in satck:
    # 1. push
    # 2. pop
    # 3. peak or top
    # 4. is_empty

#############################################################

# Define  a Stack class
class Stack:

    def __init__(self):
        self.stack = []

    # Add element at end
    def push(self, val):
        self.stack.append(val)

    # Remove element at end
    def pop(self):
        self.stack.pop(len(self.stack)-1)

    # Find last element
    def peak(self):
        return self.stack[len(self.stack)-1]

    # Check is empty or not
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    # Return length of stack
    def length(self):
        return len(self.stack)

    # Return sum of stack
    def sum(self):

        sum = 0
        for i in self.stack:
            # It will allow only int, float values to find the sum.         
            if type(i) in [int, float]:          
                sum += i
            else:
                print('ERROR: all elements data types must be Numaric for find the sum()')
                break
        return sum


#####################################################################
            
# Creating Stack obj
stk = Stack()

# Add values
stk.push(23)
stk.push(23)
stk.push(23.45)
stk.push('Eswar')

# Print stack
print(stk.stack)

# Remove last item
stk.pop()
print(stk.stack)
stk.push('Eswar')
print(stk.stack)

print(stk.peak())

print(stk.length())

# Finding sum with string element inclusion 
print(stk.sum()) # Throw an error
# Remove str element
stk.pop()
# again find sum now with all numaric values of stack
print(stk.stack)
print(stk.sum())