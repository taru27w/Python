
H,W,N,n = map(int,input().split())

# 盤面情報
banmen = [list(input()) for _ in range(H)]

# print(banmen)

# 縦盤面変更
def tate(y,x,player,banmen):
    
    # 上方向確認
    tatekakuninzahyo = y-1
    riverseflag = False

    while tatekakuninzahyo >= 0 and riverseflag==False:
        
        # 障害物だった場合はすぐぬける
        if banmen[tatekakuninzahyo][x] == "#":
            break
        # 自分と同じ場合は、間の区間を自分のマスに塗り替え
        elif banmen[tatekakuninzahyo][x] == player:
            if y - tatekakuninzahyo > 1:
                for i in range(tatekakuninzahyo +1,y):
                    banmen[i][x] = player
                riverseflag = True

        tatekakuninzahyo-=1

    # 下方向確認
    tatekakuninzahyo = y+1
    riverseflag = False

    while tatekakuninzahyo < H and riverseflag==False:
        
        # 障害物だった場合はすぐぬける
        if banmen[tatekakuninzahyo][x] == '#':
            break
        # 自分と同じ場合は、間の区間を自分のマスに塗り替え
        elif banmen[tatekakuninzahyo][x] == player:
            if tatekakuninzahyo - y  > 1:
                for i in range(y+1,tatekakuninzahyo):
                    banmen[i][x] = player
                riverseflag = True

        tatekakuninzahyo+=1
    
    return banmen


# 横盤面変更
def yoko(y,x,player,banmen):
    
    # 左方向確認
    yokokakuninzahyo = x-1
    riverseflag = False

    while yokokakuninzahyo >= 0 and riverseflag==False:
        
        # 障害物だった場合はすぐぬける
        if banmen[y][yokokakuninzahyo] == "#":
            break
        # 自分と同じ場合は、間の区間を自分のマスに塗り替え
        elif banmen[y][yokokakuninzahyo] == player:
            if x - yokokakuninzahyo > 1:
                for j in range(yokokakuninzahyo+1,x):
                    banmen[y][j] = player
                riverseflag = True

        yokokakuninzahyo-=1

    # 右方向確認
    yokokakuninzahyo = x+1
    riverseflag = False
    
    while yokokakuninzahyo < W and riverseflag==False:
        
        # 障害物だった場合はすぐぬける
        if banmen[y][yokokakuninzahyo] == "#":
            break
        # 自分と同じ場合は、間の区間を自分のマスに塗り替え
        elif banmen[y][yokokakuninzahyo] == player:
            if yokokakuninzahyo - x > 1:
                for j in range(x+1,yokokakuninzahyo):
                    banmen[y][j] = player
                riverseflag = True

        yokokakuninzahyo+=1

    return banmen


# ななめ変更
def naname(y,x,player,banmen):
    
    # 左上方向確認
    nanamekuninzahyo = [y-1,x-1]
    riverseflag = False

    while nanamekuninzahyo[0] >= 0 and nanamekuninzahyo[1] >= 0 and riverseflag==False:
        
        # 障害物だった場合はすぐぬける
        if banmen[nanamekuninzahyo[0]][nanamekuninzahyo[1]] == "#":
            break
        # 自分と同じ場合は、間の区間を自分のマスに塗り替え
        elif banmen[nanamekuninzahyo[0]][nanamekuninzahyo[1]] == player:
            if y - nanamekuninzahyo[0] > 1:

                tempnanamekuninzahyo=nanamekuninzahyo
                for i in range(nanamekuninzahyo[0] +1,y):
                    tempnanamekuninzahyo[0]+=1
                    tempnanamekuninzahyo[1]+=1
                    banmen[tempnanamekuninzahyo[0]][tempnanamekuninzahyo[1]] = player 
                riverseflag = True

        nanamekuninzahyo[0] -=1
        nanamekuninzahyo[1] -=1

    # 右下方向確認
    nanamekuninzahyo = [y+1,x+1]
    riverseflag = False
    
    while nanamekuninzahyo[0] < H and nanamekuninzahyo[1] < W and riverseflag==False:
        
        # 障害物だった場合はすぐぬける
        if banmen[nanamekuninzahyo[0]][nanamekuninzahyo[1]] == "#":
            break
        # 自分と同じ場合は、間の区間を自分のマスに塗り替え
        elif banmen[nanamekuninzahyo[0]][nanamekuninzahyo[1]] == player:
            if nanamekuninzahyo[0] - y > 1:

                tempnanamekuninzahyo=nanamekuninzahyo
                for i in range(y +1,nanamekuninzahyo[0]):
                    tempnanamekuninzahyo[0]-=1
                    tempnanamekuninzahyo[1]-=1
                    banmen[tempnanamekuninzahyo[0]][tempnanamekuninzahyo[1]] = player 
                riverseflag = True

        nanamekuninzahyo[0] +=1
        nanamekuninzahyo[1] +=1

    # 右上方向確認
    nanamekuninzahyo = [y-1,x+1]
    riverseflag = False

    while nanamekuninzahyo[0] >= 0 and nanamekuninzahyo[1] < W and riverseflag==False:
        
        # 障害物だった場合はすぐぬける
        if banmen[nanamekuninzahyo[0]][nanamekuninzahyo[1]] == "#":
            break
        # 自分と同じ場合は、間の区間を自分のマスに塗り替え
        elif banmen[nanamekuninzahyo[0]][nanamekuninzahyo[1]] == player:
            if y - nanamekuninzahyo[0] > 1:

                tempnanamekuninzahyo=nanamekuninzahyo
                for i in range(nanamekuninzahyo[0] +1,y):
                    tempnanamekuninzahyo[0]+=1
                    tempnanamekuninzahyo[1]-=1
                    banmen[tempnanamekuninzahyo[0]][tempnanamekuninzahyo[1]] = player 
                riverseflag = True

        nanamekuninzahyo[0] -=1
        nanamekuninzahyo[1] +=1

    # 左下方向確認
    nanamekuninzahyo = [y+1,x-1]
    riverseflag = False

    while nanamekuninzahyo[0] < H and nanamekuninzahyo[1] >= 0 and riverseflag==False:
        
        # 障害物だった場合はすぐぬける
        if banmen[nanamekuninzahyo[0]][nanamekuninzahyo[1]] == "#":
            break
        # 自分と同じ場合は、間の区間を自分のマスに塗り替え
        elif banmen[nanamekuninzahyo[0]][nanamekuninzahyo[1]] == player:
            if nanamekuninzahyo[0] - y > 1:

                tempnanamekuninzahyo=nanamekuninzahyo
                for i in range(y+1,nanamekuninzahyo[0]):
                    tempnanamekuninzahyo[0]-=1
                    tempnanamekuninzahyo[1]+=1
                    banmen[tempnanamekuninzahyo[0]][tempnanamekuninzahyo[1]] = player 
                riverseflag = True

        nanamekuninzahyo[0] +=1
        nanamekuninzahyo[1] -=1

    return banmen

# test
# banmen =naname(0,0,'2',banmen)

for i in range(n):
    p,y,x =map(int,input().split())
    banmen[y][x]=str(p)
    banmen =tate(y,x,str(p),banmen)
    banmen =yoko(y,x,str(p),banmen)
    banmen =naname(y,x,str(p),banmen)

# banmen =naname(0,2,'1',banmen)
# banmen =yoko(2,2,'1',banmen)

for line in banmen:
    print("".join(line))


