#include <Python.h>
#include <stdio.h>

#define MIN(x, y) (((x) < (y)) ? (x) : (y))

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
* print_python_list - Prints basic info about Python lists.
* @p: A PyObject list object.
*/
void print_python_list(PyObject *p)
{
long int size, alloc, i;
PyObject *item;

printf("[*] Python list info\n");
size = Py_SIZE(p);
alloc = ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", alloc);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: ", i);
if (PyBytes_Check(item))
print_python_bytes(item);
else
printf("%s\n", Py_TYPE(item)->tp_name);
}
}

/**
* print_python_bytes - Prints basic info about Python byte objects.
* @p: A PyObject byte object.
*/
void print_python_bytes(PyObject *p)
{
long int size;
unsigned char *str;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
str = (unsigned char *)PyBytes_AsString(p);
printf("  size: %ld\n", size);
printf("  trying string: %s\n", str);
printf("  first %ld bytes: ", MIN(size, 10));

for (int i = 0; i < MIN(size, 10); i++)
printf("%02hhx ", str[i]);

printf("\n");
}
