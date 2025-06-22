
# Simple Object Model in Python

This project implements a **minimal object model** inspired by Carl Friedrich Bolz’s *A Simple Object Model* (from the book *500 Lines or Less*). The goal is to **reconstruct core principles of object-oriented programming**—like classes, inheritance, bound methods, descriptors, and metaclasses—entirely from scratch using Python.

The implementation is **modular, testable, and enhanced** to be recruiter-friendly and educational.

---

## 🚀 Features

✅ Class and instance system  
✅ Attribute reading and writing  
✅ Method resolution order (MRO)  
✅ Support for `isinstance()` and `issubclass()`  
✅ Bound method handling (attribute-based model)  
✅ Meta-object protocol (`__getattr__`, `__setattr__`)  
✅ Descriptors (`__get__`)  
✅ Map-based optimization for efficient instance layout (like hidden classes in JS VMs)

---

## 🧠 Project Motivation

Object models form the backbone of dynamic programming languages like Python, Ruby, and JavaScript. By re-implementing a Python-inspired object model from scratch, this project demonstrates:

- Deep understanding of language internals
- System design and abstraction skills
- Custom metaprogramming
- Pythonic architecture and testing best practices

---

## 🏗️ Project Structure

```
simple_object_model/
├── src/
│   ├── base.py          # Core logic: attr lookup, callmethod, MRO
│   ├── class_model.py   # Class definition and inheritance logic
│   ├── instance.py      # Object layout and hidden class optimization
│   ├── maps.py          # Hidden class system (map-based layout)
├── tests/
│   └── test_object_model.py  # Pytest-compatible tests
```

---

## 🧪 Run the Tests

Make sure `pytest` is installed:

```bash
pip install pytest
```

Run the test suite:

```bash
pytest tests/
```

---

## 📘 Attribution

This project is **inspired by** Carl Friedrich Bolz’s *A Simple Object Model*, but the code is **entirely original**, refactored, modularized, and documented by me to reflect **best practices** and **educational clarity**.  
It serves as a foundation for exploring dynamic language behavior and object system design.

---

## 💼 Ideal For

- Technical interview prep
- Showcasing language internals understanding
- Building credibility for roles in:
  - Language tooling
  - Virtual machines (VMs)
  - Python internals
  - Systems programming
  - Compiler/interpreter development

---

## 🧑‍💻 Author

**Dharshini Vasudevan**  
M.Eng in Electrical and Computer Engineering  
Actively seeking roles in embedded systems, software development, and language tooling  
🔗 [LinkedIn](#) | 📫 [Email](#)
