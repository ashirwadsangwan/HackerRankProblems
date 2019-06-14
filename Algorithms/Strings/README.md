### [Problem 1 : SuperReducedString](https://www.hackerrank.com/challenges/reduced-string/problem)
Steve has a string of lowercase characters in range `ascii[‘a’..’z’]`. He wants to reduce the string to its shortest length by doing a series of operations. In each operation he selects a pair of adjacent lowercase letters that match, and he deletes them. For instance, the string aab could be shortened to b in one operation.

Steve’s task is to delete as many characters as possible using this method and print the resulting string. If the final string is empty, `print Empty String`.

```python
def superReducedString(s):
    if not s:
        return 'Empty String'
    for i in range(0, len(s)):
        if i< len(s)-1:
            if s[i]==s[i+1]:
                return superReducedString(s[:i]+s[i+2:])
    return s

```
