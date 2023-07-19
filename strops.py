#Program to check the palindrome words in a phrase

phrase = input('enter a phrase for checking the plaidrome words : ')

ph_lst = phrase.split(' ')

print(type(ph_lst))

palin_lst, palin_lstpos = [], []
non_palin_lst, non_palin_lstpos = [], []

def check_palin():
    i, palin_nos, non_palin = 0, 0, 0
    # Loop trhough the list to check the number of words of palidrom form
    while i < len(ph_lst):
        cur_str = ph_lst[i]
    #    print('current string is : ', cur_str)
        rev_str = cur_str[::-1]
    #    print('Reverse of current string is : ', rev_str)
        if cur_str == rev_str and len(cur_str) > 1:
            palin_nos += 1
            palin_lst.append(ph_lst[i])   
            palin_lstpos.append(i + 1)                 
        else:
            non_palin += 1
            non_palin_lst.append(ph_lst[i])
            non_palin_lstpos.append(i + 1)
        i += 1
    return palin_nos, non_palin

# Calling the function to check the plaidrome and non palidrome words in the phrase
pln, non_pln = check_palin()
# display the number of occurences og palindrome and non palindrome words
print ('The number of palindrome words in the list is : ', pln)
print ('The number of non palindrome words in the list is : ', non_pln)
print('palin list : ', palin_lst) 
print('palin list position : ', palin_lstpos) 
print('Non palin list : ', non_palin_lst) 
print('Non palindrome words in list position : ', non_palin_lstpos) 