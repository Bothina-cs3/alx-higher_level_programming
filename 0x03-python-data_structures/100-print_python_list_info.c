#include <Python.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: PyObject pointer to a Python list
 */
void print_python_list_info(PyObject *p)
{
	long int list_size, allocated, i;
	PyObject *obj;

	list_size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < list_size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
