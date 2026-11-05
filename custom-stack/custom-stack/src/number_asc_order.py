from src.custom_stack_class import CustomStack


class NumberAscOrder:
    """Ordena os números de uma CustomStack em ordem ascendente."""

    def sort(self, stack):
        if stack is None:
            raise ValueError("A pilha informada não pode ser nula.")

        if not callable(getattr(stack, "is_empty", None)) or not callable(
            getattr(stack, "pop", None)
        ):
            raise TypeError("O parâmetro deve ser uma instância de CustomStack.")

        numbers = []
        while not stack.is_empty():
            numbers.append(stack.pop())

        return sorted(numbers)
