#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# # Problem 1
# #### Regions of a DNA genome thhat code for a protein have a relatively high ratio of CG content. Given a strand of DNA determine the percentage of cytosine guanine nucleotides present in the genome. Your method should return the percentage ( between 0.0 and 1.0) of 'c' (cytosine) and 'g'(guanine) in the genome.
# #### Contraints:
# - The String dna contain only the characters 'a','g','c','t' (lowercase)
# - The String dna is between 0 and 1000 characters long (inclusive)

# In[2]:


#1
def DNAratio(input_string):
    if not(re.match("^[atgc]*$", input_string)):
        print ("Only letters a,t,g,c are allowed!")
        return
    elif len(input_string) > 1000:
        print ("Only string between 0 and 1000(inclusive) is characters allowed!")
        return
    else:
        string_len = len(input_string)
        num_gc = input_string.count('g') + input_string.count('c')
        return 'GC Ratio in this DNA strand is:', (num_gc/string_len)
    


# In[3]:


DNAratio('atgccg')


# # Problem 2
# #### In a genome, adenine.and thymine are complements and cytosine and guanine are complements. Although this complementary is a chemical process, you will write code to produce a digital complement for a strand. For a given strand of DNA represented as a string, return the complement of the strand, also as a string.
# #### Constraints
# + The string dna will contain at most 50 characters
# + The characters of dna will be either 'a','g','t','c', all lowercase
# 

# In[4]:


def DNAcomplement(input_string):
    if not (re.match("^[atgc]*$",input_string)):
        print("Only 'a',t','g','c' characters are allowed!")
        return
    elif len(input_string) > 50:
        print("Only the strings with length between 0 and 50(inclusive) are allowed!")
        return
    else:
        complement_string = []
        for i in input_string:
            if   i == 'a':
                complement_string+= 't'
            elif i == 't':
                complement_string+='a'
            elif i == 'g':
                complement_string+='c'
            elif i == 'c':
                complement_string+='g'
        return ''.join(string for string in complement_string)


# In[5]:


DNAcomplement('atttgggccc')


# # Problem 3
# #### Print reverse of a DNA strand 
# #### Contraints:
# + The String DNA contain at most 50 characters
# + The characters of DNA will be one of 'a','g','t','c' all lower-case
# 

# In[10]:


def DNAreverse(input_string):
    if not(re.match("^[atgc]*$",input_string)):
        print("Only 'a','t','g','c' characters are allowed!")
        return
    elif len(input_string) > 50:
        print("Only the strings with length between 0 and 50(inclusive) are allowed!")
    else:
        return input_string[::-1]


# In[12]:


DNAreverse('atgac')


# # Problem 4
# #### Given a DNA strand determine the number of nucleotides/base-pairs in the first protein reading from left-to-right (assume this is 5' to 3'). The beginning of a protein is signalled by the start codon. ATG(not considered part of the protein) and the end of the protein is signalled by a stop codon, one of TAA, TAG, or TGA (also not part of the protein).
# #### Constraints
# + The string DNA contains only the characters 'A','T','G','C' (uppercase)
# + The string DNA is between 0 and 1000 characters long(inclusive)

# In[161]:


def DNAnucleotides(input_string):
    start_str = 'ATG'
    end_str = ['TAA','TAG','TGA']
    ind = []
    count = 0
    if not (re.match("^[ATGC]*$",input_string)):
        print("Only 'A','T','G','C' characters are allowed in the string")
        return
    elif len(input_string) > 1000:
        print("Only the strings with length between 0 and 1000 characters long are allowed!")
        return
    elif(start_str in input_string): 
        #index in input_string for index in end_str)):
        for index in end_str:
            if index in input_string:
                ind.append(input_string.find(index))
        #print(ind)
        start_index = input_string.find(start_str)
        #print(start_index)
        end_index = min(ind)
        #print(end_index)
        i=start_index+1
        if (end_index-start_index==1):
            print('There is no protein, but there is start and stop codon!')
            return -1
        while(i>start_index and (i <= end_index)):
            if (i==end_index):
                return count-2
            count+=1;i+=1
        return -1
        
          
        


# In[162]:


DNAnucleotides('CGATGAAATAGTAATGA')


# # Problem 5
# #### Given a binary string, we encode it into a DNA strands with four bases A,T,G,C where each base represents each change of state: C=X, T=XX, A=XXX, and G=XXXX. For example, binary string 0110001111 will become a DNA strand of CTAG. 
# #### Constraints:
# + The string DNA contains only the characters 'A','T','G','C' (uppercase)
# + The string DNA is between 0 and 1000 characters long(inclusive)
# 

# # Problem 6
# #### From the DNA strand calculated in problem 5 , how can we go back to equilvalent binary string 0110001111?
# 

# # Problem 7
# #### From the DNA strand calculated in problem 5, how can we calculate its reverse complement DNA strand? For example, if our given DNA strand is ATGTCA, the reverse complement strand will be TGACAT
