import qrcode
from io import BytesIO

def generate_qr(data):
    qr = qrcode.make(str(data))
    output = BytesIO()
    qr.save(output, format="PNG")
    return output.getvalue()
