# 🛒 MasterShop System - OOP Foundation

This is a backend logic project I built to master **Object-Oriented Programming (OOP)** principles before diving into **FastAPI**. It serves as the core engine for my upcoming web services.

## 🚀 Why I Built This
Before moving to API development, I wanted to ensure a rock-solid foundation in:
- **Modular Architecture:** Separating logic into `base`, `models`, and `managers`.
- **Abstraction & Inheritance:** Using `ABC` to create scalable "contracts" for products and payments.
- **Dynamic Logic:** Handling multiple discount types and payment methods through polymorphism.

## 📂 Project Structure
- `base.py`: The core templates (Abstract Classes).
- `models.py`: Concrete products and discount implementations.
- `payments.py`: Payment gateway logic (Credit Card, etc.).
- `order_manager.py`: The main engine handling checkout and totals.

## 💡 Key Takeaway
Building this helped me understand how to manage complex data flows and inheritance chains. It’s the perfect "logic layer" to now wrap with a modern web framework like **FastAPI**.

---
**Run the demo:** `python main.py`
