# Завдання 1 – SRP
class Subscriber:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


class SMSService:
    def send_sms(self, subscriber, message):
        print(f"SMS для {subscriber.name}: {message}")


class BalanceCalculator:
    def calculate(self, subscriber):
        print(f"Баланс абонента {subscriber.name}: {subscriber.balance}")

# Завдання 2 – OCP
class Tariff:
    def calculate_price(self, minutes):
        pass


class BasicTariff(Tariff):
    def calculate_price(self, minutes):
        return minutes * 1


class PremiumTariff(Tariff):
    def calculate_price(self, minutes):
        return minutes * 0.5

# Завдання 3 – LSP
class Bird:
    def move(self):
        print("Птах рухається")


class FlyingBird(Bird):
    def move(self):
        print("Птах літає")


class WalkingBird(Bird):
    def move(self):
        print("Птах ходить")

# Завдання 4 – ISP
class Printer:
    def print_document(self, text):
        print("Друк:", text)


class Scanner:
    def scan_document(self):
        print("Сканування документа")

# Завдання 5 – DIP
class Database:
    def save(self, data):
        print("Збережено в базу:", data)


class UserService:
    def __init__(self, database):
        self.database = database

    def create_user(self, name):
        self.database.save(name)

# Запуск програми
print("\n--- Завдання 1 (SRP) ---")

subscriber = Subscriber("Ivan", 100)

sms = SMSService()
sms.send_sms(subscriber, "Привіт!")

balance = BalanceCalculator()
balance.calculate(subscriber)

print("\n--- Завдання 2 (OCP) ---")

basic = BasicTariff()
premium = PremiumTariff()
print("Basic тариф:", basic.calculate_price(10))
print("Premium тариф:", premium.calculate_price(10))

print("\n--- Завдання 3 (LSP) ---")
bird1 = FlyingBird()
bird2 = WalkingBird()

bird1.move()
bird2.move()

print("\n--- Завдання 4 (ISP) ---")
printer = Printer()
scanner = Scanner()

printer.print_document("Лабораторна робота")
scanner.scan_document()


print("\n--- Завдання 5 (DIP) ---")
db = Database()
user_service = UserService(db)

user_service.create_user("Petro")