# 🧠 Simple Object Model in Python

This project reimplements a **minimal Python-like object system** from scratch, inspired by Carl Friedrich Bolz’s “A Simple Object Model” (from the book *500 Lines or Less*). It models how classes, instances, methods, attributes, and metaclasses work under the hood.

The goal: to **understand the internals** of object-oriented programming and demonstrate deep reasoning about Python’s runtime behavior.

---

## 🚀 Features

- ✅ Class and Instance system
- ✅ Attribute reading and writing
- ✅ Method resolution order (MRO)
- ✅ Support for `isinstance()` and `issubclass()`
- ✅ Bound method handling (`f(obj)` binds `obj.f`)
- ✅ Meta-object protocol: `__getattr__`, `__setattr__`
- ✅ Unit tests using `pytest`

---

## 🧠 Why This Matters

Object models form the foundation of dynamic languages like Python, Ruby, and JavaScript. By building one manually, this project shows:

- Understanding of class-instance relationships
- Design of attribute dispatch and method binding
- MRO and inheritance resolution
- Custom metaprogramming logic

---

## 🏗️ Project Structure

```
simple_object_model/
├── src/
│   ├── base.py              # Core object logic (Base class, attribute handling)
│   ├── class_.py            # Class definition and method resolution
│   └── test_object_model.py # Pytest test cases covering core behavior
```

---

## 🧪 Running the Tests

Make sure `pytest` is installed:

```bash
pip install pytest
```

Run the test suite:

```bash
cd src/
python -m pytest test_object_model.py
```

---

## 📘 Attribution

Inspired by Carl Friedrich Bolz’s object model reimplementation, but all code is **fully original**, modularized, and written for clarity and extensibility.

---

## 💼 Author

**Dharshini Vasudevan**  
M.Eng in Electrical and Computer Engineering  
Actively seeking roles in embedded systems, software development, and language tooling.

📫 [LinkedIn](https://www.linkedin.com/in/dharshini-vasudevan/)  
🔗 GitHub: [Dharsh076](https://github.com/Dharsh076)
