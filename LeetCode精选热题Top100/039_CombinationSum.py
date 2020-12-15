#!/usr/bin python
# -*- coding: utf-8 -*-

# @Time : 2020/12/10 8:41 上午
# @Author : xiongtao
# @File : 039_CombinationSum.py 
# @Title : 39. 组合总和

'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

示例 1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
'''

class CombinationSum:
    # 返回从idx开始，target可能的组成
    def dfs(self, candidates, res, combine, idx, sum, target):
        if sum == target:
            res.append(list(combine))
            return None
        if sum > target:
            return None
        if idx == len(candidates):
            return None
        # 每一次深度遍历时，对于idx有两种可能，一种是使用，另一种是不使用。
        # 并且本次使用后下一次还可以使用或者不使用，而如果本次不使用那么要避免重复后续也不使用
        # 使用
        if target >= sum + candidates[idx]:
            combine.append(candidates[idx])
            # 注意这里idx不变，表明可以重复使用该值
            self.dfs(candidates, res, combine, idx, sum + candidates[idx], target)
            # 深度遍历之后，要从combine数组中移除该值
            combine.pop()
        # 不使用
        self.dfs(candidates, res, combine, idx + 1, sum, target)

    # 返回和为target的所有组成
    def combinationSum(self, candidates, target):
        res = []
        combine = []
        idx = 0
        sum = 0
        self.dfs(candidates, res, combine, idx, sum, target)
        return res


if __name__ == '__main__':
    CS = CombinationSum()
    candidates = [2,3,6,7]
    target = 7
    print(CS.combinationSum(candidates, target))