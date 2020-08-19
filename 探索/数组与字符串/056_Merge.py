#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/8/18 10:56 下午
# @Author : xiongtao
# @File : 056_Merge.py

'''
给出一个区间的集合，请合并所有重叠的区间

输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
'''

class Merge():
    def merge(self, intervals):
        if len(intervals) <= 0:
            return []
        merged = []
        # 排序保证可以合并的区间一定是相邻的
        intervals = sorted(intervals, key=lambda x: x[0])
        merged.append(intervals[0])
        for i in range(1, len(intervals)):
            # 比较相邻两个区间是否可以合并
            if intervals[i][0] <= merged[-1][1]:
                # 比较右区间是否属于左区间，以确定是否需要修改区间值
                if merged[-1][1] < intervals[i][1]:
                    merged[-1][1] = intervals[i][1]
            else:
                merged.append(intervals[i])
        return merged

if __name__ == '__main__':
    M = Merge()
    intervals = [[1,4],[2,3]]
    print(M.merge(intervals))