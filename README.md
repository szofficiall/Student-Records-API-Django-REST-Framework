# Student Records API — Django REST Framework

A clean and practical REST API built with Django REST Framework for handling student records through a simple and well-structured backend.

## Overview

Student Records API is a backend project designed to demonstrate the fundamentals of RESTful API development with Django REST Framework.

The API allows clients to manage student information through standard HTTP methods while using Django models, serializers, and class-based API views.

Each student record includes basic information such as:

- Student Name
- Age
- City

The project implements complete CRUD functionality with proper validation, error handling, and HTTP status codes.

## Features

- Create student records
- Retrieve all students
- Retrieve a single student
- Update existing student records
- Partially update student information
- Delete student records
- Serializer-based validation
- Proper HTTP status codes
- Error handling
- Django ORM integration
- Class-based API development using `APIView`
- RESTful endpoint structure

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/students/` | Retrieve all students |
| GET | `/students/<id>/` | Retrieve a specific student |
| POST | `/students/` | Create a new student |
| PUT | `/students/<id>/` | Update a student |
| PATCH | `/students/<id>/` | Partially update a student |
| DELETE | `/students/<id>/` | Delete a student |

## Technology Stack

- Python
- Django
- Django REST Framework
- SQLite
- Django ORM
- REST API

## Project Structure

The project follows a straightforward Django REST Framework architecture.

### Models

Defines the structure of student records and handles database interaction through Django ORM.

### Serializers

Handles data serialization, deserialization, and validation between the API and database models.

### Views

Processes API requests and returns appropriate responses using Django REST Framework's `APIView`.

### URLs

Defines the API endpoints and connects them with the corresponding views.

### Database

Student records are stored using SQLite and managed through Django ORM.

## HTTP Status Codes

The API uses standard HTTP status codes to clearly communicate the result of each request.

- **200 OK** — Request completed successfully
- **201 Created** — Student record created successfully
- **204 No Content** — Student record deleted successfully
- **400 Bad Request** — Invalid data or validation error
- **404 Not Found** — Requested student record does not exist

## CRUD Operations

### Create

Allows clients to add new student records to the database.

### Read

Allows clients to retrieve all student records or a specific student by ID.

### Update

Allows complete student information to be modified.

### Partial Update

Allows selected student fields to be updated without replacing the complete record.

### Delete

Allows existing student records to be removed from the database.

## Learning Objectives

This project provides practical experience with:

- Django REST Framework
- RESTful API development
- `APIView`
- Model Serializers
- Django Models
- Django ORM
- HTTP methods
- HTTP status codes
- Request and response handling
- Data validation
- CRUD operations
- API error handling

## Future Improvements

The API can be extended with additional functionality such as:

- JWT authentication
- User permissions
- Pagination
- Search and filtering
- Ordering
- API documentation
- Advanced validation
- Automated API testing
- Frontend integration
- PostgreSQL database support

## Purpose

This project was developed as part of my practical learning journey with Python, Django, and Django REST Framework.

It focuses on understanding how REST APIs are designed and implemented using Django's APIView, serializers, models, and ORM.

The project also provides a solid foundation for developing more advanced and production-oriented backend APIs.

## Developer

**Sultan Zaib**

Python / Django Backend Engineer

GitHub: **szofficiall**