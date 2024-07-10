# IEDC_BackendTask
This project was done using django rest_framework

## The end points accessible are as follows:
### '/books' with name 'books' - Request: GET, POST
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
  
### '/books/id' with name 'books_id' - Request: GET, PUT, DELETE
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
  
- '/favorites/users/userId' with name 'favorites_id' - Request : GET,POST,PUT
- '/favorites/users/userId/bookId' with name 'delete_fav_book' -Request :DELETE
