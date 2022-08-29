#include <Python.h>
#include <stdio.h>
#include <object.h>

/**
print_python_list_info - print basic info on python lists
@p: PyObject
*/

void print_python_list_info(PyObject *p)
{
long int i = 0;
PyObject *item;

printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (; i < Py_SIZE(p); i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}
