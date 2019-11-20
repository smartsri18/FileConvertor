from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect

from uploads.core.models import Document
from uploads.core.forms import DocumentForm
import markdown
from django.urls import reverse
import datetime

from json import loads
from dicttoxml import dicttoxml
from bs4 import BeautifulSoup


def redirect(request):
    return HttpResponseRedirect(reverse('index'))


# def home(request):
#     documents = Document.objects.all()
#     return render(request, 'core/home.html', { 'documents': documents })


# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'core/simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'core/simple_upload.html')

#assigning global file_name
document_form = ''
file_url = ''
doc_name_split = ''
now = datetime.datetime.utcnow()

def md_to_html(request):
    global document_form
    global doc_name_split
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            document_form = form.cleaned_data['document']
            print(document_form)
            input_file = open("media/documents/{}".format(document_form), mode="r", encoding="utf-8")
            print(input_file)
            text = input_file.read()
            # print(text)
            print("uploaded test.md")
            #markdown conversion
            html = markdown.markdown(text)
            #spliting the file_name
            if document_form:
                # doc_first_name = document_form.splitext('.')[0]
                doc_first_name = document_form.name
                doc_name_split = doc_first_name.split('.')[0]
                print(doc_name_split)

            output_file = open("media/documents/{}.html".format(doc_name_split), "w",
                                      encoding="utf-8",
                                      errors="xmlcharrefreplace"
            )
            output_file.write(html)
            print("created test.html")
            # txt = view()
            key_dict = {'from':text}
            return render(request, 'core/md_to_html.html',context=key_dict)

            # return redirect('md_to_html')
    else:
        form = DocumentForm()
    return render(request, 'core/md_to_html.html', {
        'form': form
    })


def convert_view(request):
    # output_text = open("media/documents/check.html", mode="r", encoding="utf-8")
    # print(output_text)
    # text_out = output_text.read()
    # print(text_out)
    # return text_out
    # t = out_file.read()
    print(doc_name_split)
    global file_url
    file_url = "http://127.0.0.1:8000/media/documents/{}.html".format(doc_name_split)
    print(file_url)
    input_file = open("media/documents/{}".format(document_form), mode="r", encoding="utf-8")
    print("-------------------")
    print(input_file)
    text = input_file.read()
    print(text)
    # print("uploaded test.md")
    # html = markdown.markdown(text)
    #
    output_file = open("media/documents/{}.html".format(doc_name_split), "r",
                              encoding="utf-8",
                              errors="xmlcharrefreplace"
    )
    # output_file.write(html)
    # print(output_file)
    text_out = output_file.read()
    print(text_out)
    # print("created test.html")
    # txt = view()
    form = DocumentForm()
    key_dict = {'form':form,'from':text,'to':text_out,'file_url':file_url}
    return render(request, 'core/md_to_html.html',context=key_dict )


#json_to_xml format conversion function
def json_to_xml(request):
    global document_form
    global doc_name_split
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            document_form = form.cleaned_data['document']
            print(document_form)
            print("*******************")
            input_file = open("media/documents/{}".format(document_form), mode="r", encoding="utf-8")
            print(input_file)
            text = input_file.read()
            # print(text)
            print("uploaded test.json")
            #json to xml conversion
            xml_format = dicttoxml(loads(text),attr_type=False,root=False)
            clean_xml_format=xml_format.decode('utf-8')
            clean_xml_format = BeautifulSoup(xml_format.decode('utf-8'),"html.parser").prettify()
            print(clean_xml_format)
            print("%%%%%%%%%%%%%%%%%%%%%%%%%")
            #spliting the file_name
            if document_form:
                # doc_first_name = document_form.splitext('.')[0]
                doc_first_name = document_form.name
                doc_name_split = doc_first_name.split('.')[0]
                print(doc_name_split)

            output_file = open("media/documents/{}.xml".format(doc_name_split), "w",
                                      encoding="utf-8",
                                      errors="xmlcharrefreplace"
            )
            output_file.write(clean_xml_format)
            print("created test.xml")
            # txt = view()
            key_dict = {'from':text}
            return render(request, 'core/json_to_xml.html',context=key_dict)

            # return redirect('md_to_html')
    else:
        form = DocumentForm()
    return render(request, 'core/json_to_xml.html', {
        'form': form
    })


# convert function from json to xml format
def convert_json_to_xml(request):
    print(doc_name_split)
    global file_url

    # document_form error or bug
    # print("...............................................")
    # print(document_form)
    file_url = "http://127.0.0.1:8000/media/documents/{}.xml".format(doc_name_split)
    print(file_url)
    input_file = open("media/documents/{}".format(document_form), mode="r", encoding="utf-8")
    print("-------------------")
    print(input_file)
    text = input_file.read()
    print(text)
    output_file = open("media/documents/{}.xml".format(doc_name_split), "r",
                              encoding="utf-8",
                              errors="xmlcharrefreplace"
    )
    text_out = output_file.read()
    print(text_out)
    form = DocumentForm()
    key_dict = {'form':form,'from':text,'to':text_out,'file_url':file_url}
    return render(request, 'core/json_to_xml.html',context=key_dict )




import xml.etree.ElementTree as ET
import csv

#xaml_to_csv file format conversion
def xaml_to_csv(request):
    global document_form
    global doc_name_split
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            document_form = form.cleaned_data['document']
            print(document_form)
            input_file = open("media/documents/{}".format(document_form), mode="r", encoding="utf-8")
            print(input_file)
            text = input_file.read()
            input_file.close()
            # print(text)
            print("uploaded test.md")
            #xml_to_csv conversion
            tree = ET.parse("media/documents/{}".format(document_form))
            root = tree.getroot()

            #spliting the file_name
            if document_form:
                # doc_first_name = document_form.splitext('.')[0]
                doc_first_name = document_form.name
                doc_name_split = doc_first_name.split('.')[0]
                print(doc_name_split)

            # open a file for writing

            Resident_data = open("media/documents/{}.csv".format(doc_name_split), 'w')

            # create the csv writer object

            csvwriter = csv.writer(Resident_data)
            resident_head = []

            count = 0
            for member in root.findall('Resident'):
            	resident = []
            	address_list = []
            	if count == 0:
            		name = member.find('Name').tag
            		resident_head.append(name)
            		PhoneNumber = member.find('PhoneNumber').tag
            		resident_head.append(PhoneNumber)
            		EmailAddress = member.find('EmailAddress').tag
            		resident_head.append(EmailAddress)
            		Address = member[3].tag
            		resident_head.append(Address)
            		csvwriter.writerow(resident_head)
            		count = count + 1

            	name = member.find('Name').text
            	resident.append(name)
            	PhoneNumber = member.find('PhoneNumber').text
            	resident.append(PhoneNumber)
            	EmailAddress = member.find('EmailAddress').text
            	resident.append(EmailAddress)
            	Address = member[3][0].text
            	address_list.append(Address)
            	City = member[3][1].text
            	address_list.append(City)
            	StateCode = member[3][2].text
            	address_list.append(StateCode)
            	PostalCode = member[3][3].text
            	address_list.append(PostalCode)
            	resident.append(address_list)
            	csvwriter.writerow(resident)

            Resident_data.close()

            #spliting the file_name
            # if document_form:
            #     # doc_first_name = document_form.splitext('.')[0]
            #     doc_first_name = document_form.name
            #     doc_name_split = doc_first_name.split('.')[0]
            #     print(doc_name_split)

            # output_file = open("media/documents/{}.csv".format(doc_name_split), "w",
            #                           encoding="utf-8",
            #                           errors="xmlcharrefreplace"
            # )
            # output_file.write(html)
            print("created test.html")
            # txt = view()
            key_dict = {'from':text}
            return render(request, 'core/xaml_to_csv.html',context=key_dict)

            # return redirect('md_to_html')
    else:
        form = DocumentForm()
    return render(request, 'core/xaml_to_csv.html', {
        'form': form
    })


# convert function from json to xml format
def convert_xml_to_csv(request):
    print(doc_name_split)
    global file_url

    # document_form error or bug
    # print("...............................................")
    # print(document_form)
    file_url = "http://127.0.0.1:8000/media/documents/{}.xml".format(doc_name_split)
    print(file_url)
    input_file = open("media/documents/{}".format(document_form), mode="r", encoding="utf-8")
    print("-------------------")
    print(input_file)
    text = input_file.read()
    print(text)
    output_file = open("media/documents/{}.csv".format(doc_name_split), "r",
                              encoding="utf-8",
                              errors="xmlcharrefreplace"
    )
    text_out = output_file.read()
    print(text_out)
    form = DocumentForm()
    key_dict = {'form':form,'from':text,'to':text_out,'file_url':file_url}
    return render(request, 'core/xaml_to_csv.html',context=key_dict )
