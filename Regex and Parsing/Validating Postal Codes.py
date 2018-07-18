regex_integer_in_range = r"[0-9]{6}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(.)(?=.\1)"	# Do not delete 'r'. Explanation: (.) take the first character and group it. ?=. look ahead(?=) one more char(.) \1 repeat the first group(1) char i.e (.)  
