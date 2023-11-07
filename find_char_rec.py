def isIn(char, aStr):
    '''
       char: a single character
       aStr: an alphabetized string

       returns: True if char is in aStr; False otherwise
       '''
    # Your code here
    def sort_asc(aStr):
        return ''.join(sorted(aStr))
    if char == aStr:
        return True
    elif len(aStr) < 2:
        return False
    else:
        astr_len = len(aStr)
        aStr= sort_asc(aStr)
        print(aStr)
        if char == aStr[astr_len//2]:
            return True
        elif char > aStr[astr_len//2]:
            return isIn(char, aStr[astr_len//2:astr_len])
        else:
            return isIn(char, aStr[0:astr_len//2])

print(isIn('t', 'jknqqstvwxzz'))