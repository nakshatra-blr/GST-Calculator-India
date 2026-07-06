"""
GST Calculator India
Calculate CGST, SGST, IGST for any amount
Supports all GST slabs: 0%, 5%, 12%, 18%, 28%
Author: Nakshatra Prakash
"""

def calculate_gst(amount, rate, transaction_type="intra"):
    """Calculate GST breakdown"""
    gst_amount = (amount * rate) / 100
    
    if transaction_type == "intra":
        cgst = gst_amount / 2
        sgst = gst_amount / 2
        return {
            "base_amount": amount,
            "gst_rate": rate,
            "cgst_rate": rate / 2,
            "sgst_rate": rate / 2,
            "cgst": cgst,
            "sgst": sgst,
            "igst": 0,
            "total_gst": gst_amount,
            "final_amount": amount + gst_amount
        }
    else:
        return {
            "base_amount": amount,
            "gst_rate": rate,
            "cgst_rate": 0,
            "sgst_rate": 0,
            "cgst": 0,
            "sgst": 0,
            "igst": gst_amount,
            "total_gst": gst_amount,
            "final_amount": amount + gst_amount
        }

def reverse_gst(inclusive_amount, rate):
    """Extract GST from an inclusive price"""
    base_amount = (inclusive_amount * 100) / (100 + rate)
    gst_amount = inclusive_amount - base_amount
    return {
        "inclusive_amount": inclusive_amount,
        "base_amount": round(base_amount, 2),
        "gst_amount": round(gst_amount, 2),
        "gst_rate": rate
    }

def print_result(result):
    """Pretty print the GST calculation"""
    print("\n" + "=" * 40)
    print("       GST CALCULATION RESULT")
    print("=" * 40)
    print(f"  Base Amount:    Rs.{result['base_amount']:,.2f}")
    if result['cgst'] > 0:
        print(f"  CGST ({result['cgst_rate']}%):    Rs.{result['cgst']:,.2f}")
        print(f"  SGST ({result['sgst_rate']}%):    Rs.{result['sgst']:,.2f}")
    if result['igst'] > 0:
        print(f"  IGST ({result['gst_rate']}%):    Rs.{result['igst']:,.2f}")
    print(f"  Total GST:      Rs.{result['total_gst']:,.2f}")
    print("-" * 40)
    print(f"  FINAL AMOUNT:   Rs.{result['final_amount']:,.2f}")
    print("=" * 40)

def main():
    print("\n" + "=" * 40)
    print("    GST CALCULATOR INDIA")
    print("    By Nakshatra Prakash")
    print("=" * 40)
    
    valid_slabs = [0, 5, 12, 18, 28]
    
    while True:
        print("\nOptions:")
        print("1. Calculate GST (add GST to amount)")
        print("2. Reverse GST (extract GST from inclusive price)")
        print("3. Exit")
        
        choice = input("\nSelect option (1/2/3): ").strip()
        
        if choice == "3":
            print("Thank you! Happy Calculating!")
            break
        
        try:
            amount = float(input("Enter amount (Rs.): "))
        except ValueError:
            print("Invalid amount!")
            continue
        
        print(f"GST Slabs available: {valid_slabs}")
        try:
            rate = int(input("Select GST rate (%): "))
            if rate not in valid_slabs:
                print(f"Invalid! Choose from {valid_slabs}")
                continue
        except ValueError:
            print("Invalid rate!")
            continue
        
        if choice == "1":
            txn_type = input("Transaction type (intra/inter): ").strip().lower()
            if txn_type not in ["intra", "inter"]:
                txn_type = "intra"
            result = calculate_gst(amount, rate, txn_type)
            print_result(result)
        
        elif choice == "2":
            result = reverse_gst(amount, rate)
            print(f"\nInclusive Amount: Rs.{result['inclusive_amount']:,.2f}")
            print(f"Base Amount: Rs.{result['base_amount']:,.2f}")
            print(f"GST ({result['gst_rate']}%): Rs.{result['gst_amount']:,.2f}")

if __name__ == "__main__":
    main()