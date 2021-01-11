# Simple book - market

## About project
Project imulates very simple book-market, where users only can views all book's instance, their authors and their genres. Users can register on the book-market API. Only administrators can create or update books, authors and genres.

<a href="https://github.com/actions/create-release"><img alt="GitHub Actions status" src="https://github.com/actions/create-release/workflows/Tests/badge.svg"></a>

## Description of the project
Users can register, login and then only view book's, author's and genre's instances. Users can use pagination, filtering, seraching or ordering features. Only admins can create and updated book's, author's and genre's instances.

## Functionality of the project
* Users can login API
* Users can view all books instances and detail information about them. They can use pagination, filtering, searching and ordering.
* Users can view all genres instances and detail information about them. They can use pagination, filtering, searching and ordering.
* Users can view all authors instances and detail information about them. They can use pagination, filtering, searching and ordering.
* Admins can update or create book's, genre's and author's instances
* Users can register on the book-market API
* All users have theit own profile

## The technology used:
* Django
* Django REST Framework
* Postgresql
* Docker

## Installing
You need _Docker_ to be installed on your computer. Then you need to go to the project's root directory and run following command:

`docker-compose up --build`
