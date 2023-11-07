def is_pal(s):
    def to_char(s):
        result = ''
        s = s.lower()
        for char in s:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                result += char
        return result

    def is_palindrome(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_palindrome(s[1:-1])
    return is_pal(to_char(s))


