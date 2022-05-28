# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(str1, str2):
    # [assignment] Add your code here
  
# convert both the strings into lowercase
    str1 = str1.lower()
    str2 = str2.lower()

# check if length is same
    if(len(str1) == len(str2)):

        # sort the strings
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)


    if(sorted(str1)==sorted(str2)):
      print("True")

    else:
        
      print("False")

    return True

str1 = "tayo"
str2 = "remi"

find_anagram(str1, str2)
