#include "lists.h"
#include <stdlib.h>

/**
* insert_node - inserts a number into a sorted singly linked list
* @head: double pointer to head of list
* @number: number to be included in new node
* Return: address of the new node, or NULL if it fails
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t *current = *head, *prev = NULL;

new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
new->next = NULL;

if (*head == NULL)
{
*head = new;
}
else
{
while (current != NULL && current->n < number)
{
prev = current;
current = current->next;
}
if (prev == NULL)
{
new->next = *head;
*head = new;
}
else
{
prev->next = new;
new->next = current;
}
}

return (new);
}
