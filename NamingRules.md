# Quy Tắc Đặt Tên Trong Dự Án

## Table of Contents

- [Quy Tắc Đặt Tên Trong Dự Án](#quy-tắc-đặt-tên-trong-dự-án)
  - [Table of Contents](#table-of-contents)
  - [1. Quy Tắc Đặt Tên File](#1-quy-tắc-đặt-tên-file)
  - [2. Quy Tắc Đặt Tên Class](#2-quy-tắc-đặt-tên-class)
  - [3. Quy Tắc Đặt Tên Function](#3-quy-tắc-đặt-tên-function)
  - [4. Quy Tắc Đặt Tên Biến](#4-quy-tắc-đặt-tên-biến)
  - [5. Quy Tắc Đặt Tên Constants](#5-quy-tắc-đặt-tên-constants)
  - [6. Quy Tắc Đặt Tên Package và Module](#6-quy-tắc-đặt-tên-package-và-module)
  - [7. Ví dụ](#7-ví-dụ)
  - [Tóm Tắt](#tóm-tắt)

## 1. Quy Tắc Đặt Tên File

- Tất cả chữ thường, sử dụng dấu gạch dưới để phân cách các từ.
- Không nên sử dụng ký tự đặc biệt hoặc khoảng trắng trong tên file.

```
app_config.py
db_config.py
user_model.py
```

## 2. Quy Tắc Đặt Tên Class

- Sử dụng PascalCase (hoặc CamelCase), mỗi từ bắt đầu bằng chữ in hoa, không dùng dấu gạch dưới.

```py
class UserProfile:
class DatabaseAccess:
class ProductModel:
```

## 3. Quy Tắc Đặt Tên Function

- Sử dụng chữ thường và dấu gạch dưới để phân cách các từ.
- Tên hàm nên mô tả chính xác chức năng của hàm.

```py
def get_user_info():
def calculate_total_price():
def connect_to_database():
```

## 4. Quy Tắc Đặt Tên Biến

- Sử dụng chữ thường và dấu gạch dưới để phân cách các từ.
- Tên biến phải rõ ràng và có ý nghĩa, mô tả chính xác dữ liệu mà biến lưu trữ.

```py
user_name = "John Doe"
total_price = 100.50
database_connection = None
```

## 5. Quy Tắc Đặt Tên Constants

- Sử dụng chữ in hoa và dấu gạch dưới để phân cách các từ.

```py
MAX_CONNECTIONS = 100
DATABASE_URL = "localhost:5432/mydb"
TIMEOUT_DURATION = 30
```

## 6. Quy Tắc Đặt Tên Package và Module

- Package: Sử dụng chữ thường, có thể sử dụng dấu gạch dưới để phân cách từ nếu cần.
- Module: Tương tự như package, sử dụng chữ thường và dấu gạch dưới để phân cách từ.

```
package_name/
module_name.py
```

## 7. Ví dụ

```py
# File: user_model.py

class UserProfile:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

    def get_user_info(self):
        return f"User ID: {self.user_id}, User Name: {self.user_name}"


# File: db_config.py

DATABASE_URL = "localhost:5432/mydb"
MAX_CONNECTIONS = 100


# File: database_access.py

class DatabaseAccess:
    def __init__(self, db_url):
        self.db_url = db_url
        self.connection = None

    def connect_to_database(self):
        # Code to connect to database
        pass

    def close_connection(self):
        # Code to close database connection
        pass
```

## Tóm Tắt

- `File`: Chữ thường, gạch dưới.
- `Class`: PascalCase.
- `Function`: Chữ thường, gạch dưới.
- `Variable`: Chữ thường, gạch dưới.
- `Constants`: Chữ in hoa, gạch dưới.
- `Package và Module`: Chữ thường, gạch dưới (nếu cần).
