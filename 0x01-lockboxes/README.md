#Lockboxes

This repository contains the implementation of a Python algorithm for solving the "Lockboxes" problem.

##Problem Description

You are given n number of locked boxes, each numbered sequentially from 0 to n - 1. Each box may contain keys to the other boxes. The goal is to determine if it is possible to open all the boxes.

The algorithm should be implemented in a method called canUnlockAll(boxes), which takes a list of lists as a parameter. Each element in the list represents a box, and the list within each box contains the keys it holds.

The following rules apply:

    A key with the same number as a box opens that box.
    You can assume all keys will be positive integers.
    There can be keys that do not have boxes.
    The first box, boxes[0], is always unlocked.

The method should return True if all boxes can be opened, and False otherwise.


Usage

To test the algorithm, you can use the provided main_0.py script. It includes example test cases for the canUnlockAll method.

bash
```
$ ./main_0.py
```
The expected output for the given test cases is:

graphql
```
True
True
False
```
