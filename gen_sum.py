import os

def write(a):
    with open('./SUMMARY.md', 'a') as f:
        f.writelines(a + '\n')

def add(d, a):
    from1 = a//100*100 + 1

    if from1 not in d:
        d[from1] = {}

    from2 = a//10*10+1
    if from2 not in d[from1]:
        d[from1][from2] = []
    d[from1][from2].append(a)

def flush(d):
    for from1 in d:
        write('* Problem %d-%d' % (from1, from1+99))
        for from2 in d[from1]:
            write('\t* Problem %d-%d' % (from2, from2+9))
            for key in d[from1][from2]:
                write('\t\t* [Problem %d](./solutions/%d.md)' % (key, key))

if __name__ == '__main__':
    os.remove('./SUMMARY.md')
    write('* [序言](./README.md)')
    dic = {}
    for file in os.listdir('./solutions'):
        add(dic, int(file[:len(file)-3]))
    flush(dic)
