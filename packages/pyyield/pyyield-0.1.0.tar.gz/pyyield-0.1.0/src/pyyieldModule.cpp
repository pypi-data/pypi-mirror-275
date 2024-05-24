#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <thread>

// Only added for IDE complaint.
#ifndef NULL
#define NULL nullptr
#endif

static PyObject* pyyield(PyObject* self, PyObject* args) {
	// Just yield, nothing else.
	::std::this_thread::yield();
	Py_RETURN_NONE;
}

static PyMethodDef PyYieldMethods[] = {
	{"pyyield", pyyield, METH_NOARGS, "Execute a OS thread 'yield' command."},
	{nullptr, nullptr, 0, nullptr} /* Sentinel */
};

static struct PyModuleDef pyyieldmodule
	= {PyModuleDef_HEAD_INIT,
	   "pyyield", /* name of module */
	   nullptr,	  /* module documentation, may be NULL */
	   -1,		  /* size of per-interpreter state of the module,
					 or -1 if the module keeps state in global variables. */
	   PyYieldMethods};

PyMODINIT_FUNC PyInit_pyyield(void) { return PyModule_Create(&pyyieldmodule); }

int main(int argc, char* argv[]) {
	wchar_t* program = Py_DecodeLocale(argv[0], nullptr);
	if (program == nullptr) {
		fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
		exit(1);
	}

	/* Add a built-in module, before Py_Initialize */
	if (PyImport_AppendInittab("pyyield", PyInit_pyyield) == -1) {
		fprintf(stderr, "Error: could not extend in-built modules table\n");
		exit(1);
	}

	/* Pass argv[0] to the Python interpreter */
	Py_SetProgramName(program);

	/* Initialize the Python interpreter.  Required.
	   If this step fails, it will be a fatal error. */
	Py_Initialize();

	/* Optionally import the module; alternatively,
	   import can be deferred until the embedded script
	   imports it. */
	PyObject* pmodule = PyImport_ImportModule("pyyield");
	if (!pmodule) {
		PyErr_Print();
		fprintf(stderr, "Error: could not import module 'pyyield'\n");
	}

	PyMem_RawFree(program);
	return 0;
}
