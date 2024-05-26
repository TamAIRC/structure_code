# Cấu trúc dự án Python

```
/project-root
│
├── /configs         # Thư mục chứa các file cấu hình
│   ├── app_config.yaml
│   ├── db_config.yaml
│   └── logging_config.yaml
│
├── /database        # Thư mục chứa các script và model liên quan đến cơ sở dữ liệu
│   ├── database_access # Thu muc chua cac lop thuc hien tuong tac database
│   │   ├── 001_initial_setup.py
│   │   ├── 002_add_user_table.py
│   └── database_models # Cac model tuong duong voi tung bang databse
│       ├── base_model.py
│       ├── user_model.py
│       └── product_model.py
│
├── /docs            # Thư mục chứa tài liệu dự án
│   ├── oop.md
│   ├── design_patterns.md
│   └── database.md
│
├── /patterns        # thư muc chua base class/abtract class
│
├── /logger          # Thư mục chứa các module liên quan đến logging
│   ├── logger.py
│   └── log_formatter.py
│
├── /scripts         # Thư mục chứa các tập lệnh tự động hóa
│   ├── automation_script.py
│   ├── performance_measurement.py
│   └── project_management.py
│
├── /controllers     # Thư mục chứa các bộ điều khiển chung (logic điều hướng)
│   ├── __init__.py
│   ├── user_controller.py
│   ├── product_controller.py
│   └── order_controller.py│
│
├── /models        # Thư mục chứa các business models có thể bao hàm nhiều db model
│   ├── __init__.py
│   └── user_model.py
│
├── /services        # Thư mục chứa các dịch vụ chung
│   ├── __init__.py
│   ├── user_service.py
│   ├── product_service.py
│   └── order_service.py
│
├── /utils           # Thư mục chứa các tiện ích và hàm dùng chung
│   ├── __init__.py
│   ├── file_utils.py
│   ├── date_utils.py
│   └── string_utils.py
│
├── /tests           # Thư mục chứa các bài kiểm thử (unit tests)
│   ├── __init__.py
│   ├── test_user.py
│   ├── test_product.py
│   └── test_order.py
├── /modules             # Thư mục chứa mã nguồn chính của dịch vụ
│   ├── __init__.py
│   └── /module1
│       ├── /controllers     # Thư mục chứa các bộ điều khiển của modules (logic điều hướng)
│       │   ├── __init__.py
│       │   ├── user_controller.py
│       │   ├── product_controller.py
│       │   └── order_controller.py
│       │
│       ├── /self_model        # Thư mục chứa các business model riêng của modules
│       │   ├── __init__.py
│       │   └── user_model.py
│       │
│       ├── /self_services        # Thư mục chứa các dịch vụ/support riêng của modules
│       │   ├── __init__.py
│       │   ├── user_service.py
│       │   ├── product_service.py
│       │   └── order_service.py
│       │
│       ├── /tests           # Thư mục chứa các bài kiểm thử (unit tests) module
│       │   ├── __init__.py
│       │   ├── test_user.py
│       │   ├── test_product.py
│       │   └── test_order.py
│       │
│       └── setup.py        # Tệp cấu hình setuptools cho việc cài đặt và phân phối module
│
├── /tests           # Thư mục chứa các bài kiểm thử (unit tests) hệ thống
│   ├── __init__.py
│   ├── test_user.py
│   ├── test_product.py
│   └── test_order.py
│
├── setup.py        # Tệp cấu hình setuptools cho việc cài đặt và phân phối dự án
├── .gitignore       # File cấu hình git để bỏ qua các file/thư mục không cần track
├── README.md        # File giới thiệu dự án
└── requirements.txt # File liệt kê các package cần thiết (Python)

```

## Chú thích

- **project_name/**: Thư mục gốc của dự án.

- **README.md**: Tài liệu mô tả dự án.

- **requirements.txt**: Danh sách các gói Python cần thiết để chạy dự án, có thể được cài đặt bằng pip.

- **setup.py**: Tệp cấu hình setuptools cho việc cài đặt và phân phối dự án.

- **.gitignore**: Tệp này định nghĩa các tệp và thư mục không nên được Git theo dõi.

- **config/**: Thư mục chứa các tệp cấu hình cho dự án.

