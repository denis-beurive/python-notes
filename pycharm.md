# PyCharm

This document contains useful information for using PyCharm.

# Configuring a remote Python interpreter

`File` **>** `Settings` **>** `Project Interpreter`

![Project Interpreter Dettings](images/pycharm-project-interpreter-settings.png)

`Label[Project Interpreter]` **>** `Add`

![Add Project Interpreter](images/pycharm-add-project-interpreter.png)

Select `SSH Interpreter` : set the network configuration for SSH.

![SSH interpreter](images/pycharm-configure-ssh-interpreter.png)

`Next` : set the credentials for SSH.

![Configure SSH authentiction](images/pycharm-ssh-auth.png)

`Next` : configure the interpreter.

> Make sure to specify the Python interpreter bound to the Pipven environment !

    (thermo) dev@unassigned-hostname:~/projects/thermo$ which python
    /home/dev/.local/share/virtualenvs/thermo-hZt1O9lB/bin/python

![Set path to the remote interpreter](images/pycharm-remote-interpreter-path.png)

> If you are using a VM, then you should have set a shared folder. If that's the case then you would like to uncheck "_Automatically upload project files to the server_"

> Please note that if the remote host is a VM running on the same host as the one running PyCharm (let's call it, the "_editor host_"), then you probably used a shared directory (between the VM and the "_editor host_"). In this case, you don't need to configure any _deployment settings_ ("`Build, Extension, Deployment`" => "`Deployment`": **leave everything empty**).

# Configuration deployment over FTP

If you work on a remote host, then you must set up a mechanism used to deploy the project sources.

There is one thing to know: 

The _deployment path_ (`Build, Execution, Deployment` **=>** `Deployment` **=>** [`Mappings`] ) is relative to the _root path_ (`Build, Execution, Deployment` **=>** `Deployment` **=>** [`Connection`]).

![Deployment Connecion](images/deploument-ftp-connection.png)

![Deployment Deployment](images/deployment-ftp-mappings.png)

# Configuring the code inspection

![Code inspection](images/pycharm-code-inspection-py-version.png)

> These configuration panel allows you to configure the version of python against which the editor should perform its inspection.

# Configuring the docstring format

![Python Integrated Tools Settings](images/pycharm-docstring-settings.png)

# Configuring PYTHONPATH

This configuration works whether you are using a local or a remote interpreter.

`File` **>** `Settings` **>** `Project Interpreter`

`Label[Project Interpreter]` **>** `Show All`

![PythonPath 1](images/pycharm-pythonpath-1.png)

Select the interpreter to configure, and then click on the icon with the subtext: `Show Paths for the selected interpreter`.

![PythonPath 2](images/pycharm-pythonpath-2.png)

Then, click on '`+`' and add the path:

![PythonPath 3](images/pycharm-pythonpath-3.png)

# Comments used to configure the code analysis

This list comes for the [excellent document](https://gist.github.com/pylover/7870c235867cf22817ac5b096defb768).

    # noinspection PyPep8
    # noinspection PyPep8Naming
    # noinspection PyTypeChecker
    # noinspection PyAbstractClass
    # noinspection PyArgumentEqualDefault
    # noinspection PyArgumentList
    # noinspection PyAssignmentToLoopOrWithParameter
    # noinspection PyAttributeOutsideInit
    # noinspection PyAugmentAssignment
    # noinspection PyBroadException
    # noinspection PyByteLiteral
    # noinspection PyCallByClass
    # noinspection PyChainedComparsons
    # noinspection PyClassHasNoInit
    # noinspection PyClassicStyleClass
    # noinspection PyComparisonWithNone
    # noinspection PyCompatibility
    # noinspection PyDecorator
    # noinspection PyDefaultArgument
    # noinspection PyDictCreation
    # noinspection PyDictDuplicateKeys
    # noinspection PyDocstringTypes
    # noinspection PyExceptClausesOrder
    # noinspection PyExceptionInheritance
    # noinspection PyFromFutureImport
    # noinspection PyGlobalUndefined
    # noinspection PyIncorrectDocstring
    # noinspection PyInitNewSignature
    # noinspection PyInterpreter
    # noinspection PyListCreation
    # noinspection PyMandatoryEncoding
    # noinspection PyMethodFirstArgAssignment
    # noinspection PyMethodMayBeStatic
    # noinspection PyMethodOverriding
    # noinspection PyMethodParameters
    # noinspection PyMissingConstructor
    # noinspection PyMissingOrEmptyDocstring
    # noinspection PyNestedDecorators
    # noinspection PynonAsciiChar
    # noinspection PyNoneFunctionAssignment
    # noinspection PyOldStyleClasses
    # noinspection PyPackageRequirements
    # noinspection PyPropertyAccess
    # noinspection PyPropertyDefinition
    # noinspection PyProtectedMember
    # noinspection PyRaisingNewStyleClass
    # noinspection PyRedeclaration
    # noinspection PyRedundantParentheses
    # noinspection PySetFunctionToLiteral
    # noinspection PySimplifyBooleanCheck
    # noinspection PySingleQuotedDocstring
    # noinspection PyStatementEffect
    # noinspection PyStringException
    # noinspection PyStringFormat
    # noinspection PySuperArguments
    # noinspection PyTrailingSemicolon
    # noinspection PyTupleAssignmentBalance
    # noinspection PyTupleItemAssignment
    # noinspection PyUnboundLocalVariable
    # noinspection PyUnnecessaryBackslash
    # noinspection PyUnreachableCode
    # noinspection PyUnresolvedReferences
    # noinspection PyUnusedLocal
    # noinspection ReturnValueFromInit



