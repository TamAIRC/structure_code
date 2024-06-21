# Git Workflow

Mô tả Workflow làm việc của team khi triển khai dự án

## Table of Contents

- [Git Workflow](#git-workflow)
  - [Table of Contents](#table-of-contents)
  - [0. Quy tắc viết Issue](#0-quy-tắc-viết-issue)
  - [1. Branch structure (Branching Strategy)](#1-branch-structure-branching-strategy)
  - [2. Quy Tắc Đặt Tên Branch](#2-quy-tắc-đặt-tên-branch)
  - [3. Commit Message](#3-commit-message)
  - [4. Pull Request](#4-pull-request)
  - [5. Các Quy Tắc Khác](#5-các-quy-tắc-khác)
  - [6. Workflow](#6-workflow)
    - [6.1. Quy trình tạo và phát triển nhánh Feature](#61-quy-trình-tạo-và-phát-triển-nhánh-feature)
    - [6.2. Quy trình tạo và phát triển nhánh Experiment:](#62-quy-trình-tạo-và-phát-triển-nhánh-experiment)
    - [6.3. Quy trình sửa lỗi khẩn cấp (`hotfix`):](#63-quy-trình-sửa-lỗi-khẩn-cấp-hotfix)
    - [Tóm Tắt Các Bước:](#tóm-tắt-các-bước)

## 0. Quy tắc viết Issue

- **Tiêu đề Issue**:
  - Tiêu đề phải ngắn gọn, mô tả rõ ràng vấn đề hoặc yêu cầu.
- **Mô tả Issue**:
  - **Mô tả chi tiết**: Giải thích chi tiết về vấn đề hoặc yêu cầu.
  - **Các bước để tái hiện (`Reproduction Steps`)**: Nếu là bug, mô tả các bước để tái hiện lỗi.
  - **Kết quả mong đợi (`Expected Result`)**: Mô tả kết quả mong đợi nếu không có lỗi.
  - **Kết quả thực tế (`Actual Result`)**: Mô tả kết quả thực tế khi lỗi xảy ra.
  - **Ảnh chụp màn hình (`Screenshots`)**: Nếu cần, thêm ảnh chụp màn hình để mô tả lỗi.
  - **Môi trường (`Environment`)**: Mô tả môi trường nơi lỗi xảy ra (ví dụ: hệ điều hành, trình duyệt, phiên bản phần mềm).
  - Liên kết tới task hoặc PR liên quan: Nếu có, liên kết tới task hoặc PR liên quan.
- **Gắn nhãn (`Labels`)**:
  - Sử dụng nhãn để phân loại issue (`bug`, `enhancement`, `question`, `documentation`, v.v.)
- **Gắn người thực hiện (`Assignees`)**:
  - Gắn người thực hiện có trách nhiệm giải quyết issue.
- **Thời gian hoàn thành (`Due Date`)**:
  - Đặt thời gian hoàn thành nếu cần thiết.
- **Ưu tiên (`Priority`)**:
  - Đánh dấu mức độ ưu tiên của issue (`high`, `medium`, `low`).

```markdown
# Tiêu đề

Lỗi không thể đăng nhập khi sử dụng mật khẩu chứa ký tự đặc biệt

## Mô tả chi tiết

Người dùng không thể đăng nhập khi mật khẩu chứa ký tự đặc biệt như `!`, `@`, `#`.

## Các bước để tái hiện

1. Truy cập trang đăng nhập.
2. Nhập tên tài khoản và mật khẩu chứa ký tự đặc biệt.
3. Nhấn nút "Đăng nhập".

## Kết quả mong đợi

Người dùng được chuyển tới trang chính.

## Kết quả thực tế

Hiển thị thông báo lỗi "Mật khẩu không hợp lệ".

## Ảnh chụp màn hình

![Login Error](link_to_screenshot)

## Môi trường

- Hệ điều hành: Windows 10
- Trình duyệt: Chrome 90.0
- Phiên bản phần mềm: 1.2.3

## Liên kết tới task hoặc PR liên quan

- Task [#123](link_to_task)
- Pull Request [#456](link_to_pr)
```

## 1. Branch structure (Branching Strategy)

**Các loại nhánh cơ bản:**

1. `main` (hoặc `master`): Nhánh chính, chứa mã nguồn ổn định nhất (base code).
2. `develop`: Nhánh phát triển, nơi tích hợp tất cả các thay đổi từ các nhánh tính năng.
3. `feature`: Nhánh tính năng, tạo cho mỗi tính năng hoặc chức năng cụ thể.
4. `experiment`: Nhánh thử nghiệm, dùng cho các thử nghiệm hoặc nghiên cứu các khái niệm mới.
5. `deploy`: Nhánh triển khai.
6. `bugfix/hotfix`: Nhánh sửa lỗi, dùng để sửa các lỗi phát hiện trong nhánh phát triển hoặc triển khai.

## 2. Quy Tắc Đặt Tên Branch

- Tên branch phải mô tả ngắn gọn và rõ ràng về nhiệm vụ của nó.
- Định dạng: [username]/[name_branch]/t[task-id]-[task-label]-[screen-id|api-description]
  - Ví dụ:
    - Task 101 về UI: `ngotam/t101-ui-com_003_02`
    - Task 101 về Event JS: `ngotam/t101-event-com_003_02`
    - Task 101 về API: `khanhly/t101-api-get_question`

## 3. Commit Message

- Commit message phải ngắn gọn, rõ ràng và mô tả chính xác thay đổi.
- Sử dụng thì hiện tại (present tense).
- Cấu trúc: `[type]: [message]`
- `type` có thể là `feat` (tính năng), `fix` (sửa lỗi), `docs` (tài liệu), `style` (định dạng), `refactor` (tái cấu trúc), `test` (kiểm thử), hoặc `chore` (công việc phụ).
- Ví dụ:
  - `feat`: Thêm chức năng đăng nhập
  - `fix`: Sửa lỗi không thể đăng xuất

## 4. Pull Request

- Mỗi pull request (PR) phải gắn với ít nhất một task hoặc issue.
- PR description phải bao gồm:
  - Mô tả ngắn gọn về thay đổi.
  - Liên kết tới task hoặc issue liên quan.
  - Hướng dẫn kiểm tra và test.
- Ví dụ

```markdown
### Mô tả

Thêm chức năng đăng nhập cho ứng dụng.

### Task liên quan

- Task [#101](link_to_task)

### Cách kiểm tra

1. Truy cập trang đăng nhập.
2. Nhập thông tin tài khoản và mật khẩu.
3. Nhấn nút "Đăng nhập".
4. Xác nhận rằng người dùng được chuyển tới trang chính.
```

## 5. Các Quy Tắc Khác

- **Code Review**:
  - Mọi thay đổi cần được `code review` bởi ít nhất một thành viên khác trong nhóm.
  - Các nhận xét (`comments`) phải mang tính xây dựng và tập trung vào cải - thiện chất lượng code.
- **Phân Nhánh (Branching)**:
  - Sử dụng mô hình Gitflow cho quy trình phân nhánh: `feature`, `develop`, `release`, `hotfix`, `master`.
- **Tagging**:

  - Sử dụng tags để đánh dấu các phiên bản phát hành (`v1.0.0`, `v1.1.0`).

- Code Merge:

  - Chỉ merge code vào `main` hoặc `develop` khi đã được kiểm tra và thông qua - `code review`.
  - Sử dụng `rebase` thay cho `merge` khi cập nhật branch để giữ lịch sử commit - sạch sẽ.

- **Documentation**:
  - Cập nhật tài liệu dự án khi có thay đổi quan trọng về chức năng hoặc cấu - trúc.
  - Sử dụng Markdown cho tài liệu.
- **Security**:
  - Bảo mật thông tin nhạy cảm (API keys, mật khẩu) bằng cách sử dụng biến - môi trường hoặc các công cụ quản lý bảo mật.
  - Luôn cập nhật các gói phần mềm để tránh lỗ hổng bảo mật.
- **Performance**:

  - Tối ưu hóa code để đảm bảo hiệu suất.
  - Sử dụng các công cụ phân tích hiệu suất để tìm và sửa các `bottleneck`.

- **Accessibility**:

  - Đảm bảo ứng dụng thân thiện với người dùng có khuyết tật.
  - Sử dụng các tiêu chuẩn và công cụ kiểm tra accessibility như [`WCAG`](https://www.w3.org/TR/WCAG21/).

- **Internationalization (I18n)**:

  - Hỗ trợ đa ngôn ngữ và địa phương hóa.
  - Sử dụng các thư viện [I18n](https://www.i18next.com/) để quản lý bản dịch.

- **DevOps**:

  - Tự động hóa quy trình `CI/CD` để đảm bảo chất lượng và tốc độ triển khai.
  - Sử dụng `Docker` và `Kubernetes` để triển khai và quản lý `container`.

- **Communication**:

  - Sử dụng các kênh giao tiếp như `Slack`, `Teams` để trao đổi và cập nhật thông tin.
  - Thường xuyên tổ chức các cuộc họp để cập nhật tiến độ và giải quyết vấn đề.

- **Learning and Development**:
  - Khuyến khích học hỏi và phát triển kỹ năng mới.
  - Tham gia các buổi đào tạo, hội thảo và đọc sách chuyên môn.

## 6. Workflow

### 6.1. Quy trình tạo và phát triển nhánh Feature

- **1. Tạo nhánh tính năng từ nhánh `develop`:**

```sh
git checkout develop
git checkout -b [username]/[name_branch]/t[task-id]-[task-label]-[screen-id|api-description]
```

Ví dụ: `git checkout -b khanhly/t101-api-get_question`

- **2. Phát triển tính năng hoặc thực hiện lại trên nhánh tính năng.**

- **3. Commit và đẩy nhánh lên repository:**

```sh
git add .
git commit -m "Mô tả thay đổi"
git push origin [username]/[name_branch]/t[task-id]-[task-label]-[screen-id|api-description]
```

Ví dụ: `git push origin khanhly/t101-api-get_question`

- **4. Tạo Pull Request (PR):**

  - Mở pull request từ nhánh tính năng đến nhánh develop.
  - Mô tả chi tiết về thay đổi và khái niệm đã học trong PR.

- **5. Kiểm tra mã (Code Review):**

  - Các thành viên khác xem xét và đưa ra phản hồi trên PR.
  - Thảo luận và chỉnh sửa mã dựa trên phản hồi.

- **6. Hợp nhất nhánh tính năng vào nhánh phát triển:**
  - Sau khi PR được chấp thuận, hợp nhất (merge) vào nhánh develop

```sh
git checkout develop
git merge [username]/[name_branch]/t[task-id]-[task-label]-[screen-id|api-description]
```

Ví dụ: `git merge khanhly/t101-api-get_question`

### 6.2. Quy trình tạo và phát triển nhánh Experiment:

- **1. Tạo nhánh `experiment` từ nhánh `develop`:**

```sh
git checkout develop
git checkout -b [username]/experiment-[experiment_name]
```

Ví dụ: `git checkout -b ngotam/experiment-api_get_question`

- **2. Thực hiện thử nghiệm và commit.**

- **3. Đẩy nhánh thử nghiệm lên repository:**

```sh
git add .
git commit -m "Mô tả kết quả thử nghiệm"
git push origin [username]/experiment-[experiment_name]
```

Ví dụ: `git push origin ngotam/experiment-api_get_question`

- **4. Tạo Pull Request (PR):**

- Tạo PR từ nhánh thử nghiệm đến nhánh develop.
- Mô tả chi tiết về thử nghiệm và kết quả.

- **5. Kiểm tra mã (Code Review) và hợp nhất tương tự như nhánh tính năng.**

### 6.3. Quy trình sửa lỗi khẩn cấp (`hotfix`):

- **1. Tạo nhánh sửa lỗi từ nhánh `deploy`:**

```sh
git checkout deploy
git checkout -b [username]/hotfix-[bug_name]
```

Ví dụ: `git checkout -b ngotam/hotfix-api_get_question`

- **2. Thực hiện hotfix, thử nghiệm nhanh và commit.**

### Tóm Tắt Các Bước:

- `Tạo Issue`: Mô tả tính năng hoặc vấn đề.
- `Tạo nhánh feature`: Phát triển và đẩy lên.
- `Tạo PR từ feature đến develop`: Code review và hợp nhất.
- `Tạo nhánh experiment`: Thử nghiệm và đẩy lên.
- `Tạo PR từ experiment đến develop`: Code review và hợp nhất.
- `Merge develop vào deploy`: Triển khai thực tế.
