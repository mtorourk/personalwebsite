from django.shortcuts import render_to_response
from annoying.decorators import render_to

@render_to("homepage.html")
def homepage(request):
	context = {
		"title": "Home",
	}
	return context

@render_to("portfolio.html")
def portfolio(request):
	context = {
		"title": "Portfolio",
	}
	return context

@render_to("contact.html")
def contact(request):
	context = {
		"title": "Contact",
	}
	return context

@render_to("about.html")
def about(request):
	context = {
		"title": "About",
	}
	return context

@render_to("kalite.html")
def kalite(request):
	context = {
		"title": "Kalite",
	}
	return context

@render_to("ucsd.html")
def ucsd(request):
	context = {
		"title": "Ucsd",
	}
	return context

@render_to("eslgenie.html")
def eslgenie(request):
	context = {
		"title": "Eslgenie",
	}
	return context

@render_to("lindamoodbell.html")
def lindamoodbell(request):
	context = {
		"title": "Lindamoodbell",
	}
	return context


