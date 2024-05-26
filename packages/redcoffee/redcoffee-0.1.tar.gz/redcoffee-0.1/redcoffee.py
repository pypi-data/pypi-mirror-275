import requests
import logging
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.colors import Color,black,red,yellow,green,lightgrey,orange,seagreen,teal
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
import datetime
import os
import click

def get_reported_issues_by_sonarqube(host_name,auth_token,project_name):
    print("auth token is "+auth_token)
    sqa_headers={"Authorization": "Bearer "+auth_token}
    url_to_hit="http://"+host_name+"/api/issues/search?componentKeys="+project_name+"&resolved=false"
    logging.info("URL that has we are hitting to fetch SonarQube reports are "+url_to_hit)
    response=requests.get(url=url_to_hit,headers=sqa_headers)
    if(response.status_code==200):
        return response
    else:
        print("Status code is "+str(response.status_code))


def get_issues_by_type(response,issue_type):
    component_list=[]
    fix_list=[]
    line_number=[]
    impact=[]

    response_body=response.json()
    for i in range(0,len(response_body["issues"])):
        actual_issue_type=response_body["issues"][i]["type"]
        if(actual_issue_type==issue_type):
            component_list.append(response_body["issues"][i]["component"])
            fix_list.append(response_body["issues"][i]["message"])
            line_number.append(response_body["issues"][i]["line"])
            impact.append(response_body["issues"][i]["impacts"][0]["severity"])
            
        else:
            print("Issue type is not matching")
    return component_list,fix_list,line_number,impact

def draw_severity_icon(severity):
    if severity == "CRITICAL":
        return "<font color='red' size='12'>&#9679;</font>"
    elif severity == "HIGH":
        return "<font color='orange' size='12'>&#9679;</font>"
    elif severity == "MEDIUM":
        return "<font color='teal' size='12'>&#9679;</font>"
    else:  # Low
        return "<font color='green' size='12'>&#9679;</font>"

def create_issues_report(file_path, host_name, auth_token, project_name):
    response = get_reported_issues_by_sonarqube(host_name, auth_token, project_name)
    component_list, fix_list, line_number_list, impact = get_issues_by_type(response, "CODE_SMELL")
    component_list_vulnerability, fix_list_vulnerability, line_number_list_vulnerability, impact_vulnerability = get_issues_by_type(response, "VULNERABILITY")
    component_list.append(component_list_vulnerability)
    fix_list.append(fix_list_vulnerability)
    line_number_list.append(line_number_list_vulnerability)
    impact.append(impact_vulnerability)

    doc = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'title_style',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=16,
        spaceAfter=12,
    )
    subtitle_style = ParagraphStyle(
        'subtitle_style',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=12,
        spaceAfter=8,
    )
    normal_style = ParagraphStyle(
        'normal_style',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=8,
        spaceAfter=8,
        alignment=TA_CENTER
    )
    normal_style_info = ParagraphStyle(
        'normal_style',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10,
        spaceAfter=8
    )
    header_style = ParagraphStyle(
        'header_style',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        textColor=colors.whitesmoke,
        alignment=TA_CENTER
    )

    elements = []

    # Title
    elements.append(Paragraph("SonarQube Vulnerability Tracker", title_style))

    # Project Info
    project_info = f"""
    <b>Project Name:</b> {project_name}<br/>
    <b>Analysis Run On:</b> {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}<br/>
    <b>Branch Name:</b> Main / Master
    """
    elements.append(Paragraph(project_info, normal_style_info))
    elements.append(Spacer(1, 0.2 * inch))

    # Subtitle
    elements.append(Paragraph("List of Issues Detected", subtitle_style))

    # Table headers
    data = [
        [Paragraph("Severity", header_style), 
         Paragraph("Description", header_style), 
         Paragraph("Type", header_style), 
         Paragraph("File Name", header_style), 
         Paragraph("Line No", header_style)]
    ]

    # Table content
    print("Total Issues detected are "+str(len(component_list)))
    for i in range(0,len(component_list)-1):
        print("i is "+str(i))
        severity_icon = draw_severity_icon(impact[i])
        description = fix_list[i]
        file_name = "/".join(component_list[i].split("/")[1:])
        line_number = str(line_number_list[i])

        data.append([
            Paragraph(severity_icon, normal_style),
            Paragraph(description, normal_style),
            Paragraph("CODE SMELL", normal_style),
            Paragraph(file_name, normal_style),
            Paragraph(line_number, normal_style),
        ])

    # Create table
    table = Table(data, colWidths=[0.75 * inch, 3 * inch, 1 * inch, 2.5 * inch, 0.75 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)
    doc.build(elements)



@click.group()
def cli():
    pass



@click.command()
@click.option("--token",help="Setting up SonarQube Global Analysis Token")
def configure(token):
    print("We are setting up the token")
    os.environ["SQA_ANALYSIS_TOKEN"]=token
    print(os.getenv("SQA_ANALYSIS_TOKEN"))

@click.command()
@click.option("--host",help="The host url where SonarQube server is running")
@click.option("--project",help="Name of the Project Key that we want to search for in SonarQube report ")
@click.option("--path",help="Path where we want to the PDF Report")
@click.option("--token",help="SonarQube Global Analysis Token")
def generatepdf(host,project,path,token):
    create_issues_report(path,host,token,project)
    

cli.add_command(configure)
cli.add_command(generatepdf)
if __name__=="__main__":
    cli()
