import os


def create_project_structure(project_name):
    # Tạo thư mục gốc
    os.makedirs(project_name)

    # Tạo các thư mục con
    dirs = [
        "configs",
        "database/database_access",
        "database/database_models",
        "docs",
        "patterns",
        "logger",
        "scripts",
        "controllers",
        "models",
        "services",
        "utils",
        "modules/module1/controllers",
        "modules/module1/self_model",
        "modules/module1/self_services",
        "modules/module1/tests",
        "tests",
        "output",
    ]

    for d in dirs:
        os.makedirs(os.path.join(project_name, d))

    # Tạo các tệp tin cần thiết
    # Tạo các tệp tin cần thiết
    files = [
        "README.md",
        "requirements.txt",
        "setup.py",
        ".gitignore",
        "configs/__init__.py",
        "configs/app_config.py",
        "configs/db_config.py",
        "configs/logging_config.py",
        "database/database_access/001_initial_setup.py",
        "database/database_access/002_add_user_table.py",
        "database/database_models/base_model.py",
        "database/database_models/user_model.py",
        "database/database_models/product_model.py",
        "docs/oop.md",
        "docs/design_patterns.md",
        "docs/database.md",
        "patterns/base_service.py",
        "patterns/base_controller.py",
        "patterns/base_model.py",
        "logger/logger.py",
        "logger/log_formatter.py",
        "scripts/automation_script.py",
        "scripts/performance_measurement.py",
        "scripts/project_management.py",
        "controllers/__init__.py",
        "controllers/user_controller.py",
        "controllers/product_controller.py",
        "controllers/order_controller.py",
        "models/__init__.py",
        "models/user_model.py",
        "services/__init__.py",
        "services/user_service.py",
        "services/product_service.py",
        "services/order_service.py",
        "utils/__init__.py",
        "utils/file_utils.py",
        "utils/date_utils.py",
        "utils/string_utils.py",
        "modules/module1/controllers/__init__.py",
        "modules/module1/controllers/user_controller.py",
        "modules/module1/controllers/product_controller.py",
        "modules/module1/controllers/order_controller.py",
        "modules/module1/self_model/__init__.py",
        "modules/module1/self_model/user_model.py",
        "modules/module1/self_services/__init__.py",
        "modules/module1/self_services/user_service.py",
        "modules/module1/self_services/product_service.py",
        "modules/module1/self_services/order_service.py",
        "modules/module1/tests/__init__.py",
        "modules/module1/tests/test_user.py",
        "modules/module1/tests/test_product.py",
        "modules/module1/tests/test_order.py",
        "tests/__init__.py",
        "tests/test_user.py",
        "tests/test_product.py",
        "tests/test_order.py",
        "output/.gitignore",
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
            elif f == "README.md":
                file.write(f"# {project_name}\n\nProject description here.")
            elif f == "requirements.txt":
                file.write("# List of dependencies\n")
            elif f == "setup.py":
                file.write(
                    """from setuptools import setup, find_packages
setup(
    name='your_project_name',
    version='0.1.0',
    packages=find_packages(exclude=['tests', 'docs']),
    include_package_data=True,
    install_requires=[
        # List the required libraries here
    ],
    entry_points={
        'console_scripts': [
            # Ex: 'your_command = your_module:main_function'
        ],
    },
)
"""
                )
            else:
                file.write(f"# {f}")


# Sử dụng hàm để tạo cấu trúc thư mục
create_project_structure("basic_project")
