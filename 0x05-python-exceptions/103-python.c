#include <Python.h>
#include <stdio.h>

/**
* print_python_list - Prints basic info about Python lists.
* @p: A PyObject list object.
*/
void print_python_list(PyObject *p)
{
long int size, i;
PyListObject *list;
PyObject *item;

printf("[*] Python list info\n");
if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object\n");
return;
}

list = (PyListObject *)p;
size = PyList_GET_SIZE(p);

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", list->allocated);
for (i = 0; i < size; i++)
{
item = PyList_GET_ITEM(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
if (PyBytes_Check(item))
print_python_bytes(item);
}
}

/**
* print_python_bytes - Prints basic info about Python bytes objects.
* @p: A PyObject bytes object.
*/
void print_python_bytes(PyObject *p)
{
unsigned char *str;
Py_ssize_t size;
Py_ssize_t i;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
str = PyBytes_AsString(p);

printf("  size: %ld\n", size);
printf("  trying string: %s\n", str);
printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);
for (i = 0; i < size + 1 && i < 10; i++)
printf("%02hhx%s", str[i], i + 1 < size + 1 && i + 1 < 10 ? " " : "\n");
}

/**
* print_python_float - Prints basic info about Python float objects.
* @p: A PyObject float object.
*/
void print_python_float(PyObject *p)
{
double value;
printf("[.] float object info\n");
if (!PyFloat_Check(p))
{
printf("  [ERROR] Invalid Float Object\n");
return;
}

value = ((PyFloatObject *)p)->ob_fval;
printf("  value: %s\n", PyOS_double_to_string(value, 'r',
0, Py_DTSF_ADD_DOT_0, NULL));
}
