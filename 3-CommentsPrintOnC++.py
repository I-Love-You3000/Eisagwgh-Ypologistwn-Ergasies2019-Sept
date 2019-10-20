from comment_parser import comment_parser

a = comment_parser.extract_comments(input("Please enter path of the C++ file you want:"), mime='text/x-c++')
print("Comment(actual_comment, number_of_line, False 1 line comment/True multiple line comment)")
print(a)
