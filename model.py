import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DECIMAL,
    Date,
)
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    salaries = relationship("Salary", back_populates="employee")

    def pay(self, amount, bonus, date=None, comments=None):
        salary = Salary(amount=amount, bonus=bonus)

        if date is not None:
            salary.date = date

        if comments is not None:
            salary.comments = comments

        self.salaries.append(salary)

    def __repr__(self):
        return f"Employee({self.id}, {self.first_name}, {self.last_name})"


class Salary(Base):
    __tablename__ = "salaries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(DECIMAL, nullable=False)
    bonus = Column(DECIMAL, nullable=False, default=0)
    date = Column(
        Date,
        nullable=False,
        default=datetime.date.today
    )
    comments = Column(String(150))

    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)

    employee = relationship("Employee", back_populates="salaries")

    def __repr__(self):
        return f"Salary({self.amount}, {self.date}, {self.employee_id})"


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"Department({self.id}, {self.name})"
