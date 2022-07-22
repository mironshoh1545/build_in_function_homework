# the task condition is placed in the README file
# https://github.com/codeschool43/Build_in_function_homework#build_func03

from multiprocessing.connection import answer_challenge


def build_func03(n):
    answer = 3 * (n + 1) ** 2
    return answer
n = 3.5
print(build_func03(n))