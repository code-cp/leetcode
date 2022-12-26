- 第 325 场力扣周赛 https://leetcode.cn/circle/discuss/RmydJj/
- 灵茶山艾府 逆向思维 + 01 背包方案数（Python/Java/C++/Go https://leetcode.cn/problems/number-of-great-partitions/solutions/2032009/ni-xiang-si-wei-01-bei-bao-fang-an-shu-p-v47x/

```
给你一个正整数数组 nums 和一个整数 k 。

分区 的定义是：将数组划分成两个有序的 组 ，并满足每个元素 恰好 存在于 某一个 组中。如果分区中每个组的元素和都大于等于 k ，则认为分区是一个好分区。

返回 不同 的好分区的数目。由于答案可能很大，请返回对 109 + 7 取余 后的结果。

如果在两个分区中，存在某个元素 nums[i] 被分在不同的组中，则认为这两个分区不同。

You are given an array nums consisting of positive integers and an integer k.

Partition the array into two ordered groups such that each element is in exactly one group. A partition is called great if the sum of elements of each group is greater than or equal to k.

Return the number of distinct great partitions. Since the answer may be too large, return it modulo 109 + 7.

Two partitions are considered distinct if some element nums[i] is in different groups in the two partitions.
```