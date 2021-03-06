from django.db import models
import datetime
from django.utils import timezone


class Category( models.Model ):
	name = models.CharField( max_length = 100 )
	def __unicode__( self ):
		return self.name

class Visualization( models.Model ):
	category = models.ForeignKey( Category )

	vis_name          = models.CharField( max_length = 256 )
	short_description = models.CharField( max_length = 256 )
	description       = models.TextField()
	template_slug     = models.CharField( max_length = 256 )

	pub_date  = models.DateTimeField( 'date published' )
	last_edit = models.DateTimeField( 'last edited' )

	def __unicode__( self ):
		return self.vis_name
