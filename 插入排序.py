"""alist=[93     ，54，77，31，44，55，226]
 alist=[54，93   ，77，31，44，55，226]
 alist=[54,77,93     ，31,44,55,226]
 分为有序和无序序列
 先将第一个值固定，后续拿一个值与第一个值对比，排序插入
 此时再将 后续拿一个值 与刚形成的有序序列对比，排序插入
 从无序序列中拿出一个值，与有序序列对比，看插入哪个位
"""

def insert_sort(alist):
    '''插入排序'''
    n = len(alist)
    # 从右边的无序序列中取出多少个元素执行这样的过程
    for j in range(1,n):
        # i = [1,2,3,....n]
        # i 代表内层循环起始值
        i = j
        # 执行从右边的无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置中
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
                i -= 1
            else:
                break
    return alist

if __name__ == '__name__':
    alist=[54,93,77,31,44,55,226]
    print(insert_sort(alist))

# 最坏时间复杂度O（n^2）
# 最优时间复杂度O（n）
# 稳定