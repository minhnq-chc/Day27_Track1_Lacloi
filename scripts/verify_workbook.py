import openpyxl
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
wb_path = os.path.join(base_dir, "[Lacloi]_CS12.xlsx")

if not os.path.exists(wb_path):
    raise FileNotFoundError(f"Workbook not found: {wb_path}")

wb = openpyxl.load_workbook(wb_path, data_only=False)

def eval_cell(cond, desc=""):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {desc}")
    if not cond:
        raise AssertionError(f"Check failed: {desc}")

print("=== CHECKING BÀI 1 ===")
ws1 = wb['Bài 1']
eval_cell(abs(ws1['C19'].value - 2) <= 0.01, "1.1: 2")
eval_cell(abs(ws1['C20'].value - 0.84) <= 0.006 or abs(ws1['C20'].value - 84) <= 0.6, "1.2: 84%")
eval_cell(ws1['C21'].value == "Có", "1.3: Có")
eval_cell(abs(ws1['C22'].value - 0.6) <= 0.006 or abs(ws1['C22'].value - 60) <= 0.6, "1.4: 60%")
eval_cell(abs(ws1['C23'].value - 30) <= 0.01, "1.5: 30")
eval_cell(ws1['C24'].value == "B", "1.6: B")
eval_cell(ws1['C25'].value == "Khoảng 1.000 ca", "1.7: Khoảng 1.000 ca")
eval_cell(ws1['C26'].value == "B", "1.8: B")
eval_cell(ws1['C27'].value == "Trục 2", "1.9: Trục 2")

print("\n=== CHECKING BÀI 2 ===")
ws2 = wb['Bài 2']
eval_cell(ws2['C10'].value == "Không", "2.1: Không")
eval_cell(ws2['C11'].value == "Có", "2.2: Có")
eval_cell(ws2['C12'].value == "Không", "2.3: Không")
eval_cell(ws2['C13'].value == "Có", "2.4: Có")
eval_cell(ws2['C14'].value == "Có", "2.5: Có")
eval_cell(ws2['C15'].value == "Không", "2.6: Không")
eval_cell(abs(ws2['C16'].value - 36) <= 0.01, "2.7: 36")
eval_cell(abs(ws2['C17'].value - 24) <= 0.01, "2.8: 24")
eval_cell(abs(ws2['C18'].value - 48) <= 0.01, "2.9: 48")
eval_cell(ws2['C19'].value == "Đại diện", "2.10: Đại diện")
eval_cell(ws2['C20'].value == "Thử thách", "2.11: Thử thách")
eval_cell(ws2['C21'].value == "Thử thách", "2.12: Thử thách")
eval_cell(ws2['C22'].value == "Hồi quy nghiêm trọng", "2.13: Hồi quy nghiêm trọng")
eval_cell(ws2['C23'].value == "B", "2.14: B")

print("\n=== CHECKING BÀI 3 ===")
ws3 = wb['Bài 3']
eval_cell(ws3['C29'].value == 2, "3.1: 2")
eval_cell(ws3['C30'].value == "wrong_intent", "3.2: wrong_intent")
eval_cell(ws3['C31'].value == 3, "3.3: 3")
eval_cell(ws3['C32'].value == "missing_lookup", "3.4: missing_lookup")
eval_cell(ws3['C33'].value == 4, "3.5: 4")
eval_cell(ws3['C34'].value == "missing_escalation", "3.6: missing_escalation")
eval_cell(ws3['C35'].value == 4, "3.7: 4")
eval_cell(ws3['C36'].value == "no_next_step", "3.8: no_next_step")
eval_cell(ws3['C37'].value == "A", "3.9: A")

print("\n=== CHECKING BÀI 4 ===")
ws4 = wb['Bài 4']
eval_cell(ws4['C17'].value == "Thiếu đặc tả → sửa câu lệnh", "4.1: Thiếu đặc tả → sửa câu lệnh")
eval_cell(ws4['C18'].value == "Thiếu năng lực hệ thống → sửa kỹ thuật", "4.2: Thiếu năng lực hệ thống → sửa kỹ thuật")
eval_cell(ws4['C19'].value == "Lúc được lúc không → viết bài đánh giá tự động", "4.3: Lúc được lúc không → viết bài đánh giá tự động")
eval_cell(ws4['C20'].value == "Mã lệnh", "4.4: Mã lệnh")
eval_cell(ws4['C21'].value == "Mã lệnh", "4.5: Mã lệnh")
eval_cell(ws4['C22'].value == "Mã lệnh", "4.6: Mã lệnh")
eval_cell(ws4['C23'].value == "Mã lệnh", "4.7: Mã lệnh")
eval_cell(ws4['C24'].value == "Giám khảo AI", "4.8: Giám khảo AI")
eval_cell(ws4['C25'].value == "Người quyết", "4.9: Người quyết")
eval_cell(ws4['C26'].value == "Đạt · đúng 1 nhãn", "4.10: Đạt · đúng 1 nhãn")
eval_cell(ws4['C27'].value == "Không đạt · không có nhãn hợp lệ", "4.11: Không đạt · không có nhãn hợp lệ")
eval_cell(ws4['C28'].value == "Không đạt · nhiều hơn 1 nhãn", "4.12: Không đạt · nhiều hơn 1 nhãn")
eval_cell(ws4['C29'].value == "B", "4.13: B")
eval_cell(ws4['C30'].value == "Lặp tiếp", "4.14: Lặp tiếp")
eval_cell(ws4['C31'].value == "Sửa câu lệnh", "4.15: Sửa câu lệnh")

print("\n=== CHECKING BÀI 5 ===")
ws5 = wb['Bài 5']
eval_cell(ws5['C25'].value == 8, "5.1: 8")
eval_cell(ws5['C26'].value == 9, "5.2: 9")
eval_cell(ws5['C27'].value == 9, "5.3: 9")
eval_cell(ws5['C28'].value == 7, "5.4: 7")
eval_cell(ws5['C29'].value == 2, "5.5: 2")
eval_cell(ws5['C30'].value == 1, "5.6: 1")
eval_cell(ws5['C31'].value == 2, "5.7: 2")
eval_cell(abs(ws5['C32'].value - 0.875) <= 0.006 or abs(ws5['C32'].value - 87.5) <= 0.6, "5.8: 87.5%")
eval_cell(abs(ws5['C33'].value - 0.5) <= 0.006 or abs(ws5['C33'].value - 50) <= 0.6, "5.9: 50%")
eval_cell(ws5['C34'].value == "B", "5.10: B")
eval_cell(ws5['C35'].value == "Cho qua lỗi", "5.11: Cho qua lỗi")
eval_cell(abs(ws5['C36'].value - 0.4) <= 0.006, "5.12: 0.4")
eval_cell(ws5['C37'].value == 4, "5.13: 4")
eval_cell(ws5['C38'].value == "Có", "5.14: Có")
eval_cell(ws5['C39'].value == "Sai", "5.15: Sai")
eval_cell(ws5['C40'].value == "Sai", "5.16: Sai")
eval_cell(ws5['C41'].value == "Sai", "5.17: Sai")
eval_cell(ws5['C42'].value == "Đúng", "5.18: Đúng")

print("\n=== CHECKING XƯỞNG ===")
ws_x = wb['Xưởng']
# X1 check formula:
c7 = ws_x['C7'].value or ""
len_ok = len(c7) >= 60
arrow_ok = "→" in c7
vague_words = ["tốt", "hợp lý", "phù hợp", "đầy đủ", "chính xác", "hài lòng", "thân thiện"]
vague_found = [w for w in vague_words if w in c7]
eval_cell(len_ok and arrow_ok and not vague_found, f"X1: len={len(c7)}, arrow={arrow_ok}, vague={vague_found}")

# X2 check formula:
c12 = ws_x['C12'].value
c13 = ws_x['C13'].value
c14 = ws_x['C14'].value
c15 = c12 * c13 * c14
c16 = ws_x['C16'].value
c17 = c15 - c16
c18 = ws_x['C18'].value
c19 = ws_x['C19'].value
c20 = c18 * c19
eval_cell(c18 <= c17, f"X2 tình huống <= còn lại: {c18} <= {c17}")
eval_cell(40 <= c20 <= 50, f"X2 số đầu vào: {c20} in [40, 50]")

# X3 check formula:
b_vals = [ws_x[f'B{r}'].value for r in range(25, 33)]
e_vals = [ws_x[f'E{r}'].value for r in range(25, 33)]
count_rep = e_vals.count("Đại diện")
count_chal = e_vals.count("Thử thách")
count_reg = e_vals.count("Hồi quy nghiêm trọng")
eval_cell(len([b for b in b_vals if b]) == 8, f"X3 8 tình huống: {len([b for b in b_vals if b])}")
eval_cell(count_rep > 0 and count_chal > 0 and count_reg > 0, f"X3 đủ 3 loại: rep={count_rep}, chal={count_chal}, reg={count_reg}")
eval_cell(count_chal >= 3, f"X3 >= 3 thử thách: {count_chal}")

# X4 check formula:
eval_cell(ws_x['B56'].value == 3 and ws_x['C56'].value == "missing_lookup", "X4 W1: step=3, code=missing_lookup")
eval_cell(ws_x['B57'].value == 2 and ws_x['C57'].value == "wrong_intent", "X4 W2: step=2, code=wrong_intent")
eval_cell(ws_x['B58'].value == 4 and ws_x['C58'].value == "missing_escalation", "X4 W3: step=4, code=missing_escalation")

# X5 check formula:
x5_cells = [ws_x.cell(r, c).value for r in range(63, 67) for c in range(2, 8)]
x5_empty = [c for c in x5_cells if c is None or str(c).strip() == ""]
c_cols = [ws_x[f'C{r}'].value or "" for r in range(63, 67)]
vague_in_c = [w for w in vague_words for text in c_cols if w in text]
eval_cell(len(x5_empty) == 0, f"X5 không ô trống: {len(x5_cells)} / 24")
eval_cell(len(vague_in_c) == 0, f"X5 không từ mơ hồ trong 'Đạt khi': {vague_in_c}")

# X6 check formula:
f72 = ws_x['F72'].value
f73 = ws_x['F73'].value
f74 = ws_x['F74'].value
f75 = ws_x['F75'].value
tpr = f72 / (f72 + f73)
tnr = f75 / (f74 + f75)
f84 = ws_x['F84'].value
eval_cell(f72 == 12 and f73 == 2 and f74 == 0 and f75 == 6, f"X6 4 ô: 12, 2, 0, 6 (tổng={f72+f73+f74+f75})")
eval_cell(f84 == "B", f"X6 kết luận: {f84} (tpr={tpr:.1%}, tnr={tnr:.1%})")

# X7 check formula:
eval_cell(ws_x['C105'].value == "Phát hành", f"X7 kết luận: {ws_x['C105'].value}")
eval_cell(len(ws_x['C106'].value or "") > 100, f"X7 kế hoạch: {len(ws_x['C106'].value or '')} chars")
eval_cell(abs(ws_x['C110'].value - 0.75) <= 0.006 or abs(ws_x['C110'].value - 75) <= 0.6, f"X7 tỷ lệ đạt nền: {ws_x['C110'].value}")
eval_cell(ws_x['C111'].value == 50, f"X7 chống tái phát: {ws_x['C111'].value}")
eval_cell(abs(ws_x['C112'].value - 0.84) <= 0.006 or abs(ws_x['C112'].value - 84) <= 0.6, f"X7 tỷ lệ khớp: {ws_x['C112'].value}")

print("\n>>> ALL VERIFICATION CHECKS PASSED (100% SUCCESS) <<<")
