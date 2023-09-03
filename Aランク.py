
# # じゃんけん
# N,M = map(int,input().split())

# aite = [0,0,0]
# for i in list(input()):
#     if i=='G':
#         aite[0]+=1
#     elif i=='C':
#         aite[1]+=1
#     elif i=='P':
#         aite[2]+=1
        

# # MからCとPの数の組み合わせを取得
# gcpkumiawase=[]
# ccount=0
# while M-ccount*2 >=0:
#     if (M-ccount*2)%5==0 and ccount + (M-ccount*2)/5 <=N:
#         gcpkumiawase.append([int(N-ccount - (M-ccount*2)/5),ccount,int((M-ccount*2)/5)])
#     ccount+=1

# # jankenから数を取得
# maxreturncount=0
# for kumiawase in gcpkumiawase:
#     returncount=0
#     # 相手がGの場合、相手のGと自分のPの小さいほう
#     returncount+=min(aite[0],kumiawase[2])
#     # 相手がCの場合、相手のC
#     returncount+=min(aite[1],kumiawase[0])
#     # 相手がPの場合、相手のPと自分のCの小さいほう
#     returncount+=min(aite[2],kumiawase[1])

#     # 最大数をセット
#     maxreturncount=max(maxreturncount,returncount)

# print(maxreturncount)


# RGB
H,W = map(int,input().split())
field=[]
for i in range(H):
    inputlinelist = list(input())
    yokolist=[]
    for j in range(W):
        yokolist.append([inputlinelist[j],0])
    field.append(yokolist)

# 座標を指定したら、隣接する色を塗る関数
def nuru(y,x):
    field[y][x][1]=1

    nurinokosiflg=True
    while nurinokosiflg:
        # 上
        if y > 0 and field[y-1][x][0] == field[y][x][0] and field[y-1][x][1] ==0:
            y-=1
        # 下
        elif y < H -1  and field[y+1][x][0] == field[y][x][0] and field[y+1][x][1] ==0:
            y+=1
        # 左
        elif x > 0 and field[y][x-1][0] == field[y][x][0] and field[y][x-1][1] ==0:
            x-=1
        # 右
        elif x < W-1 and field[y][x+1][0] == field[y][x][0] and field[y][x+1][1] ==0:
            x+=1
        else:
            nurinokosiflg=False
        
        field[y][x][1]=1

irocount = [0,0,0]
for i in range(H):
    for j in range(W):
        if field[i][j][1]==0:
            nuru(i,j)

            if field[i][j][0]=='R':
                irocount[0]+=1
            elif field[i][j][0]=='G':
                irocount[1]+=1
            elif field[i][j][0]=='B':
                irocount[2]+=1

R = str(irocount[0])
G = str(irocount[1])
B = str(irocount[2])

print('{} {} {}'.format(R,G,B))

