'''Write a function that takes a string as input and reverse only the vowels of a string.
Example 1:
Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''

class Solution(object):
    def reverseVowels(self, s):
        vogals = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
        word = list(s.strip(''))
        i = 0
        j = len(word) - 1

        while i < j:
            if word[i] in vogals and word[j] in vogals:
                aux = word[i]
                word[i] = word[j]
                word[j] = aux
                i += 1
                j -= 1

            if word[i] not in vogals:
                i += 1

            if word[j] not in vogals:
                j -= 1

        return "".join(word)