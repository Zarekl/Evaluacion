# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from odoo.exceptions import UserError


class DeliveryDetail(models.Model):
    _name = 'delivery.detail'
    _description = 'Cabecera de detalle de Entrega'

    # ------------------------------------------------------
    # ACTIONS
    # ------------------------------------------------------

    def action_mark_as_invoiced(self):
        """
        Acción masiva que marca como facturado solo si la factura está pagada.
        Solo usuarios con permiso 'Verificar Detalle Entrega' pueden ejecutar.
        """
        if not self.env.user.has_group('test.group_delivery_detail_administrator'):
            raise UserError("No tienes permiso para verificar el detalle de entrega.")

        for detail in self:
            if detail.account_move_id.payment_state not in ['paid', 'in_payment']:
                raise UserError(
                    f"La factura {detail.account_move_id.name} no está pagada. "
                    "Solo puedes marcar como facturado si está totalmente pagada."
                )
            detail.invoiced = True
            
    # ------------------------------------------------------
    # CRUD METHODS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # COMPUTE METHODS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # CONSTRAINTS AND VALIDATIONS
    # ------------------------------------------------------

    @api.constrains('invoiced')
    def _check_invoiced_permission(self):
        """
        Verifica permisos para modificar el campo 'Facturado'.
        """
        if not self.env.user.has_group('test.group_delivery_detail_administrator'):
            raise UserError("No tienes permisos para modificar el campo 'Facturado'.")
    
    # ------------------------------------------------------
    # ONCHANGE METHODS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # OTHER METHODS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # VARIABLES
    # ------------------------------------------------------

    account_move_id = fields.Many2one(
        'account.move',
        string='Factura',
        help='Factura asociada a la entrega',
    )
    picking_id = fields.Many2one(
        'stock.picking',
        string='Transferencia',
        help='Transferencia asociada a la entrega',
        readonly=True,
    )

    invoiced = fields.Boolean(
        string='Facturado',
        default=False,
        help='Indica si la entrega ha sido facturada',
        tracking=True,
    )

    delivery_detail_line_ids = fields.One2many(
        'delivery.detail.line',
        'delivery_detail_id',
        string='Líneas de detalle de Entrega',
        help='Líneas de detalle asociadas al detalle de entrega',
        readonly=True,
    )