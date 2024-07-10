# IEDC_BackendTask
This project was done using django rest_framework

## The end points accessible are as follows:

### 1. '/books' with name 'books' - Request: GET, POST
- Function based view used [views.py](./api/views.py)
- View name: getData
- No input expected
- `POST` request require book details:
    ```
    Request Body:
      {
      "title": "Brave New World",
      "author": "Aldous Huxley",
      "pages": 268
      }
    ```

  
### 2. '/books/id' with name 'books_id' - Request: GET, PUT, DELETE
- Function based view used [views.py](./api/views.py)
- View name: getDataDetail
- input `id` for BookId expected for all
- `PUT` request require book details:
    ```
    {
    "title": "Brave New World (Updated)",
    "author": "Aldous Huxley",
    "pages": 270
    }
    ```

  
### 3. '/favorites/users/userId' with name 'favorites_id' - Request : GET,POST,PUT
- Function based view [views.py](./users/views.py)
- View name: getUserData
- input: `userId` which is the userId field of users model
- `GET` request simply gets the user details including favourites list. No data expected
- `POST` request adds a book to favorites list of the user. `bookId` is expected as request body
  ```
      Request Body:
        {
        "bookId": 3
        }
  ```
- `PUT` request expects a second userId named `userId` and a bookId named `bookId`. The book referred to by bookId is added to the favorites list of both users (userId given in url and userId in body)
  ```
  Request Body:
        {
        "userId":1,
        "bookId": 3
        }
  ```
  
 
### 4. '/favorites/users/userId/bookId' with name 'delete_fav_book' -Request :DELETE
- Function based view [views.py](./users/views.py)
- View name: delete_user_book
- input: `userId` and `bookId` in url
- Deletes the book `bookId` if exists from the favorites list of the user `userId`
