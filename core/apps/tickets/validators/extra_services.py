# from django.core.exceptions import ValidationError


class ExtraServicesValidator:
    def __init__(self): ...

    def __call__(self):
        return True


class PaidServicesValidator:
    def __init__(self): ...

    def __call__(self):
        return True
