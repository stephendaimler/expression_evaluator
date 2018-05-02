EXPRESSION EVALUATOR
--------------------

AUTHOR
------

Stephen Daimler


CONTENTS OF THIS FILE
---------------------

* Introduction
* Python Environment
* Instructions to Run


INTRODUCTION
------------

The purpose of this command-line program is to evaluate simple mathematical
operator expressions such as '+ 1 2' which is the same as '1 + 2' which would
evaluate to 3. Here are the rules:

1. The syntax is always 'Operator Expression Expression' with one operator followed by two expressions.  
2. Operators supported are '+' and '-'
3. Expressions can be a positive or negative number such as 5 or another
(nested) expression like '- 4 5'.
4. The input is a space delimited string like '- 7 8' and the output is a
number like -1.

Here are examples of valid operator expressions:
+ '+ 1 5' evaluates to 6
+ '- 7 11' evaluates to -4
+ '+ 3 - 8 9' evaluates to 2
+ '- 1 + 4 - 3 2' evaluates to -4

An invalid operator expression would be:
+ '- 5 + 2'

This is because the syntax is incorrect: 'Operator Expression Operator Expression'


PYTHON ENVIRONMENT
------------------

* python 3.6.2


INSTRUCTIONS
------------

To get started, setup your environment like listed above. To execute the code
below, on the command line, navigate to the directory with the exp_eval.py file.

Execute the following command from the command line with the string to test as
an argument.

python exp_eval.py {string to test}

For example:

python exp_eval.py "+ 1 2 - 3 4"

To execute the unit tests, in the same directory, run:

python test_exp_eval.py
