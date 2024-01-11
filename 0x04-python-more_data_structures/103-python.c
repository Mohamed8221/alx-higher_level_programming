#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);
#define MIN(x, y) (((x) < (y)) ? (x) : (y))

void print_python_list(PyObject *p) {
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (int i = 0; i < Py_SIZE(p); i++) {
        printf("Element %d: ", i);
        PyObject *item = PyList_GetItem(p, i);
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        } else {
            printf("%s\n", Py_TYPE(item)->tp_name);
        }
    }
}
void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytesObject *bytes = (PyBytesObject *)p;
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", bytes->ob_base.ob_size);
    printf("  trying string: %s\n", PyBytes_AS_STRING(bytes));
    printf("  first %ld bytes: ", MIN(bytes->ob_base.ob_size, 10));

    for (int i = 0; i < MIN(bytes->ob_base.ob_size, 10); i++) {
        printf("%02x ", ((unsigned char *)bytes->ob_sval)[i]);
    }

    printf("\n");
}
