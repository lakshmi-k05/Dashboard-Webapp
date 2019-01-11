from django.shortcuts import render, redirect, get_object_or_404
from .forms import MemberForm
from .models import Members
from django import forms

def home_view(request):
	template_name = "signin/home.html"
	if request.method == "POST":
		form = MemberForm(request.POST)

		if form.is_valid():
			print("VALID")
			usnt = form.cleaned_data['usn']
			passt = form.cleaned_data['pwd']
			print(usnt, passt)
			objtry = get_object_or_404(Members, usn=usnt)
			if objtry:
				print("Obj is ", objtry)
				if objtry.pwd!=passt:
					print("Failure")
					form = MemberForm()
				else:
					return render(request, "details/details.html")


	else:
		form = MemberForm()

	return render(request, template_name, {'form': form})
