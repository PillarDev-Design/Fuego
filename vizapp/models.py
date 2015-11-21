from django.db import models
import datetime
from django.utils import timezone

class Visualization( models.Model ):
	vis_name = models.CharField( max_length = 256 )

	pub_date = models.DateTimeField( 'date published' )
	last_edit = models.DateTimeField( 'last edited' )
	short_description = models.CharField( max_length = 256 )
	description = models.TextField()

	def __unicode__( self ):
		return self.vis_name
