from pypdf import PdfReader , PdfWriter
reader = PdfReader(r"check.pdf")
pdf_name = input("Enter pdf name ")

length = len(reader.pages)
print(length) 
for i in range(0,length):
    page = reader.pages[i] # in reader.pages pages is stored like in array at index
    print(f"Text from page no of {pdf_name}.{i+1} is :- ")
    print(page.extract_text(extraction_mode="layout"))
    # 1st page ,1st index 2nd page so loop is used
    # by using extraction mode it wil print with same sapces as in pdf 

    no = 0

    for photo in (page.images): # pages.images  gave all the images  of a pdf 
        photo.image.save(f"{pdf_name}{i+1}page.image_{no}.png")
        no +=1
    #The .image attribute gives you the actual image (



