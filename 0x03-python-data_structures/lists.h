#ifndef LISTS_H
#define LISTS_H

#include <Python.h>

/**
* struct listint_s - singly linked list
* @n: integer
* @next: points to the next node
*
* Description: singly linked list node structure
* for project
*/
typedef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;

listint_t *reverse(listint_t *head);
void print_python_list_info(PyObject *p);
int is_palindrome(listint_t **head);
#endif /* LISTS_H */
