use strict;
 
if ('ab' =~ m/a(?=b)/) {
	print("${&}\n")  # => b
}
 
if ('ax' =~ m/a(?!b)/) {
	print("${&}\n")  # => a
}

if ('ab' =~ m/(?<=a)b/) {
	print("${&}\n")  # => b
}
 
if ('xb' =~ m/(?<!a)b/) {
	print("${&}\n")  # => b
}
 
