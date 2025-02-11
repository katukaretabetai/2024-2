import re
                
def calc(A, B):
    ai = str(A)
    bi = str(B)
    p = re.compile(r'^\d+$')  # 整数のみマッチする正規表現

    if p.fullmatch(ai) and p.fullmatch(bi):
        a = int(ai)
        b = int(bi)
        if 1 <= a <= 999 and 1 <= b <= 999:
            return a * b
        else:
            return -1
    else:
        return -1
        
def main():
    while True:
        A = input('input A (type "end" to quit): ')
        if A == 'end':
            break
        B = input('input B: ')
        print('input A * input B =', calc(A, B))

if __name__ == '__main__':
    main()
