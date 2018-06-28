# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Models):
    name = fields.Char(string="Title", required=True)
        description = fields.Text()

    responsible_id = fields.Many2one(
        'res.users',
        ondelete='set null',
        string="Responsible",
        index=True)
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")


class Session(models.Model):
    _name = 'openacademy.session'

    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one('res.partner', string="Instructor",
       domain=['|', ('instructor', '=', True),
                     ('category_id.name', 'ilike', "Teacher")])
        ondelete='cascade',string="Course", required=True
        attendee_ids = fields.Many2many('res.partner', string="Attendees")
