from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views import generic
#from .models import Question, Choice
from .models import Visualization, Category

def index( request ):
	latest_vis_list = Visualization.objects.order_by( '-pub_date' )[:2]
	context = { 'latest_vis_list': latest_vis_list }
	return render( request, 'vizapp/index.html', context )

def datasets( request ):
	cat_list = Category.objects.all()
	vis_list = Visualization.objects.all()
	context = { 
			'cat_list' : cat_list,
			'vis_list' : vis_list,
		  }
	return render( request, 'vizapp/datasets.html', context )

def about( request ):
	context = { }
	return render( request, 'vizapp/about.html', context )

def usa_natality_2013( request ):
	vis = Visualization.objects.all().filter(template_slug="usa_natality_2013");
	print vis
	context = { 'vis': vis }
	return render( request, 'vizapp/usa_natality_2013.html', context )

def usa_natality_2012( request ):
	context = { }
	return render( request, 'vizapp/usa_natality_2012.html', context )
