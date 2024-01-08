#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pyobject list
*/

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	pyobject *obj;

	size = py_SIZE(p);
	alloc = ((pylistobject *)p)->allocated;

	printf("[*] size of the python list = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = pylist_GetItem(p, i);
		printf("%s\n", py_TYPE(obj)->tp_name);
	}
}
