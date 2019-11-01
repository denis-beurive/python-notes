# Exceptions

## Get the full exception traceback

You can use `traceback.format_exc()`:

	try:
		# Do something that can raise an exception...
	except Exception as e:
		print(traceback.format_exc())

