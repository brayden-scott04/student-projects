# OOP Assignments

This folder contains three assignments completed as part of an Object-Oriented Programming (OOP) module, written in Python.

## Assignments

| File | Topic | Key Concepts |
|--------|-------|--------------|
| A1.py | Personal Training Management System | Classes, encapsulation, private attributes |
| A2.py | Clinic Booking System | Abstract classes, inheritance, polymorphism |
| A3.py | Movie Analytics System | File I/O, CSV parsing, data filtering |

# Assignment 1 – Personal Training Management System

A Python program that models a gym's personal training operations using OOP principles.

## What it does
- Manages trainers, trainees, and exercise sessions
- Calculates total training duration and average intensity per trainee
- Prevents duplicate entries and supports session removal

## Key Concepts Demonstrated
- Class design with private attributes and encapsulation
- Methods for data retrieval and manipulation
- Use of `datetime` for age calculation

## Language
Python 3

# Assignment 2 – Clinic Booking System

A Python program that simulates a physiotherapy clinic's session booking system.

## What it does
- Books four types of therapy sessions: General, Sports Injury, Post-Surgery Rehab, and Paediatric
- Calculates session costs with dynamic pricing rules (age discounts, athlete discounts, rehab surcharges)
- Validates patient age eligibility and session duration

## Key Concepts Demonstrated
- Abstract base classes using `ABC` and `@abstractmethod`
- Inheritance and method overriding across session types
- Encapsulation with protected getters

## Language
Python 3

# Assignment 3 – Movie Analytics System

A Python program that loads and analyses movie data from a CSV file.

## What it does
- Reads and validates CSV records, logging any errors to `errors.txt`
- Supports flexible filtering by title, genre, director, studio, year range, sales range, critic score, and rating
- Retrieves unique genres and directors from the dataset

## Key Concepts Demonstrated
- File I/O and CSV parsing without external libraries
- Data validation with structured error handling
- Flexible filtering using a multi-parameter `match()` method

## Language
Python 3


## License
This project is licensed under the [MIT License](../LICENSE)
