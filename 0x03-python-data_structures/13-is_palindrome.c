#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: pointer to the head of the linked list
* Return: 0 if not a palindrome, 1 if a palindrome
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head, *prev = NULL, *temp;

if (!*head || !(*head)->next)
return (1);

while (fast && fast->next)
{
fast = fast->next->next;

temp = slow->next;
slow->next = prev;
prev = slow;
slow = temp;
}

if (fast)
slow = slow->next;

while (prev && slow)
{
if (prev->n != slow->n)
return (0);

prev = prev->next;
slow = slow->next;
}

return (1);
}
