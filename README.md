# Object-Oriented Library Management System with Customized Core Algorithms (Python)

A native Command-Line Interface (CLI) application built using pure Python 3.x to handle comprehensive book inventory management, user transactions, and library borrowing workflows. This repository demonstrates foundational computer science structures, clean code practices, and manual algorithmic optimization from scratch without relying on Python's built-in sorting or searching methodologies.

## 🛠️ System Architecture: The 4 Pillars of OOP in Python

This application strictly implements Object-Oriented Programming (OOP) design patterns using Pythonic standards to ensure scalability, clean code isolation, and easy maintainability:

1. **Encapsulation:** Secured sensitive system states (e.g., book database records, user profiles, and borrowing logs) inside class access control by utilizing Pythonic private/protected naming conventions (`_variable` or `__variable`). Interaction is restricted via formal getter/setter methods and explicit constructors (`__init__`).
2. **Inheritance:** Modeled hierarchical user types, where specialized roles (e.g., `Admin`, `RegisteredMember`) inherit baseline operational properties from a parent `User` base class via native Python class inheritance.
3. **Polymorphism:** Overrode inventory transactional methods to support flexible, multi-format media borrowing logic (e.g., the `borrow_item()` method exhibits different behaviors based on whether the caller instance is an Admin or a Regular Member).
4. **Abstraction:** Concealed background array index modifications, item pop operations, and data dictionary mutations behind clean interface controllers, exposing only high-level method interfaces to the main runtime loop.

---

## ⚡ Algorithmic Enhancements & Manual Optimizations

To demonstrate core computer science foundations, search and sort functionalities are built completely from scratch using primitive indexing loops, purposely bypassing Python's native `.sort()`, `sorted()`, or `in` operator keywords:

### 1. Optimized Searching (Binary Search)
- **Implementation:** Programmed a custom iterative **Binary Search** algorithm to find books by unique identifiers (ISBN/ID) or pre-sorted attributes.
- **Complexity:** Reduces search overhead from linear time \(O(n)\) to logarithmic time \(O(\log n)\), ensuring highly efficient record lookups as the internal list catalog grows.

### 2. Index Sorting (Bubble Sort)
- **Implementation:** Built a manual **Bubble Sort** mechanism to sort Python array structures based on alphabetical titles or historical transaction timestamps.
- **Use Case:** Pre-conditions the list datasets to satisfy the strict sorted-array requirement needed for the Binary Search algorithm to function.

### 3. Structural Data Ingestion (CRU Loops)
- Designed a continuous `while` command loop supporting comprehensive data updates:
  - **Create:** Instantiating new book and member object instances securely into memory array tracking blocks.
  - **Read:** Displaying formatted library catalogues and dynamic transaction logs via clean console text layouts.
  - **Update:** Real-time state mutation for returning books, updating inventory counters, and calculation of transaction states.

---

## 📁 Repository Structure

```text
library-management-system-oop/
├── src/
│   ├── __init__.py
│   ├── main.py                <- Application entry point and interactive CLI loop
│   └── models/                <- Domain class definitions
│       ├── __init__.py
│       ├── user.py            <- Base User class, Admin, and Member child classes
│       └── item.py            <- Book and Inventory class models
└── README.md                  <- Comprehensive system documentation
```

---

## ⚙️ How to Run the System

### Prerequisites
Ensure you have Python 3.8+ installed on your system. No external third-party libraries (`pip`) are required.

### Execution
Run the script directly via your terminal interpreter:
```bash
python src/main.py
```
