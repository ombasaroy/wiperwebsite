from .models import PDFDocument


def pdf_documents(request):
    return {"pdf_documents": PDFDocument.objects.all()}
