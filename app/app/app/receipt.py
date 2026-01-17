from fpdf import FPDF
import qrcode

def create_receipt():
    name = input("Аты-жөні: ")
    number = input("Номер: ")
    item = input("Тауар: ")
    amount = input("Сома: ")

    qr = qrcode.make(f"{name} {number} {item} {amount}")
    qr.save("qr.png")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "PayFlow цифрлық чек", ln=True)
    pdf.cell(200, 10, f"Аты: {name}", ln=True)
    pdf.cell(200, 10, f"Номер: {number}", ln=True)
    pdf.cell(200, 10, f"Тауар: {item}", ln=True)
    pdf.cell(200, 10, f"Сома: {amount}", ln=True)

    pdf.image("qr.png", x=10, y=60, w=40)
    pdf.output("receipt.pdf")

    print("Чек дайын ✅ receipt.pdf")
