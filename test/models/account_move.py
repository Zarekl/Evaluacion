# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit= 'account.move'


    # ------------------------------------------------------
    # ACTIONS
    # ------------------------------------------------------

    def action_show_delivery_details(self):
        """
        Muestra los detalles de entrega asociados a la factura.
        """
        self.ensure_one()
        return {
            'name': 'Detalle de Entrega',
            'type': 'ir.actions.act_window',
            'res_model': 'delivery.detail',
            'view_mode': 'tree,form',
            'domain': [('account_move_id', '=', self.id)],
            'views': [
                (self.env.ref('test.view_delivery_detail_tree').id, 'tree'),
                (self.env.ref('test.view_delivery_detail_form').id, 'form'),
            ],
            'context': {'default_account_move_id': self.id},
            'target': 'current',
        }

    # ------------------------------------------------------
    # CRUD METHODS
    # ------------------------------------------------------

    @api.model_create_multi
    def create(self, vals_list):
        """
        Crea registros de factura y genera detalles de entrega para las líneas de factura
        que están asociadas a órdenes de venta con entregas completadas.
        """
        records = super().create(vals_list)
        for record in records:
            pickings = record.invoice_line_ids.mapped('sale_line_ids.order_id.picking_ids')
            for picking in pickings.filtered(lambda p: p.state == 'done'):
                # Crear el detalle de entrega
                delivery_detail = self.env['delivery.detail'].create({
                    'account_move_id': record.id,
                    'picking_id': picking.id,
                    'invoiced': True,
                })

                # Crear las líneas del detalle
                for move_line in picking.move_line_ids:
                    self.env['delivery.detail.line'].create({
                        'delivery_detail_id': delivery_detail.id,
                        'product_id': move_line.product_id.id,
                        'qty': move_line.qty_done,
                        'uom_id': move_line.product_uom_id.id,
                        'lot_id': move_line.lot_id.id,
                    })
        return records

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
    
    delivery_detail_ids = fields.One2many(
        'delivery.detail',
        'account_move_id',
        string="Detalles de Entrega",
        help='Detalles de entrega asociados a la factura',
    )