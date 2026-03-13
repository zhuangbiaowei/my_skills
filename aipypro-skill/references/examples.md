# AipyPro Usage Examples
*Comprehensive collection of AipyPro usage examples*
*Last Updated: 2026-03-13 12:25:52*
## Basic Examples
### Example 1: Hello World
**Command:**
```bash
aipypro run "print Hello World"
```
**Generated Code:**
```python
print("Hello World")
```
**Expected Output:**
Hello World
**Use Case:** Testing basic AipyPro functionality
### Example 2: Simple Calculation
**Command:**
```bash
aipypro run "calculate 7 * 8"
```
**Generated Code:**
```python
result = 7 * 8
print("7 * 8 =", result)
```
**Expected Output:**
7 * 8 = 56
**Use Case:** Quick calculations
### Example 3: Current Directory
**Command:**
```bash
aipypro run "show current directory"
```
**Generated Code:**
```python
import os
current_dir = os.getcwd()
print("Current Directory:", current_dir)
```
**Expected Output:**
Current Directory: /path/to/current/dir
**Use Case:** Quick directory inspection
## Programming Examples
### Example 4: Function Creation
**Command:**
```bash
aipypro run "create a Python function to calculate factorial"
```
**Generated Code:**
```python
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
print(factorial(5))
```
**Expected Output:**
120
**Use Case:** Learning Python functions
### Example 5: Stack Data Structure
**Command:**
```bash
aipypro run "implement a stack data structure in Python"
```
**Generated Code:**
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def is_empty(self):
        return len(self.items) == 0
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())
```
**Expected Output:**
2
**Use Case:** Learning data structures
## Data Analysis Examples
### Example 6: Basic Statistics
**Command:**
```bash
aipypro run "calculate mean for [10, 20, 30, 40, 50]"
```
**Generated Code:**
```python
data = [10, 20, 30, 40, 50]
mean = sum(data) / len(data)
print("Mean:", mean)
```
**Expected Output:**
Mean: 30.0
**Use Case:** Quick statistical analysis
### Example 7: Data Visualization
**Command:**
```bash
aipypro run "create a simple plot"
```
**Generated Code:**
```python
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("Simple Plot")
plt.savefig("plot.png")
print("Plot saved as plot.png")
```
**Expected Output:**
A plot saved as plot.png
**Use Case:** Creating visualizations
## File System Examples
### Example 8: Directory Analysis
**Command:**
```bash
aipypro run "list files in current directory"
```
**Generated Code:**
```python
import os
files = os.listdir(".")
for file in files:
    print(file)
```
**Expected Output:**
file1.txt
file2.py
folder1
**Use Case:** File system operations
### Example 9: File Search
**Command:**
```bash
aipypro run "search for Python files"
```
**Generated Code:**
```python
import os
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            print(os.path.join(root, file))
```
**Expected Output:**
./script1.py
./src/script2.py
**Use Case:** File searching
## System Administration Examples
### Example 10: System Monitoring
**Command:**
```bash
aipypro run "check system information"
```
**Generated Code:**
```python
import platform
print("System:", platform.system())
print("Release:", platform.release())
print("Python Version:", platform.python_version())
```
**Expected Output:**
System: Windows
Release: 10
Python Version: 3.12.0
**Use Case:** System information
## Conclusion
This document provides basic examples for AipyPro usage.
