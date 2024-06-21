# Cấu trúc dự án Python

```
/basic_project
│
├── .gitignore
├── README.md
├── __init__.py
├── main.py
├── requirements.txt
├── setup.py
│
├── /configs          # Thư mục chứa các file cấu hình
│   ├── __init__.py
│   ├── app_config.py
│   ├── config.py
│   ├── db_config.py
│   └── logging_config.py
│
├── /controllers      # Thư mục chứa các bộ điều khiển chung (logic điều hướng)
│   ├── __init__.py
│   ├── question_controller.py
│   └── session_manager.py
│
├── /database         # Thư mục chứa các script và model liên quan đến database
│   ├── __init__.py
│   ├── /connect      # Thư mục chứa các lớp quản lý kết nối database
│   │   ├── __init__.py
│   │   └── connect.py
│   │
│   ├── /connection   # Thư mục chứa các lớp quản lý kết nối database cụ thể
│   │   ├── __init__.py
│   │   ├── mongo_connection.py
│   │   ├── mysql_connection.py
│   │   ├── postgresql_connection.py
│   │   └── sqlserver_connection.py
│   │
│   ├── /database_migration  # Thư mục chứa các lớp tạo và quản lý database
│   │   └── 001_initial_setup.py
│   │
│   ├── /dba         # Thư mục chứa các lớp thực hiện tương tác database (DBA)
│   │   ├── __init__.py
│   │   ├── mongo_dba.py
│   │   └── question_dba.py
│   │
│   └── /dbo         # Các model tương đương với từng bảng database (DBO) - Thực hiện định dạng dữ liệu
│       ├── __init__.py
│       └── question_dbo.py
│
├── /docs             # Thư mục chứa tài liệu dự án
│   ├── database.md
│   ├── design_patterns.md
│   └── oop.md
│
├── /logger           # Thư mục chứa các module liên quan đến logging
│   ├── log_formatter.py
│   ├── logger.py
│   └── logger.txt
│
├── /models           # Thư mục chứa các business models
│   ├── __init__.py
│   └── question_model.py
│
├── /modules          # Thư mục chứa mã nguồn chính của các module dịch vụ
│   ├── /module_ex    # Thư mục của module example
│   │   ├── /controllers      # Thư mục chứa các bộ điều khiển của module (logic điều hướng)
│   │   │   ├── __init__.py
│   │   │   └── question_controller.py
│   │   │
│   │   ├── /self_model       # Thư mục chứa các business model riêng của module
│   │   │   ├── __init__.py
│   │   │   └── question_model.py
│   │   │
│   │   ├── /self_services    # Thư mục chứa các dịch vụ riêng của module
│   │   │   ├── __init__.py
│   │   │   └── question_service.py
│   │   │
│   │   └── /tests            # Thư mục chứa các bài kiểm thử của module
│   │       ├── __init__.py
│   │       └── test_question.py
│   │
│   └── setup.py
│
├── /output           # Thư mục chứa các tệp đầu ra
│
├── /patterns         # Thư mục chứa các base class/abstract class
│   ├── base_connection.py
│   ├── base_controller.py
│   ├── base_dba.py
│   ├── base_dbo.py
│   └── singleton_meta.py
│
├── /routes           # Thư mục chứa các route của ứng dụng
│   ├── __init__.py
│   └── question_routes.py
│
├── /scripts          # Thư mục chứa các tập lệnh tự động hóa
│   ├── automation_script.py
│   ├── performance_measurement.py
│   └── project_management.py
│
├── /services         # Thư mục chứa các dịch vụ chung
│   ├── __init__.py
│   └── question_service.py
│
├── /tests            # Thư mục chứa các bài kiểm thử hệ thống
│   ├── __init__.py
│   ├── test_connect_db.py
│   └── test_question.py
│
└── /utils            # Thư mục chứa các tiện ích và hàm dùng chung
    ├── __init__.py
    ├── date_utils.py
    ├── file_utils.py
    ├── json_encoder.py
    ├── number_utils.py
    ├── string_utils.py
    └── util.py
```

## Chú Thích

**1. Main Directory**

- `basic_project/:` Thư mục gốc của dự án.

**2. Subfolder**

- `/configs:` Thư mục chứa các file cấu hình.
  - `app_config.py`: Cấu hình cho ứng dụng.
  - `db_config.py`: Cấu hình cho cơ sở dữ liệu.
  - `config.py`: Cấu hình chung.
  - `logging_config.py`: Cấu hình cho logging.
- `/controllers`: Thư mục chứa các bộ điều khiển chung (logic điều hướng).
  - `question_controller.py`: Bộ điều khiển cho các câu hỏi.
  - `session_manager.py`: Quản lý phiên làm việc.
- `/database`: Thư mục chứa các script và model liên quan đến database.
  - `/connect`: Thư mục chứa các lớp quản lý kết nối database.
    - `connect.py`: Quản lý kết nối cơ bản.
  - `/connection`: Thư mục chứa các lớp quản lý kết nối database cụ thể.
    - `mongo_connection.py`: Kết nối tới MongoDB.
    - `mysql_connection.py`: Kết nối tới MySQL.
    - `postgresql_connection.py`: Kết nối tới PostgreSQL.
    - `sqlserver_connection.py`: Kết nối tới SQL Server.
  - `/database_migration`: Thư mục chứa các lớp tạo và quản lý database.
    - `001_initial_setup.py`: Tạo cấu trúc database ban đầu.
  - `/dba`: Thư mục chứa các lớp thực hiện tương tác database (DBA).
    - `mongo_dba.py`: Thực hiện tương tác với MongoDB.
    - `question_dba.py`: Thực hiện tương tác với bảng câu hỏi.
  - `/dbo`: Các model tương đương với từng bảng database (DBO) - Thực hiện định dạng dữ liệu.
    - `question_dbo.py`: Model cho bảng câu hỏi.
- `/docs`: Thư mục chứa tài liệu dự án.
  - `database.md`: Tài liệu về cơ sở dữ liệu.
  - `design_patterns.md`: Tài liệu về các mẫu thiết kế.
  - `oop.md`: Tài liệu về lập trình hướng đối tượng (OOP).
- `/logger`: Thư mục chứa các module liên quan đến logging.
  - `log_formatter.py`: Định dạng log.
  - `logger.py`: Module quản lý logging.
  - `logger.txt`: File log.
- `/models`: Thư mục chứa các business models.
  - `question_model.py`: Business model cho câu hỏi.
- `/modules`: Thư mục chứa mã nguồn chính của các module dịch vụ.
  - `/module_ex`: Thư mục của module example.
    - `/controllers`: Thư mục chứa các bộ điều khiển của module (logic điều hướng).
      - `question_controller.py`: Bộ điều khiển cho các câu hỏi của module.
    - `/self_model`: Thư mục chứa các business model riêng của module.
      - `question_model.py`: Model cho câu hỏi của module.
    - `/self_services`: Thư mục chứa các dịch vụ riêng của module.
      - `question_service.py`: Dịch vụ cho câu hỏi của module.
    - `/tests`: Thư mục chứa các bài kiểm thử của module.
      - `test_question.py`: Bài kiểm thử cho câu hỏi của module.
    - `setup.py`: Tệp cấu hình setuptools cho việc cài đặt và phân phối module.
- `/output`: Thư mục chứa các tệp đầu ra.
- `/patterns`: Thư mục chứa các base class/abstract class.
  - `base_connection.py`: Base class cho các kết nối.
  - `base_controller.py`: Base class cho các controller.
  - `base_dba.py`: Base class cho các DBA.
  - `base_dbo.py`: Base class cho các DBO.
  - `singleton_meta.py`: Meta class cho Singleton pattern.
- `/routes`: Thư mục chứa các route của ứng dụng.
  - `question_routes.py`: Route cho các câu hỏi.
- `/scripts`: Thư mục chứa các tập lệnh tự động hóa.
  - `automation_script.py`: Tập lệnh tự động hóa.
  - `performance_measurement.py`: Tập lệnh đo lường hiệu suất.
  - `project_management.py`: Tập lệnh quản lý dự án.
- `/services`: Thư mục chứa các dịch vụ chung.
  - `question_service.py`: Dịch vụ cho câu hỏi.
- `/tests`: Thư mục chứa các bài kiểm thử hệ thống.
  - `test_connect_db.py`: Kiểm thử kết nối database.
  - `test_question.py`: Kiểm thử câu hỏi.
- `/utils`: Thư mục chứa các tiện ích và hàm dùng chung.
  - `date_utils.py`: Các hàm tiện ích liên quan đến xử lý ngày tháng.
  - `file_utils.py`: Các hàm tiện ích liên quan đến file.
  - `json_encoder.py`: Mã hóa JSON.
  - `number_utils.py`: Các hàm tiện ích liên quan đến xử lý số.
  - `string_utils.py`: Các hàm tiện ích liên quan đến chuỗi.
  - `util.py`: Các hàm tiện ích chung.
