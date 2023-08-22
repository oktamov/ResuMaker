from io import BytesIO

import pdfkit
from django.core.files.base import ContentFile

path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)


def resumemaker(validated_data):
    first_name = validated_data.pop('first_name')
    last_name = validated_data.pop('last_name')
    birth_year = validated_data.pop('birth_year')
    address = validated_data.pop('address')
    html_content = f"""
        <html>
        <body>
            <h1>Resume</h1>
            <p>Ism: {first_name}</p>
            <p>Familiya: {last_name}</p>
            <p>Tug'ilgan yil: {birth_year}</p>
            <p>Manzil: {address}</p>
        </body>
        </html>
        """

    pdf = pdfkit.from_string(html_content, False, configuration=config)
    buffer = BytesIO(pdf)
    pdf_file_name = f"{first_name} {last_name}.pdf"
    pdf_file = ContentFile(buffer.getvalue(), name=pdf_file_name)
    return pdf_file
