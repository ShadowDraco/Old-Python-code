"""
# RECURSIVE REVERSE TEXT

def reverse(text):
    if len(text) < 2:
        return text
    else:
        print(text[-1], end = "")
        return reverse(text[0 : len(text) - 1])
            

##
text = ''.join(input("Enter text: ").split()).upper() # ask user for text                                               # print empty line
rev_text = reverse(text)                              # reverse text
print(rev_text)                                       # print reversed string
##
"""
##
##
##

"""
# BINARY KMERS

import random
import math
# use a set so that there can be no repeats

def generate_kmers(k, mers = set()):
    #possible combinations
    possible = math.factorial(k) + math.factorial(2)
    if k == 1:
        return ['0', '1']
    elif k == 2:
        return ['00', '01', '10', '11']
    else: 
        #Use a variable to append a string rather than a list to mers
        temp = ""
        # until you reach the maxium number of combinations generate 
        # a random string of numbers and check if it already exists then repeat
        for i in range(possible):
            if len(mers) == possible:
                final = list(mers) 
                return final
            else:
                for j in range(k):
                    # add a random string
                    temp += str(random.randrange(2))
                if temp in mers:
                    # if it already existed run the loop again but don't 
                    #call the function to avoid depth limit
                    temp = ""
                else:
                    mers.add(temp)
                    generate_kmers(k, mers)



##
k = int(input("Enter k: ")) # ask user for number
print()                     # print empty line
kmers = generate_kmers(k)   # generate all k-mers
print(kmers)                # print the result

##

"""
#
#
#
"""
 # BINARY KMERS TWO

def generate_kmers(k, mers = ['0', '1']):

    if k == 1:

        return mers
    if k > 1:
        for i in range(k-1):
            copy = list(mers)

            for j in range(len(mers)):
                mers[j] += '0'

                copy[j] += '1'
            for p in copy:
                if p not in mers:
                    mers.append(p)

        return mers


k = int(input("Enter k: ")) # ask user for number
print()                     # print empty line
kmers = generate_kmers(k)   # generate all k-mers
print(kmers)                # print the result
"""
#
#
#
"""
# BINARY KMERS THREE

def generate_kmers(k):
    if k == 1:
        return ['0', '1']
    else:
        copy = []
        mers = generate_kmers(k-1)
        for mer in mers:
            copy.append(mer + '0')
            copy.append(mer+ '1')

        return copy

k = int(input("Enter k: ")) # ask user for number
print()                     # print empty line
kmers = generate_kmers(k)   # generate all k-mers
print(kmers)                # print the result

"""
#
#
#
""" PARSE RECEIPT 

def parse_receipt():
    ingredients = ["powdered sugar", "granulated sugar", "almond flour", "salt", "egg yolks", "vanilla extract"]
    counts = []
    ing = []
    name = ""
    total = 0
    made = 0
    text = open("Testing Files/receipt.txt")
    
    for line in text.readlines():

        if line[0 : 4] == "Your":
            for i in range(len(line)):
                if line[i] == ":":
                    name = line[i+2 : len(line)]

        if line[0 : 5] == "TOTAL":
            for i in range(len(line)):
                if line[i] == "$":
                    total = line[i+1 : len(line)]
                               
        if line[0].isdigit():
            for i in range(len(line)):
               
                if line[i+1].isdigit():
                    counts.append(int(line[i] + line[i+1]))
                    break
                else:
                    counts.append(int(line[i]))
                    break
            holder = line.strip().split("...")
            ing.append(holder[1])
           
        if len(ing) > 5:
                can_make = True
                while can_make:
                 
                    for i in counts:
                        if i > 0:
                            i -= 1
                        else:
                            can_make = False
                    made += 1
       
        else: 
            continue
    print(name.strip().strip("!"))
    print(made) 
    print("$" + str(total))

parse_receipt()

"""
#
#
#
""" Macaron Message

def macaron_message():
    ingredients = ["powdered sugar", "granulated sugar", "almond flour", "salt", "egg yolks", "egg whites", "vanilla extract"]
    good_ingredients = 0
    counts = []
    ing = []
   
    text = open("Testing Files/receipt.txt")
    for line in text.readlines():
        if line[0].isdigit():
                for i in range(len(line)):
                
                    if line[i+1].isdigit():
                        counts.append(int(line[i] + line[i+1]))
                        break
                    else:
                        counts.append(int(line[i]))
                        break
                holder = line.strip().split("...")
                ing.append(holder[1])

        
    file = open("message.txt", "w")  
    for i in ing:
        if i in ingredients:
            good_ingredients += 1 
            print(i) 
       
    if good_ingredients > 5:
        file.write("Fresh macarons being baked now!")
    else:
        file.write("We're all sold out!")
    return file
       
macaron_message()

"""
#
#
#
"""Add to Budget 

def add_to_budget(spent, earned):
    t = open("budget.txt", "a")
    profit = earned - spent
    line = "$" + str(spent) + ",  $" + str(earned) + ",  $" + str(profit)
    t.write(line)
    
add_to_budget(20, 50)


"""
#
#
#
""" Counting words from file
# YOUR CODE HERE
def count(filename):
    file = open("Testing Files/" +filename)
    all_words = []
    count_dict = dict()
    
    for line in file:
        words = line.split(" ")
        for word in words:
            all_words.insert(len(all_words), word)

    for word in words:
        count_dict[word] = 0
    
    for word in words:
        if word in count_dict.keys():
            count_dict[word] += 1
            

    return count_dict
    

### DO NOT MODIFY ###
filename = input("Enter filename: ").strip() # ask user for filename
print()                                      # print empty line
counts = count(filename)                     # count words
print(counts)                                # print result
### DO NOT MODIFY ###

"""
#
#
#
""" Fixing Grades

# YOUR CODE HERE
def fix_grades(in_filename, bonus, out_filename):
    in_file = open("Testing Files/" + in_filename)
    out_lines = []
    
    for line in in_file:
        values = line.strip().split(",")
        
        for i in range(len(values)):
            if values[i].replace(".","").isdigit():
                values[i]= float(values[i]) + bonus
    
        out_lines.append(values)

    print(out_lines)
    out_file = open("Testing Files/" +out_filename, "w")
    for line in out_lines:
        for i in range(len(line)):
            out_file.write(str(line[i]))
            if i < len(line) - 1:
                out_file.write(",")
            
        out_file.write("\n")
        

### DO NOT MODIFY ###
in_filename = input("Enter input CSV filename: ").strip()   # ask user for input filename
bonus = float(input("Enter bonus: "))                       # ask user for bonus
out_filename = input("Enter output CSV filename: ").strip() # ask user for output filename
print()                                                     # print empty line
fix_grades(in_filename, bonus, out_filename)                # fix grades
### DO NOT MODIFY ###

"""