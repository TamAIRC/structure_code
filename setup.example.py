from setuptools import setup, find_packages

"""
- `setuptools` là một thư viện giúp tạo, phân phối và cài đặt các gói Python.
- `setup` là hàm chính được sử dụng để cung cấp thông tin về gói Python.
- `find_packages` tự động tìm kiếm tất cả các gói con trong thư mục hiện tại.
"""

setup(
    # `name`: Tên của gói. Đây là tên mà người dùng sẽ sử dụng khi cài đặt gói của bạn (ví dụ: `pip install my_package`).
    name="my_package",
    # `version`: Phiên bản hiện tại của gói. Phiên bản này sẽ giúp người dùng biết được bản cập nhật của gói.
    version="0.1.0",
    # `packages`: Danh sách các gói Python trong dự án. `find_packages()` sẽ tự động tìm và liệt kê tất cả các gói con.
    packages=find_packages(),
    # `install_requires`: Danh sách các thư viện phụ thuộc mà gói của bạn cần. Khi cài đặt gói của bạn, các thư viện này cũng sẽ được cài đặt nếu chưa có.
    install_requires=["requests", "torch", "torchvision", "torchaudio"],
    # `entry_points`: Tạo các lệnh dòng lệnh từ gói của bạn. Ở đây, `my_package_script` sẽ trở thành một lệnh có thể chạy từ terminal và sẽ gọi hàm main trong tệp` script.py` của gói `my_package`.
    entry_points={
        "console_scripts": [
            "my_package_script=my_package.script:main",
        ],
    },
    # `include_package_data`: Bao gồm các tập tin dữ liệu được liệt kê trong `MANIFEST.in`.
    include_package_data=True,
    # `description`: Mô tả ngắn gọn về gói của bạn.
    description="A utility package for downloading files, extracting ZIP archives, and installing packages.",
    # `long_description`: Mô tả chi tiết hơn, thường được lấy từ tệp README.
    long_description=open("README.md").read(),
    # `long_description_content_type`: Loại nội dung của `long_description` (ví dụ: `text/markdown`).
    long_description_content_type="text/markdown",
    # `author`: Tên của tác giả gói.
    author="Your Name",
    # `author_email`: Email của tác giả.
    author_email="your.email@example.com",
    # `url`: URL đến trang web hoặc kho lưu trữ của dự án (thường là GitHub).
    url="https://github.com/yourusername/my_package",  # Update this with your actual URL
    # `classifiers`: Các phân loại giúp người dùng tìm kiếm và hiểu rõ hơn về gói của bạn. Ví dụ như:
    # Ngôn ngữ lập trình (`Programming Language :: Python :: 3`)
    # Loại giấy phép (`License :: OSI Approved :: MIT License`)
    # Hệ điều hành (`Operating System :: OS Independent`)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # `python_requires`: Phiên bản Python tối thiểu mà gói của bạn hỗ trợ.
    python_requires=">=3.11",
)
