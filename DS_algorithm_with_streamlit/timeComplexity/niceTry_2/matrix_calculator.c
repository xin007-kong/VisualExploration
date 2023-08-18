// #include <stdio.h>
// #include <stdlib.h>

// int main(int argc, char *argv[]) {
//     int rows = atoi(argv[1]);
//     int cols = atoi(argv[2]);
//     double matrix1[rows][cols], matrix2[rows][cols];

//     int idx = 3;
//     for (int i = 0; i < rows; i++) {
//         for (int j = 0; j < cols; j++) {
//             matrix1[i][j] = atof(argv[idx++]);
//         }
//     }

//     for (int i = 0; i < rows; i++) {
//         for (int j = 0; j < cols; j++) {
//             matrix2[i][j] = atof(argv[idx++]);
//         }
//     }

//     printf("加法结果:\n");
//     for (int i = 0; i < rows; i++) {
//         for (int j = 0; j < cols; j++) {
//             printf("%lf ", matrix1[i][j] + matrix2[i][j]);
//         }
//         printf("\n");
//     }

//     printf("减法结果:\n");
//     for (int i = 0; i < rows; i++) {
//         for (int j = 0; j < cols; j++) {
//             printf("%lf ", matrix1[i][j] - matrix2[i][j]);
//         }
//         printf("\n");
//     }

//     return 0;
// }

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int rows = atoi(argv[1]);
    int cols = atoi(argv[2]);
    double matrix1[rows][cols], matrix2[rows][cols];

    int idx = 3;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            matrix1[i][j] = atof(argv[idx++]);
        }
    }

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            matrix2[i][j] = atof(argv[idx++]);
        }
    }

    printf("加法结果:\n");
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            printf("%lf ", matrix1[i][j] + matrix2[i][j]);
        }
        printf("\n");
    }

    printf("减法结果:\n");
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            printf("%lf ", matrix1[i][j] - matrix2[i][j]);
        }
        printf("\n");
    }

    return 0;
}
