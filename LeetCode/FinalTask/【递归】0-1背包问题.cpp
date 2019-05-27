#include <iostream>
#include<cstdio>
#define N 100
#define MAX(a,b) a < b ? b : a
using namespace std;

struct goods{
int sign;//物品序号
int wight;//物品重量
int value;//物品价值
};

int n,bestValue,cv,cw,C;//物品数量，价值最大，当前价值，当前重量，背包容量
int X[N],cx[N];//最终存储状态，当前存储状态
struct goods goods[N];

int KnapSack(int n,struct goods a[],int C,int x[]){
    int V[N][10*N];
    for(int i = 0; i <= n; i++)//初始化第0列
        V[i][0] = 0;
    for(int j = 0; j <= C; j++)//初始化第0行
        V[0][j] = 0;
    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= C; j++)
        if(j < a[i-1].wight)
            V[i][j] = V[i-1][j];
        else
            V[i][j] = MAX(V[i-1][j],V[i-1][j-a[i-1].wight] + a[i-1].value);

    for(int i = n,j = C; i > 0; i--){
        if(V[i][j] > V[i-1][j]){
            x[i-1] = 1;
            j = j - a[i-1].wight;
        }
        else
            x[i-1] = 0;
    }
    return V[n][C];
}
int main()
{
    printf("物品种类n：");
    scanf("%d",&n);
    printf("背包容量C：");
    scanf("%d",&C);
    for(int i = 0; i < n; i++){
        printf("物品%d的重量w[%d]及其价值v[%d]：",i+1,i+1,i+1);
        scanf("%d%d",&goods[i].wight,&goods[i].value);
    }
    int sum2 = KnapSack(n,goods,C,X);
     printf("动态规划法求解0/1背包问题:\nX=[");
     for(int i = 0; i < n; i++)
        cout<<X[i]<<" ";//输出所求X[n]矩阵
     printf("]   装入总价值%d\n", sum2);
     return 0;
}
