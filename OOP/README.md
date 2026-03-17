# Object-Oriented Programming Projects

This folder contains selected Python assignments from my object-oriented programming coursework. These projects are uploaded as code samples to show my understanding of classes, objects, encapsulation, inheritance, abstraction, validation, and data processing.

These assignments were originally completed for school, but I’ve organized them here so the code is easier to review. The focus is on implementation quality, class design, problem-solving approach, and practical use of object-oriented programming concepts.

## What this folder shows

- Class-based system design in Python
- Object-oriented modeling of real-world scenarios
- Encapsulation through class attributes and methods
- Inheritance and abstraction using base and derived classes
- Data validation and rule-based logic
- Aggregation and management of related objects
- Use of lists and dictionaries to organize records
- File handling and data analysis from CSV input

## Tech Stack

- Python
- Object-Oriented Programming (OOP)
- Abstract Base Classes (`abc`)
- File I/O
- CSV-style data processing
- Python `datetime`

## Projects

### A1 — Personal Training Management System

A Python-based management system for handling trainers, trainees, and exercise sessions. The project models a simple personal training environment using separate classes for each entity and a management class to coordinate them.

#### Scope
- Trainer record management
- Trainee record management
- Exercise session creation and removal
- Duplicate checking for trainers, trainees, and sessions
- Duration and intensity calculations across sessions

#### Key Features
- `Trainee`, `Trainer`, and `ExerciseSession` classes for entity modeling
- Automatic age calculation based on birthdate
- Session tracking by trainer and trainee
- Total session duration calculations for trainees and trainers
- Average intensity calculation for trainee sessions
- Session lookup and deletion by ID
- Duplicate prevention when adding records

#### Technical Concepts Demonstrated
- Class design and object relationships
- Encapsulation with private attributes
- Use of constructors and string representations
- Aggregation of objects inside a management system
- Iteration over stored objects for search and reporting
- Rule-based calculations using object data
- Date handling with Python `datetime`

### A2 — Clinic Booking System with Inheritance and Abstract Classes

A clinic booking system built with Python OOP principles, using abstract base classes and multiple therapy session types. The project models patients and therapy bookings while applying pricing rules based on session type, age, and booking conditions.

#### Scope
- Patient registration
- Therapy session booking
- Support for multiple session types
- Session cost calculation based on different rules
- Validation of booking inputs and patient eligibility

#### Key Features
- Abstract `Session` base class with shared properties and abstract cost calculation
- Specialized subclasses for general therapy, sports injury, post-surgery rehab, and paediatric therapy
- Automatic patient ID generation
- Age-based discounts for eligible patients
- Special pricing rules by therapy type
- Validation for session duration and required booking arguments
- Dictionary-based storage of patients and their sessions

#### Technical Concepts Demonstrated
- Inheritance and polymorphism
- Abstract base classes with `ABC` and `@abstractmethod`
- Encapsulation of patient and session data
- Use of helper methods for controlled access to private values
- Conditional business logic for pricing and eligibility
- Dictionary-based data organization
- Object creation based on user-selected type

### A3 — CSV Data Analytics and Validation Tool

A Python analytics class that loads structured records from a CSV file, validates each row, stores valid entries, and records data issues in an error log. The project focuses on input validation, filtering, and basic analysis of media-related records.

#### Scope
- CSV file loading
- Record validation and cleaning
- Error reporting for invalid rows
- Access to unique genres and directors
- Record filtering based on multiple optional criteria

#### Key Features
- Reads and parses CSV-style input data
- Validates required fields and field counts
- Converts values into correct types such as integers and floats
- Rejects invalid records based on year and score rules
- Writes validation issues into `errors.txt`
- Stores cleaned records as dictionaries
- Supports multi-criteria filtering using optional parameters

#### Technical Concepts Demonstrated
- File reading and writing
- Data validation and exception handling
- Dictionary creation from row data
- Property usage for record counts
- Set-based extraction of unique values
- Multi-condition filtering across structured records
- Default argument handling for flexible search behavior

## Skills Demonstrated

| Skill Area | Evidence Across Projects |
|---|---|
| Class Design | Trainers, trainees, sessions, patients, analytics records |
| Encapsulation | Private attributes and controlled access through methods |
| Inheritance | Session subclasses extending a shared base class |
| Abstraction | Abstract `Session` class with required cost calculation |
| Polymorphism | Different therapy classes implementing their own pricing rules |
| Data Structures | Lists, dictionaries, sets, and nested object collections |
| Validation Logic | Duplicate checks, booking constraints, field validation, eligibility rules |
| File Handling | Reading CSV input and writing validation errors to a file |
| Data Processing | Type conversion, filtering, aggregation, and record matching |
| Problem Solving | Rule-based calculations, object coordination, and record management |

## Notes

- These projects were originally completed as academic assignments and are included here as code samples.
- Only core source code files are included in this folder.
- Some sample input files or assignment documents may not be included.
- The focus of this repository is code review, technical clarity, and implementation quality.

## Improvement Areas

If I revisited these projects, I would improve them further by:

- Adding docstrings and more consistent inline documentation
- Refactoring repeated lookup logic into reusable helper methods
- Replacing direct access to name-mangled private attributes with cleaner getter methods or properties
- Splitting larger classes into smaller responsibility-focused components where useful
- Adding unit tests for validation, calculations, and filtering logic
- Improving input handling and error messaging for edge cases
