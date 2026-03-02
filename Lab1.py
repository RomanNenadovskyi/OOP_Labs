# Приклад SRP (Один клас - одна робота)
class report_generator:
    def create(self): return "Звіт готовий"


class report_saver:
    def save(self, text): print(f"Збережено: {text}")


# Запуск програми
if __name__ == "__main__":
    rep = report_generator()
    data = rep.create()

    saver = report_saver()
    saver.save(data)