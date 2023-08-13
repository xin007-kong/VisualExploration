#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node
{
    int value;
    struct Node *next;
};

struct Node *head = NULL;

__declspec(dllexport) void append(int value)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->value = value;
    newNode->next = NULL;

    if (head == NULL)
    {
        head = newNode;
        return;
    }

    struct Node *current = head;
    while (current->next != NULL)
    {
        current = current->next;
    }
    current->next = newNode;
}

__declspec(dllexport) void delete_last()
{
    if (head == NULL)
        return;

    if (head->next == NULL)
    {
        free(head);
        head = NULL;
        return;
    }

    struct Node *current = head;
    while (current->next->next != NULL)
    {
        current = current->next;
    }
    free(current->next);
    current->next = NULL;
}

__declspec(dllexport) char *get_list()
{
    static char buffer[1000];
    memset(buffer, 0, sizeof(buffer));
    struct Node *current = head;
    while (current != NULL)
    {
        sprintf(buffer + strlen(buffer), "%d -> ", current->value);
        current = current->next;
    }
    strcat(buffer, "NULL");
    return buffer;
}
