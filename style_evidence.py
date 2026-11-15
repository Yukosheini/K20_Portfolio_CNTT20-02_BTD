from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from pathlib import Path

src=Path('C:/Users/ADMIN/Documents/Minh_chung_cuoi_buoi.docx')
dst=Path('output/Minh_chung_cuoi_buoi_thiet_ke.docx')
d=Document(src)
original=[p.text for p in d.paragraphs]
for s in d.styles:
 if s.type==1:
  s.font.name='Times New Roman'; s.font.size=Pt(11)
  s.font.color.rgb=RGBColor.from_string('000000')
  s.element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'),'Times New Roman')
  for el in list(s.element.xpath('.//w:pBdr')): el.getparent().remove(el)
for p in d.paragraphs:
 pf=p.paragraph_format; pf.line_spacing=1.15; pf.space_after=Pt(6)
 for el in list(p._p.xpath('./w:pPr/w:pBdr')): el.getparent().remove(el)
 for r in p.runs:
  r.font.name='Times New Roman'; r.font.size=Pt(11); r.font.color.rgb=RGBColor(0,0,0)
 if p.style.name=='Title':
  pf.space_before=Pt(8); pf.space_after=Pt(10); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
  for r in p.runs:
   r.bold=True
   sp=OxmlElement('w:spacing'); sp.set(qn('w:val'),'24'); r._r.get_or_add_rPr().append(sp)
 elif p.style.name.startswith('Heading'):
  pf.keep_with_next=True; pf.space_before=Pt(10); pf.space_after=Pt(5)
  for r in p.runs:r.bold=True
 elif p.text and p!=d.paragraphs[1]:
  pf.widow_control=True
  if len(p.text)>200:p.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY
for r in d.paragraphs[1].runs:r.italic=True
d.paragraphs[1].paragraph_format.space_after=Pt(12)
meta=d.paragraphs[2]
meta.paragraph_format.line_spacing=1.3
for r in meta.runs:
 if r.text.strip() in ['Họ và tên:','Lớp:','Mã sinh viên:','Ngày thực hiện:']:r.bold=True
for t in d.tables:
 for i,row in enumerate(t.rows):
  for c in row.cells:
   c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
   pr=c._tc.get_or_add_tcPr()
   for el in list(pr.findall(qn('w:shd'))):pr.remove(el)
   sh=OxmlElement('w:shd'); sh.set(qn('w:fill'),'29465B' if i==0 else ('F1F5F8' if i%2 else 'FFFFFF')); pr.append(sh)
   mar=OxmlElement('w:tcMar')
   for side,val in [('top','75'),('bottom','75'),('left','95'),('right','95')]:
    e=OxmlElement('w:'+side);e.set(qn('w:w'),val);e.set(qn('w:type'),'dxa');mar.append(e)
   pr.append(mar)
   for p in c.paragraphs:
    p.paragraph_format.space_before=Pt(0);p.paragraph_format.space_after=Pt(0);p.paragraph_format.line_spacing=1.05
    for r in p.runs:
     r.font.name='Times New Roman';r.font.size=Pt(11);r.font.color.rgb=RGBColor.from_string('FFFFFF' if i==0 else '000000');r.bold=(i==0)
for sec in d.sections:
 sec.header_distance=Cm(.85);sec.footer_distance=Cm(.85)
 hp=sec.header.paragraphs[0];hp.text='BÙI TRUNG ĐỨC  /  HỒ SƠ MINH CHỨNG HỌC TẬP'
 for r in hp.runs:r.font.name='Times New Roman';r.font.size=Pt(11);r.font.color.rgb=RGBColor(0,0,0)
 fp=sec.footer.paragraphs[0];fp.clear();fp.alignment=WD_ALIGN_PARAGRAPH.RIGHT
 r=fp.add_run('MINH CHỨNG CUỐI BUỔI   •   ');r.font.name='Times New Roman';r.font.size=Pt(11);r.font.color.rgb=RGBColor.from_string('526878')
 field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');fp._p.append(field)
assert original==[p.text for p in d.paragraphs]
d.save(dst)
print(dst.resolve())
