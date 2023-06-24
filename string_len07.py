def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    s=""
    a = len(s1)%2==1
    b = len(s2)%2==1
    c = len(s3)%2==1
    if a and b:
        return f"[{s1},{s2}]"
    if a and c:
        return f"[{s1},{s3}]"
    if b and c:
        return f"[{s2},{s3}]"
    if a:
        return f"[{s1}]"
    if b:
        return f"[{s2}]"
    if c:
        return f"[{s3}]"
    if a and b and c:
        return f"[{s1},{s2},{s3}]"
s1,s2,s3 = "Code","Academy","markazi"
print(main(s1,s2,s3))