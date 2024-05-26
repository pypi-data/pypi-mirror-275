import os
import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


def generate(invoices_path, pdfs_path, image_path, product_id, product_name, amount_purchased, price_per_unit,
             total_price):
    """
    Converts invoice Excel files into PDF invoices.

    :param invoices_path: Path to the directory containing invoice Excel files.
    :param pdfs_path: Path to the directory where PDF invoices will be saved.
    :param image_path: Path to the image file to be included in the PDF.
    :param product_id: Column name for product ID in the Excel file.
    :param product_name: Column name for product name in the Excel file.
    :param amount_purchased: Column name for the amount purchased in the Excel file.
    :param price_per_unit: Column name for the price per unit in the Excel file.
    :param total_price: Column name for the total price in the Excel file.
    """

    # Get all Excel files in the invoices_path directory
    filepaths = glob.glob(f"{invoices_path}/*.xlsx")

    for filepath in filepaths:
        # Create a PDF object
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.add_page()

        # Extract the invoice name and date from the filename
        filename = Path(filepath).stem
        invoice_name, date = filename.split("-")

        # Set title and date on the PDF
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_name}", ln=1)

        pdf.set_font(family="Times", size=15, style="B")
        pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

        # Read the Excel file into a DataFrame
        df = pd.read_excel(filepath, sheet_name="Sheet 1")

        # Create table headers
        pdf.set_font(family="Times", size=10, style="B")
        columns = [product_id, product_name, amount_purchased, price_per_unit, total_price]
        col_headers = [item.replace("_", " ").title() for item in columns]

        for col in col_headers:
            pdf.cell(w=40, h=8, txt=col, border=1, align="C")
        pdf.ln(8)

        # Add table rows
        for index, item in df.iterrows():
            pdf.set_font(family="Times", size=10)
            pdf.set_text_color(80, 80, 80)
            pdf.cell(w=40, h=8, txt=str(item[product_id]), border=1, align="C")
            pdf.cell(w=40, h=8, txt=str(item[product_name]), border=1, align="C")
            pdf.cell(w=40, h=8, txt=str(item[amount_purchased]), border=1, align="C")
            pdf.cell(w=40, h=8, txt=str(item[price_per_unit]), border=1, align="C")
            pdf.cell(w=40, h=8, txt=str(item[total_price]), border=1, align="C")
            pdf.ln(8)

        # Calculate and add the total price
        total = df[total_price].sum()
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=160, h=8, txt="", border=1, align="C")
        pdf.cell(w=40, h=8, txt=f"{total:.2f}", border=1, align="C")
        pdf.ln(8)
        # Add a final total price statement
        pdf.set_font(family="Times", size=10, style="B")
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=200, h=8, txt=f"The total price is {total:.2f}", ln=1)

        # Add image to the PDF
        pdf.image(image_path, x=10, y=pdf.get_y(), w=30)

        # Create the output directory if it does not exist
        if not os.path.exists(pdfs_path):
            os.makedirs(pdfs_path)

        # Save the PDF file
        pdf.output(f"{pdfs_path}/{filename}.pdf")

# Example usage
# generate('invoices_path', 'pdfs_path', 'image_path', 'product_id', 'product_name',
# 'amount_purchased', 'price_per_unit', 'total_price')
