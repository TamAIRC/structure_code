import os

def create_project_structure(project_name):
    # Tạo thư mục gốc
    os.makedirs(project_name)

    # Tạo các thư mục con
    dirs = [
        "config",
        "dataset",
        "models",
        "log",
        "docs",
        "src/package_name",
        "src/tests",
        "examples",
        "docker",
        "scripts",
        "tools"
    ]

    for d in dirs:
        os.makedirs(os.path.join(project_name, d))

    # Tạo các tệp tin cần thiết
    files = [
        "README.md",
        "requirements.txt",
        "setup.py",
        ".gitignore",
        "config/config.ini",
        "src/package_name/__init__.py",
        "src/package_name/module1.py",
        "src/package_name/module2.py",
        "src/tests/__init__.py",
        "src/tests/test_module1.py",
        "src/tests/test_module2.py",
        "docker/Dockerfile"
        # Thêm các tệp tin khác nếu cần
    ]

    for f in files:
        with open(os.path.join(project_name, f), "w") as file:
            pass

# Sử dụng hàm để tạo cấu trúc thư mục
create_project_structure("project_name")
