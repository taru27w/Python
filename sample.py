# print("hello!")
# print("hello!")

# # C117:大量出店
# # 店舗数と月数を取得
# input_line1 = input().split()
# tenposu = int(input_line1[0])
# tukisu = int(input_line1[1])

# # 建設費、人件費、利益の順で取得
# input_line2 = input().split()
# kensetsuhi = int(input_line2[0])
# jinkenhi = int(input_line2[1])
# rieki = int(input_line2[2])

# # 赤字店舗
# akaji =[]

# for x in range(tenposu):
#     hanbaisu = int(input())
#     if kensetsuhi + jinkenhi * tukisu > rieki * hanbaisu:
#         akaji.append(x+1)


# # C020:残り物の量
# # 最初のサイズと割合を取得
# input_line1 = input().split()
# shokisize = float(input_line1[0])
# wariai1 = float(input_line1[1])
# wariai2 = float(input_line1[2])

# print(shokisize-shokisize*wariai1/100-(shokisize-shokisize*wariai1/100)*wariai2/100)

# # 盤面情報
# # 最初のサイズと割合を取得
# H, W, N = map(int, input().split())
# S = [list(input()) for _ in range(H)]
# for _ in range(N):
#   y, x = map(int, input().split())
#   print(S[y][x])

# # 盤面情報
# # 最初のサイズと割合を取得
# H, W, N = map(int, input().split())

# # 2次元リストに内包表記でつっこむ
# S = [list(input()) for _ in range(H)]

# # 指定の座標の値を変更
# for _ in range(N):
#   y, x = map(int, input().split())
#   S[y][x]='#'

# for y in range(h):
#     print("".join(s[y]))

# # 盤面情報 左右判定
# # 最初のサイズと割合を取得
# H, W = map(int, input().split())

# # 2次元リストに内包表記でつっこむ
# S = [list(input()) for _ in range(H)]

# # 横が#を判定する
# for y in range(h):
#     for x in range(w):
#         if x == 0 or s[y][x - 1] == "#":
#             if x == w - 1 or s[y][x + 1] == "#":
#                 print(y, x)

# # 盤面情報 縦判定
# # 最初のサイズと割合を取得
# h, w = map(int, input().split())

# # 2次元リストに内包表記でつっこむ
# s = [list(input()) for _ in range(h)]

# # 縦が#を判定する
# for y in range(h):
#     for x in range(w):
#         if y == 0 or s[y -1][x] == "#":
#             if y == h - 1 or s[y + 1][x] == "#":
#                 print(y, x)


# # 盤面情報 縦横判定
# # 最初のサイズと割合を取得
# h, w = map(int, input().split())

# # 2次元リストに内包表記でつっこむ
# s = [list(input()) for _ in range(h)]

# # 縦が#を判定する
# for y in range(h):
#     for x in range(w):
#         if y == 0 or s[y -1][x] == "#":
#             if x == 0 or s[y][x-1] == "#":
#                 if y == h - 1 or s[y + 1][x] == "#":
#                     if x == w - 1 or s[y][x +1] == "#":
#                         print(y, x)


# # 盤面情報 縦横判定
# # 最初のサイズと割合を取得
# y, x ,n = map(int, input().split())

# # 移動方向をリスト可
# idou = [input() for _ in range(n)]

# for i in idou:
#     if i =='N':
#         y-=1
#     elif i =='S':
#         y+=1
#     elif i =='W':
#         x-=1
#     elif i =='E':
#         x+=1
#     print(y,x)

# Bランク特訓
# kosu = int(input())
# result = 0

# for _ in range(kosu):
#     y = int(input())
#     if y >= 5:
#         result +=y

# print(result)

# n = int(input())
# result = 0

# for _ in range(n):
#     x = [int(y) for y in input().split()]
#     if x[0]==x[1]:
#         result+=x[0]*x[1]
#     else:
#         result+=x[0]+x[1]

# print(result)

# s,e = map(int,input().split())
# strlist = list(input())
# for x in range(s-1,e):
#     strlist[x]=strlist[x].upper()
# # strlist[e-1]=strlist[e-1].upper()
# # str[s] = 'a'
# print("".join(strlist))

# n = input()
# dic = {}

# for x in range(n):
#     line = input().split()
#     dic[int(line[1])] = line[0]

# result = sorted(dic)

# for r in result:
#     print(r[1])

# n = int(input())
# temp = {}

# for _ in range(n):
#     line = input().split()
#     # キーを含む場合は、元の値に＋
#     if line[0] in temp:
#         temp[line[0]]+=int(line[1])
#     else :
#         temp[line[0]]=int(line[1])

# result = sorted(temp.items(),key = lambda x:x[1],reverse=True)

# for r in result:
#     print(r[0],r[1])

# import string
# s = input()
# e = input()
# target = input()

# alphabetlist = string.ascii_uppercase

# i_s = alphabetlist.find(s)
# i_e = alphabetlist.find(e)
# i_target = alphabetlist.find(target)

# # print(i_s)

# if i_s > i_e:
#     print('false')
# else:
#     print(i_s <= i_target and  i_target <= i_e)


# dic = {}

# for y in range(5):
#     line = list(input())
#     for x in range(5):
#         dic[(y,x)]=line[x]

# # 縦判定
# for x in range(5):
#     if dic[(0,x)]==dic[(1,x)] and dic[(0,x)]==dic[(2,x)] and dic[(0,x)]==dic[(3,x)] and dic[(0,x)]==dic[(4,x)] :
#         print(dic[(0,x)])

# # 横判定
# for y in range(5):
#     if dic[(y,0)] == dic[(y,1)] and dic[(y,0)] == dic[(y,2)] and dic[(y,0)] == dic[(y,3)] and dic[(y,0)] == dic[(y,4)]:
#         print(dic[(y,0)])

# # ななめ判定
# if dic[(0,0)] == dic[(1,1)] == and dic[(0,0)] == dic[(2,2)] == and dic[(0,0)] == dic[(3,3)] == and dic[(0,0)] == dic[(4,4)]:
#     print(dic[(2,2)])
# elif dic[(0,4)] == dic[(1,3)] == and dic[(0,4)] == dic[(2,2)] == and dic[(0,4)] == dic[(3,1)] == and dic[(0,4)] == dic[(4,0)]): 
#     print(dic[(2,2)])
# else 
#     print('D')



# n= int(input())
# person={}
# master ={}

# for i in range(n):
#     line = list(input().split())
#     person[line[0]]= line[1]

# m= int(input())

# for i in range(m):
#     line = list(input().split())
#     master[line[0]]= line[1]
    
# for i in person.keys():
#     print(i,master[i])

# # 縦横座標
# x,y,n= list(input().split())
# zahyo =[int(x),int(y)]

# # 向いている方角
# bector = 0 #0:北、1:東ｍ、2:南、3:西

# # 方角を出す関数
# def newbector(bector,lorr):

#     # 左右で方角を変更
#     if(lorr=='L'):
#         bector-=1
#         if(bector==-1):
#             bector=3
#     else:
#         bector+=1
#         if(bector==4):
#             bector=0

#     return bector

# # 座標を出す関数
# def newzahyo(zahyo,bector,lorr):

#     if(bector==0):
#         if(lorr=='L'):
#             zahyo[0]-=1
#         else:
#             zahyo[0]+=1
#     if(bector==2):
#         if(lorr=='L'):
#             zahyo[0]+=1
#         else:
#             zahyo[0]-=1
#     if(bector==1):
#         if(lorr=='L'):
#             zahyo[1]-=1
#         else:
#             zahyo[1]+=1
#     if(bector==3):
#         if(lorr=='L'):
#             zahyo[1]+=1
#         else:
#             zahyo[1]-=1

#     return zahyo


# for x in range(int(n)):
#     lorr = input()
#     zahyo = newzahyo(zahyo,bector,lorr)
#     bector = newbector(bector,lorr)

#     print(zahyo[0],zahyo[1])




# # へび
# h,w,y,x,n= map(int,input().split())


# # マップ
# # 2次元リストに内包表記でつっこむ
# s = [list(input()) for _ in range(h)]
# zahyo =[x,y]

# # 向いている方角
# bector = 0 #0:北、1:東ｍ、2:南、3:西

# # 方角を出す関数
# def newbector(bector,lorr):

#     # 左右で方角を変更
#     if(lorr=='L'):
#         bector-=1
#         if(bector==-1):
#             bector=3
#     else:
#         bector+=1
#         if(bector==4):
#             bector=0

#     return bector

# # 座標を出す関数
# def newzahyo(zahyo,bector):

#     if(bector==0):
#         zahyo[1]-=1
#     if(bector==2):
#         zahyo[1]+=1
#     if(bector==1):
#         zahyo[0]+=1
#     if(bector==3):
#         zahyo[0]-=1

#     return zahyo

# def isstop(zahyo,s,h,w,time):
#     if zahyo[0]<0 or zahyo[0]>= w or zahyo[1] < 0 or zahyo[1] >= h:
#         return True
#     elif s[zahyo[1]][zahyo[0]] == '#' or s[zahyo[1]][zahyo[0]] == '*':
#         return True
#     elif time > 98:
#         return True
#     else :
#         return False

# isbreak = False
# time =0
# # 回数と向き変更を繰り返す
# for i in range(n):
#     kaisu,lorr = map(str,input().split())
#     while time < int(kaisu):
#         s[zahyo[1]][zahyo[0]]='*'
#         zahyo = newzahyo(zahyo,bector)
#         time+=1

#         if isstop(zahyo,s,h,w,time):
#             isbreak = True
#             break
    
#     if isbreak:
#         break
#     else:
#         bector = newbector(bector,lorr)

# if isbreak == False :

#     for i in range(max(h,w)):
#         s[zahyo[1]][zahyo[0]]='*'
#         zahyo = newzahyo(zahyo,bector)
#         time+=1
#         if isstop(zahyo,s,h,w,time):
#             isbreak = True
#             break

# for y in range(h):
#     print("".join(s[y]))





# # 陣取り
# h,w= map(int,input().split())
# senko = input()
# turn = senko
# field_A = []
# field_B = []

# field = [list(input()) for _ in range(h) ]

# for y in range(h):
#     for x in range(w):

#         if field[y][x] == 'A':
#             field_A.append([y,x])

# # ターンチェンジ
# def changeturn(turn):
#     if turn == 'A':
#         return 'B'
#     else :
#         return 'A'

# # 陣地追加
# def jinti(field_A,field_B,turn,h,w):
#     if turn == 'A':
#         returnfield = field_A
#         for i in field_A:
#             if(i[0]-1>=0):
#                 returnfield.append(i[0]-1,i[1])
#             if(i[0]+1<h):
#                 returnfield.append(i[0]+1,i[1])
#             if(i[1]-1>=0):
#                 returnfield.append(i[0],i[1]-1)
#             if(i[1]+1<w):
#                 returnfield.append(i[0],i[1]+1)
             

# # 陣地とり
# def fieldmark (field,shorifield,turn,field_A,field_B):
#     for zahyo in shorifield:
#         if field[zahyo] == '.' :
#             field[zahyo] = turn
#     return field

# # ターンの方の埋める陣地を追加
# shorifield = jinti(field_A,field_B,turn,h,w)
# if turn =='A':
#     field_A = shorifield
# else :
#     field_B = shorifield
# # fieldに反映
# field = fieldmark(field,shorifield,turn,field_A,field_B,)

# n,m = map(int,input().split())
# answer =[int(input()) for _ in range(m)]

# print(answer)

# maxscore = 0
# calcscore = 100

# for i in range(n):
#     calcscore = 100
#     for j in range(m):
#         sa = abs(answer[j]-int(input()))
#         if sa > 30:
#             calcscore -=5
#         elif sa > 20:
#             calcscore -=3
#         elif sa > 10:
#             calcscore -=2
#         elif sa > 5:
#             calcscore -=1
    
#     if maxscore < calcscore:
#         maxscore = calcscore

# print(maxscore)

# import math
# h,w = map(int,input().split())

# a =[]
# b =[]
# for i in range(h):
#     pixelyoko = []
#     for pixel in input().split():
#         pixelyoko.append(int(pixel))
#         pixelyoko.append(int(pixel))
#     a.append(pixelyoko)
#     a.append(pixelyoko)

# for i in range(h):
#     pixelyoko = []
#     for pixel in input().split():
#         pixelyoko.append(int(pixel))
#         pixelyoko.append(int(pixel))
#     b.append(pixelyoko)
#     b.append(pixelyoko)

# # output = []
# for i in range(2*h-1):
#     for j in range(2*w-1):
#         if j < 2*w-2:
#             print(math.floor((a[i+1][j+1]+b[i][j])/2),end=' ')
#         else: 
#             print(math.floor((a[i+1][j+1]+b[i][j])/2))

# import itertools
# h,w = map(int,input().split())

# ita = [list(input().split()) for _ in range(h)]

# # とりうる組み合わせのインデックスをh,wから取得する
# allindexlist=[]
# # for indexlist in itertools.combinations_with_replacement(range(w), h):

# maxpoint =0
# point =0

# for indexlist in list(itertools.product(range(w), repeat=h)):

#     count =0
#     point = 0
#     while count < h:
#         if count < h-1 and abs(indexlist[count]-indexlist[count+1])<2 :
#             point += int(ita[count][indexlist[count]])
#             count+=1
#         else :
#             break
        
#         if count==h-1 :
#             point += int(ita[count][indexlist[count]])
#             if maxpoint < point:
#                 maxpoint=point

# print(maxpoint)