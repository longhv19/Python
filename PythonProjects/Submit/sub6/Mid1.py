import math
from typing import re


def getTopWord(filename, n):
    '''
    Hàm trả lại danh sách (list) n từ có số lần nhiều nhất trong file văn bản filename.
    Trong file văn bản filename, mỗi từ phân cách nhau bởi dấu cách
    Danh sách kết quả được sắp xếp giảm dần theo thứ tự từ điển của các từ.
    Nếu 2 từ có tần số xuất hiện bằng nhau thì ưu tiên từ có thứ tự từ điển lớn hơn
    (ví dụ 'd' > 'c' vì vậy nếu 'd' và 'c' có cùng số lần xuất hiện thì lấy 'd')
    Ví dụ, file văn bản có nội dung như sau:
    "
    a b c a a a b c d f d a d a f g s g h f s s a
    a g h b c e f g m n j s a r t y y u v z x k l a
    "

    danh sách các từ cùng số lần xuất hiện sắp xếp theo số lần xuất hiện giảm dần, từ giảm dần theo thứ tự từ điển như sau:

    [('a', 10), ('s', 4), ('g', 4), ('f', 4), ('d', 3), ('c', 3), ('b', 3), ('y', 2)
    , ('h', 2), ('z', 1), ('x', 1), ('v', 1), ('u', 1), ('t', 1), ('r', 1), ('n', 1)
    , ('m', 1), ('l', 1), ('k', 1), ('j', 1), ('e', 1)]

    Như vậy với n = 6, kết quả là

    ['s', 'g', 'f', 'd', 'c', 'a']


    Chú ý, file văn bản có nhiều dòng và không có ký tự unicode
    Nếu n > số từ thì kết quả là toàn bộ danh sách các từ.
    '''
    f = open(filename,'r', encoding='utf-8')
    token = f.read().split()
    w = []  #dict
    c = []
    res = []
    counts = ()
    for t in token:
        if t not in w:
            w.append(t)
    for j in w:
        count = 0
        for w in token:
            if(w == j):
                count += 1
        counts = (j,count)
        c.append(counts)
    c.sort(key= lambda x: x[1], reverse= False)
    c.reverse()
    if(n > len(c)):
        res = c
    else:
        for i in range(n):
            res.append(c[i])
    Top = []
    for counts in c:
        Top.append(counts[0])
    Top.sort(reverse=True)
    return Top


    # pass


def getVector(filename, topword):
    '''
        Hàm này trả lại danh sách (list) số nguyên tương ứng với vector biểu diễn văn bản trong file filename.
        phần tử thứ i trong danh sách là số lần từ topword[i] xuất hiện trong văn bản.

        ví dụ văn bản là
        "
        a b c a a a b c d f d a d a f g s g h f s s a
        a g h b c e f g m n j s a r t y y u v z x k l a
        "


        topword = ['s', 'g', 'f', 'd', 'a']

        kết quả là: [4, 4, 4, 3, 10]
    '''


    pass

def numerator(u,v):
    n = sum([u[i]*v[i] for i in range(0,len(u))])
    return n

def denominator(u):
    x = sum([i**2 for i in u])
    return math.sqrt(x)


def getCosineSim(u, v):
    '''
        Phương thức tính cosine góc tạo bởi hai vector u, v

        cosine(u,v) = (u.v)/(||u||x||v||)

        ví dụ với u = [1,2,3,4], v = [1,2,1,1], kết quả làm tròn đến 5 chữ số là: 0.82808
    '''
    num = numerator(u,v)
    den = denominator(u)*denominator(v)
    cosin = num/den
    return cosin

    # pass

def sinhTaylor(x, e):
    '''
     Viết chương trình tính sinh(x) theo khai triển Taylor,
     trong đó e là sai số để xác định  thời điểm dừng thuật toán,
     Thuật toán dừng lại tại số hạng Pi nếu |Pi - Pi-1| <= e

     ví dụ x = 5.5, e = 0.00001 kết quả làm tròn đến 5 chữ số là: 122.34392
          nhưng với e = 0.5     kết quả làm tròn đến 5 chữ số là: 122.34289

    '''
    result = x
    a = x
    i = 1
    while(a>e):
        a = a * (pow(x,2)) / (2 * i * (2 * i + 1))
        result += a
        i = i+1
    a = a * (pow(x, 2)) / (2 * i * (2 * i + 1))
    result += a
    return result
    # pass


'''
    Chú ý, các phương thức sẽ được gọi đến để chấm điểm, 
    do vậy bài nộp của sinh viên cần phải bỏ hết (hoặc comment #) các lệnh in ra màn hình

'''


def testDemo():
    print(getTopWord('text.txt', 5))
    print(getVector('text.txt', getTopWord('text.txt', 5)))

    print(round(getCosineSim([1, 2, 3, 4], [1, 2, 1, 1]), 5))

    print(round(sinhTaylor(5.5, 0.5), 5))


'''
Bỏ comment lệnh testDemo() dưới đây để test chương trình, và comment lại lệnh đó khi nộp bài
'''
testDemo()
