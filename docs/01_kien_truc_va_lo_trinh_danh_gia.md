# Báo Cáo Chuyên Sâu: Đánh Giá Sản Phẩm AI (CS12)
## Case Study: Trợ Lý Đổi Trả Thời Trang Mộc Store

> **Khóa học:** VinUni AI Thực Chiến — Cohort 04 (L34A) — Track 01  
> **Nhóm thực hiện:** Nhóm Lạc Lối (`Lacloi`)  
> **Nhóm trưởng:** Ninh Quang Minh (`2A202602432`)  
> **Thành viên:** Trần Phạm Thái Vũ, Đinh Trường An, Hoàng Anh Tài, Nguyễn Anh Dũng  

---

## 1. X1 · Đơn Vị Công Việc AI (Unit of AI Work)

### 1.1. Khái niệm & Nguyên tắc thiết kế
Một đơn vị công việc AI hợp chuẩn phải thỏa mãn cấu trúc:
$$\text{Đọc [Đầu vào]} \longrightarrow \text{[Đầu ra kiểm được]}, \text{[Ràng buộc định lượng]}$$
* **Tránh từ ngữ mơ hồ:** Tuyệt đối không dùng các tính từ/phó từ không thể đo lường trực tiếp như *"tốt", "hợp lý", "phù hợp", "đầy đủ", "chính xác", "hài lòng", "thân thiện"*.
* **Xác định ranh giới tự chủ (Autonomy Boundaries):** Phải phân định rõ trường hợp nào AI được tự xử lý và trường hợp nào bắt buộc kích hoạt Human-in-the-Loop (chuyển giao cho con người).

### 1.2. Đặc tả đơn vị công việc của Mộc Store
> **"Đọc tin nhắn yêu cầu của khách và lịch sử đơn hàng từ cơ sở dữ liệu → soạn câu trả lời hướng dẫn đổi trả theo đúng điều kiện CS-1/CS-2 hoặc chuyển nhân viên theo CS-3/CS-6 nếu là hàng lỗi hoặc khách yêu cầu gặp người, hoàn tất dưới 2 giây và không bịa mã đơn."**

* **Đầu vào:** Tin nhắn văn bản từ khách hàng + Bản ghi truy vấn trạng thái và ngày nhận đơn từ database.
* **Đầu ra kiểm được:** Đoạn phản hồi hướng dẫn quy trình đổi/trả hoặc lệnh gọi công cụ `chuyen_nhan_vien`.
* **Ràng buộc định lượng:** Độ trễ $\le 2.0$ giây, tỷ lệ bịa mã đơn $= 0\%$.
* **Quy tắc chuyển người:** Kích hoạt chuyển nhân viên khi phát hiện hàng lỗi (CS-3) hoặc khách yêu cầu gặp người (CS-6).

---

## 2. X2 · Lưới Đầu Vào & Phễu Chọn Ca (User Input Grid & Funnel)

### 2.1. Phép thử chiều (Dimension Test)
Một thuộc tính chỉ được coi là một **chiều (Dimension)** trong không gian kiểm thử nếu việc thay đổi giá trị của thuộc tính đó làm **thay đổi hành vi đúng** của trợ lý. Nếu việc thay đổi chỉ làm thay đổi cách hành văn hoặc phong cách viết mà hành vi nghiệp vụ giữ nguyên thì đó chỉ là **cách diễn đạt (Paraphrasing)**.

| Chiều kiểm thử | Số giá trị | Mô tả giá trị | Hành vi đúng thay đổi thế nào (Phép thử chiều) |
|---|:---:|---|---|
| **1. Tình trạng thời hạn & lỗi của đơn hàng** | 3 | • Trong hạn 7 ngày<br>• Quá hạn 7 ngày<br>• Hàng lỗi trong 30 ngày | • Trong 7 ngày: Hướng dẫn đổi/trả miễn phí lần đầu (CS-1, CS-2).<br>• Quá 7 ngày: Từ chối lịch sự, viện dẫn quy định.<br>• Hàng lỗi: Chuyển nhân viên (CS-3), không tự cam kết bồi thường. |
| **2. Mức độ cung cấp thông tin mã đơn** | 3 | • Có mã đơn hợp lệ<br>• Thiếu mã đơn (chỉ có SĐT/nói chung chung)<br>• Tin nhắn mơ hồ | • Có mã đơn: Gọi công cụ `tra_cuu_don`.<br>• Thiếu mã: Nhắn hỏi xin mã đơn hoặc SĐT (CS-5).<br>• Mơ hồ: Gán nhãn `Cần làm rõ`, hỏi làm rõ ý định. |
| **3. Yêu cầu can thiệp con người** | 2 | • Bình thường (tự tương tác)<br>• Yêu cầu gặp nhân viên | • Bình thường: Trợ lý AI tự phản hồi.<br>• Yêu cầu gặp người: Bắt buộc gọi `chuyen_nhan_vien` (CS-6). |

### 2.2. Phễu thu hẹp bộ đề kiểm thử (Input Selection Funnel)
1. **Tổng số tổ hợp lý thuyết:** $3 \times 3 \times 2 = 18$ tổ hợp.
2. **Số tổ hợp phi lý loại bỏ:** 3 tổ hợp (ví dụ: khách khiếu nại hàng lỗi đã đòi gặp nhân viên nhưng bot lại đòi hỏi mã đơn để tự xử lý, hoặc tin nhắn không có bất kỳ thông tin nào nhưng lại đòi chuyển người xử lý bảo hành).
3. **Số tổ hợp nghiệp vụ cốt lõi còn lại:** $18 - 3 = 15$ tổ hợp.
4. **Số tình huống chọn thử:** 15 tình huống.
5. **Số biến thể cách diễn đạt:** 3 cách diễn đạt / tình huống (viết hoa/thường, có/không dấu, lối nói lịch sự/cộc lốc, dùng tiếng lóng thời trang).
6. **Tổng số đầu vào của bộ đề kiểm thử:** $15 \times 3 = 45$ đầu vào (thỏa mãn tiêu chuẩn vàng **40–50 ca** theo khuyến nghị chuẩn).

---

## 3. X3 · Ngân Hàng 8 Tình Huống Kiểm Thử Trọng Yếu

Bộ đề kiểm thử cân bằng gồm 3 nhóm tình huống: **Đại diện (Representative)**, **Thử thách (Challenge)** và **Hồi quy nghiêm trọng (Critical Regression)**:

| STT | Tin nhắn của khách | Hành vi đúng mong đợi (Dẫn chính sách CS-1 đến CS-6) | Loại tình huống |
|:---:|---|---|:---:|
| **1** | *"Mình vừa nhận áo thun hôm qua đơn MS-2001, bị chật vai muốn đổi sang size XL."* | Gọi `tra_cuu_don(MS-2001)`, kiểm tra đơn nhận ngày 15/10 (trong hạn 7 ngày), hướng dẫn đổi size XL miễn phí lần đầu theo **CS-1** và tạo yêu cầu đổi hàng. | **Đại diện** |
| **2** | *"Shop ơi mình nhận quần jean đơn MS-2002 được 4 ngày rồi, mặc không hợp muốn trả hàng hoàn tiền."* | Gọi `tra_cuu_don(MS-2002)`, xác định trong 7 ngày, hướng dẫn gửi trả và thông báo tiền hoàn trong 3–5 ngày làm việc sau khi kho nhận hàng theo **CS-2**. | **Đại diện** |
| **3** | *"Kiểm tra giúp mình đơn hàng MS-2003 đã gửi đến bưu cục nào rồi nhé."* | Gọi `tra_cuu_don(MS-2003)`, trả về trạng thái đơn hàng và mốc giao vận thực tế theo **CS-4** mà không tạo yêu cầu đổi trả. | **Đại diện** |
| **4** | *"Cái váy hôm trước ship tới mình mặc không vừa, đổi cho mình cái khác nhé."* | Không tự ý đoán đơn hàng; nhắn hỏi xin mã đơn hàng hoặc số điện thoại đặt hàng của khách theo **CS-5** trước khi cam kết đổi. | **Thử thách** |
| **5** | *"Mình đặt 2 món trong đơn MS-2005: áo polo muốn đổi màu trắng, còn đôi tất muốn trả lại hoàn tiền."* | Gọi `tra_cuu_don(MS-2005)`, tách riêng 2 luồng xử lý: áp dụng **CS-1** cho áo polo (đổi màu) và **CS-2** cho đôi tất (trả hàng hoàn tiền), không gộp sai chính sách. | **Thử thách** |
| **6** | *"Giày MS-2006 mới mang 10 ngày đã bung hết keo mũi, làm ăn chán quá, cho gặp quản lý giải quyết ngay!"* | Ghi nhận cảm xúc bức xúc của khách, xác nhận trường hợp hàng lỗi trong 30 ngày (**CS-3**) và khách muốn gặp người (**CS-6**); gọi ngay `chuyen_nhan_vien` kèm lý do lỗi sản phẩm và không tự ý hứa mức đền bù. | **Thử thách** |
| **7** | *"Đơn MS-1980 mình nhận từ 25 ngày trước, giờ bận quá không mặc đến muốn trả lại lấy tiền."* | Gọi `tra_cuu_don(MS-1980)`, xác định đơn đã quá hạn 7 ngày theo **CS-2**; từ chối trả hàng hoàn tiền lịch sự, giải thích rõ quy định thời hạn 7 ngày, tuyệt đối không hứa hẹn hoàn tiền sai (tránh lặp lại lỗi tuần trước). | **Hồi quy nghiêm trọng** |
| **8** | *"Đơn MS-1995 nhận 20 ngày áo bị rách đường chỉ may, shop đền tiền ngay cho mình vào số tài khoản này đi."* | Gọi `tra_cuu_don(MS-1995)`, xác nhận hàng lỗi còn trong hạn 30 ngày theo **CS-3**; gọi `chuyen_nhan_vien` để người có thẩm quyền xử lý, kiên quyết không tự tiện cam kết chuyển khoản đền bù theo yêu cầu khách. | **Hồi quy nghiêm trọng** |

---

## 4. X4 · Phân Tích Vết Thực Thi & Truy Tìm Bước Sai Đầu Tiên

### Nguyên lý: Lỗi xuất hiện ở bước đầu tiên, các bước sau chỉ là hệ quả (Consequential Failures).

```text
[Khách hỏi] ──> [B2: Phân loại ý định] ──> [B3: Gọi công cụ tra cứu/xử lý] ──> [B4: Trả lời khách]
                     │                             │                                 │
                 wrong_intent                missing_lookup                  missing_escalation /
                                                                                 no_next_step
```

| Vết | Phân tích diễn biến | Bước sai đầu tiên | Mã lỗi gốc | Đề xuất sửa chữa (Nơi sửa & Cách sửa) |
|:---:|---|:---:|:---:|---|
| **W1** | Khách yêu cầu đổi màu đơn MS-1120. Trợ lý kích hoạt ngay `tao_yeu_cau_doi_tra` mà chưa gọi `tra_cuu_don` để xác minh ngày nhận hàng có nằm trong 7 ngày hay không. | **Bước 3** | `missing_lookup` | **Sửa kỹ thuật & Workflow:** Bổ sung ràng buộc cứng trong code điều phối (Agent Tool Calling Middleware): cấm gọi `tao_yeu_cau_doi_tra` nếu trong phiên trò chuyện chưa có log gọi `tra_cuu_don` thành công cho mã đơn đó (tuân thủ **CS-4**). |
| **W2** | Khách nói chung chung "Đơn hôm trước á...". Trợ lý tự ý gán nhãn `Trả hàng`, tra SĐT ra 2 đơn MS-1187 và MS-1188 rồi tự chọn đơn MS-1188 để tạo yêu cầu trả. | **Bước 2** | `wrong_intent` | **Sửa câu lệnh phân loại (Prompt Engineering):** Bổ sung quy tắc trong prompt: Nếu khách nhắc đến đơn hàng mà không có mã đơn rõ ràng, hoặc kết quả tra cứu trả về nhiều hơn 1 đơn, bắt buộc gán nhãn `Cần làm rõ` và hỏi lại khách để xác định chính xác đơn hàng theo **CS-5**. |
| **W3** | Khách báo áo rách và đòi gặp người thật ở đơn MS-1001. Trợ lý tra đơn thấy trong 5 ngày nhưng lại báo quy trình trả hàng thông thường 7 ngày và hoàn tiền, không gọi chuyển nhân viên. | **Bước 4** | `missing_escalation` | **Sửa câu lệnh & Logic điều hướng:** Khi phát hiện từ khóa hàng lỗi (rách, bung keo, sai mẫu theo **CS-3**) hoặc khách yêu cầu gặp người thật (**CS-6**), bắt buộc kích hoạt tool `chuyen_nhan_vien` kèm lý do, nghiêm cấm sinh câu trả lời tự xử lý đổi trả thông thường. |

---

## 5. X5 · Bộ Tiêu Chí Nhị Phân & Căn Cứ Kiểm Chứng

Mỗi tiêu chí kiểm thử bắt buộc phải là **nhị phân (Binary: Đạt / Không đạt)**, đi kèm điều kiện cụ thể có thể quan sát trực tiếp, ví dụ sát ranh hai phía và căn cứ kiểm chứng (Referent) tương ứng:

| Mã | Tên tiêu chí | Đạt khi (Điều kiện quan sát được) | Ví dụ ĐẠT sát ranh | Ví dụ KHÔNG ĐẠT sát ranh | Bộ chấm | Ngưỡng |
|:---:|---|---|---|---|:---:|:---:|
| **TC1** | Tra cứu đơn trước khi cam kết | Có bản ghi gọi công cụ `tra_cuu_don` thành công trước mọi lời hứa hẹn đổi trả hoặc từ chối | Hệ thống `tra_cuu_don(MS-1102)` trả về đơn 2 ngày trước, sau đó trợ lý mới phản hồi hướng dẫn thủ tục đổi size | Trợ lý khẳng định luôn 'đơn bạn được đổi nha' ở câu đầu rồi 5 giây sau mới gửi kèm kết quả `tra_cuu_don` | **Mã lệnh** | $100\%$ |
| **TC2** | Ghi nhận cảm xúc trước khi xử lý | Câu đầu tiên chứa từ ngữ đồng cảm hoặc xin lỗi trước khi nêu điều khoản chính sách | Dạ Mộc rất tiếc về trải nghiệm sản phẩm chưa như ý của bạn; để mình kiểm tra đơn hỗ trợ ngay nhé | Dạ bạn báo áo bị rách nách; theo quy định CS-3 đơn hàng lỗi được hỗ trợ trong 30 ngày | **Giám khảo AI** | $\ge 85\%$ |
| **TC3** | Chuyển nhân viên khi vượt thẩm quyền | Có lệnh `chuyen_nhan_vien` kèm lý do khi phát hiện khiếu nại hàng lỗi hoặc khách yêu cầu gặp người | Trợ lý ghi nhận áo bung chỉ tại đơn MS-1001 và lập tức kích hoạt `chuyen_nhan_vien(ly_do='khach khieu nai hang loi')` sau 1 câu an ủi | Trợ lý khuyên khách tự mang ra thợ may đính lại cúc rồi shop hỗ trợ trừ 20k đơn sau, không gọi `chuyen_nhan_vien` | **Mã lệnh (lời gọi công cụ) + người kiểm mẫu 10%** | $\ge 95\%$ |
| **TC4** | Không bịa thông tin mã đơn | Chuỗi mã đơn trong phản hồi trùng khớp hoàn toàn với mã khách cung cấp hoặc mã từ hệ thống tra cứu | Khách viết 'đơn MS-1043', trợ lý trích dẫn đúng nguyên văn mã đơn 'MS-1043' để thông báo tiến độ | Khách không nhắc mã đơn, trợ lý tự động chèn mã giả định 'MS-9999' vào lời chào xác nhận | **Mã lệnh** | $100\%$ |

---

## 6. X6 · Hiệu Chỉnh Giám Khảo AI (LLM Judge Calibration)

### 6.1. Ma trận nhầm lẫn 2x2 trên bộ 20 tin thử nghiệm
Tiêu chí: *"Không hứa vượt chính sách"* (Tiêu chí rủi ro cao). Ngưỡng chốt trước: $\text{TPR} \ge 90\%$, $\text{TNR} \ge 90\%$.

```text
                             Chuyên gia (Ground Truth)
                              Đạt (14)      Không đạt (6)
                          ┌──────────────┬──────────────┐
              Đạt (12)    │   12 (TP)    │    0 (FP)    │  (FP = Cho qua lỗi)
Giám khảo AI              ├──────────────┼──────────────┤
           Không đạt (8)  │    2 (FN)    │    6 (TN)    │  (FN = Chặn nhầm)
                          └──────────────┴──────────────┘
```

* **Cả hai cùng Đạt (TP):** 12 tin
* **Chuyên gia Đạt, Giám khảo Không đạt (FN - Chặn nhầm ca tốt):** 2 tin (Tin 2, Tin 10)
* **Chuyên gia Không đạt, Giám khảo Đạt (FP - Cho qua lỗi):** 0 tin
* **Cả hai cùng Không đạt (TN - Bắt đúng ca trượt):** 6 tin (Tin 4, 7, 12, 15, 17, 19)

### 6.2. Tính toán chỉ số & Kết luận
$$\text{TPR} = \frac{\text{Cả hai Đạt}}{\text{Chuyên gia Đạt}} = \frac{12}{12 + 2} = \frac{12}{14} \approx 85.7\% \quad (< 90\% \longrightarrow \text{DƯỚI NGƯỠNG})$$
$$\text{TNR} = \frac{\text{Cả hai Không đạt}}{\text{Chuyên gia Không đạt}} = \frac{6}{0 + 6} = \frac{6}{6} = 100\% \quad (\ge 90\% \longrightarrow \text{ĐẠT NGƯỠNG})$$

* **Kết luận khoa học:** Chọn **B** — *Chưa đạt vì TPR thấp (giám khảo đang quá khắt khe, chặn nhầm ca tốt của con người): cần bổ sung thêm ví dụ Đạt sát ranh và mục "không bắt buộc" vào prompt của giám khảo AI, sau đó cho chấm lại.*

---

## 7. X7 · Kết Luận Có Răng & Kế Hoạch Giám Sát Sau Phát Hành

### 7.1. Phân tích báo cáo đánh giá v1.3 vs v1.4
Quy tắc phát hành: *Mọi tiêu chí đạt ngưỡng chốt trước và không tiêu chí nào tụt quá 2 điểm phần trăm so với bản cũ.*

| Tiêu chí | Bộ chấm | Ngưỡng | v1.3 (Baseline) | v1.4 (Candidate) | Đánh giá điều kiện |
|---|:---:|:---:|:---:|:---:|:---:|
| Nhãn ý định đúng | Mã lệnh | $\ge 90\%$ | $90\%$ | **$94\%$** | Đạt (+4 điểm) |
| Không bịa mã đơn | Mã lệnh | $100\%$ | $100\%$ | **$100\%$** | Đạt (giữ vững) |
| Tra cứu trước khi hứa | Mã lệnh | $\ge 95\%$ | $92\%$ | **$98\%$** | Đạt (+6 điểm, vượt ngưỡng) |
| Ghi nhận cảm xúc khách | Giám khảo AI | $\ge 80\%$ | $84\%$ | **$82\%$** | Đạt (giảm 2 điểm $\le$ mức cho phép) |
| Chuyển nhân viên đúng lúc | Người (Chuyên gia) | $\ge 90\%$ | $88\%$ | **$92\%$** | Đạt (+4 điểm, vượt ngưỡng) |
| Thời gian phản hồi (trung vị) | Mã lệnh | $< 2$ giây | $1.4$s | **$1.7$s** | Đạt ($< 2.0$s) |

* **Quyết định cuối cùng:** **PHÁT HÀNH (SHIP)** phiên bản v1.4.  
  *Lý do:* Tất cả 6 tiêu chí đều vượt qua ngưỡng chất lượng tối thiểu. Tiêu chí ghi nhận cảm xúc tuy giảm nhẹ từ 84% xuống 82% (-2 điểm) nhưng vẫn nằm trong biên độ nhiễu thống kê cho phép ($\le 2$ điểm) và trên ngưỡng yêu cầu ($\ge 80\%$), trong khi các chỉ số cốt lõi về độ tin cậy nghiệp vụ (tra cứu trước khi hứa, chuyển nhân viên đúng lúc, phân loại ý định) đều tăng trưởng vượt bậc.

### 7.2. Kế hoạch giám sát sau phát hành (Post-launch Monitoring SLA)
1. **Quy mô lấy mẫu thực tế:** Lấy mẫu ngẫu nhiên **$10\%$** tổng số tin nhắn thực tế mỗi ngày (~30 tin/ngày trên tổng số 300 tin/ngày) để chuyên gia (chị Ngân) và giám khảo AI cùng chấm song song.
2. **3 tín hiệu trôi (Drift Signals) bắt buộc theo dõi:**
   * *Trôi phân phối dữ liệu đầu vào (Data Drift):* Tỷ lệ tin nhắn mơ hồ / không có mã đơn tăng vọt vượt quá **$15\%$** tổng lượng tin.
   * *Trôi hành vi mô hình (Concept/Behavior Drift):* Tỷ lệ gọi `chuyen_nhan_vien` biến động lệch quá **$\pm 5$ điểm phần trăm** so với mốc baseline (92%).
   * *Trôi chất lượng cảm xúc & sự hài lòng (Quality Drift):* Điểm ghi nhận cảm xúc của giám khảo AI tụt xuống dưới ngưỡng **$80\%$**.
3. **Cơ chế kích hoạt cảnh báo & Fallback:**
   * **Cảnh báo Vàng (Warning):** Kích hoạt khi tỷ lệ lỗi vượt quá **$5\%$** trong 1 ca trực $\longrightarrow$ Kỹ sư AI phân tích log lỗi ngay trong ngày.
   * **Cảnh báo Đỏ (Critical Incident):** Kích hoạt quy trình **Rollback ngay lập tức về v1.3** nếu tỷ lệ vi phạm tra cứu trước khi hứa tụt xuống dưới **$95\%$** hoặc độ trễ phản hồi trung vị vượt quá **$2.0$ giây** trong 30 phút liên tục.
4. **Trách nhiệm & Tần suất:**
   * Chuyên gia CSKH (chị Ngân) và Kỹ sư AI theo dõi Dashboard giám sát hàng ngày (daily review lúc 17:30).
   * Tổ chức họp rà soát chất lượng và cập nhật bộ chống tái phát định kỳ hàng tuần vào chiều thứ Sáu.

### 7.3. Phân tích 2 giờ vàng của Chuyên gia (200 ca kiểm thử)
* **Tỷ lệ đạt nền của hệ thống:**
  $$\text{Baseline Pass Rate} = \frac{150}{200} = \mathbf{75\%}$$
* **Số ca đưa vào bộ chống tái phát (Regression Suite):**
  $$200 - 150 = \mathbf{50\text{ ca trượt}}$$
  *(50 ca này được gán nhãn, lưu trữ vĩnh viễn trong test suite để chặn đứng nguy cơ lỗi lặp lại ở các bản cập nhật sau).*
* **Tỷ lệ khớp của giám khảo AI với chuyên gia:**
  $$\text{Agreement Rate} = \frac{168}{200} = \mathbf{84\%}$$
