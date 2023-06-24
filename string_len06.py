def main(s1,s2):
    """
    Given two strings, s1 and s2. Return the shortest length between them.
    Args:
        s1: string
        s2: string
    Returns:
        shortest string
    """
    s=""
    if len(s1)>len(s2):
        s=s2
    else:
        s=s1
    return s
s1,s2 = "code","academy"
print(main(s1,s2))