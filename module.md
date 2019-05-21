# Module

## Loading a module given its path

	import importlib.util
	from importlib.machinery import ModuleSpec

	path: str = '/path/to/module.py'

	spec: ModuleSpec = importlib.util.spec_from_file_location("nom", path)
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)

	# Now you can use "module".
	# Assuming that "/path/to/module.py" contains a class YourClass.

	my_object = module.YourClass()

