# Calculator Project

## Student

Name: Megha Patel

## Purpose

The purpose of this project is to create a small Python calculator package that supports addition and subtraction. The project uses pytest to verify the calculator functions locally and through GitHub Actions.

## Environment

Python version: 3.12.14

pytest version: 8.4.2

## Setup

I created a Python virtual environment named `.venv` using:

python3 -m venv .venv

I activated the virtual environment using:

source .venv/bin/activate

I copied `requirements.txt` and `pytest.ini` from the `provided` directory into the project root.

I installed the required dependencies using:

python -m pip install -r requirements.txt

The `.venv` directory stays on my local computer and is excluded from Git. Virtual environment files, caches, and Python bytecode should not be committed to the repository.

## Running Tests

To run the student test suite:

python -m pytest

To run the student tests and complete checks:

python -m pytest tests checks -v

## Project Issues

Setup Issue:
https://github.com/mp2395/is218_test1_official/issues/1

Addition Issue:
https://github.com/mp2395/is218_test1_official/issues/3

Subtraction Issue:
https://github.com/mp2395/is218_test1_official/issues/5

Delivery Issue:
https://github.com/mp2395/is218_test1_official/issues/7

## Test Explanation

One addition test uses 2 and 3 as its inputs. The expected result is 5. The assertion verifies that the `add` function returns 5 when given the inputs 2 and 3.

## Verification

The project uses the supplied pytest configuration.

The calculator implementation and student tests are verified locally with pytest and through the supplied GitHub Actions assessment workflow.