class Validadores():
    def validate_cpf(self, text):
        if text == "": return True

        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 100000000000

    def validate_tel(self, text):
        if text == "": return True

        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 100000000000
