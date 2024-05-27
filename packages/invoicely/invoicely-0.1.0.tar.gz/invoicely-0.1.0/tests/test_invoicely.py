import fitz
import PIL

import invoicely

filename = 'tests/test_invoice.pdf'
snapshot_filename = 'tests/test_invoice_snapshot_latest.png'
snapshot_baseline = 'tests/test_invoice_snapshot.png'


def compare_images(img1_path, img2_path):
    img1 = PIL.Image.open(img1_path)
    img2 = PIL.Image.open(img2_path)
    diff = PIL.ImageChops.difference(img1, img2)
    if diff.getbbox():
        return False
    return True


def snapshot():
    pdf_document = fitz.open(filename)
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        pix = page.get_pixmap()
        img = PIL.Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
        img.save(snapshot_filename)


def assert_snapshot():
    img1 = PIL.Image.open(snapshot_filename)
    img2 = PIL.Image.open(snapshot_baseline)
    diff = PIL.ImageChops.difference(img1, img2)
    assert diff.getbbox() is None, 'Snapshot does not match baseline'


def test_invoice():
    invoicely.invoice(
        filename=filename,
        provider=invoicely.Provider(
            address_line_1='Address line 1',
            address_line_2='Address line 2',
            address_line_3='Address line 3',
            address_line_4='Address line 4',
            address_line_5='Address line 5',
            phone='01234567890',
            email='test@andycaine.com',
            vat_number='123 234 345'
        ),
        customer=invoicely.Customer(
            name='Test Customer',
            address='Address'
        ),
        logo=invoicely.Logo(
            path='tests/invoicely_100_100.png',
            width=100,
            height=100
        ),
        invoice_number='12345',
        invoice_date='01/05/2024',
        line_items=[
            ['Name', 'Quantity', 'Unit Price', 'Total'],
            ['Foo Clip', '2', '£120.00', '£240.00'],
            ['Flux Capacitor', '1', '£1,234.00', '£1,234.00']
        ],
        line_item_col_widths=[0.5, 0.1, 0.2, 0.2],
        invoice_totals=[
            ['Subtotal', '£1,474'],
            ['VAT (%)', '20%'],
            ['Total VAT', '£284.80'],
            ['Balance', '£1,768.80']
        ]
    )

    snapshot()
    assert_snapshot()
