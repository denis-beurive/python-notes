# Encoding

## Declaring the source encoding

Insert this line at the very top of the source file. This line should be the first or the second line of the file. If it is the second line, then the first line must also be a comment.

    # -*- coding: <encoding-name> -*-

Example:

    # -*- coding: utf-8 -*-

See [Encoding declarations](https://docs.python.org/3/reference/lexical_analysis.html#encoding-declarations)

> If a comment in the first or second line of the Python script matches the regular expression `coding[=:]\s*([-\w.]+)`, this comment is processed as an encoding declaration; the first group of this expression names the encoding of the source code file. The encoding declaration must appear on a line of its own. If it is the second line, the first line must also be a comment-only line.
