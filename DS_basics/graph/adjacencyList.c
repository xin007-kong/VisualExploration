#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_VERTEX_NUM 20

// 定义顶点类型
typedef struct
{
    char name[20]; // 地点名称
} VertexType;

// 定义边类型
typedef struct ArcNode
{
    int adjvex;           // 邻接点在顶点数组中的下标
    struct ArcNode *next; // 指向下一个邻接点的指针
} ArcNode;

// 定义顶点类型
typedef struct VNode
{
    VertexType data; // 顶点数据
    ArcNode *first;  // 指向第一个邻接点的指针
} VNode, AdjList[MAX_VERTEX_NUM];

// 定义邻接表类型
typedef struct
{
    AdjList vertices;   // 邻接表
    int vexnum, arcnum; // 顶点数和边数
} ALGraph;

// 初始化邻接表
void InitGraph(ALGraph *G)
{
    int i;
    G->vexnum = 4;
    G->arcnum = 5;
    char *names[] = {"教学楼", "食堂", "宿舍楼", "体育馆"};
    for (i = 0; i < G->vexnum; i++)
    {
        strcpy(G->vertices[i].data.name, names[i]);
        G->vertices[i].first = NULL;
    }
    // 添加边
    ArcNode *p;
    p = (ArcNode *)malloc(sizeof(ArcNode));
    p->adjvex = 1;
    p->next = G->vertices[0].first;
    G->vertices[0].first = p;

    p = (ArcNode *)malloc(sizeof(ArcNode));
    p->adjvex = 2;
    p->next = G->vertices[0].first;
    G->vertices[0].first = p;

    p = (ArcNode *)malloc(sizeof(ArcNode));
    p->adjvex = 0;
    p->next = G->vertices[1].first;
    G->vertices[1].first = p;

    p = (ArcNode *)malloc(sizeof(ArcNode));
    p->adjvex = 3;
    p->next = G->vertices[2].first;
    G->vertices[2].first = p;

    p = (ArcNode *)malloc(sizeof(ArcNode));
    p->adjvex = 0;
    p->next = G->vertices[2].first;
    G->vertices[2].first = p;
}

// 打印邻接表
void PrintGraph(ALGraph G)
{
    int i;
    ArcNode *p;
    for (i = 0; i < G.vexnum; i++)
    {
        printf("%s: ", G.vertices[i].data.name);
        p = G.vertices[i].first;
        while (p != NULL)
        {
            printf("%s ", G.vertices[p->adjvex].data.name);
            p = p->next;
        }
        printf("\n");
    }
}

int main()
{
    ALGraph G;
    InitGraph(&G);
    PrintGraph(G);
    return 0;
}