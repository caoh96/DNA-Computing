#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re


# # Problem 1
# #### Regions of a DNA genome thhat code for a protein have a relatively high ratio of CG content. Given a strand of DNA determine the percentage of cytosine guanine nucleotides present in the genome. Your method should return the percentage ( between 0.0 and 1.0) of 'c' (cytosine) and 'g'(guanine) in the genome.
# #### Contraints:
# - The String dna contain only the characters 'a','g','c','t' (lowercase)
# - The String dna is between 0 and 1000 characters long (inclusive)

# In[ ]:


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
    


# In[ ]:


DNAratio('atgccg')


# # Problem 2
# #### In a genome, adenine.and thymine are complements and cytosine and guanine are complements. Although this complementary is a chemical process, you will write code to produce a digital complement for a strand. For a given strand of DNA represented as a string, return the complement of the strand, also as a string.
# #### Constraints
# + The string dna will contain at most 50 characters
# + The characters of dna will be either 'a','g','t','c', all lowercase
# 

# In[ ]:


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


# In[ ]:


DNAcomplement('atttgggccc')


# # Problem 3
# #### Print reverse of a DNA strand 
# #### Contraints:
# + The String DNA contain at most 50 characters
# + The characters of DNA will be one of 'a','g','t','c' all lower-case
# 

# In[ ]:


def DNAreverse(input_string):
    if not(re.match("^[atgc]*$",input_string)):
        print("Only 'a','t','g','c' characters are allowed!")
        return
    elif len(input_string) > 50:
        print("Only the strings with length between 0 and 50(inclusive) are allowed!")
    else:
        return input_string[::-1]


# In[ ]:


DNAreverse('atgac')


# # Problem 4
# #### Given a DNA strand determine the number of nucleotides/base-pairs in the first protein reading from left-to-right (assume this is 5' to 3'). The beginning of a protein is signalled by the start codon. ATG(not considered part of the protein) and the end of the protein is signalled by a stop codon, one of TAA, TAG, or TGA (also not part of the protein).
# #### Constraints
# + The string DNA contains only the characters 'A','T','G','C' (uppercase)
# + The string DNA is between 0 and 1000 characters long(inclusive)

# In[ ]:


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
        
          
        


# In[ ]:


DNAnucleotides('CGATGAAATAGTAATGA')


# # Problem 5
# #### Given a binary string, we encode it into a DNA strands with four bases A,T,G,C where each base represents each change of state: C=X, T=XX, A=XXX, and G=XXXX. For example, binary string 0110001111 will become a DNA strand of CTAG. 
# #### Constraints:
# + The string DNA contains only the characters 'A','T','G','C' (uppercase)
# + The string DNA is between 0 and 1000 characters long(inclusive)
# 

# In[310]:


def BinarytoDNA(input_string):
    i=0
    DNA = []
    while i in range(len(input_string)):
        if (len(input_string) - i > 3):
            if ((input_string[i] == input_string[i+1]) and (input_string[i+1] == input_string[i+2])
                and (input_string[i+2] == input_string[i+3])):
                DNA.append('G')
                i += 4
            elif ((input_string[i] == input_string[i+1]) and (input_string[i+1] == input_string[i+2])):
                DNA.append('A')
                i += 3
            elif (input_string[i] == input_string[i+1]):
                DNA.append('T')
                i+= 2
            else:
                DNA.append('C')
                i+=1       
        elif (len(input_string) - i -1 == 3):
            if ((input_string[i] == input_string[i+1]) and (input_string[i+1] == input_string[i+2])
                and (input_string[i+2] == input_string[i+3])):
                DNA.append('G')
                break
            elif ((input_string[i] == input_string[i+1]) and (input_string[i+1] == input_string[i+2])):
                DNA.append('A')
                i +=3
            elif (input_string[i] == input_string[i+1]):
                DNA.append('T')
                i+= 2
            else:
                DNA.append('C')
                i+=1
        elif (len(input_string) -1-i == 2):
            if ((input_string[i] == input_string[i+1]) and (input_string[i+1] == input_string[i+2])):
                DNA.append('A')
                break
            elif (input_string[i] == input_string[i+1]):
                DNA.append('T')
                i+= 2
            else:
                DNA.append('C')
                i+=1
        elif (len(input_string)-i-1 ==1):
            if (input_string[i] == input_string[i+1]):
                DNA.append('T')
                break
            else:
                DNA.append('CC')
                break
        
    return ''.join(string for string in DNA)
                


# In[312]:


BinarytoDNA('0110001111100')


# # Problem 6
# #### From the DNA strand calculated in problem 5 , how can we go back to equilvalent binary string 0110001111?
# 

# For DNA strands with n bases, there will be 2^n possibilities to decode the DNA strings to binary. Therefore, we cannot go back to binary from DNA strand using this technique

# # Problem 7
# #### From the DNA strand calculated in problem 5, how can we calculate its reverse complement DNA strand? For example, if our given DNA strand is ATGTCA, the reverse complement strand will be TGACAT.

# # Problem 8
# #### Given a binary string, we encode it into a DNA strands with four bases A,T,G,C where each base represents each change of state: T=X, A=XX, and G=XXX and C to indicate the next base represents string with 1. For example, binary string 0110001111 will become a DNA strand of TCAGCGCT. 
# #### Constraints:
# + The string DNA contains only the characters 'A','T','G','C' (uppercase)
# + The string DNA is between 0 and 1000 characters long(inclusive)
# 
# 
#                   

# In[328]:


def BinarytoDNA2(input_string):
    i=0
    DNA = []
    while i in range(len(input_string)):
        if (len(input_string) - i > 2):
            if(input_string[i]== '1'):
                if ((input_string[i] == input_string[i+1]) and (input_string[i+1] == input_string[i+2])):
                    DNA.append('CG')
                    i += 3
                elif (input_string[i] == input_string[i+1]):
                    DNA.append('CA')
                    i += 2
                else:
                    DNA.append('CT')
                    i+= 1
            else:
                if ((input_string[i] == input_string[i+1]) and (input_string[i+1] == input_string[i+2])):
                    DNA.append('G')
                    i += 3
                elif (input_string[i] == input_string[i+1]):
                    DNA.append('A')
                    i += 2
                else:
                    DNA.append('T')
                    i+= 1
        elif (len(input_string) - i -1 == 2):
            if(input_string[i]== '1'):
                if ((input_string[i] == input_string[i+1]) and (input_string[i+1] == input_string[i+2])):
                    DNA.append('CG')
                    break
                elif (input_string[i] == input_string[i+1]):
                    DNA.append('CA')
                    i += 2
                else:
                    DNA.append('CT')
                    i+= 1
            else:
                if ((input_string[i] == input_string[i+1]) and (input_string[i+1] == input_string[i+2])):
                    DNA.append('G')
                    break
                elif (input_string[i] == input_string[i+1]):
                    DNA.append('A')
                    i += 2
                else:
                    DNA.append('T')
                    i+= 1
        elif (len(input_string) -1-i == 1):
            if(input_string[i]== '1'):
                if (input_string[i] == input_string[i+1]):
                    DNA.append('CA')
                    break
                else:
                    DNA.append('CT')
                    i+= 1
            else:
                if (input_string[i] == input_string[i+1]):
                    DNA.append('A')
                    break
                else:
                    DNA.append('T')
                    i+= 1
        else:
            if(input_string[i] == '1'):
                DNA.append('CT')
                break
            else:
                DNA.append('T')
                break
        
    return ''.join(string for string in DNA)
                


# In[338]:


BinarytoDNA2('0110001111')


# In[351]:


BinarytoDNA2('1000000111111')


# # Problem 9
# #### From problem 8 can we go from DNA strand back to Binary string? 

# In[352]:


def DNAtoBinary(input_string):
    i=0
    Binary=[]
    while i in range(len(input_string)):
        if (len(input_string) -i >2):
            if input_string[i] == 'C':
                if input_string[i+1] == 'T':
                    Binary.append('1')
                    i+=2
                elif input_string[i+1] == 'A':
                    Binary.append('11')
                    i+=2
                elif input_string[i+1] == 'G':
                    Binary.append('111')
                    i+=2
            elif input_string[i] == 'T':
                Binary.append('0')
                i+=1
            elif input_string[i] == 'A':
                Binary.append('00')
                i+=1
            elif input_string[i] == 'G':
                Binary.append('000')
                i+=1
        elif (len(input_string) - i - 1 == 1):
            if input_string[i] == 'C':
                if input_string[i+1] == 'T':
                    Binary.append('1')
                    break
                elif input_string[i+1] == 'A':
                    Binary.append('11')
                    break
                elif input_string[i+1] == 'G':
                    Binary.append('111')
                    break
            else:
                if input_string[i] == 'T':
                    Binary.append('0')
                    i+=1
                elif input_string[i] == 'A':
                    Binary.append('00')
                    i+=1
                elif input_string[i] == 'G':
                    Binary.append('000')
                    i+=1
        else:
            if input_string[i] == 'T':
                    Binary.append('0')
                    break
            elif input_string[i] == 'A':
                    Binary.append('00')
                    break
            elif input_string[i] == 'G':
                    Binary.append('000')
                    break
    return ''.join(string for string in Binary)
            


# In[348]:


DNAtoBinary('CTTCAACGGAT')


# In[349]:


DNAtoBinary('CTTTCAAACGGGAT')


# In[ ]:





# In[ ]:




