# # print hello world
# '''print('Hello World')
# '''


# #assignment 1.2
# #printing tictactoe board

# '''print('       |      |')
# print('----------------------')
# print('       |      |')
# print('----------------------')
# print('       |      |')'''

# a = ('       |      |')
# b= ('----------------------')

# print(a ,'\n',b ,'\n',a ,'\n',b ,'\n',a)



#1.3 

# a= ((3*5)/2+3)
# print(a)

# b = ((-19+100)**(1/4))
# print(b)


# class_list = [[['peter', 'parker'], [80.0,70.0, 85.0]],[['bruce', 'wayne'], [100.0, 80.0, 74.0]]]

# def get_stats(class_list):
#     new_stats = []
#     for student in class_list:
#         new_stats.append([student[0], student[1], avg(student[1])]) # i had to create a function for avg before it would world
#     print(new_stats)
#     return new_stats

# def avg(scores):
#     average_grades = round(sum(scores)/len(scores),2)
#     return average_grades


# get_stats(class_list)

# import math

# class Coordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def distance(self, other):
#         x_diff_sq = (self.x - other.x)**2
#         y_diff_sq = (self.y - other.y)**2
#         return(math.sqrt(x_diff_sq + y_diff_sq))
        
        
#     def __str__(self):
#         return('(' + str(self.x) + ',' + str(self.y)+ ')')
        

# c = Coordinate(3, 4)
# d = Coordinate(5, 6)
# print(f'The distance between {c} and {d} is {round(c.distance(d), 2)}')


# class Fraction(object):
#     def __init__(self,num, denom):
#         self.num = num
#         self.denom = denom
        
#     def __str__(self):
#         return str(f'{self.num} / {self.denom}')
#         # return (f'{self.num}/{self.denom}')
    
#     def __add__(self, other):
#         '''adding fractions'''
#         top = self.num * other.denom + self.denom * other.num
#         down = self.denom*other.denom
#         return Fraction(top, down)
    
#     def __sub__(self, other):
#         '''subtracting fractions'''
#         top = self.num * other.denom - self.denom * other.num
#         down = self.denom*other.denom
#         return Fraction(top, down)
    
#     def __mul__(self, other):
#         '''multiplication of fractions'''
#         top = self.num * other.num
#         down = self.denom * other.denom
#         return(Fraction(top, down))
    
#     def __truediv__(self, other):
#         '''division of fractions'''
#         top = self.num * other.denom
#         down = self.denom * other.num
#         return(Fraction(top, down))    
    
#     def inverse(self):
#         return Fraction(self.denom , self.num)
    
    
# f1 = Fraction(3,4)
# f2 = Fraction (2, 3)
# result = f1 / f2

# print(f'{f1} / {f2} = {result}')
# print(f1.inverse())
        
        
        
# '''INHERITANCE'''

# class Animal(object):
#     def __init__(self, age):
#         self.age = age
#         self.name = None
#     def get_age(self):
#         return self.age
#     def get_name(self):
#         return self.name
#     def set_age(self, newage):
#         self.age = newage
#     def set_name(self, newname=""):
#         self.name = newname
#     def __str__(self):
#         return (f'animal: {self.name} : {self.age}')
    
    

# class Cat(Animal):
#     def speak(self):
#         print('Meow')
#     def __str__(self):
#         return f'cat: {self.name}: {self.age}'
        
        

# '''BUBBLE SORT'''
# def bubble_sort(L):
#     swap = False
#     while not swap:
#         swap = True
#         print('bubble sort: ' + str(L))
#         for j in range(1, len(L)):
#             if L[j-1] > L[j]:
#                 swap = False
#                 temp = L[j]
#                 L[j] = L[j-1]
#                 L[j-1] = temp
                
                
# test_list = [4,22,5,1,7,2, 10,3]
# print('')
# print(bubble_sort(test_list))
# print(test_list)



# '''SELECTION SORT'''
# def selection_sort(L):
#     suffix = 0
#     while suffix != len(L):
#         for i in range(suffix, len(L)):
#             if L[i] < L[suffix]:
#                 # printing the values to check the changes 
#                 print(f'After Switching:  {L}')
#                 print("")
    
#                 temp = L[suffix]
#                 # printing the values to check the changes
#                 print(f'{temp} switches from index {suffix} to index {i} swapping with {L[i]}')
#                 print (f'Before Switching: {L}')
                
#                 L[suffix] = L[i] 
#                 L[i] = temp
#         suffix += 1

# def selection_sort(L):
    # suffix = 0
    # while suffix != len(L):
        # # print(suffix)
        # min_index = suffix
        # for i in range(suffix + 1, len(L)):
        #     if L[i] < L[min_index]:
        #         min_index = i
        # L[suffix] = L[min_index]
        # L[min_index] = L[suffix]  # swap
        # suffix += 1


                
# test_list = [4,22,5,1,7,2, 10,3]
# print('')
# print(selection_sort(test_list))
# print(test_list)



# '''MERGING SUBLISTS'''
# def merge(left, right):
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             print(f'Appending item { j + i + 1}: {left[i]}')
#             result.append(left[i])
#             i += 1
#         else:
#             print(f'Appending item {j + i + 1}: {right[j]}')
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         print(f'Appending item {j + i + 1}: {left[i]}')
#         result.append(left[i])
#         i +=1
#     while j < len(right):
#         print(f'Appending item {j + i + 1}: {right[j]}')
#         result.append(right[j])
#         j +=1
#     return result      

# list_a  = [7, 2, 4, 9,8, 0]
# a = sorted(list_a) #makes sure list_a is always sorted
# list_b = [5, 1, 3, 10, 6]
# b = sorted(list_b) #makes sure list_b is always sorted
# print(merge(a, b))
            

class Exams:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        