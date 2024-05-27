# Cấu trúc dự án Python

```
/project-root
│
├── /configs          # Thư mục chứa các file cấu hình
│   ├── app_config.py
│   ├── db_config.py
│   └── logging_config.py
│
├── /database         # Thư mục chứa các script và model liên quan đến database
│   ├── /database_connection # Thư mục chứa các lớp quản lý kết nối database
│   │   ├── mongo_connection.py
│   │   └── sql_connection.py
│   │
│   ├── /database_migration  # Thư mục chứa các lớp tạo và quản lý database
│   │   ├── 001_initial_setup.py # Tạo cấu trúc database ban đầu
│   │   └── 002_user_table.py
│   │
│   ├── /database_access     # Thư mục chứa các lớp thực hiện tương tác database (DBA)
│   │   ├── user_access.py
│   │   └── product_access.py
│   │
│   └── /database_models     # Các model tương đương với từng bảng database (DBO) - Thực hiện định dạng dữ liệu
│       ├── user_model.py
│       └── product_model.py
│
├── /docs             # Thư mục chứa tài liệu dự án
│   ├── oop.md
│   ├── design_patterns.md
│   └── database.md
│
├── /patterns         # Thư mục chứa các base class/abstract class
│   ├── base_model.py     # Base class cho các model
│   ├── base_object.py    # Base class cho các object
│   ├── base_service.py   # Base class cho các service
│   └── base_controller.py# Base class cho các controller
│
├── /logger           # Thư mục chứa các module liên quan đến logging
│   ├── logger.py
│   └── log_formatter.py
│
├── /scripts          # Thư mục chứa các tập lệnh tự động hóa
│   ├── automation_script.py
│   ├── performance_measurement.py
│   └── project_management.py
│
├── /controllers      # Thư mục chứa các bộ điều khiển chung (logic điều hướng)
│   ├── __init__.py
│   ├── user_controller.py
│   ├── product_controller.py
│   └── order_controller.py
│
├── /models           # Thư mục chứa các business models có thể bao hàm nhiều db model
│   ├── __init__.py
│   └── user_model.py       # Business model cho user
│
├── /services         # Thư mục chứa các dịch vụ chung
│   ├── __init__.py
│   ├── user_service.py
│   ├── product_service.py
│   └── order_service.py
│
├── /api              # Thư mục chứa các API
│   ├── __init__.py
│   ├── web_api.py          # API cho ứng dụng web
│   └── mobile_api.py       # API cho ứng dụng di động
│
├── /utils            # Thư mục chứa các tiện ích và hàm dùng chung
│   ├── __init__.py
│   ├── file_utils.py       # Các hàm tiện ích liên quan đến file
│   ├── date_utils.py       # Các hàm tiện ích liên quan đến xử lý ngày tháng
│   ├── number_utils.py     # Các hàm tiện ích liên quan đến xử lý số
│   └── string_utils.py     # Các hàm tiện ích liên quan đến chuỗi
│
├── /modules          # Thư mục chứa mã nguồn chính của các module dịch vụ
│   ├── __init__.py
│   └── /module_ex      # Thư mục của module 1
│       ├── /controllers      # Thư mục chứa các bộ điều khiển của module (logic điều hướng)
│       │   ├── __init__.py
│       │   ├── user_controller.py
│       │   ├── product_controller.py
│       │   └── order_controller.py
│       │
│       ├── /self_model       # Thư mục chứa các business model riêng của module
│       │   ├── __init__.py
│       │   └── user_model.py
│       │
│       ├── /self_services    # Thư mục chứa các dịch vụ/support riêng của module
│       │   ├── __init__.py
│       │   ├── user_service.py
│       │   ├── product_service.py
│       │   └── order_service.py
│       │
│       ├── /tests            # Thư mục chứa các bài kiểm thử (unit tests) của module
│       │   ├── __init__.py
│       │   ├── test_user.py
│       │   ├── test_product.py
│       │   └── test_order.py
│       │
│       └── setup.py
│
├── /tests            # Thư mục chứa các bài kiểm thử (unit tests) hệ thống
│   ├── __init__.py
│   ├── test_user.py
│   ├── test_product.py
│   └── test_order.py
│
├── setup.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Chú thích

### 1. Main Directory

- `project-root/`: Thư mục gốc của dự án.

### 2. Subfolder

- `/configs`: Thư mục chứa các file cấu hình
  - `app_config.py`: Cấu hình cho ứng dụng.
  - `db_config.py`: Cấu hình cho cơ sở dữ liệu.
  - `logging_config.py`: Cấu hình cho logging.
- `/database`: Thư mục chứa các script và model liên quan đến database
  - `/database_migration`: Thư mục chứa các lớp tạo và quản lý database.
    - `001_initial_setup.py`: Tạo cấu trúc database ban đầu.
  - `/database_connection`: Thư mục chứa các lớp quản lý kết nối database.
    - `mongo_connection.py`: Kết nối tới MongoDB.
    - `sql_connection.py`: Kết nối tới SQL database.
  - `/database_access`: Thư mục chứa các lớp thực hiện tương tác database (DBA).
  - `/database_models`: Các model tương đương với từng bảng database (DBO) - Thực hiện định dạng dữ liệu.
- `/docs`: Thư mục chứa tài liệu dự án.
  - `oop.md`: Tài liệu về lập trình hướng đối tượng (OOP).
  - `design_patterns.md`: Tài liệu về các mẫu thiết kế (Design Patterns).
  - `database.md`: Tài liệu về cơ sở dữ liệu.
- `/patterns`: Thư mục chứa các base class/abstract class.
  - `base_model.py`: Base class cho các model.
  - `base_object.py`: Base class cho các object.
  - `base_service.py`: Base class cho các service.
  - `base_controller.py`: Base class cho các controller.
- `/logger`: Thư mục chứa các module liên quan đến logging.
  - `logger.py`: Module quản lý logging.
  - `log_formatter.py`: Định dạng log.
- `/scripts`: Thư mục chứa các tập lệnh tự động hóa.
  - `automation_script.py`: Tập lệnh tự động hóa.
  - `performance_measurement.py`: Tập lệnh đo lường hiệu suất.
  - `project_management.py`: Tập lệnh quản lý dự án.
- `/controllers`: Thư mục chứa các bộ điều khiển chung (logic điều hướng).
  - `**init**.py`: Khởi tạo package controllers.
- `/models`: Thư mục chứa các business models có thể bao hàm nhiều db model.
  - `**init**.py`: Khởi tạo package models.
  - `/services`: Thư mục chứa các dịch vụ chung.
    - `**init**.py`: Khởi tạo package services.
- `/api`: Thư mục chứa các API.
  - `**init**.py`: Khởi tạo package api.
  - `web_api.py`: API cho ứng dụng web.
  - `mobile_api.py`: API cho ứng dụng di động.
- `/utils`: Thư mục chứa các tiện ích và hàm dùng chung.
  - `**init**.py`: Khởi tạo package utils.
  - `file_utils.py`: Các hàm tiện ích liên quan đến file.
  - `date_utils.py`: Các hàm tiện ích liên quan đến xử lý ngày tháng.
  - `number_utils.py`: Các hàm tiện ích liên quan đến xử lý số.
  - `string_utils.py`: Các hàm tiện ích liên quan đến chuỗi.
- `/modules`: Thư mục chứa mã nguồn chính của các module dịch vụ.
  - `**init**.py`: Khởi tạo package modules.
  - `/module_ex`: Thư mục của module 1.
    - `/controllers`: Thư mục chứa các bộ điều khiển của module (logic điều hướng).
      - `**init**.py`: Khởi tạo package controllers của module.
    - `/self_model`: Thư mục chứa các business model riêng của module.
      - `**init**.py`: Khởi tạo package self_model của module.
    - `/self_services`: Thư mục chứa các dịch vụ/support riêng của module.
      - `**init**.py`: Khởi tạo package self_services của module.
    - `/tests`: Thư mục chứa các bài kiểm thử (unit tests) của module.
      - `**init**.py`: Khởi tạo package tests của module.
    - `setup.py`: Tệp cấu hình setuptools cho việc cài đặt và phân phối module.
