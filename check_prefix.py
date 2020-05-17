def check_prefix(string,prefix):
    if len(prefix)>len(string):
        return False
    i=0
    while i<len(prefix):
        if prefix[i]!=string[i]:
            return False
        i=i+1

    return True


print(check_prefix("abcdef","abc"))


print(check_prefix("abcdef","abcf"))