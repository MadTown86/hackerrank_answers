def main(n: int):
    l = []
    for number in range(0, n):
        #  Splitting line into parts
        line = input()
        line = line.split(' ')
        if len(line) == 3:
            cmd, index, val = line
        elif len(line) == 2:
            cmd, val = line
        else:
            cmd = line[0]

        if cmd:
            if cmd == 'insert':
                l.insert(int(index), int(val))
                continue
            if cmd == 'print':
                print(l)
                continue
            if cmd == 'append':
                l.append(int(val))
                continue
            if cmd == 'remove':
                l.remove(int(val))
                continue
            if cmd == 'sort':
                l.sort()
                continue
            if cmd == 'pop':
                l.pop()
                continue
            if cmd == 'reverse':
                l.reverse()
                continue

        l.append(input())

if __name__ == '__main__':
    N = int(input())
    main(N)
