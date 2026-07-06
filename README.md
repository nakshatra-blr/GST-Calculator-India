# 🧮 GST Calculator India

A simple, easy-to-use **GST Calculator** for Indian businesses and students.

## Features

- ✅ Calculate **CGST + SGST** (Intra-state)
- ✅ Calculate **IGST** (Inter-state)
- ✅ Supports all GST slabs: **0%, 5%, 12%, 18%, 28%**
- ✅ Reverse GST calculation (extract GST from inclusive price)
- ✅ Works for both goods and services

## GST Slabs in India (2026)

| Slab | Items |
|------|-------|
| **0%** | Essential food items, books, healthcare |
| **5%** | Packaged food, transport, small restaurants |
| **12%** | Processed food, business class air tickets |
| **18%** | Most goods & services, IT services, restaurants |
| **28%** | Luxury goods, cars, tobacco, aerated drinks |

## Quick Formula

```
GST Amount = (Original Price × GST Rate) / 100
CGST = GST Amount / 2
SGST = GST Amount / 2
IGST = GST Amount (full, for inter-state)
Total Price = Original Price + GST Amount
```

## Usage

```python
python gst_calculator.py
```

## Example

```
Enter amount (₹): 10000
Select GST slab (5/12/18/28): 18
Transaction type (intra/inter): intra

Results:
Base Amount:  ₹10,000.00
CGST (9%):    ₹900.00
SGST (9%):    ₹900.00
Total GST:    ₹1,800.00
Final Amount: ₹11,800.00
```

## Who is this for?

- 📚 **B.Com / M.Com students** learning GST
- 💼 **Small business owners** calculating invoices
- 📊 **CA/CMA aspirants** practicing taxation
- 🏢 **Accountants** doing quick calculations

## About

Made by [Nakshatra Prakash](https://github.com/nakshatra-blr) — B.Com Graduate passionate about making finance concepts accessible.

⭐ Star this repo if you find it useful!