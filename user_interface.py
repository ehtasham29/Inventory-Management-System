def main_messages(message, symbol="=", width=50):
    print("\n" + symbol * width)
    print(f" {message} ".center(width, symbol))
    print(symbol * width)

