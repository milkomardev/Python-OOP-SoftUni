from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENTS = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def get_loan_by_type(self, loan_type):
        existing_loan = [l for l in self.loans if l.__class__.__name__ == loan_type]
        if existing_loan:
            return existing_loan[0]
        return None

    def get_client_by_id(self, client_id):
        existing_client = [c for c in self.clients if c.client_id == client_id]
        if existing_client:
            return existing_client[0]
        return None

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        loan = self.VALID_LOANS[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = self.get_loan_by_type(loan_type)
        client = self.get_client_by_id(client_id)

        if loan_type == 'StudentLoan' and client.__class__.__name__ == "Adult" or \
                loan_type == "MortgageLoan" and client.__class__.__name__ == "Student":
            raise Exception("Inappropriate loan type!")

        client.loans.append(loan)
        self.loans.remove(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self.get_client_by_id(client_id)
        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)

        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        total_loans_affected = 0
        for l in self.loans:
            if l.__class__.__name__ == loan_type:
                l.increase_interest_rate()
                total_loans_affected += 1

        return f"Successfully changed {total_loans_affected} loans."

    def increase_clients_interest(self, min_rate: float):
        total_clients_affected = 0
        for c in self.clients:
            if c.interest < min_rate:
                c.increase_clients_interest()
                total_clients_affected += 1

        return f"Number of clients affected: {total_clients_affected}."

    def get_statistics(self):
        try:
            average_interest_rate = sum([c.interest for c in self.clients]) / len(self.clients)
        except ZeroDivisionError:
            average_interest_rate = 0

        return f"Active Clients: {len(self.clients)}\n" \
               f"Total Income: {sum([c.income for c in self.clients]):.2f}\n" \
               f"Granted Loans: {sum([len(c.loans) for c in self.clients])}, " \
               f"Total Sum: {sum([sum([l.amount for l in c.loans]) for c in self.clients]):.2f}\n" \
               f"Available Loans: {len(self.loans)}, Total Sum: {sum([l.amount for l in self.loans]):.2f}\n" \
               f"Average Client Interest Rate: {average_interest_rate:.2f}"
