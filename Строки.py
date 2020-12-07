# minefield

def get_mines(n):
     return [[int(k) for k in input().split(sep=' ')] for i in range(n)]


def fill(i, j, mine_list):
     if [i, j] in mine_list:
          return 1
     else:
          return 0


# initial data

n, m, amount = (int(i) for i in input().split(sep=' '))

mine_list = get_mines(amount)

field = [[fill(i + 1, j + 1, mine_list) for j in range(m)] for i in range(n)]

sum = 0

a = [-1, 0, 1]

for i in range(n):

     for j in range(m):

          if [i + 1, j + 1] in mine_list:
               print('*', end=' ')

               continue

          for di in a:

               for dj in a:

                    ai = i + di

                    aj = j + dj

                    if (0 <= ai < n) and (0 <= aj < m):
                         sum += field[ai][aj]

          print(sum, end=' ')

          sum = 0

     print()

# b=[[1,2,3],[5,2,3],[1,4,3]]
# while True:
#      a = input().split()
#      if a[0]!="end":
#           b.append(a)
#      else:
#           break
# c = len(b)
# i = 0
# j = 0
# while i < len(b):
#      while j < len(i):
#           print(j)
#          j+=1
#      i+=1
# while i < len(b):
#      while j < len(i):
#           print(j)
#          j+=1
#      i+=1
# for line in b:
#     print(*line)


# a, b, c, j = [int(i) for i in input().split()], int(input()), [], 0
# while j!= len(a):
#      if b==a[j]:
#           c.append(j)
#      j+=1
# if c:
#      print(*c)
# else:
#      print("Отсутствует")
#


#





# c = int(input())+1
# a, b = [[i]*i for i in  range(c)],[]
# for j in a:
#      for f in j:
#           b.append(f)
# print(*b[:c-1])


# print(b)
# a,s=[],0
# a.append(int(input()))
# while sum(a)!= 0:
#      a.append(int(input()))
# for i in a:
#      s += i*i
# print(s)