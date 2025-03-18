# Install necessary libraries
!pip install fpdf

# Import required libraries
from fpdf import FPDF
import datetime

# Sample data for vulnerabilities and mitigation recommendations
vulnerabilities = [
    {"type": "SQL Injection", "description": "Injection of malicious SQL code.", "severity": "High", "recommendation": "Use prepared statements and parameterized queries."},
    {"type": "Cross-Site Scripting (XSS)", "description": "Injecting scripts into web pages.", "severity": "Medium", "recommendation": "Implement proper output encoding and input validation."},
    {"type": "Insecure Headers", "description": "Missing security headers in HTTP responses.", "severity": "Low", "recommendation": "Add appropriate security headers like CSP and X-Frame-Options."}
]

# Function to generate vulnerability report as a PDF
def generate_report(vulnerabilities, report_file="vulnerability_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Vulnerability Assessment Report", ln=True, align="C")
    pdf.ln(10)

    # Report Date
    report_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Report Date: {report_date}", ln=True)
    pdf.ln(10)

    # Add vulnerabilities and recommendations
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt="Identified Vulnerabilities:", ln=True)
    pdf.ln(5)

    # Add vulnerability details
    for vuln in vulnerabilities:
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt=f"Vulnerability: {vuln['type']}", ln=True)

        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=f"Description: {vuln['description']}")
        pdf.multi_cell(0, 10, txt=f"Severity: {vuln['severity']}")
        pdf.multi_cell(0, 10, txt=f"Recommendation: {vuln['recommendation']}")
        pdf.ln(10)

    # Save the PDF report
    pdf.output(report_file)
    print(f"Vulnerability report generated and saved as '{report_file}'")

# Generate the report
generate_report(vulnerabilities)
