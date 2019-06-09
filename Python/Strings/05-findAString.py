def count_substring(string, sub_string):
    
    string = string.strip()
    sub_string = sub_string.strip()
    
    return (sum(1 for i in range(len(string)) if string[i:i+len(sub_string)]==sub_string))


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
