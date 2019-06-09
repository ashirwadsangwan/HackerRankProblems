def split_and_join(line):
    split = line.split()
    return "-".join(split)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
