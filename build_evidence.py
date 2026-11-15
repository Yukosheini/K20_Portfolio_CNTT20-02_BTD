from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from pathlib import Path

out=Path('output'); out.mkdir(exist_ok=True)
d=Document(); sec=d.sections[0]
sec.page_width=Cm(21); sec.page_height=Cm(29.7)
sec.top_margin=Cm(2); sec.bottom_margin=Cm(2); sec.left_margin=Cm(2.3); sec.right_margin=Cm(2)
for name in ['Normal','Title','Heading 1','Heading 2']:
 s=d.styles[name]; s.font.name='Times New Roman'; s.font.size=Pt(11); s.font.color.rgb=RGBColor(0,0,0)
 s.element.rPr.rFonts.set(qn('w:eastAsia'),'Times New Roman')
 s.paragraph_format.space_after=Pt(6); s.paragraph_format.line_spacing=1.15
d.styles['Title'].font.bold=True
d.styles['Heading 1'].paragraph_format.space_before=Pt(10)
d.styles['Heading 2'].paragraph_format.space_before=Pt(6)
def p(t):
 a=d.add_paragraph(t); a.paragraph_format.widow_control=True; return a
def h(t): d.add_paragraph(t,'Heading 1')
def sub(t): d.add_paragraph(t,'Heading 2')
def table(headers, rows, widths):
 t=d.add_table(rows=1, cols=len(headers)); t.autofit=False
 for c,w in zip(t.columns,widths): c.width=Cm(w)
 for c,txt in zip(t.rows[0].cells,headers):
  c.text=txt
  sh=OxmlElement('w:shd'); sh.set(qn('w:fill'),'EDEDED'); c._tc.get_or_add_tcPr().append(sh)
  for r in c.paragraphs[0].runs:r.bold=True
 rep=OxmlElement('w:tblHeader'); t.rows[0]._tr.get_or_add_trPr().append(rep)
 for row in rows:
  cells=t.add_row().cells
  for c,txt in zip(cells,row): c.text=txt
 for row in t.rows:
  no=OxmlElement('w:cantSplit'); row._tr.get_or_add_trPr().append(no)
  for c,w in zip(row.cells,widths):
   c.width=Cm(w); pr=c._tc.get_or_add_tcPr()
   borders=OxmlElement('w:tcBorders')
   for side in ['top','left','bottom','right']:
    b=OxmlElement('w:'+side); b.set(qn('w:val'),'single'); b.set(qn('w:sz'),'4'); b.set(qn('w:color'),'D9D9D9'); borders.append(b)
   pr.append(borders)
   for a in c.paragraphs:
    a.paragraph_format.space_before=Pt(4); a.paragraph_format.space_after=Pt(4)
    a.paragraph_format.line_spacing=1.05
 return t

a=d.add_paragraph('MINH CHỨNG CUỐI BUỔI','Title'); a.alignment=WD_ALIGN_PARAGRAPH.CENTER
a=p('Sử dụng AI hỗ trợ tự học và lập trình website portfolio'); a.alignment=WD_ALIGN_PARAGRAPH.CENTER
p('Họ và tên: Bùi Trung Đức\nLớp: [cần bổ sung]                 Mã sinh viên: [cần bổ sung]\nNgày thực hiện: [cần bổ sung]')
h('1 Bản thảo báo cáo cá nhân')
p('Trong quá trình xây dựng website portfolio, em sử dụng AI để hỗ trợ tìm hiểu kiến thức, phân tích lỗi và đề xuất cách cải tiến. Báo cáo này trình bày cách AI hỗ trợ tư duy, tự học và lập trình nhập môn; đồng thời tập hợp kế hoạch, phản hồi và những thay đổi của sản phẩm. Mục tiêu là từng bước hiểu cách xây dựng website, biết kiểm tra kết quả và sử dụng AI có trách nhiệm.')
sub('AI hỗ trợ phát triển tư duy')
p('AI có thể giúp em chia một vấn đề lớn thành những việc nhỏ để xử lý. Với yêu cầu website hiển thị phù hợp trên điện thoại và máy tính, vấn đề có thể được phân tích riêng thành thanh điều hướng, hình ảnh, nội dung và bảng thời khóa biểu. Việc xác định từng phần giúp em đặt câu hỏi rõ hơn và lựa chọn cách sửa phù hợp.')
p('Em cần yêu cầu AI giải thích nguyên nhân và so sánh các phương án trước khi áp dụng. Chẳng hạn, khi menu che nội dung, cần tìm hiểu vị trí của menu và cách bố trí trang thay vì chỉ thay đổi kích thước chữ. Sau mỗi đề xuất, em cần xem giải pháp có đáp ứng yêu cầu ban đầu và có ảnh hưởng đến phần khác hay không.')
sub('AI hỗ trợ tự học')
p('AI có thể giải thích khái niệm bằng ngôn ngữ đơn giản, đưa ví dụ ngắn và tạo câu hỏi tự kiểm tra. Khi chưa hiểu, em có thể hỏi tiếp vào phần còn vướng, sau đó đối chiếu với tài liệu học tập. Để tránh phụ thuộc, em cần tự tóm tắt kiến thức và thử làm lại một bài tương tự mà không xem ngay đáp án.')
p('Prompt đề xuất cho những lần tự học tiếp theo: “Tôi là sinh viên mới học lập trình web. Hãy giải thích vì sao menu có thể che nội dung trên điện thoại. Đưa ra hai hướng xử lý, nêu ưu điểm và hạn chế của từng hướng. Hãy gợi ý từng bước và đặt câu hỏi để tôi tự chọn phương án trước khi cung cấp mã hoàn chỉnh.”')
sub('AI hỗ trợ lập trình nhập môn')
p('Trong dự án portfolio, AI đã hỗ trợ đề xuất và chỉnh sửa giao diện trên điện thoại, đồng thời xử lý logic thời khóa biểu. Theo lịch sử trao đổi, bản cập nhật đã bổ sung cách xuống dòng cho menu và bỏ qua ô lịch trống để tránh báo nhầm trạng thái đang học. Đây là ví dụ cụ thể về việc dùng AI để phân tích yêu cầu và hỗ trợ sửa lỗi.')
p('Qua dự án, em cần nắm được vai trò của các thành phần: HTML tạo cấu trúc nội dung, CSS định dạng và bố trí trang, JavaScript bổ sung tương tác [2]. Khi nhận mã do AI tạo, em cần đọc từng phần liên quan, xác định điều kiện xử lý và giải thích lại tác dụng của thay đổi. Việc có mã chạy được chưa đủ để khẳng định em đã hiểu cách làm.')

d.add_page_break()
sub('Giới hạn và rủi ro khi sử dụng AI')
p('AI có thể đưa ra thông tin sai, giải thích chưa đầy đủ hoặc tạo mã không phù hợp với dự án. Mã không có lỗi cú pháp vẫn có thể sai logic và hiển thị chưa đúng. Vì vậy, kết quả từ AI cần được đối chiếu với tài liệu và kiểm tra trong tình huống thực tế, đặc biệt ở các trường hợp như lịch trống, trước giờ học và sau giờ học.')
p('Nếu sao chép kết quả mà không hiểu, em sẽ khó tự sửa lỗi và dễ phụ thuộc vào công cụ. Ngoài ra, không nên đưa mật khẩu, mã truy cập hoặc dữ liệu cá nhân không cần thiết vào cuộc trao đổi. Em cần khai báo phần AI hỗ trợ, ghi nguồn tham khảo và không trình bày nội dung AI tạo như kết quả hoàn toàn tự làm. Hướng dẫn của UNESCO nhấn mạnh cách tiếp cận lấy con người làm trung tâm khi sử dụng AI trong giáo dục [1].')
sub('Cách kiểm chứng và kết luận')
p('Quy trình đề xuất là xác định yêu cầu, hỏi AI, đọc lại giải thích, đối chiếu nguồn, chạy thử và ghi nhận kết quả. Nếu kết quả chưa đạt, cần mô tả rõ tình huống lỗi rồi điều chỉnh từng phần. Với giao diện, cần mở website ở các kích thước màn hình khác nhau và chụp ảnh; với logic, cần ghi rõ đầu vào và trạng thái mong đợi.')
p('AI có thể hỗ trợ em học hiệu quả hơn khi được dùng để giải thích, gợi ý và phản hồi. Để phát triển năng lực thực tế, em vẫn cần tự đọc mã, thử thay đổi và giải thích cách làm bằng lời của mình. Những mục chưa có ảnh hoặc kết quả tự kiểm tra sẽ được tiếp tục bổ sung vào hồ sơ minh chứng.')
h('2 Danh mục nguồn và trích dẫn')
p('[1] UNESCO. (2023). Guidance for generative AI in education and research.\nhttps://www.unesco.org/en/articles/guidance-generative-ai-education-and-research')
p('[2] MDN Web Docs. (Không ghi năm). Your first website. Truy cập ngày 04/11/2026.\nhttps://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website')
p('[3] Dự án K20_Portfolio_CNTT20-02_BTD. Bản cập nhật mã nguồn, commit 3632232.\nhttps://github.com/Yukosheini/K20_Portfolio_CNTT20-02_BTD/commit/3632232')
p('Nguồn [1] và [2] được dùng làm tài liệu đối chiếu cho nội dung báo cáo; nguồn [3] là vị trí kiểm tra thay đổi mã. Trước khi nộp, em cần đọc các nguồn và điều chỉnh cách trích dẫn theo yêu cầu của giảng viên.')
h('3 Khai báo sử dụng AI')
p('Em sử dụng ChatGPT/Codex để hỗ trợ phân tích và chỉnh sửa website portfolio, gợi ý cách kiểm tra lỗi, xây dựng bố cục và diễn đạt báo cáo này. Nội dung báo cáo và một phần mã chỉnh sửa có sự hỗ trợ của AI. Em chịu trách nhiệm rà soát thông tin, kiểm tra sản phẩm và điều chỉnh nội dung cho đúng với những việc mình thực sự thực hiện.')
p('Phần em đã tự kiểm tra và có thể giải thích: [cần bổ sung tên chức năng, cách kiểm tra và kết quả thực tế].')

d.add_page_break()
h('4 Kế hoạch và tiến độ đã cập nhật')
table(['Công việc','Tình trạng có căn cứ','Việc tiếp theo'],[
('Xác định vấn đề','Đã có yêu cầu cải thiện giao diện điện thoại và thời khóa biểu.','Đối chiếu lại yêu cầu bài học.'),
('Chỉnh sửa với AI','Đã có bản cập nhật mã trên GitHub.','Tự đọc và giải thích các thay đổi.'),
('Kiểm tra chương trình','Theo báo cáo của trợ lý, kiểm tra cú pháp và 6 tình huống lịch học đã đạt.','Tự chạy lại và lưu kết quả.'),
('Kiểm tra giao diện','Chưa có minh chứng kiểm tra trực tiếp trong phần trao đổi đã đọc.','Kiểm tra trên máy tính, điện thoại; chụp ảnh.'),
('Hoàn thiện báo cáo','Đã có bản thảo theo 6 mục minh chứng.','Bổ sung thông tin, phản hồi và minh chứng thật.')
],[3.1,7,6.6])
p('Thời hạn hoàn thành các việc còn lại: [cần bổ sung theo lịch học].')
h('5 Phản hồi nhận được')
p('Phản hồi từ AI khi rà soát dự án: cần xử lý ô thời khóa biểu trống để tránh thông báo sai; điều chỉnh menu trên điện thoại để hạn chế che nội dung; kiểm tra giao diện trực tiếp vì kiểm tra mã chưa đủ để kết luận website hiển thị tốt.')
p('Cách tiếp thu: bản cập nhật đã xử lý menu và điều kiện kiểm tra lịch học. Phần kiểm tra trực quan vẫn cần thực hiện và lưu ảnh minh chứng. Phản hồi của giảng viên hoặc bạn học: [bổ sung đúng nội dung đã nhận; nếu chưa có, ghi “Chưa nhận được”].')
h('6 Minh chứng nội dung đã cải tiến')
table(['Nội dung','Trước cải tiến','Thay đổi và minh chứng'],[
('Menu điện thoại','Có nguy cơ che nội dung.','Cho phép menu xuống dòng, điều chỉnh vị trí trong bố cục. Có bản cập nhật GitHub; cần bổ sung ảnh kiểm tra.'),
('Thời khóa biểu','Ô trống có thể bị nhận là đang học.','Bỏ qua ô trống khi xác định trạng thái. Có bản cập nhật GitHub; cần bổ sung kết quả tự chạy.'),
('Báo cáo cá nhân','Cần tập hợp nội dung theo yêu cầu cuối buổi.','Tổ chức thành 6 mục, có nguồn, khai báo AI và phần việc còn lại. Minh chứng là bản thảo báo cáo này.')
],[3.1,5,8.6])
p('Hồ sơ cần lưu gồm bản báo cáo mới nhất, danh mục nguồn, khai báo AI, kế hoạch cập nhật, đoạn chat góp ý, liên kết mã nguồn và ảnh kiểm tra thực tế. Chỉ xác nhận đã lưu trên LMS sau khi thực sự tải lên.')
for section in d.sections:
 f=section.footer.paragraphs[0]; f.alignment=WD_ALIGN_PARAGRAPH.CENTER
 r=f.add_run(); fld=OxmlElement('w:fldSimple'); fld.set(qn('w:instr'),'PAGE'); r._r.addnext(fld)
for para in d.paragraphs:
 for r in para.runs: r.font.name='Times New Roman'; r.font.size=Pt(11)
d.core_properties.title='Minh chứng cuối buổi về sử dụng AI trong tự học và lập trình'
d.save(out/'Minh_chung_cuoi_buoi.docx')
print((out/'Minh_chung_cuoi_buoi.docx').resolve())
