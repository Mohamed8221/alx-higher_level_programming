#include <Python.h>

/**
 * print_python_string - Prints Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
    long int length;

    fflush(stdout);

    /* Check if p is a string object */
    if (!PyUnicode_Check(p))
    {
        printf("[ERROR] Invalid String Object\n");
        return;
    }

    /* Get the length of the string and print the string object info */
    length = PyUnicode_GET_LENGTH(p);
    printf("[.] string object info\n");
    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");
    printf("  length: %ld\n", length);
    printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
