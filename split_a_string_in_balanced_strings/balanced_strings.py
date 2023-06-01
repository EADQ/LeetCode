# class Solution(object):
    # def balancedStringSplit(self, s):
        # """
        # :type s: str
        # :rtype: int
        # """
# def balancedStringSplit(s):
    # balance = 0
    # count = 0
    # for i in s:
        # if i == 'R':
            # balance +=1
        # else:
            # balance -= 1

        # if balance == 0:
            # count +=1

        # return count

# s = ['RRLL']
# test = balancedStringSplit(s)
# print(test)


def balanced_string_split(s):
    balance = 0
    indices = []
    for i, char in enumerate(s):
        if char == 'R':
            balance += 1
        else:  # char == 'L'
            balance -= 1
        if balance == 0:
            indices.append(i)
    substrings = [s[i:j+1] for i, j in zip([0]+indices, indices+[(len(s)-1)])]
    return substrings
