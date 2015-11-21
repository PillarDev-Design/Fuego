from django.contrib import admin
from .models import Visualization

class VisualizationAdmin( admin.ModelAdmin ):
	fieldsets = [
		( None, { 'fields': ['vis_name'] } ),
		( 'Short Description', { 'fields': ['short_description' ] } ),
		( 'Description', { 'fields': ['description' ] } ),
		( 'Date Published', { 'fields': ['pub_date'],
				      'classes': ['collapse'] } ),
		( 'Last Edited', { 'fields': ['last_edit'],
				    'classes': ['collapse' ] } ),
	]
	list_display = ( 'vis_name', 'short_description',
			 'pub_date', 'last_edit' )
	list_filter = [ 'pub_date' ]
	search_fields = [ 'vis_name' ]

admin.site.register( Visualization, VisualizationAdmin )

