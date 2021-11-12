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

    def __init__(self, stack_len = 0):
        self.stack = []
        self.stack_len = stack_len

    # Add element at end
    def push(self, val):
        # If the length is predefind, add element restricted to defind length [self.length < self.stack_len]
        # If the length is not defind, Then lenhth of stack is unlimited [self.stack_len == 0]
        if self.length() < self.stack_len or self.stack_len == 0:
            self.stack.append(val)
        else:
            print('ERROR: Stack out of range.')

    # Remove element at end
    def pop(self):
        if self.stack:
            self.stack.pop(len(self.stack)-1)
        else:
            print('ERROR: Stack is empty. Item can\'t be remove')

    # Find last element
    def peak(self):
        return self.stack[len(self.stack)-1]

    # Check is empty or not
    def is_empty(self):
        if not self.stack:
            return True
        else:
            return False

    # For clear stack
    def clear(self):
        return self.stack.clear()

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
# If we not pass length of stack, by default it take 0 [stack_len = 0 ]
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

# Check is stack empty or not
print(stk.is_empty())
# elete stack
print(stk.clear())
print(stk.is_empty())

#######################################################################

# Create predefind stack
stk2 = Stack(3)
stk2.push(4)
stk2.push(5)
stk2.push(6)

print('Stack 2:',stk2.stack)
stk2.push(7)
