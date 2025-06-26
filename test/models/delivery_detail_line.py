# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class DeliveryDetailLine(models.Model):
    _name = 'delivery.detail.line'
    description = 'Línea de detalle de Entrega'

    # ------------------------------------------------------
    # ACTIONS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # CRUD METHODS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # COMPUTE METHODS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # CONSTRAINTS AND VALIDATIONS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # ONCHANGE METHODS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # OTHER METHODS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # VARIABLES
    # ------------------------------------------------------

    delivery_detail_id = fields.Many2one(
        'delivery.detail',
        string='Detalle de Entrega',
        help='Detalle de entrega asociado a esta línea',
    )
    qty = fields.Float(
        string='Cantidad',
        help='Cantidad de producto en esta línea de detalle',
        readonly=True,
    )
    uom_id = fields.Many2one(
        'uom.uom',
        string='Unidad de Medida',
        help='Unidad de medida para la cantidad de producto',
        readonly=True,
    )
