# 🔍 DSA Day 01 – Binary Search in Python

This repository contains Python implementation of the **Binary Search algorithm**, a fundamental concept in Data Structures and Algorithms (DSA). This is part of the 100-day AI & DSA coding challenge.

---

## 📌 What is Binary Search?

Binary Search is a fast search algorithm with **O(log n)** time complexity. It works on sorted arrays by repeatedly dividing the search interval in half.

---

## 📁 File Structure

D-Day-01-Binary-Search-Python/
├── binary_search.py # Python implementation of Binary Search


---

## 🧠 Features of the Code

- Works on sorted lists (ascending)
- Takes input as array and target
- Handles element found / not found
- Contains both **iterative** and **recursive** examples (optional extension)

---

## 💻 Example Code (binary_search.py)

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

# Example
arr = [1, 3, 5, 7, 9, 11]
target = int(input("Enter target: "))
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")


👨‍💻 Author
Shankar Kumar
💡 Passionate about AI, DSA, and System Design
🔗 GitHub: @Shank312

📌 Repository
🔗 GitHub Repo: D-Day-01-Binary-Search-Python

🚀 “Binary Search is the foundation of algorithmic thinking. Master it, and you master speed.”
