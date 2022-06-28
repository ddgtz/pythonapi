"""
    example01.py
    This example retrieves arguments from the command line.  Test it by opening
    a command-line, changing to the student_files directory, then run the
    following statement:

        python example01.py cat bird

        python example01.py
"""
import sys

pet1, pet2 = 'dog', 'cat'

if len(sys.argv) >= 3:
    pet1 = sys.argv[1]
    pet2 = sys.argv[2]

print('My', pet1, 'chases my', pet2)
