from django.shortcuts import render

from staff_fellows.models import Staff, Fellow
from faq.models import FaqQuestion

def home(request):
		return render(request, "index.html")

def program(request):
	return render(request, "program.html", {})

def alumni(request):
	alumniList = Fellow.objects.filter(year = 2014)

	return render(request, "alumni.html", {'alumniList':alumniList})

def faq(request):
	faqList = FaqQuestion.objects.all()
	return render(request, "faq.html", {'faqList':faqList})

def contact(request):
	return render(request, "contact.html", {})

def staff(request):

	staffList = Staff.objects.all()
	context = {'staffList': staffList,}
	return render(request, "staff.html", context)

def apply(request):
	return render(request, "apply.html", {})

def partner(request):
	return render(request, "apply.html", {})

def community(request):
	return render(request, "apply.html", {})