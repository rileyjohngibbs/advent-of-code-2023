#!/bin/bash

DAY=$(printf "%02d" $1)

SOLUTION_DIR=$(dirname $BASH_SOURCE)/aoc/solutions/day$DAY
mkdir $SOLUTION_DIR
touch $SOLUTION_DIR/__init__.py
sed "s/DAY = 0/DAY = $1/g" $(dirname $BASH_SOURCE)/aoc/template.txt > $SOLUTION_DIR/alpha.py

TEST_DIR=$(dirname $BASH_SOURCE)/aoc/tests/day$DAY
mkdir $TEST_DIR
touch $TEST_DIR/__init__.py
sed "s/day00/day$DAY/g" $(dirname $BASH_SOURCE)/aoc/test_template.txt > $TEST_DIR/test_alpha.py