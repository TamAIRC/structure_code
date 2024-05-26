# Cấu trúc dự án Python

```
/project-root
│
├── /configs          # Thư mục chứa các file cấu hình
│   ├── app_config.py
│   ├── db_config.py
│   └── logging_config.py
│
├── /database         # Thư mục chứa các script và model liên quan đến cơ sở dữ liệu
│   ├── /database_access  # Thư mục chứa các lớp thực hiện tương tác database
│   │   ├── 001_initial_setup.py
│   │   ├── 002_add_user_table.py
│   │
│   └── /database_models  # Các model tương đương với từng bảng database
│       ├── base_model.py
│       ├── user_model.py
│       └── product_model.py
│
├── /docs             # Thư mục chứa tài liệu dự án
│   ├── oop.md
│   ├── design_patterns.md
│   └── database.md
│
├── /patterns         # Thư mục chứa các base class/abstract class
│   ├── base_service.py
│   ├── base_controller.py
│   └── base_model.py
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
│   └── user_model.py
│
├── /services         # Thư mục chứa các dịch vụ chung
│   ├── __init__.py
│   ├── user_service.py
│   ├── product_service.py
│   └── order_service.py
│
├── /utils            # Thư mục chứa các tiện ích và hàm dùng chung
│   ├── __init__.py
│   ├── file_utils.py
│   ├── date_utils.py
│   └── string_utils.py
│
├── /modules          # Thư mục chứa mã nguồn chính của các module dịch vụ
│   ├── __init__.py
│   └── /module1      # Thư mục của module 1
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
│       └── setup.py          # Tệp cấu hình setuptools cho việc cài đặt và phân phối module
│
├── /tests            # Thư mục chứa các bài kiểm thử (unit tests) hệ thống
│   ├── __init__.py
│   ├── test_user.py
│   ├── test_product.py
│   └── test_order.py
│
├── setup.py          # Tệp cấu hình setuptools cho việc cài đặt và phân phối dự án
├── .gitignore        # File cấu hình git để bỏ qua các file/thư mục không cần track
├── README.md         # File giới thiệu dự án
└── requirements.txt  # File liệt kê các package cần thiết (Python)
```

## Chú thích

- `project-root/`: Thư mục gốc của dự án.
- `README.md`: Tài liệu mô tả dự án, cung cấp thông tin cơ bản về dự án và hướng dẫn sử dụng.
- `requirements.txt`: Danh sách các gói Python cần thiết để chạy dự án, có thể được cài đặt bằng pip.
- `setup.py`: Tệp cấu hình setuptools cho việc cài đặt và phân phối dự án.
- `.gitignore`: Tệp này định nghĩa các tệp và thư mục không nên được Git theo dõi.
- `configs/`: Thư mục chứa các tệp cấu hình cho dự án.
- `database/`: Thư mục chứa các script và model liên quan đến cơ sở dữ liệu.
  - `database_access/`: Thư mục chứa các lớp thực hiện tương tác database.
  - `database_models/`: Thư mục chứa các model tương đương với từng bảng database.
- `docs/`: Thư mục chứa tài liệu dự án, bao gồm tài liệu về OOP, các mẫu thiết kế và cơ sở dữ liệu.
- `patterns/`: Thư mục chứa các base class và abstract class.
- `logger/`: Thư mục chứa các module liên quan đến logging.
- `scripts/`: Thư mục chứa các tập lệnh tự động hóa.
- `controllers/`: Thư mục chứa các bộ điều khiển chung (logic điều hướng).
- `models/`: Thư mục chứa các business models, có thể bao hàm nhiều db model.
- `services/`: Thư mục chứa các dịch vụ chung của ứng dụng.
- `utils/`: Thư mục chứa các tiện ích và hàm dùng chung.
- `modules/`: Thư mục chứa mã nguồn chính của các module dịch vụ.
  - `module1/`: Thư mục của module cụ thể.
    - `controllers/`: Thư mục chứa các bộ điều khiển của module.
    - `self_model/`: Thư mục chứa các business model riêng của module.
    - `self_services/`: Thư mục chứa các dịch vụ/support riêng của module.
    - `tests/`: Thư mục chứa các bài kiểm thử của module.
    - `setup.py`: Tệp cấu hình setuptools cho việc cài đặt và phân phối module.
- `tests/`: Thư mục chứa các bài kiểm thử (unit tests) hệ thống.
