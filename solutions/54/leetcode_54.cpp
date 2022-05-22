// [video](https://www.bilibili.com/video/BV1mK411M7Ng) 
// 遍历矩阵上下左右的时候，可以用两个数组存储偏移量，而不是直接遍历坐标
// 蛇形矩阵走法：先向右走，撞墙后顺时针旋转90度往下走，规定右是1，下是2，左是3，上是0，可以用1，2，3，0，1，2，3，0...表示
// x, y向d方向偏移一格，相当于(x, y) = (x, y) + (dx[d], dy[d])，顺时针旋转用d = (d+1)%4 实现
// 撞墙：1. 出界 2. 走到了之前走过的格子

#include <iostream>

using namespace std; 

const int N = 110; 

int n, m; 
int q[N][N]; 

int main()
{
    cin >> n >> m; 
    int dx[] = {-1, 0, 1, 0}, dy[] = {0, 1, 0, -1};
    // initially move to right 
    int x = 0, y = 0, d = 1; 
    
    for (int i = 1; i <= n*m; i++)
    {
        q[x][y] = i; 
        int a = x + dx[d], b = y + dy[d]; 
	// check whether we need to change direction 
	if (a < 0 || a >= n || b < 0 || b >= m || q[a][b]) 
	{
            d = (d + 1) % 4;
	    a = x + dx[d], b = y + dy[d]; 
	}
	x = a, y = b; 
    } 

    for (int i = 0; i < n; i++)
    {
	for (int j = 0; j < m; j++)
	{ 
	    // cout << q[i][j] << " " << endl; 
	    printf("%7d", q[i][j]);
	}
    }

    return 0; 
} 

