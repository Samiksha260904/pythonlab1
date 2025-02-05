class Employee:
    def __init__(
            self,
            designation: str = 'Developer',
            frontend: bool = False,
            backend: bool = False
    ):
        self.designation = designation
        self.frontend = frontend
        self.backend = backend

    def __repr__(self):
        return '{}'.format(self.designation)

    def verifier(self):
        if self.frontend and self.backend:
            return "Fullstack"
        elif self.frontend:
            return "Frontend"
        elif self.backend:
            return "Backend"
        else:
            return "Not a developer"

if __name__ == '__main__':
    firstEmployee = Employee(frontend=True, backend=False)
    print(firstEmployee.verifier())

    secondEmployee = Employee(frontend=True, backend=True)
    print(secondEmployee.verifier())

    thirdEmployee = Employee(frontend=False, backend=False)
    print(thirdEmployee.verifier())

    fourthEmployee = Employee(frontend=False, backend=True)
    print(fourthEmployee.verifier())
