#!/usr/bin/python3

# Here's a simple use of two dimensional lists. Here, we're going
# to keep track of 4 students' grades on 3 exams.
student_scores = [
  [68, 77, 98],
  [88, 86, 89],
  [91, 92, 94],
  [99, 89, 90]
]

# Here's a slightly modified version that doesn't use indices
# but rather just loops directly over the lists' items.
for s in student_scores:
  s.clear()
  total = 0  # Let's keep a running total
  for g in s:  # Remember, s is a list so we can iterate over it
    total += g
  print('Average grade: ', total / 3)

print(student_scores)
