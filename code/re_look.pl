use strict;
 
if ('ab' =~ m/a(?:b)/) {
	print("${&}\n")  # => ab
}
 
if ('ax' =~ m/a(?!b)/) {
	print("${&}\n")  # => a
}
 
if ('xb' =~ m/(?<!a)b/) {
	print("${&}\n")  # => b
}
 
if ('ab' =~ m/(?<=a)b/) {
	print("${&}\n")  # => b
}