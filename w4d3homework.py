#########COdewars PROBLEM 1 #####link-------https://www.codewars.com/kata/563e320cee5dddcf77000158/python
           
            # It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.
            # Return the average of the given array rounded down to its nearest integer.
            # The array will never be empty.


#my first attempt
def get_average(marks):
    sum = 0
    for x in marks:
        sum = sum + x
        num = len(marks)
        ans = sum/num
    return int(ans)
print(get_average([2,2,4,2]))





#my optimizition attempt using the built in function SUM
# fewer lines of code

def get_average(marks):
    return sum(marks) // len(marks)
print(get_average([2,2,4,2]))



######## Codewars PROBLEM 2  #######-------https://www.codewars.com/kata/reviews/53dbd54c3721866025000604/groups/642eca837be37d0001d8ca2b
   
              #In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.



#my first attempt
def filter_list(l):
    lst1=[]
    for item in l:
        if type(item)== int:
            lst1.append(item)
         
    return lst1
print(filter_list([1,2,'a','b']))    



#my second attempt using comprehention

def filter_list(l):
  'return a new list with the strings filtered out'
  return [item for item in l if type(item) is not str]
print(filter_list([1,2,'a','b']))


######## Codewars PROBLEM 3  #######-------https://www.codewars.com/kata/reviews/554e4dbd33d156cfbf0000ff/groups/642f52eba262d00001d7603f

        # Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

        # If you want to know more: http://en.wikipedia.org/wiki/DNA

        # In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

        # More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

        # Example: (input --> output)

        # "ATTGC" --> "TAACG"
        # "GTAT" --> "CATA"

#my first attempt
def DNA_strand(dna):
    es=""
    for l in dna:
        
        if l == "A":
            es+="T"
        if l == "T":
            es+="A"
        if l == "C":
            es+="G"
        if l == "G":
            es+="C"
    return es
print(DNA_strand("GTAT"))  

#my second attempt using comprehention
def DNA_strand(dna):
    return ''.join([{'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}[letter] for letter in dna])  
print(DNA_strand("GTAT")) 
        