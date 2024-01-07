#include "lists.h"

/**
* reverse - reverses a linked list
* @head: double pointer to head node
* Return: void
*/
void reverse(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next;

while (current)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
*head = prev;
}

/**
* compare - compares two linked lists
* @head1: head of first linked list
* @head2: head of second linked list
* Return: 1 if lists are the same, 0 otherwise
*/
int compare(listint_t *head1, listint_t *head2)
{
listint_t *temp1 = head1;
listint_t *temp2 = head2;

while (temp1 && temp2)
{
if (temp1->n == temp2->n)
{
temp1 = temp1->next;
temp2 = temp2->next;
}
else
return (0);
}
if (!temp1 && !temp2)
return (1);
return (0);
}

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: double pointer to head node
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head;
listint_t *second_half, *prev = *head;
listint_t *midnode = NULL;
int res = 1;

if (*head && (*head)->next)
{
while (fast && fast->next)
{
fast = fast->next->next;
prev = slow;
slow = slow->next;
}
if (fast)
{
midnode = slow;
slow = slow->next;
}
second_half = slow;
prev->next = NULL;
reverse(&second_half);
res = compare(*head, second_half);
reverse(&second_half);
if (midnode)
{
prev->next = midnode;
midnode->next = second_half;
}
else
prev->next = second_half;
}
return (res);
}
