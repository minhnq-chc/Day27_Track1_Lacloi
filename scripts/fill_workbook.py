import openpyxl
import sys
import os
import shutil

sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_file = os.path.join(base_dir, "CS12_BaiTap_HocVien.xlsx")
dst_file = os.path.join(base_dir, "[Lacloi]_CS12.xlsx")

if not os.path.exists(src_file):
    raise FileNotFoundError(f"Source file not found: {src_file}")

shutil.copyfile(src_file, dst_file)
wb = openpyxl.load_workbook(dst_file)

# 1. BÀI 1
ws1 = wb['Bài 1']
ws1['C19'] = 2
ws1['C20'] = 0.84
ws1['C21'] = 'Có'
ws1['C22'] = 0.60
ws1['C23'] = 30
ws1['C24'] = 'B'
ws1['C25'] = 'Khoảng 1.000 ca'
ws1['C26'] = 'B'
ws1['C27'] = 'Trục 2'

# 2. BÀI 2
ws2 = wb['Bài 2']
ws2['C10'] = 'Không'
ws2['C11'] = 'Có'
ws2['C12'] = 'Không'
ws2['C13'] = 'Có'
ws2['C14'] = 'Có'
ws2['C15'] = 'Không'
ws2['C16'] = 36
ws2['C17'] = 24
ws2['C18'] = 48
ws2['C19'] = 'Đại diện'
ws2['C20'] = 'Thử thách'
ws2['C21'] = 'Thử thách'
ws2['C22'] = 'Hồi quy nghiêm trọng'
ws2['C23'] = 'B'

# 3. BÀI 3
ws3 = wb['Bài 3']
ws3['C29'] = 2
ws3['C30'] = 'wrong_intent'
ws3['C31'] = 3
ws3['C32'] = 'missing_lookup'
ws3['C33'] = 4
ws3['C34'] = 'missing_escalation'
ws3['C35'] = 4
ws3['C36'] = 'no_next_step'
ws3['C37'] = 'A'

# 4. BÀI 4
ws4 = wb['Bài 4']
ws4['C17'] = 'Thiếu đặc tả → sửa câu lệnh'
ws4['C18'] = 'Thiếu năng lực hệ thống → sửa kỹ thuật'
ws4['C19'] = 'Lúc được lúc không → viết bài đánh giá tự động'
ws4['C20'] = 'Mã lệnh'
ws4['C21'] = 'Mã lệnh'
ws4['C22'] = 'Mã lệnh'
ws4['C23'] = 'Mã lệnh'
ws4['C24'] = 'Giám khảo AI'
ws4['C25'] = 'Người quyết'
ws4['C26'] = 'Đạt · đúng 1 nhãn'
ws4['C27'] = 'Không đạt · không có nhãn hợp lệ'
ws4['C28'] = 'Không đạt · nhiều hơn 1 nhãn'
ws4['C29'] = 'B'
ws4['C30'] = 'Lặp tiếp'
ws4['C31'] = 'Sửa câu lệnh'

# 5. BÀI 5
ws5 = wb['Bài 5']
ws5['C25'] = 8
ws5['C26'] = 9
ws5['C27'] = 9
ws5['C28'] = 7
ws5['C29'] = 2
ws5['C30'] = 1
ws5['C31'] = 2
ws5['C32'] = 0.875
ws5['C33'] = 0.50
ws5['C34'] = 'B'
ws5['C35'] = 'Cho qua lỗi'
ws5['C36'] = 0.40
ws5['C37'] = 4
ws5['C38'] = 'Có'
ws5['C39'] = 'Sai'
ws5['C40'] = 'Sai'
ws5['C41'] = 'Sai'
ws5['C42'] = 'Đúng'

# 6. XƯỞNG
ws_x = wb['Xưởng']
# Thông tin nhóm dòng 3 (C3:G3 merged):
ws_x['C3'] = 'Nhóm Lạc Lối: Ninh Quang Minh (NT - 2A202602432), Trần Phạm Thái Vũ (2A202602695), Đinh Trường An (2A202602393), Hoàng Anh Tài (2A202602612), Nguyễn Anh Dũng (2A202602554)'

# X1:
ws_x['C7'] = 'Đọc tin nhắn yêu cầu của khách và lịch sử đơn hàng từ cơ sở dữ liệu → soạn câu trả lời hướng dẫn đổi trả theo đúng điều kiện CS-1/CS-2 hoặc chuyển nhân viên theo CS-3/CS-6 nếu là hàng lỗi hoặc khách yêu cầu gặp người, hoàn tất dưới 2 giây và không bịa mã đơn.'

# X2:
ws_x['B12'] = 'Tình trạng thời hạn và lỗi của đơn hàng'
ws_x['C12'] = 3
ws_x['D12'] = 'Trong 7 ngày cho đổi/trả miễn phí lần đầu (CS-1, CS-2); quá 7 ngày từ chối; hàng lỗi trong 30 ngày gọi chuyen_nhan_vien (CS-3)'

ws_x['B13'] = 'Mức độ cung cấp thông tin mã đơn'
ws_x['C13'] = 3
ws_x['D13'] = 'Có mã đơn thì gọi tra_cuu_don; thiếu mã đơn thì hỏi xin mã đơn/SĐT (CS-5); tin nhắn mơ hồ thì yêu cầu làm rõ thông tin'

ws_x['B14'] = 'Yêu cầu can thiệp con người'
ws_x['C14'] = 2
ws_x['D14'] = 'Khách trao đổi bình thường thì bot giải quyết; khách khiếu nại gay gắt đòi gặp người thì bắt buộc gọi chuyen_nhan_vien (CS-6)'

ws_x['C16'] = 3
ws_x['C18'] = 15
ws_x['C19'] = 3

# X3: 8 tình huống
situations = [
    (1, "Mình vừa nhận áo thun hôm qua đơn MS-2001, bị chật vai muốn đổi sang size XL.",
     "Gọi tra_cuu_don(MS-2001), kiểm tra đơn nhận ngày 15/10 (trong hạn 7 ngày), hướng dẫn đổi size XL miễn phí lần đầu theo CS-1 và tạo yêu cầu đổi hàng.",
     "Đại diện"),
    (2, "Shop ơi mình nhận quần jean đơn MS-2002 được 4 ngày rồi, mặc không hợp muốn trả hàng hoàn tiền.",
     "Gọi tra_cuu_don(MS-2002), xác định trong 7 ngày, hướng dẫn gửi trả và thông báo tiền hoàn trong 3–5 ngày làm việc sau khi kho nhận hàng theo CS-2.",
     "Đại diện"),
    (3, "Kiểm tra giúp mình đơn hàng MS-2003 đã gửi đến bưu cục nào rồi nhé.",
     "Gọi tra_cuu_don(MS-2003), trả về trạng thái đơn hàng và mốc giao vận thực tế theo CS-4 mà không tạo yêu cầu đổi trả.",
     "Đại diện"),
    (4, "Cái váy hôm trước ship tới mình mặc không vừa, đổi cho mình cái khác nhé.",
     "Không tự ý đoán đơn hàng; nhắn hỏi xin mã đơn hàng hoặc số điện thoại đặt hàng của khách theo CS-5 trước khi cam kết đổi.",
     "Thử thách"),
    (5, "Mình đặt 2 món trong đơn MS-2005: áo polo muốn đổi màu trắng, còn đôi tất muốn trả lại hoàn tiền.",
     "Gọi tra_cuu_don(MS-2005), tách riêng 2 luồng xử lý: áp dụng CS-1 cho áo polo (đổi màu) và CS-2 cho đôi tất (trả hàng hoàn tiền), không gộp sai chính sách.",
     "Thử thách"),
    (6, "Giày MS-2006 mới mang 10 ngày đã bung hết keo mũi, làm ăn chán quá, cho gặp quản lý giải quyết ngay!",
     "Ghi nhận cảm xúc bức xúc của khách, xác nhận trường hợp hàng lỗi trong 30 ngày (CS-3) và khách muốn gặp người (CS-6); gọi ngay chuyen_nhan_vien kèm lý do lỗi sản phẩm và không tự ý hứa mức đền bù.",
     "Thử thách"),
    (7, "Đơn MS-1980 mình nhận từ 25 ngày trước, giờ bận quá không mặc đến muốn trả lại lấy tiền.",
     "Gọi tra_cuu_don(MS-1980), xác định đơn đã quá hạn 7 ngày theo CS-2; từ chối trả hàng hoàn tiền lịch sự, giải thích rõ quy định thời hạn 7 ngày, tuyệt đối không hứa hẹn hoàn tiền sai (tránh lặp lại lỗi tuần trước).",
     "Hồi quy nghiêm trọng"),
    (8, "Đơn MS-1995 nhận 20 ngày áo bị rách đường chỉ may, shop đền tiền ngay cho mình vào số tài khoản này đi.",
     "Gọi tra_cuu_don(MS-1995), xác nhận hàng lỗi còn trong hạn 30 ngày theo CS-3; gọi chuyen_nhan_vien để người có thẩm quyền xử lý, kiên quyết không tự tiện cam kết chuyển khoản đền bù theo yêu cầu khách.",
     "Hồi quy nghiêm trọng")
]

for idx, (num, msg, expected, stype) in enumerate(situations, start=25):
    ws_x[f'B{idx}'] = msg
    ws_x[f'C{idx}'] = expected
    ws_x[f'E{idx}'] = stype

# X4: Đọc 3 vết thực thi mới
ws_x['B56'] = 3
ws_x['C56'] = 'missing_lookup'
ws_x['D56'] = 'Bổ sung ràng buộc trong câu lệnh và workflow hệ thống: bắt buộc gọi công cụ tra_cuu_don kiểm tra ngày nhận và trạng thái đơn trước khi kích hoạt tao_yeu_cau_doi_tra theo đúng quy định CS-4.'

ws_x['B57'] = 2
ws_x['C57'] = 'wrong_intent'
ws_x['D57'] = 'Sửa câu lệnh phân loại ý định: tin nhắn thiếu mã đơn hoặc chưa rõ đơn cụ thể phải gán nhãn Cần làm rõ và hỏi lại mã đơn hoặc xác nhận số điện thoại theo CS-5, cấm tự ý chọn 1 trong các đơn tìm thấy.'

ws_x['B58'] = 4
ws_x['C58'] = 'missing_escalation'
ws_x['D58'] = 'Sửa câu lệnh và logic điều hướng: khi tin nhắn có dấu hiệu hàng lỗi (CS-3) hoặc khách yêu cầu gặp người thật (CS-6), hệ thống bắt buộc phải gọi công cụ chuyen_nhan_vien kèm tóm tắt ngữ cảnh, nghiêm cấm tự hứa đổi trả thông thường.'

# X5: 4 tiêu chí nhị phân
criteria = [
    (63, "Tra cứu đơn trước khi cam kết",
     "Đạt khi có bản ghi gọi công cụ tra_cuu_don thành công trước mọi lời hứa hẹn đổi trả hoặc từ chối",
     "Hệ thống tra_cuu_don(MS-1102) trả về đơn 2 ngày trước, sau đó trợ lý mới phản hồi hướng dẫn thủ tục đổi size",
     "Trợ lý khẳng định luôn 'đơn bạn được đổi nha' ở câu đầu rồi 5 giây sau mới gửi kèm kết quả tra_cuu_don",
     "Mã lệnh", "100%"),
    (64, "Ghi nhận cảm xúc trước khi xử lý",
     "Đạt khi câu đầu tiên chứa từ ngữ đồng cảm hoặc xin lỗi trước khi nêu điều khoản chính sách",
     "Dạ Mộc rất tiếc về trải nghiệm sản phẩm chưa như ý của bạn; để mình kiểm tra đơn hỗ trợ ngay nhé",
     "Dạ bạn báo áo bị rách nách; theo quy định CS-3 đơn hàng lỗi được hỗ trợ trong 30 ngày",
     "Giám khảo AI", "≥ 85%"),
    (65, "Chuyển nhân viên khi vượt thẩm quyền",
     "Đạt khi có lệnh chuyen_nhan_vien kèm lý do khi phát hiện khiếu nại hàng lỗi hoặc khách yêu cầu gặp người",
     "Trợ lý ghi nhận áo bung chỉ tại đơn MS-1001 và lập tức kích hoạt chuyen_nhan_vien(ly_do='khach khieu nai hang loi') sau 1 câu an ủi",
     "Trợ lý khuyên khách tự mang ra thợ may đính lại cúc rồi shop hỗ trợ trừ 20k đơn sau, không gọi chuyen_nhan_vien",
     "Mã lệnh (lời gọi công cụ) + người kiểm mẫu 10%", "≥ 95%"),
    (66, "Không bịa thông tin mã đơn",
     "Đạt khi chuỗi mã đơn trong phản hồi trùng khớp hoàn toàn với mã khách cung cấp hoặc mã từ hệ thống tra cứu",
     "Khách viết 'đơn MS-1043', trợ lý trích dẫn đúng nguyên văn mã đơn 'MS-1043' để thông báo tiến độ",
     "Khách không nhắc mã đơn, trợ lý tự động chèn mã giả định 'MS-9999' vào lời chào xác nhận",
     "Mã lệnh", "100%")
]

for row_idx, name, pass_cond, pass_ex, fail_ex, grader, threshold in criteria:
    ws_x[f'B{row_idx}'] = name
    ws_x[f'C{row_idx}'] = pass_cond
    ws_x[f'D{row_idx}'] = pass_ex
    ws_x[f'E{row_idx}'] = fail_ex
    ws_x[f'F{row_idx}'] = grader
    ws_x[f'G{row_idx}'] = threshold

# X6: Hiệu chỉnh giám khảo
ws_x['F72'] = 12
ws_x['F73'] = 2
ws_x['F74'] = 0
ws_x['F75'] = 6
ws_x['F84'] = 'B'

# X7: Kết luận có răng
ws_x['C105'] = 'Phát hành'
ws_x['C106'] = 'Lấy mẫu ngẫu nhiên 10% tin thật hàng ngày (~30 tin/ngày) để chuyên gia và giám khảo AI cùng chấm song song. Theo dõi sát 3 tín hiệu trôi: (1) Tỷ lệ tin nhắn mơ hồ tăng vượt 15% (Data Drift); (2) Tỷ lệ gọi chuyen_nhan_vien biến động lệch quá ±5 điểm % so với mốc 92% (Concept Drift); (3) Điểm ghi nhận cảm xúc tụt dưới ngưỡng 80% (Quality Drift). Kích hoạt cảnh báo vàng khi tỷ lệ lỗi vượt 5%/ca trực; cảnh báo đỏ kích hoạt Rollback về v1.3 nếu tra cứu trước khi hứa dưới 95% hoặc thời gian phản hồi vượt 2.0s trong 30 phút liên tục. Chuyên gia CSKH (chị Ngân) và Kỹ sư AI theo dõi Dashboard hàng ngày lúc 17:30 và họp rà soát chất lượng hàng tuần vào thứ Sáu.'

ws_x['C110'] = 0.75
ws_x['C111'] = 50
ws_x['C112'] = 0.84

wb.save(dst_file)
print("Saved filled workbook to:", dst_file)
