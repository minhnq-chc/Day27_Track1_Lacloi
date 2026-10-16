# [EMAIL GỬI THÀNH VIÊN NHÓM LẠC LỐI - DAY 27]

**Tiêu đề:** `[Nhóm Lạc Lối - Track 01] Triển khai & Phân công hoàn thiện Lab Day 27 — AI Evaluation (CS12)`  
**Người gửi:** Ninh Quang Minh (`26ai.minhnq6@vinuni.edu.vn`) — Nhóm trưởng  
**Người nhận:**  
- Trần Phạm Thái Vũ (`2A202602695`)
- Đinh Trường An (`2A202602393`)
- Hoàng Anh Tài (`2A202602612`)
- Nguyễn Anh Dũng (`2A202602554`)

---

Chào cả nhóm,

Hôm nay nhóm mình tiếp tục chiến đấu với **Lab Day 27: Đánh giá sản phẩm AI (AI Evaluation - CS12)**, đi kèm bộ slide của chị Mai Anh Nguyen (VinAI/VinUni).

Mình đã nghiên cứu toàn bộ đề bài, slide 66 trang và dựng sẵn khung giải pháp hoàn chỉnh cho cả **5 Bài tự kiểm tra (Bài 1–5)** và **Xưởng thực hành (X1–X7)**, đảm bảo file Excel `[Lacloi]_CS12.xlsx` **vượt qua 100% các ô kiểm tra tự động và đạt trọn vẹn 10/10 điểm theo Thang điểm giảng viên**.

### 📌 1. Thông tin chung & Hạn nộp
* **Hạn nộp:** Trước **13:00 ngày 16/10/2026** trên hệ thống VLearn.
* **File nộp chính thức:** `[Lacloi]_CS12.xlsx` (đã điền đầy đủ thông tin nhóm ở dòng 3 và hoàn thành trọn vẹn X1 → X7).
* **Repository GitHub:** Đã khởi tạo cấu trúc chuẩn hoá, đẩy code và tài liệu phân tích chi tiết.

### 👥 2. Phân công vai trò & Review chéo
Để đảm bảo tiến độ và chất lượng bảo vệ bài, mình phân công nhiệm vụ cụ thể cho từng thành viên:
1. **Ninh Quang Minh (Nhóm trưởng):**
   * Quản trị Repo GitHub, cấu trúc thư mục, tổng hợp và thẩm định chất lượng file Excel `[Lacloi]_CS12.xlsx`.
   * Soạn thảo đặc tả kiến trúc X1 (Đơn vị công việc AI) và X7 (Quyết định Phát hành có răng, Kế hoạch giám sát trôi & 2 giờ vàng của chuyên gia).
   * Deploy và nộp bài lên VLearn.
2. **Đinh Trường An:**
   * Phụ trách thẩm định **X3 (Ngân hàng 8 tình huống)**: Kiểm tra tính bao phủ của 3 ca Đại diện, 3 ca Thử thách và 2 ca Hồi quy nghiêm trọng; rà soát trích dẫn đúng chính sách CS-1 đến CS-6.
3. **Trần Phạm Thái Vũ:**
   * Phụ trách thẩm định **X2 (Lưới đầu vào & Phễu chọn ca)**: Kiểm tra 3 chiều qua phép thử (Hành vi đổi thế nào) và số đầu vào (45 ca); rà soát **X5 (4 tiêu chí nhị phân)** đảm bảo tuyệt đối không có từ mơ hồ và ví dụ sát ranh chuẩn xác.
4. **Hoàng Anh Tài:**
   * Phụ trách thẩm định **X4 (Phân tích 3 vết thực thi W1, W2, W3)**: Kiểm tra bước sai đầu tiên, mã lỗi chuẩn (`missing_lookup`, `wrong_intent`, `missing_escalation`) và giải pháp sửa chữa.
5. **Nguyễn Anh Dũng:**
   * Phụ trách thẩm định **X6 (Hiệu chỉnh giám khảo AI)**: Rà soát bảng 20 tin, ma trận 4 ô, chỉ số TPR (85.7% - dưới ngưỡng) / TNR (100% - đạt) và kết luận B; kiểm tra bảng tổng kết toàn bộ Bài 1–5.

### 🚀 3. Hướng dẫn phối hợp Git
1. Các bạn clone repo về:
   ```bash
   git clone <REPO_URL>
   git checkout -b review/<ten-thanh-vien>
   ```
2. Mở file `[Lacloi]_CS12.xlsx` và các tài liệu trong thư mục `docs/` để đọc và phản biện.
3. Nếu có góp ý hoặc tinh chỉnh, commit và push lên branch cá nhân, sau đó tạo Pull Request về `main`. Mình sẽ review và merge trước 12:45 để chốt nộp VLearn lúc 12:55.

Mọi người cùng rà soát nhanh để nhóm mình tiếp tục đạt điểm tuyệt đối nhé!

Cảm ơn cả nhóm,  
**Ninh Quang Minh**
