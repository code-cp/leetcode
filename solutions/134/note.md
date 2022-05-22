- [discussion](https://leetcode-cn.com/problems/gas-station/solution/shi-yong-tu-de-si-xiang-fen-xi-gai-wen-ti-by-cyayc/671970)
```
首先判断总gas能不能大于等于总cost，如果总gas不够，一切都白搭对吧（总（gas- cost）不用单独去计算，和找最低点时一起计算即可，只遍历一次）；

再就是找总（gas-cost）的最低点，不管正负（当然如果最低点都是正的话那肯定能跑完了）；

找到最低点后，如果有解，那么解就是最低点的下一个点，因为总（gas-cost）是大于等于0的，所以前面损失的gas我从最低点下一个点开始都会拿回来！（此处@小马哥！“我要争一口气，不是想证明我了不起。我是要告诉人家，我失去的东西一定要拿回来！”），别管后面的趋势是先加后减还是先减后加，最终结果我是能填平前面的坑的。
```
- [blog](https://www.geeksforgeeks.org/maximum-contiguous-circular-sum/), [blog](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)
- [blog](https://www.cnblogs.com/felixfang/p/3814463.html)

