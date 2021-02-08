from collections import Counter
if __name__ == '__main__':
    for i in Counter(sorted(input())).most_common(3):
        print(*i)
