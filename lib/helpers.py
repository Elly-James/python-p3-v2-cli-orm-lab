from models.department import Department
from models.employee import Employee

import json

def read_employees(file_path="employees.json"):
    """Read employee data from a JSON file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def write_employees(employees, file_path="employees.json"):
    """Write employee data to a JSON file."""
    with open(file_path, "w") as file:
        json.dump(employees, file, indent=4)

def update_employee(employee_id, updated_data, file_path="employees.json"):
    """Update an employee's data."""
    employees = read_employees(file_path)
    for employee in employees:
        if employee["id"] == employee_id:
            employee.update(updated_data)
            write_employees(employees, file_path)
            return True
    return False

def delete_employee(employee_id, file_path="employees.json"):
    """Delete an employee by ID."""
    employees = read_employees(file_path)
    updated_employees = [emp for emp in employees if emp["id"] != employee_id]
    if len(updated_employees) < len(employees):
        write_employees(updated_employees, file_path)
        return True
    return False

def list_employees(file_path="employees.json"):
    """List all employees."""
    employees = read_employees(file_path)
    return employees

def find_employee_by_id(employee_id, file_path="employees.json"):
    """Find an employee by ID."""
    employees = read_employees(file_path)
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return None

def list_employees_by_department(department, file_path="employees.json"):
    """List all employees in a specific department."""
    employees = read_employees(file_path)
    return [emp for emp in employees if emp.get("department") == department]

def calculate_average_salary(file_path="employees.json"):
    """Calculate the average salary of employees."""
    employees = read_employees(file_path)
    total_salary = sum(emp.get("salary", 0) for emp in employees)
    count = len(employees)
    return total_salary / count if count > 0 else 0

def list_employees_above_salary(threshold, file_path="employees.json"):
    """List employees earning above a certain salary."""
    employees = read_employees(file_path)
    return [emp for emp in employees if emp.get("salary", 0) > threshold]

def count_employees_by_role(role, file_path="employees.json"):
    """Count the number of employees in a specific role."""
    employees = read_employees(file_path)
    return sum(1 for emp in employees if emp.get("role") == role)

def add_employee(employee_data, file_path="employees.json"):
    """Add a new employee."""
    employees = read_employees(file_path)
    employees.append(employee_data)
    write_employees(employees, file_path)
