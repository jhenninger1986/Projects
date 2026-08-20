import sys
import ctypes

def show_windows_popup(title, message, box_type):
    # 0x40000 ensures the popup stays on top of all other windows
    style = box_type | 0x40000 
    ctypes.windll.user32.MessageBoxW(0, message, title, style)

def main():
    # We now need 3 extra inputs: operation, num1, num2 (plus script name = 4 total)
    if len(sys.argv) < 4:
        print("\n[!] Error: Missing inputs.")
        print("Usage: python math.py <operation> <number1> <number2>")
        print("Operations: add, sub, mul, div")
        return

    # Grab the inputs from the command line
    operation = sys.argv[1].lower() # Converts to lowercase to prevent typos
    input1 = sys.argv[2]
    input2 = sys.argv[3]

    try:
        num1 = float(input1)
        num2 = float(input2)
        
        # Determine the operation
        if operation == "add":
            result = num1 + num2
            op_word = "plus"
        elif operation == "sub":
            result = num1 - num2
            op_word = "minus"
        elif operation == "mul":
            result = num1 * num2
            op_word = "multiplied by"
        elif operation == "div":
            if num2 == 0:
                show_windows_popup("Math Error", "You cannot divide by zero!", 16) # Error icon
                return
            result = num1 / num2
            op_word = "divided by"
        else:
            show_windows_popup("Invalid Operation", f"'{operation}' is not a valid operation.\nUse: add, sub, mul, or div", 48) # Warning icon
            return

        # Success Popup
        msg_title = f"Operation: {operation.upper()}"
        msg_text = f"Calculation:\n{num1} {op_word} {num2}\n\nResult = {result}"
        show_windows_popup(msg_title, msg_text, 0) # Info icon

    except ValueError:
        show_windows_popup("Input Error", "Please make sure your second and third inputs are numbers!", 16)

if __name__ == "__main__":
    main()
