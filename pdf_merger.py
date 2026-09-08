from pypdf import PdfWriter

Merge = PdfWriter() # this creates a empty pdf writter  means merger is a empty
                    # Pdf in which we will add merge pdf sam elike we do
                    # page = PdfReader it will pyt the pdf in pages form where we read
try:
    
    list_pdf = ["demo1.pdf",
                "demo2.pdf",
                "demo3.pdf"]

    for pdf in list_pdf:
        Merge.append(pdf) # this means in merge i.e virtual empty pdf , append the
                          # pdf's from the list
    Merge.write("Merged.pdf") # this means write or save the merge pdf

except:   #added try exxcept ,if any pdf that deos exist i get a message 
    print("there are some error in odf names o merging")
Merge.close()       # this is good practice to close the pdf after we have done
                    # work with it
 
