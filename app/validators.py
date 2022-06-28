from django.forms import ValidationError

class MaxSizeFileValidator:
    def __init__(self, max_size_file=2):
        self.max_size_file = max_size_file

    def __call__(self, value):
        size = value.size
        max_size = self.max_size_file*1048576

        if size > max_size:
            raise ValidationError(f"el tamaÃ±o maximo del archivo debe ser de {self.max_size_file}MB")
        return value