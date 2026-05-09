from odoo import models, fields, api

class HotelBooking(models.Model):
    _name = 'hotel.booking'
    _description = 'Hotel Booking'


    name = fields.Char(string='Booking ID', required=True, copy=False, readonly=False)
