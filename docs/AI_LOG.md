| Ngày | Dùng AI làm gì | Em sửa lại gì |
|---|---|---|
| 20/10 | Dùng AI để thiết kế website. | Em giữ nguyên thiết kế ban đầu của trang web, sửa lại phần background và hiệu ứng hover. |
| 21/10 | Dùng AI để chỉnh sửa bố cục văn bản. | Em giữ nội dung văn bản, thêm hiệu ứng xuất hiện và hiệu ứng chữ cho văn bản. |
| 25/10 | Nhờ AI sửa lỗi. | Em sửa các lỗi sai chính tả trong file. |

## Khai báo bổ sung của AI — 15/11/2026

Phần này do trợ lý AI OpenAI Codex tự ghi lại về các công việc đã thực hiện theo yêu cầu của Bùi Trung Đức. Không phải lời xác nhận rằng sinh viên đã tự viết hoặc chỉnh sửa các phần mã này.

| Hạng mục | Công việc AI đã thực hiện | Vai trò của sinh viên |
|---|---|---|
| Thông tin cá nhân | Bổ sung vào `index.html` thông tin sinh viên năm nhất ngành Công nghệ thông tin, Trường Đại học Đại Nam. | Cung cấp thông tin và yêu cầu cập nhật. |
| Thành tựu | Thêm thẻ giải Ba Trại kỹ năng mềm Đại học Đại Nam vào `hello.html`; dùng công cụ chỉnh ảnh AI để tách nền ảnh huy chương do sinh viên cung cấp, giữ huy chương và dây đeo; thêm CSS căn ảnh. | Cung cấp thành tựu, ảnh gốc và yêu cầu cách hiển thị. |
| Thời khóa biểu | Thêm bộ chọn học kì 1 và 2 trong `schedule.html`, giữ lịch cũ ở học kì 1; nhập 5 tiết chiều thứ 2, 4, 6 của học kì 2 với môn học và phòng học đã cung cấp. | Cung cấp lịch học hai học kì và ảnh khung giờ K20. |
| Giờ học K20 | Đọc ảnh khung giờ để nhập các tiết chiều 12:45–13:45, 13:50–14:40, 14:55–15:45, 15:50–16:40, 16:45–17:25; kết nối với chức năng báo tiết đang học và đếm thời gian. | Xác nhận bản thân thuộc khóa K20. |
| Hiệu ứng giao diện | Xóa JavaScript tạo hiệu ứng nghiêng khung trong cả bốn trang HTML và các thuộc tính CSS 3D liên quan. | Yêu cầu bỏ hiệu ứng nghiêng. |
| Kiểm tra | Kiểm tra cú pháp JavaScript và `git diff --check`; chạy kiểm tra mô phỏng chuyển học kì, môn/phòng, ngày nghỉ, giờ học và các khoảng nghỉ 5/15 phút bằng Node.js. Các kiểm tra này không thay thế kiểm thử toàn diện trên mọi thiết bị. | Đưa ra phản hồi và yêu cầu điều chỉnh qua trao đổi. |
| Quản lý phiên bản | Commit, đẩy thay đổi lên GitHub; sao chép phiên bản có chatbot sang repo riêng `Yukosheini/Yuuko-portfolio-AI`; sau đó đưa repo hiện tại về `4bfedfb` theo yêu cầu. | Chọn tên repo, chế độ công khai và chỉ định hai commit cần gỡ khỏi repo gốc. |

### Phạm vi phiên bản hiện tại

Tính năng chatbot Gemini, mã bí mật và mã kết nối Supabase từng được AI xây dựng trong quá trình trao đổi, nhưng đã được tách sang repo `Yuuko-portfolio-AI`. Hai commit `6265fd1` và `da52216` đã được gỡ khỏi nhánh `main` của repo hiện tại theo yêu cầu sinh viên; không tính chatbot là tính năng đang có trong bản này. Các dịch vụ Supabase/Gemini đã cấu hình bên ngoài không bị xóa khi gỡ commit.

AI trực tiếp viết và chỉnh sửa mã cho các hạng mục nêu trên. Nội dung cá nhân, lịch học, thành tựu và ảnh đầu vào do sinh viên cung cấp. Nhật ký bổ sung này cũng do AI soạn; các dòng nhật ký cũ được giữ nguyên.
