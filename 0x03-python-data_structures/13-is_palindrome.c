#include "lists.h"
#include <stdlib.h>

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: double pointer to the head node of the singly linked list
*
* Return: 1 if the list is a palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head, *prev = *head, *tmp = NULL;
while (fast && fast->next)
{
fast = fast->next->next;
prev = slow;
slow = slow->next;
}
prev->next = NULL;
while (slow)
{
tmp = slow->next;
slow->next = prev;
prev = slow;
slow = tmp;
}
while (*head && prev)
{
if ((*head)->n != prev->n)
return (0);
*head = (*head)->next;
prev = prev->next;
}
return (1);
}
