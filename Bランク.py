
# # n毛作
# # 初期変数
# n,m=map(int,input().split())
# h,w=map(int,input().split())

# # 畑
# hatake =[list('.' for _ in range(w)) for _ in (range(h))]

# # 収穫物
# shukaku = list(0 for _ in range(m))

# for i in range(n):
#     gs,ge,rs,re,shukakugyou = map(int,input().split())

     
#     for y in range(gs-1,ge):
#         for x in range(rs-1,re):
#             # 収穫
#             if hatake[y][x] !='.':
#                 shukaku[int(hatake[y][x])-1] += 1
    
#             # 植える
#             hatake[y][x]=str(shukakugyou)


# for i in range(m):
#     print(shukaku[i])

# for j in range(h):
#     print("".join(hatake[j]))

# # 階段上り
# n=int(input())
# a,b =map(int,input().split())

# # まずa*bまでの到達可能な段数を求める
# abkanoukaisu =0

# # a*bの組み合わせがなんかい入るか確認
# while abkanoukaisu*a*b <n:
#     abkanoukaisu+=1
# abkanoukaisu-=1

# abkanou ={0}
# akaisu =0
# bakaisu =0
# abkaisu =0

# for x in range(a):
#     while a*akaisu<(x+1)*b:
#         for y in range(a-x):
#             # a*bの倍数分いれる
#             count=0
#             while count < abkanoukaisu + 1:
#                 if count < abkanoukaisu:
#                     abkanou.add((akaisu*a + y*b)+a*b*count)
#                 if count ==abkanoukaisu and ((akaisu*a + y*b)+a*b*count) <n:
#                     abkanou.add((akaisu*a + y*b)+a*b*count)
#                 count+=1
#         akaisu+=1

# # abkanou=sorted(abkanou)

# number ={0}
# for k in range(n):
#     number.add(k)

# print(number)
# print(abkanou)
# print(number - abkanou)
# print(len(number - abkanou))

# # イルミネーション
# import math
# n,m=map(int,input().split())

# denkyu=[int(y) for y in input().split()]

# kukansu = int(input())

# for i in range(kukansu):
#     s,e = map(int,input().split())

#     goukei =0
#     # 電球の合計を計算
#     for j in range(s-1,e):
#         goukei+=denkyu[j]

#     avarage = goukei / (e - s + 1)

#     if avarage < m:
#         sabun = math.ceil(m-avarage)
        
#         for j in range(s-1,e):
#             denkyu[j]+=sabun

# print(denkyu)


# # シャッフル

# N,M,K = map(int,input().split())

# card = list(range(1,N+1))
# kugiri =[]

# def wake(card):
#     outputkugiri=[]
#     count=1
#     while N - count + 1 >= M:
#         outputkugiri.append([card[i] for i in range(count-1,count-1 +M)])
#         count+=M

#     if N-count + 1 > 0:
#         outputkugiri.append([card[i] for i in range(count-1,N)])

#     return outputkugiri

# def shuffle(card):
#     outputcard =[]
#     for i in range(len(card)):
#         outputcard.append(card[len(card)-i-1])
#     return outputcard

# def naraberu(kugiri):
#     outputcard = []
#     for matomari in kugiri:
#         for i in matomari:
#             outputcard.append(i)
#     return outputcard


# for i in range(K):
#     kugiri =wake(card)
#     kugiri=shuffle(kugiri)
#     card = naraberu(kugiri)



# for i in card:
#     print(i)

# # スワイプ
# N =int(input())
# field =[]
# for _ in range(N):
#     field.append([int(i) for i in list(input())])


# def sita(y,x):
#     count =0
#     if abs(field[y][x]-field[y+1][x])==1:
#         count+=1
#         while y+1+count < N and field[y+count][x]-field[y+1+count][x]==field[y][x]-field[y+1][x]:
#             count+=1
#     return count

# def ue(y,x):
#     count =0
#     if abs(field[y][x]-field[y-1][x])==1:
#         count+=1
#         while y-1-count >= 0 and field[y-count][x]-field[y-1-count][x]==field[y][x]-field[y-1][x]:
#             count+=1
#     return count

# def tate(y,x):
#     maxcount=0
#     if y == 0:
#         maxcount= sita(y,x)
#     elif y > 0 and y < N - 1:
#         maxcount= max(sita(y,x),ue(y,x))
#     elif y == N -1 :
#         maxcount= ue(y,x)
    
#     return maxcount

# def migi(y,x):
#     count =0
#     if abs(field[y][x]-field[y][x+1])==1:
#         count+=1
#         while x+1+count < N and field[y][x+count]-field[y][x+1+count]==field[y][x]-field[y][x+1]:
#             count+=1
#     return count

# def hidari(y,x):
#     count =0
#     if abs(field[y][x]-field[y][x-1])==1:
#         count+=1
#         while x-1-count >= 0 and field[y][x-count]-field[y][x-1-count]==field[y][x]-field[y][x-1]:
#             count+=1
#     return count

# def yoko(y,x):
#     maxcount=0
#     if x == 0:
#         maxcount= migi(y,x)
#     elif x > 0 and x < N - 1:
#         maxcount= max(migi(y,x),hidari(y,x))
#     elif x == N -1 :
#         maxcount= hidari(y,x)
    
#     return maxcount

# def migisita(y,x):
#     count =0
#     if abs(field[y][x]-field[y+1][x+1])==1:
#         count+=1
#         while y+1+count < N and x+1+count < N and field[y+count][x+count]-field[y+1+count][x+1+count]==field[y][x]-field[y+1][x+1]:
#             count+=1
#     return count

# def hidariue(y,x):
#     count =0
#     if abs(field[y][x]-field[y-1][x-1])==1:
#         count+=1
#         while y-1-count >=0 and x-1-count >=0 and field[y-count][x-count]-field[y-1-count][x-1-count]==field[y][x]-field[y-1][x-1]:
#             count+=1
#     return count

# def hidarisita(y,x):
#     count =0
#     if abs(field[y][x]-field[y+1][x-1])==1:
#         count+=1
#         while y+1+count < N and x-1-count >=0 and field[y+count][x-count]-field[y+1+count][x-1-count]==field[y][x]-field[y+1][x-1]:
#             count+=1
#     return count

# def migiue(y,x):
#     count =0
#     if abs(field[y][x]-field[y-1][x+1])==1:
#         count+=1
#         while y-1-count >=0 and x+1+count < N and field[y-count][x+count]-field[y-1-count][x+1+count]==field[y][x]-field[y-1][x+1]:
#             count+=1
#     return count

# def naname(y,x):
#     maxcount=0
#     if y == 0:
#         if x==0:
#             maxcount= migisita(y,x)
#         elif x > 0 and x < N - 1:
#             maxcount= max(migisita(y,x),hidarisita(y,x))
#         else:
#             maxcount= hidarisita(y,x)
#     elif y > 0 and y < N - 1:
#         if x==0:
#             maxcount= max(migiue(y,x),migisita(y,x))
#         elif x > 0 and x < N - 1:
#             maxcount= max(migiue(y,x),migisita(y,x),hidariue(y,x),hidarisita(y,x))
#         else:
#             maxcount= max(hidariue(y,x),hidarisita(y,x))
#     elif y == N - 1:
#         if x==0:
#             maxcount= migiue(y,x)
#         elif x > 0 and x < N - 1:
#             maxcount= max(migiue(y,x),hidariue(y,x))
#         else:
#             maxcount= hidariue(y,x)

#     return maxcount

# def masu(y,x):
#     return max((tate(y,x),yoko(y,x),naname(y,x)))

# maxcount =0
# for y in range(N):
#     for x in range(N):
#         count=masu(y,x)
#         if maxcount < count:
#             maxcount = count  

# print(maxcount+1)

# N,M = map(int,input().split())

# load = [input().split() for _ in range(N)]

# okload=[]
# for i in range(N):
#     for j in range(N):
#         if int(load[j][i])>=M:
#             break

#         if j==N-1:
#             okload.append(str(i+1))
    
# if len(okload)>0:
#     print(" ".join(okload))

# else:
#     print('wait')

# N = int(input())
# schedule = list(int(i) for i in input().split())

# # print(schedule)

# # 最初の７日間だけ先に確認
# count=0
# for i in range(7):
#     if schedule[i] ==0:
#         count+=1

# renkyuschedule=[]
# renkyucount=0
# maxrenkyucount=0
# if count>=2:
#     # ７日目までは週休２日、かつその休暇日数を記録
#     renkyuschedule.append(count)
#     renkyucount += 1
# else :
#     # ７日目までは週休２日でない、かつその休暇日数を記録
#     renkyuschedule.append(count)
#     renkyucount = 0

# for i in range(N-7):
#     # 前日までの連休カウントから計算
#     yasumicount = renkyuschedule[i]
#     # 前日までの連休カウントから計算
#     if schedule[i]==0:
#         yasumicount -=1
#     if schedule[i+7]==0:
#         yasumicount +=1

#     if  yasumicount >= 2:
#         renkyuschedule.append(yasumicount)
#         renkyucount+=1
#         maxrenkyucount=max(maxrenkyucount,renkyucount)

#     else :
#         renkyuschedule.append(yasumicount)
#         maxrenkyucount=max(maxrenkyucount,renkyucount)
#         renkyucount=0

# if maxrenkyucount > 0:
#     print(maxrenkyucount+6)
# else :
#     print(0)

# N = int(input())

# tumikilist = [[int(i) for i in input().split()] for _ in range(N)]

# # 短い編が先に来るように並び替え
# for tumiki in tumikilist:
#     if tumiki[1]>tumiki[2]:
#         a = tumiki[1]
#         tumiki[1]=tumiki[2]
#         tumiki[2]=a

# # 下上に配置できる組み合わせを取得
# kumiawaselist =[]
# dodailist =[]
# takasacount =0
# maxcount = 0


# for i in range(N):
#     for j in range(N):
#         if i != j and tumikilist[i][1] >= tumikilist[j][1] and tumikilist[i][2] >= tumikilist[j][2]:
#             kumiawaselist.append([i,tumikilist[i][0],j,tumikilist[j][0]])
#             dodailist.append(i)

# 取りうる組み合わせとその合計を取得
# maxcount = 0
# for i in len(kumiawaselist):
#     # count = kumiawaselist[i][1] + kumiawaselist[i][3]
#     genzaidodai = kumiawaselist[i][2]
#     while genzaidodai in dodailist:
#         # 土台となりうる候補の数だけ取得
#         indexes = [j for j, x in enumerate(dodailist) if x == genzaidodai]
#         for index in indexes :
#             count+=kumiawaselist[index][3]
#             genzaidodai=kumiawaselist[index][2]

# kumiawasekumiawase =[]
# for i in len(kumiawaselist):
#     kumiawasekumiawase.append(i)
#     genzaidodai = kumiawaselist[i][2]
#     while genzaidodai in dodailist:
#         genzaidodai = dodailist.index(genzaidodai)
#         kumiawasekumiawase.append(genzaidodai)

# print(tumikilist)
# print(kumiawaselist)

# H,W = map(int,input().split())

# choco = [list(int(i) for i in input().split()) for _ in range(H)]

# # 半分の数字を取得
# hanbunlist = []
# for i in range(H):
#     count = 0
#     for j in range(W):
#         count+=choco[i][j]
    
#     hanbunlist.append(count/2)

# # 端から合計していき、半分ちょうどになるかどうかを確認
# yprintflg = True
# ablistlist=[]
# for i in range(H):
#     alicetoudcount=0
#     ablist=[]
#     ynFLG=False

#     for j in range(W):
#         alicetoudcount+=choco[i][j]

#         if alicetoudcount < hanbunlist[i]:
#             ablist.append('A')
#         elif alicetoudcount == hanbunlist[i]:
#             ynFLG=True
#             ablist.append('A')
#         elif alicetoudcount > hanbunlist[i]:
#             ablist.append('B')

#     if ynFLG  :
#         ablistlist.append(ablist)
#     else:
#         print('No')
#         yprintflg = False
#         break

# if yprintflg:
#     print('Yes')
#     for i in range(H):
#         print("".join(ablistlist[i]))

# import sys

# def main(lines):
#     # このコードは標準入力と標準出力を用いたサンプルコードです。
#     # このコードは好きなように編集・削除してもらって構いません。
#     # ---
#     # This is a sample code to use stdin and stdout.
#     # Edit and remove this code as you like.

#     for i, v in enumerate(lines):
#         print("line[{0}]: {1}".format(i, v))

# if __name__ == '__main__':
#     lines = []
#     for l in sys.stdin:
#         lines.append(l.rstrip('\r\n'))
#     main(lines)


# クレンジング
# import math
# import sys

# lines = []
# for l in sys.stdin:
#     lines.append(l.rstrip('\r\n'))

# from importclass import stdimport

# N,M = map(int,stdimport()[0].split())

# for j in range(M):
#     datacount=0
#     datatotal=0
#     for i in range(N):
#         line =list(lines[i+1].split())
#         if line[j].isnumeric() and int(line[j]) >= 0 and int(line[j]) <=100:
#             datacount+=1
#             datatotal+=int(line[j])
    
#     if datacount==0:
#         print(0)
#     else:
#         print(math.floor(datatotal/datacount))



# from importclass import stdimport

# importlines=stdimport()
# H = int(importlines[0])

# def sanchokakunin(y,x,line):
#     sanchoflg = True
#     # 縦確認
#     if y==1:
#         sanchoflg = importlines[]

# hyokolist=[]
# for i in range(H):
#     line = importlines[i+1]
#     intline = [int(j) for j in list(line)]
#     for k in intline:
#         if i==1:

# H = int(input())

# yamalist = [[int(i) for i in input().split()] for _ in range(H)]

# print(yamalist)

# def sanchokakunin(y,x):
#     sanchoflg=True
#     # 縦確認
#     if y==0:
#         sanchoflg=yamalist[y][x]>yamalist[y+1][x]
#     elif y>0 and y<H-1:
#         sanchoflg=yamalist[y][x]>yamalist[y+1][x] and yamalist[y][x]>yamalist[y-1][x]
#     elif y==H-1:
#         sanchoflg=yamalist[y][x]>yamalist[y-1][x]

#     if sanchoflg ==False:
#         return False
    
#     # 横確認
#     if x==0:
#         sanchoflg=yamalist[y][x]>yamalist[y][x+1]
#     elif x>0 and x<H-1:
#         sanchoflg=yamalist[y][x]>yamalist[y][x+1] and yamalist[y][x]>yamalist[y][x-1]
#     elif x==H-1:
#         sanchoflg=yamalist[y][x]>yamalist[y][x-1]

#     return sanchoflg

# # 山頂確認
# sancholist = []
# for i in range(H):
#     for j in range(H):
#         if sanchokakunin(i,j):
#             sancholist.append(yamalist[i][j])

# sancholist_sorted = sorted(sancholist,reverse=True)

# for i in sancholist_sorted:
#     print(i)


# # 爆弾の大爆発
# import sys

# def shori(lines):

#     H,W = map(int,lines[0].split())
#     # フィールド
#     field=[]
#     # 爆弾を含むインデックス
#     bomindexes=[]
#     for i in range(1,H+1):
#         field.append(list(lines[i]))
#         if '#' in field[i-1]:
#             bomindexes += [bomindex for bomindex in range(W) if '#' == field[i-1][bomindex]]
#             field[i-1] = ['%' if i == '.' else i for i in field[i-1]]

#     # 縦分の置換しながら、爆風の位置を数える
#     count =0 
#     for i in range(H):
#         for j in set(bomindexes):
#             if field[i][j] == '.':
#                 field[i][j] ='%'
        
#         for k in field[i]:
#             if k=='#' or k=='%':
#                 count+=1

#     # 出力

#     print(count)

# if __name__ == '__main__':
#     lines = []
#     for l in sys.stdin:
#         lines.append(l.rstrip('\r\n'))
    
#     shori(lines)
