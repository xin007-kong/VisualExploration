#include <stdio.h>
#include <string.h>

#define MVNum 100
#define MAX_NAME_LEN 20

typedef char VerTexType[MAX_NAME_LEN];
typedef int ArcType;

typedef struct
{
    VerTexType vexs[MVNum];
    ArcType arcs[MVNum][MVNum];
    int vexnum, arcnum;
} AMGraph;

// 计算字符串的显示宽度（考虑中英文字符宽度差异）
int displayWidth(const char *str)
{
    int width = 0;
    int i;
    for (i = 0; str[i] != '\0'; i++)
    {
        if ((unsigned char)str[i] >= 0x80)
        { // 如果是中文字符，增加2
            width += 2;
            i++; // 跳过下一个字节，因为中文字符是双字节的
        }
        else
        {
            width++;
        }
    }
    return width;
}

void CreateGraph(AMGraph *G)
{
    int i, j;
    G->vexnum = 5;
    G->arcnum = 5;
    char *nodes[] = {"图书馆", "计算机系大楼", "食堂", "学生宿舍", "体育馆"};

    for (i = 0; i < G->vexnum; i++)
    {
        strcpy(G->vexs[i], nodes[i]);
        for (j = 0; j < G->vexnum; j++)
        {
            G->arcs[i][j] = 0;
        }
    }

    G->arcs[0][1] = G->arcs[1][0] = 1;
    G->arcs[1][2] = G->arcs[2][1] = 1;
    G->arcs[2][3] = G->arcs[3][2] = 1;
    G->arcs[3][4] = G->arcs[4][3] = 1;
    G->arcs[0][2] = G->arcs[2][0] = 1;
}

void PrintGraph(AMGraph G)
{
    int i, j, max_width = 0;
    for (i = 0; i < G.vexnum; i++)
    {
        int width = displayWidth(G.vexs[i]);
        if (width > max_width)
        {
            max_width = width;
        }
    }

    printf("%-*s|", max_width, "");
    for (i = 0; i < G.vexnum; i++)
    {
        printf(" %-*s |", max_width, G.vexs[i]);
    }
    printf("\n");

    for (i = 0; i < G.vexnum + 1; i++)
    {
        for (j = 0; j < max_width + 2; j++)
        {
            printf("-");
        }
        printf("|");
    }
    printf("\n");

    for (i = 0; i < G.vexnum; i++)
    {
        printf("%-*s|", max_width, G.vexs[i]);
        for (j = 0; j < G.vexnum; j++)
        {
            printf(" %-*d |", max_width, G.arcs[i][j]);
        }
        printf("\n");
    }
}

int main()
{
    AMGraph G;
    CreateGraph(&G);
    PrintGraph(G);
    return 0;
}
