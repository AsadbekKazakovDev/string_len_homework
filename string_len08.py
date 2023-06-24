def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    s1 = ""
    if len(s)%2==1:
        s1=s[len(s)//2]
    if len(s)%2==0:
        s1 = s[len(s)//2-1:len(s)//2+1]
    return s1
s = "cool"
print(main(s))
s = "abcdf"
print(main(s))