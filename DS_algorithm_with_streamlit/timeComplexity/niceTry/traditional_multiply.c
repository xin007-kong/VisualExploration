#include <stdio.h>

void matrix_multiply(int A[][10], int B[][10], int C[][10], int n_rows, int n_cols)
{
    int i, j, k;
    for (i = 0; i < n_rows; i++)
    {
        for (j = 0; j < n_cols; j++)
        {
            C[i][j] = 0;
            for (k = 0; k < n_rows; k++)
            {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main()
{
    int n_rows, n_cols;
    FILE *fileA = fopen("matrix_a.txt", "r");
    FILE *fileB = fopen("matrix_b.txt", "r");

    fscanf(fileA, "%d", &n_rows);
    fscanf(fileA, "%d", &n_cols);

    int A[10][10];
    int B[10][10];
    int C[10][10];
    int i, j;

    for (i = 0; i < n_rows; i++)
    {
        for (j = 0; j < n_cols; j++)
        {
            fscanf(fileA, "%d", &A[i][j]);
        }
    }

    for (i = 0; i < n_cols; i++)
    {
        for (j = 0; j < n_rows; j++)
        {
            fscanf(fileB, "%d", &B[i][j]);
        }
    }

    matrix_multiply(A, B, C, n_rows, n_cols);

    printf("Matrix C:\n");
    for (i = 0; i < n_rows; i++)
    {
        for (j = 0; j < n_cols; j++)
        {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }

    fclose(fileA);
    fclose(fileB);

    return 0;
}
