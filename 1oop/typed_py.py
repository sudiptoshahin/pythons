class Person:
    def __init__(self, first_name: str, last_name: str, age: int, address: str) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self.age = age
        self.address = address
    
    @property
    def first_name(self) -> str:
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name: str) -> None:
        self._first_name = first_name
    
    @property
    def last_name(self) -> str:
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name: str) -> None:
        self._last_name = last_name

    def get_full_name(self) -> str:
        return f"{self._first_name} {self._last_name}"


if __name__ == '__main__':
    # Example usage:
    person = Person("John", "Doe", 30, "123 Main St")
    print(person.get_full_name())  # Output: John Doe
    print(person.first_name)  # Output: John
    print(person.last_name)  # Output: Doe