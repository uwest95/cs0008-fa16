#!/usr/bin/python3

# Here's a simple use of two dimensional lists. Here, we're going
# to keep track of 4 students' grades on 3 exams.
student_scores = [
  [68, 77, 98],
  [88, 86, 89],
  [91, 92, 94],
  [99, 89, 90]
]


# To loop through a 2D list, we need to use two loops.
# The first loop will iterate on the rows/students of the table.
for r in range(len(student_scores)):
  total = 0  # Let's keep a running total
  # The second loop needs to look at the grade in each 'column'
  # Notice how we need to say student_scores[r] to get the length
  # of the list in position r of the student_scores list.
  for c in range(len(student_scores[r])):
    total += student_scores[r][c]
  print('Student {} Average grade: {}'.format(r, total / 3))

# Here's a slightly modified version that doesn't use indices
# but rather just loops directly over the lists' items.
for s in student_scores:
  total = 0  # Let's keep a running total
  for g in s:  # Remember, s is a list so we can iterate over it
    total += g
  print('Average grade: ', total / 3)
