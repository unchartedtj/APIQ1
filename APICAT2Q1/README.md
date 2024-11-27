# E-Commerce Django Project

## Project Overview

This is a Django-based e-commerce project that includes models for customers and orders. The project allows customers to place multiple orders, and each order is associated with only one customer.

### Features

- **Customer Model**: Stores customer information like first name, last name, email, and phone number.
- **Order Model**: Stores order details such as the customer who made the order, order date, total amount, and order status.
- **Relationships**: 
  - A `Customer` can have multiple `Orders`.
  - An `Order` is associated with one `Customer`.

## Setup Instructions

### 1. Clone the repository

Clone the repository to your local machine by running the following command:

```bash
git clone (https://github.com/unchartedtj/APICAT2Q1)
