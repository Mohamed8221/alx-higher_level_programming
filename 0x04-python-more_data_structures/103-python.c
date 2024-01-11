#include <time.h>
#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

void print_python_bytes(PyObject *p)
{
    long int size;
    unsigned char *str;
    int i;

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

    printf("  first %ld bytes:", (size < 10) ? size + 1 : 10);
    for (i = 0; i <= size && i < 10; i++)
        printf(" %02hhx", str[i]);

    printf("\n");
}

void print_python_list(PyObject *p)
{
    long int size = PyList_Size(p);
    int i;
    PyObject *item;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);

        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}
