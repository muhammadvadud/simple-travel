from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from core.apps.tickets.models.tickets import TicketorderModel
from django.shortcuts import get_object_or_404
import random

pdfmetrics.registerFont(TTFont("DejaVuSans", "resources/fonts/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", "resources/fonts/DejaVuSans-Bold.ttf"))


def get_section_titles(lang):
    titles = {
        "uz": ["Sana", "Yo‘ldoshlar", "Turlar paketi", "Xizmatlar", "Qo‘shimcha xizmatlar"],
        "ru": ["Дата", "Попутчики", "Турпакет", "Услуги", "Дополнительные услуги"],
        "en": ["Date", "Companions", "Tour Package", "Services", "Additional Services"],
    }
    return titles.get(lang, titles["uz"])


def create_tour_pdf(file_name, base_info, services_data, companions, lang):
    section_titles = get_section_titles(lang)

    pdf = SimpleDocTemplate(file_name, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='TitleCenter', fontName='DejaVuSans-Bold', fontSize=16, alignment=1))
    styles.add(ParagraphStyle(name='NormalUnicode', fontName='DejaVuSans', fontSize=10))

    order_code = f"{random.randint(0, 9999):04d}"
    title_text = {
        "uz": "Турпакет маълумотлари",
        "ru": "Информация о турпакете",
        "en": "Tour Package Information"
    }[lang]

    elements.append(Paragraph(f"{title_text} (ID: {order_code})", styles['TitleCenter']))
    elements.append(Spacer(1, 12))

    data = base_info.copy()

    data.append(["", ""])
    section_label = {
        "uz": "Yo‘ldoshlar",
        "ru": "Попутчики",
        "en": "Companions"
    }[lang]
    data.append([section_label, ""])
    for i, companion in enumerate(companions, start=1):
        data.append([f"{section_label[:-1]} {i}", companion])

    for section_title, section_items in services_data.items():
        data.append(["", ""])
        data.append([section_title, ""])
        for name, price in section_items:
            data.append([name, price])

    table = Table(data, colWidths=[180, 350])

    style = TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'DejaVuSans'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.3, colors.grey),
    ])

    # Bo‘limlar fonini qo‘llash
    for i, row in enumerate(data):
        if row[0] in section_titles:
            style.add('BACKGROUND', (0, i), (-1, i), colors.lightgrey)
            style.add('FONTNAME', (0, i), (-1, i), 'DejaVuSans-Bold')

    table.setStyle(style)
    elements.append(table)
    pdf.build(elements)


def creator_pdf(order_id, lang='uz'):
    order = get_object_or_404(TicketorderModel, pk=order_id)
    hotel = getattr(order.ticket, "hotel", None)
    animates = getattr(order.ticket, "animates", None)
    if animates:
        try:
            features = ", ".join(a.name for a in animates.all())
        except:
            features = str(animates.name)
    else:
        features = "—"

    base_info = [
        ["Sana", ""],
        ["Qayerdan", order.departure],
        ["Qayerga", order.destination],
        ["Jo‘nash vaqti", str(order.departure_date)],
        ["Qaytish vaqti", str(order.arrival_time)],
        ["", ""],
        ["Turlar paketi", order.ticket.title],
        ["Mehmonxona", hotel.name if hotel else "—"],
        ["Joylashuv", order.ticket.location_name],
        ["Reyting", f"{hotel.rating}/5 yulduz" if hotel and hotel.rating else "—"],
        ["Xususiyatlar", features],
        ["Paket turi", order.tariff],
        ["Transport", order.transport],
    ]
    companions = []
    participants = order.participant.all()

    if participants.exists():
        for p in participants:
            full_name = f"{p.first_name} {p.last_name}".strip()
            companions.append(full_name)
    else:
        companions.append("Yo‘ldoshlar mavjud emas")

    services_data = {}

    extra_services = order.extra_service.all()
    if extra_services.exists():
        services_data["Xizmatlar"] = [
            (s.name, f"-") for s in extra_services
        ]

    extra_paid_services = order.extra_paid_service.all()
    if extra_paid_services.exists():
        services_data["Qo‘shimcha xizmatlar"] = [
            (s.name, f"+{s.price:,} sum") for s in extra_paid_services
        ]

    file_name = f"resources/media/order_pdf/{order.user.first_name}_{order.ticket.title}_{order.id}.pdf"
    create_tour_pdf(file_name, base_info, services_data, companions, lang)
    return file_name
