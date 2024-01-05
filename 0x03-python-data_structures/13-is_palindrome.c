#include <stdlib.h>
#include "lists.h"

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

if (*head != NULL && (*head)->next != NULL)
{
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev = slow;
slow = slow->next;
}
if (fast != NULL)
{
midnode = slow;
slow = slow->next;
}

second_half = slow;
prev->next = NULL;
reverse(&second_half);
res = compareLists(*head, second_half);

reverse(&second_half);
if (midnode != NULL)
{
prev->next = midnode;
midnode->next = second_half;
}
else
prev->next = second_half;
}
return (res);
}
/**
* reverse - reverses a linked list
* @head_ref: double pointer to head node
*/
void reverse(listint_t **head_ref)
{
listint_t *prev   = NULL;
listint_t *current = *head_ref;
listint_t *next;
while (current != NULL)
{
next  = current->next;
current->next = prev;
prev = current;
current = next;
}
*head_ref = prev;
}
/**
* compareLists - compares two linked lists
* @head1: first linked list
* @head2: second linked list
* Return: 1 if the lists are identical, 0 otherwise
*/
int compareLists(listint_t *head1, listint_t *head2)
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
{
return (0);
}
}

if (temp1 == NULL && temp2 == NULL)
{
return (1);
}
return (0);
}
