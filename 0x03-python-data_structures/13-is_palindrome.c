#include "lists.h"

/**
* reverse - reverses a linked list
* @head: a pointer to the head of the linked list
*
* Return: a pointer to the head of the reversed list
*/
listint_t *reverse(listint_t *head)
{
listint_t *prev = NULL, *next;

while (head)
{
next = head->next;
head->next = prev;
prev = head;
head = next;
}

return (prev);
}

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: a double pointer to the head of the linked list
*
* Return: 1 if the list is a palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head, *tmp, *rev;

if (!head)
return (1);

while (fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
}

rev = reverse(slow);
tmp = *head;

while (rev)
{
if (tmp->n != rev->n)
return (0);
tmp = tmp->next;
rev = rev->next;
}

return (1);
}
