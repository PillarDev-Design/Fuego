from django.contrib import admin
from .models import Visualization, Category

"""
class CategoryInline( admin.TabularInline ):
	model = Category
	extra = 1
"""

class VisualizationAdmin( admin.ModelAdmin ):
	fields = [ 'category',
		   'vis_name',
		   'short_description',
		   'description',
		   'template_slug',
		   'pub_date',
		   'last_edit',
		 ]
	list_display = ( 'vis_name', 'short_description', )


admin.site.register( Visualization, VisualizationAdmin )
admin.site.register( Category )
