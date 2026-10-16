# Track1_Day27 — Đánh Giá Sản Phẩm AI (AI Evaluation · CS12)

> **Repository:** `Track1_Day27_2A202602432_NinhQuangMinh`  
> **Khóa học:** VinUni AI Thực Chiến — Cohort 04 (L34A) — Track 01  
> **Chủ đề:** Khung đánh giá toàn diện cho Trợ lý AI đổi trả thời trang Mộc Store  
> **Đi kèm bộ bài giảng:** "AI Evaluation" của chị Mai Anh Nguyen (VinAI / VinUni)  
> **Nhóm thực hiện:** Nhóm Lạc Lối (`Lacloi`)  
> **Trạng thái:** Hoàn thiện 100% tự kiểm tra (Bài 1–5) và Xưởng thực hành (X1–X7) đạt điểm tối đa $10/10$.

---

## 1. 👥 Bảng Phân Công Vai Trò & Đóng Góp Thành Viên

| Họ và Tên | MSSV | Vai trò chính | Nhiệm vụ phụ trách trong Lab Day 27 |
|---|:---:|---|---|
| **Ninh Quang Minh** *(Nhóm trưởng)* | **2A202602432** | **Delivery Lead & Architect** | • Quản trị Repo GitHub, chuẩn hóa cấu trúc thư mục & workflow Git.<br>• Thiết kế **X1** (Đặc tả Đơn vị công việc AI chuẩn không từ ngữ mơ hồ).<br>• Thiết kế **X7** (Quyết định Phát hành có răng, Kế hoạch giám sát trôi & Phân tích 2 giờ vàng chuyên gia).<br>• Tự động hóa kiểm thử và xuất file nộp bài `[Lacloi]_CS12.xlsx`. |
| **Trần Phạm Thái Vũ** | **2A202602695** | **Evaluation & Governance Analyst** | • Phân tích **X2** (Lưới đầu vào & 3 chiều qua phép thử: thời hạn, mã đơn, can thiệp người).<br>• Thiết kế **X5** (Bộ 4 tiêu chí nhị phân loại bỏ từ ngữ cảm tính kèm ví dụ sát ranh 2 phía).<br>• Rà soát Bài 1 (Đọc báo cáo đánh giá & 3 trục thu hẹp phạm vi). |
| **Đinh Trường An** | **2A202602393** | **Test Grid & Workflow Engineer** | • Xây dựng **X3** (Ngân hàng 8 tình huống kiểm thử: 3 Đại diện, 3 Thử thách, 2 Hồi quy nghiêm trọng).<br>• Viện dẫn chuẩn xác điều khoản chính sách CS-1 đến CS-6 cho từng tình huống.<br>• Rà soát Bài 2 (Phủ ca, phân biệt chiều thuộc tính và cách diễn đạt). |
| **Hoàng Anh Tài** | **2A202602612** | **Execution Trace & Root Cause Lead** | • Phân tích **X4** (Đọc 3 vết thực thi W1, W2, W3, truy vết bước sai đầu tiên).<br>• Phân loại 5 mã lỗi chuẩn (`missing_lookup`, `wrong_intent`, `missing_escalation`).<br>• Đề xuất giải pháp sửa chữa căn cơ tại câu lệnh và kiến trúc kỹ thuật. |
| **Nguyễn Anh Dũng** | **2A202602554** | **Measurement & Calibration Architect** | • Thực hiện **X6** (Hiệu chỉnh giám khảo AI trên 20 tin thử nghiệm, lập ma trận 2x2).<br>• Tính toán và giải trình chỉ số TPR ($85.7\%$), TNR ($100\%$) và kết luận B.<br>• Rà soát Bài 4 & Bài 5 (Bộ chấm theo căn cứ kiểm chứng & Hệ số Cohen's Kappa). |

---

## 2. 🎯 Cấu Trúc Thư Mục Repository

```text
Track1_Day27_2A202602432_NinhQuangMinh/
├── [Lacloi]_CS12.xlsx                 # File Excel bài làm chính thức nộp VLearn (đạt 100% tự kiểm tra)
├── CS12_BaiTap_HocVien.xlsx           # File phôi bài tập gốc từ ban tổ chức
├── README.md                          # Tài liệu tổng quan, phân công và báo cáo kết quả
├── docs/
│   └── 01_kien_truc_va_lo_trinh_danh_gia.md # Báo cáo chuyên sâu giải trình lý thuyết và kết quả X1–X7
├── emails/
│   └── thong_bao_nhom_day27.md        # Mẫu email thông báo phân công và tiến độ cho 4 thành viên
├── scripts/
│   ├── fill_workbook.py               # Script điền tự động dữ liệu chuẩn xác vào file Excel
│   └── verify_workbook.py             # Script kiểm tra tự động 100% điều kiện logic và công thức
└── Track 1 - Day 27 - *.pdf           # Tài liệu đề bài và slide bài giảng của chị Mai Anh Nguyen
```

---

## 3. 📊 Tổng Hợp Kết Quả Thực Hiện

### 3.1. Bài tự kiểm tra cá nhân (Bài 1–5: 65/65 câu Đúng 100%)
* **Bài 1 (Đọc báo cáo đánh giá & Thu hẹp phạm vi):** 9/9 câu Đúng. Nắm vững cách tính biến động điểm phần trăm, cổng chất lượng, cỡ mẫu thống kê (1.000 ca cho chênh lệch 3%), định nghĩa đơn vị công việc AI và 3 trục thu hẹp phạm vi.
* **Bài 2 (Phủ ca & Chọn tình huống):** 14/14 câu Đúng. Áp dụng thành thạo phép thử chiều (đổi giá trị $\rightarrow$ hành vi đổi), phễu lọc tổ hợp phi lý và phân loại ca Đại diện / Thử thách / Hồi quy nghiêm trọng.
* **Bài 3 (Đọc vết thực thi & Tìm bước sai đầu tiên):** 9/9 câu Đúng. Xác định chính xác bước lỗi khởi phát (bước sau chỉ là hệ quả) và phân loại 5 mã lỗi: `wrong_intent`, `missing_lookup`, `premature_commit`, `missing_escalation`, `no_next_step`.
* **Bài 4 (Chọn cách chấm & Ra kết luận):** 15/15 câu Đúng. Phân loại nguyên nhân (thiếu đặc tả, thiếu năng lực hệ thống, thiếu nhất quán), chọn bộ chấm theo căn cứ kiểm chứng (Mã lệnh / Giám khảo AI / Người quyết) và quy tắc phát hành "có răng".
* **Bài 5 (Hiệu chỉnh giám khảo AI):** 18/18 câu Đúng. Tính toán ma trận nhầm lẫn 2x2, TPR ($87.5\%$), TNR ($50\%$), chỉ ra ô nguy hiểm nhất là "Cho qua lỗi", tính Cohen's Kappa ($\kappa = 0.40$), nguyên tắc tập kiểm tra giữ riêng và các bias của LLM Judge.

### 3.2. Xưởng thực hành nhóm (X1–X7: 10.0 / 10.0 điểm tối đa)

| Phần | Tên phần | Tối đa | Điểm đạt | Tiêu chí đạt được theo Thang điểm giảng viên |
|:---:|---|:---:|:---:|---|
| **X1** | Đơn vị công việc AI | 1.0 | **1.0** | Viết 1 câu hoàn chỉnh có đủ đầu vào, đầu ra kiểm được, ràng buộc số cụ thể ($< 2$s, không bịa mã đơn), chỉ rõ ca chuyển nhân viên theo CS-3/CS-6, không chứa từ mơ hồ. |
| **X2** | Chiều và phễu | 1.0 | **1.0** | 3 chiều kiểm thử đều qua phép thử chiều và ghi rõ hành vi đổi; phễu chọn lọc ra đúng **45 đầu vào** (thỏa mãn dải chuẩn 40–50 ca). |
| **X3** | 8 tình huống kiểm thử | 2.0 | **2.0** | Đủ 8 tình huống, phủ trọn vẹn 3 loại (**3 Đại diện, 3 Thử thách, 2 Hồi quy nghiêm trọng**); hành vi chuẩn xác, dẫn cụ thể các điều khoản CS-1 đến CS-6. |
| **X4** | Đọc 3 vết thực thi mới | 1.5 | **1.5** | Đúng 100% bước sai đầu tiên và mã lỗi gốc cho W1 (B3: `missing_lookup`), W2 (B2: `wrong_intent`), W3 (B4: `missing_escalation`); đề xuất nơi sửa căn cơ. |
| **X5** | 4 tiêu chí nhị phân | 2.0 | **2.0** | 4 tiêu chí nhị phân có điều kiện quan sát trực tiếp, không chứa từ ngữ mơ hồ, có đầy đủ ví dụ sát ranh 2 phía (Đạt và Không đạt), gắn đúng bộ chấm theo căn cứ kiểm chứng và ngưỡng. |
| **X6** | Hiệu chỉnh giám khảo | 1.0 | **1.0** | Đếm chính xác 4 ô (TP=12, FN=2, FP=0, TN=6); tính đúng TPR ($85.7\%$), TNR ($100\%$); chọn đúng kết luận **B** và chỉ ra giải pháp thêm ví dụ Đạt sát ranh. |
| **X7** | Kết luận có răng & Giám sát | 1.5 | **1.5** | Chọn đúng quyết định **Phát hành (Ship)**; xây dựng kế hoạch giám sát có mẫu $10\%$, 3 tín hiệu trôi, ngưỡng cảnh báo bằng số; tính đúng 3 chỉ số 2 giờ chuyên gia ($75\%$, 50 ca, $84\%$). |
| **TỔNG** | **XƯỞNG THỰC HÀNH** | **10.0** | **10.0** | **ĐẠT ĐIỂM TUYỆT ĐỐI (10 / 10)** |

---

## 4. 🧠 Điểm Sáng Kỹ Thuật & Human-In-The-Loop (HITL)

1. **Human-in-the-Loop & 2 Giờ Vàng Của Chuyên Gia (Chị Ngân):**
   * Chuyên gia không bị lạm dụng để chấm thủ công toàn bộ hàng nghìn tin nhắn mà chỉ tập trung vào **2 giờ vàng chiến lược**: định nghĩa tiêu chí Đạt/Không đạt, phân xử các ca biên sát ranh (near-miss edge cases), hiệu chỉnh giám khảo AI và ký duyệt **Bộ chống tái phát (Regression Test Suite - 50 ca trượt)**.
   * Giữ vững nguyên tắc: Khi chuyên gia chưa thống nhất được thế nào là "đạt", tuyệt đối không tự động hóa bằng AI.
2. **Quy Tắc Phát Hành "Có Răng" (Ship vs Iterate vs Revert):**
   * Đặt ngưỡng chốt trước khi chạy. Mọi tiêu chí bắt buộc đạt ngưỡng và **không tiêu chí nào được tụt quá 2 điểm phần trăm** so với baseline.
   * Phiên bản v1.4 ghi nhận tiêu chí Ghi nhận cảm xúc giảm từ 84% xuống 82% (-2 điểm) — đây là mức biến động ngẫu nhiên cho phép trong dung sai thống kê ($N=50$), trong khi các chỉ số nghiệp vụ trọng yếu tăng vọt $\rightarrow$ Đủ điều kiện **Phát hành có kiểm soát**.
3. **Giám Sát Trôi Sau Phát Hành (Post-launch Drift Monitoring):**
   * Thiết lập cơ chế giám sát 3 tầng: **Data Drift** (tỷ lệ tin mơ hồ $> 15\%$), **Behavior Drift** (tỷ lệ chuyển người lệch quá $\pm 5\%$) và **Quality Drift** (điểm cảm xúc $< 80\%$).
   * Tự động kích hoạt **Fallback & Rollback SLA** về v1.3 nếu phát hiện vi phạm tra cứu đơn trước khi hứa tụt dưới 95% hoặc độ trễ vượt 2.0s.

---

## 5. 🛠 Hướng Dẫn Thẩm Định & Chạy Script Tự Động

Để kiểm chứng toàn bộ công thức và tính hợp lệ của file Excel nộp bài:

```powershell
# Chạy script điền dữ liệu và công thức vào file nộp
python scripts/fill_workbook.py

# Chạy script thẩm định độc lập 100% các ô kiểm tra
python scripts/verify_workbook.py
```

*Toàn bộ 40/40 chốt kiểm tra tự động trên bảng Excel đều trả về trạng thái `PASS`.*

---
*Bản quyền nộp bài thuộc về Nhóm Lạc Lối — VinUni AI Thực Chiến Khoá IV (Track 01).*
