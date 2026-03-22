# MSCS532_Assignment3

## Assignment 3: Understanding Algorithm Efficiency and Scalability

**Ranjith Kumar Bollam**  
**Course:** MSCS-532 – Algorithms and Data Structures  
**University:** University of the Cumberlands  

## Overview

This assignment focuses on analyzing and comparing the efficiency and scalability of two fundamental algorithmic techniques:

- Randomized Quicksort  
- Hash Table with Chaining  

The project includes both theoretical analysis and empirical testing to evaluate algorithm performance under different input conditions.

## Implemented Components

### 🔹 1. Randomized Quicksort
- Pivot is selected randomly  
- Provides stable average-case performance  
- Time complexity: **O(n log n)** (average)


### 🔹 2. Deterministic Quicksort
- Pivot is the first element  
- Sensitive to input order  
- Worst-case complexity: **O(n²)**  


### 🔹 3. Hash Table with Chaining
- Collision resolution using linked lists  
- Supports:
  - Insert  
  - Search  
  - Delete  
- Average-case complexity: **O(1)**  


## Experimental Setup

The algorithms were tested on different types of datasets:

- Random arrays  
- Sorted arrays  
- Reverse-sorted arrays  
- Arrays with repeated elements  


## Key Observations

- Randomized Quicksort performed consistently across all datasets  
- Deterministic Quicksort failed on:
  - Sorted data  
  - Repeated data  
- Recursion errors occurred due to poor pivot selection  
- Hash table operations worked efficiently with chaining  

## How to Run the Code

### Step 1: Clone Repository
git clone https://github.com/Ranjith8534/MSCS532_Assignment3.git

### Step 2: Navigate to Folder
cd MSCS532_Assignment3

### Step 3: Run Program
python test.py


## Output

The program will display:
- Execution times for both sorting algorithms  
- Performance comparison across datasets  
- Hash table operation results  


## Conclusion

This project demonstrates that algorithm performance depends heavily on design choices. Randomized Quicksort provides reliable scalability, while Deterministic Quicksort is prone to failure under certain conditions. Hash tables using chaining offer efficient data retrieval when the load factor is properly managed.

## 📎 Submission

GitHub Repository:  
👉 https://github.com/Ranjith8534/MSCS532_Assignment3
