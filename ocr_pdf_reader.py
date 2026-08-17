#!/usr/bin/env python3
"""
OCR PDF Reader - Extract text from scanned PDFs using online OCR service
Useful for: Proforma Invoices, Contracts, Scanned Documents, Supplier Quotes

Usage:
    python3 ocr_pdf_reader.py <pdf_file> [output_file]

Example:
    python3 ocr_pdf_reader.py "PI to Silky Express.pdf" "extracted_text.txt"
"""

import sys
import subprocess
import time
from pathlib import Path


def open_ocr_in_browser(pdf_file):
    """Open online OCR service in browser and guide user through extraction"""

    pdf_path = Path(pdf_file).resolve()

    if not pdf_path.exists():
        print(f"❌ Error: File not found: {pdf_path}")
        sys.exit(1)

    print(f"\n📄 PDF OCR Reader")
    print(f"File: {pdf_path.name}")
    print(f"Size: {pdf_path.stat().st_size / 1024:.1f} KB")
    print(f"\n⚙️  Opening online OCR service in your browser...")
    print(f"Steps:")
    print(f"  1. Upload the PDF: {pdf_path.name}")
    print(f"  2. Click 'Convert File'")
    print(f"  3. Click 'Copy' to copy the extracted text")
    print(f"  4. Paste the text into the output file\n")

    # Open www.onlineocr.net in the default browser
    ocr_url = "https://www.onlineocr.net/"
    try:
        if sys.platform == "darwin":  # macOS
            subprocess.run(["open", ocr_url], check=True)
        elif sys.platform == "linux":
            subprocess.run(["xdg-open", ocr_url], check=True)
        elif sys.platform == "win32":  # Windows
            subprocess.run(["start", ocr_url], check=True)
        else:
            print(f"❓ Please manually visit: {ocr_url}")
            print(f"Then upload: {pdf_path}")
    except Exception as e:
        print(f"⚠️  Could not open browser: {e}")
        print(f"Please manually visit: {ocr_url}")


def create_markdown_template(pdf_name):
    """Create a template markdown file for organizing extracted data"""

    template = f"""# {pdf_name.replace('.pdf', '')} - Extracted Data

**Source File:** {pdf_name}
**Extraction Date:** {time.strftime('%Y-%m-%d')}
**Extracted Via:** Online OCR

---

## Document Information

### Supplier/Issuer
- **Company:**
- **Address:**
- **Contact:**

### Recipient
- **Company:** Silky Express
- **Contact:**

---

## Key Details

### Invoice/Document Number
- **Number:**
- **Issue Date:**
- **Due Date:**

### Financial Information
- **Total Amount:**
- **Currency:** USD
- **Payment Terms:**

---

## Products/Items

| Item | Quantity | Unit Price | Total |
|------|----------|-----------|-------|
|  |  |  |  |

---

## Shipping Details

### Shipping Terms
- **Incoterm:** (e.g., FOB, CIF, Ex Works)
- **Port of Origin:**
- **Destination:**
- **Partial Shipment:**
- **Insurance:**

### Timeline
- **Production Timeline:**
- **Shipping Timeline:**
- **Delivery Expected:**

---

## Next Steps for Siva
- [ ] Confirm destination port
- [ ] Calculate freight costs
- [ ] Get insurance quote
- [ ] Provide total landed cost estimate
"""

    return template


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 ocr_pdf_reader.py <pdf_file> [output_file]")
        print("\nExample:")
        print("  python3 ocr_pdf_reader.py 'invoice.pdf' 'extracted_data.md'")
        sys.exit(1)

    pdf_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else pdf_file.replace(".pdf", "_extracted.md")

    # Open OCR service
    open_ocr_in_browser(pdf_file)

    # Create template
    template = create_markdown_template(Path(pdf_file).name)

    with open(output_file, "w") as f:
        f.write(template)

    print(f"✅ Template created: {output_file}")
    print(f"📋 Fill in the extracted data in this file\n")
