#include <Python.h>

void print_python_string(PyObject *p) {
    Py_ssize_t length;
    Py_UNICODE *unicode_str;
    PyVarObject *var_obj = (PyVarObject *)p;

    if (!PyUnicode_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GET_LENGTH(p);
    unicode_str = PyUnicode_AsUnicode(p);

    printf("[.] string object info\n");
    printf("  type: %s\n", (var_obj->ob_type)->tp_name);

    if (PyUnicode_IS_COMPACT_ASCII(p)) {
        printf("  type: compact ascii\n");
    } else if (PyUnicode_IS_COMPACT_UNICODE(p)) {
        printf("  type: compact unicode object\n");
    } else {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    printf("  length: %zd\n", length);

    if (PyUnicode_IS_COMPACT_ASCII(p)) {
        printf("  value: %s\n", PyUnicode_AsUTF8(p));
    } else {
        printf("  value: %ls\n", unicode_str);
    }
}
