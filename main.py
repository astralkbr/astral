# Mukammal "print" va "hello" namunasi
def greet_user(name):
    """Foydalanuvchini salomlash funksiyasi"""
    print(f"Hello, {name}! Welcome to the Python world.")

def main():
    """Dastur boshlanish nuqtasi"""
    user_name = input("Ismingizni kiriting: ")
    greet_user(user_name)

if __name__ == "__main__":
    main()
