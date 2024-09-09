# https://level.goorm.io/exam/48190/직각다각형/quiz/1

# 상당히 개선됨
def WithListAndSet():
    n = int(input())

    h = [0]*1000001
    hkset = set()
    v = [0]*1000001
    vkset = set()
    def scale(x):
        return int(x)+500000

    bx, by = map(scale,input().split())
    fx, fy = bx, by
    for i in range(n-1):
        x, y = map(scale,input().split())
        if bx == x:
            hkset.add(y)
            hkset.add(by)
            if by > y:
                h[y] += 1
                h[by] -= 1
            else:
                h[by] += 1
                h[y] -= 1
        else:
            vkset.add(x)
            vkset.add(bx)
            if bx > x:
                v[x] += 1
                v[bx] -= 1
            else:
                v[bx] += 1
                v[x] -= 1
        bx, by = x, y
    else:
        if bx == fx:
            if by > fy:
                h[fy] += 1
                h[by] -= 1
            else:
                h[by] += 1
                h[fy] -= 1
        else:
            if bx > fx:
                v[fx] += 1
                v[bx] -= 1
            else:
                v[bx] += 1
                v[fx] -= 1
                
    res = 0
    hm = 0
    hk = sorted(list(hkset))
    for i in hk:
        hm += h[i]
        res = max(res,hm)
    vm = 0
    vk = sorted(list(vkset))
    for i in vk:
        vm += v[i]
        res = max(res,vm)
    print(res)
    
# 느림
def WithOnlyList():
    n = int(input())

    h = [0]*1000001
    v = [0]*1000001
    def scale(x):
        return int(x)+500000

    bx, by = map(scale,input().split())
    fx, fy = bx, by
    for i in range(n-1):
        x, y = map(scale,input().split())
        if bx == x:
            if by > y:
                h[y] += 1
                h[by] -= 1
            else:
                h[by] += 1
                h[y] -= 1
        else:
            if bx > x:
                v[x] += 1
                v[bx] -= 1
            else:
                v[bx] += 1
                v[x] -= 1
        bx, by = x, y
    else:
        if bx == fx:
            if by > fy:
                h[fy] += 1
                h[by] -= 1
            else:
                h[by] += 1
                h[fy] -= 1
        else:
            if bx > fx:
                v[fx] += 1
                v[bx] -= 1
            else:
                v[bx] += 1
                v[fx] -= 1
                
    res = 0
    hm = 0
    vm = 0
    for i in range(1000001):
        hm += h[i]
        vm += v[i]
        res = max(res,hm,vm)
    print(res)