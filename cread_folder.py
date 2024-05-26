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
        "tools",
        "output"
    ]

    for d in dirs:
        os.makedirs(os.path.join(project_name, d))

    # Tạo các tệp tin cần thiết
    files = [
        "README.md",
        "requirements.txt",
        "setup.py",
        ".gitignore",
        "config/config.py",
        "config/__init__.py",
        "src/package_name/__init__.py",
        "src/package_name/module1.py",
        "src/tests/__init__.py",
        "src/tests/test_module1.py",
        "docker/Dockerfile",
        "log/.gitignore",
        "models/.gitignore",
        "output/.gitignore",
        "tools/__init__.py",
        # Thêm các tệp tin khác nếu cần
    ]
    # Content for the main .gitignore file
    main_gitignore_content = """.conda\n.venv\n__pycache__\npoppler-*"""

    # Content for the nested .gitignore files
    nested_gitignore_content = "*\n!.gitignore"
    for f in files:
        file_path = os.path.join(project_name, f)
        with open(file_path, "w") as file:
            if f == ".gitignore":
                file.write(main_gitignore_content)
            elif f.endswith(".gitignore"):
                file.write(nested_gitignore_content)


# Sử dụng hàm để tạo cấu trúc thư mục
create_project_structure("basic_project")
