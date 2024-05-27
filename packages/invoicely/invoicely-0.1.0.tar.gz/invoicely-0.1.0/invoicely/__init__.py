import dataclasses

import reportlab.platypus as pp
import reportlab.lib as rl


@dataclasses.dataclass
class Provider:
    address_line_1: str
    address_line_2: str
    address_line_3: str
    address_line_4: str
    address_line_5: str
    phone: str
    email: str
    vat_number: str


@dataclasses.dataclass
class Customer:
    name: str
    address: str


@dataclasses.dataclass
class Logo:
    path: str
    width: int
    height: int


default_odd_row_bg = rl.colors.Color(red=179/255, green=212/255, blue=252/255,
                                     alpha=0.5)
default_even_row_bg = rl.colors.white


def invoice(filename, provider, customer, logo, invoice_number, invoice_date,
            line_items, line_item_col_widths, invoice_totals,
            odd_row_bg=default_odd_row_bg, even_row_bg=default_even_row_bg):

    width, _ = rl.pagesizes.A4
    margin_size = 0.05 * rl.units.inch
    usable_width = 575.83  # why is this the paragraph width reportlab uses?

    pdf = pp.SimpleDocTemplate(filename, pagesize=rl.pagesizes.A4,
                               leftMargin=margin_size,
                               rightMargin=margin_size, topMargin=margin_size,
                               bottomMargin=margin_size)
    elements = []

    def spacer():
        elements.append(pp.Spacer(1, 0.2 * rl.units.inch))

    img = pp.Image(logo.path, width=logo.width, height=logo.height)
    img.hAlign = 'LEFT'
    elements.append(img)

    spacer()

    styles = rl.styles.getSampleStyleSheet()

    def para(s, alignment=rl.enums.TA_LEFT):
        style = rl.styles.ParagraphStyle(
            name='AlignedStyle',
            parent=styles['Normal'],
            alignment=alignment
        )
        return pp.Paragraph(s, style)

    def bold(s, alignment=rl.enums.TA_LEFT):
        return para(f'<b>{s}</b>', alignment)

    def table_layout(*args, **kwargs):
        table = pp.Table(*args, **kwargs)
        table.setStyle(pp.TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 0)
        ]))
        elements.append(table)

    table_layout(
        [
            [
                bold(provider.address_line_1),
                bold(f'Tel: {provider.phone}', rl.enums.TA_CENTER),
                bold(provider.email, rl.enums.TA_RIGHT)
            ],
            [
                bold(provider.address_line_2), '', ''
            ],
            [
                bold(provider.address_line_3), '', ''
            ],
            [
                bold(provider.address_line_4), '', ''
            ],
            [
                bold(provider.address_line_5), '', ''
            ]
        ]
    )

    spacer()

    table_layout(
        [
            [
                para('<b>Customer Name:</b>'),
                customer.name,
                para('<b>Statement No:</b>'),
                invoice_number
            ],
            [
                para('<b>Address:</b>'),
                customer.address,
                para('<b>Statement Date:</b>'),
                invoice_date
            ],
            [
                '', '', para('<b>VAT No:</b>'), provider.vat_number
            ]
        ],
        colWidths=[
            usable_width * 0.15,
            usable_width * 0.55,
            usable_width * 0.15,
            usable_width * 0.15
        ]
    )

    spacer()

    def data_table(data, col_widths=None, align='CENTER',
                   alternate_row_colours=True, halign=None):
        kwargs = col_widths and {'colWidths': col_widths} or {}
        table = pp.Table(data, **kwargs)
        commands = [
            ('TEXTCOLOR', (0, 0), (-1, 0), rl.colors.black),
            ('ALIGN', (0, 0), (-1, -1), align),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, rl.colors.darkblue)
        ]
        if alternate_row_colours:
            row_colors = [(
                'BACKGROUND',
                (0, row), (-1, row),
                even_row_bg if row % 2 == 0 else odd_row_bg
            ) for row in range(len(line_items))]
            commands.extend(row_colors)
        table.setStyle(pp.TableStyle(commands))
        if halign:
            table.hAlign = halign
        elements.append(table)

    data_table(
        line_items,
        col_widths=[pc * usable_width for pc in line_item_col_widths]
    )

    spacer()

    data_table(invoice_totals, align='RIGHT', alternate_row_colours=False,
               halign='RIGHT')

    pdf.build(elements)
