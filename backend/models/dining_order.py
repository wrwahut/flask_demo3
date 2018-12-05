# -*- coding:utf-8 -*-

from .base import CRUD
from . import db

class Dining_order(CRUD,db.Model):
    __bind_key__ = "other"

    id = db.Column(db.Integer, primary_key=True)
    order_num = db.Column(db.VARCHAR(255))
    shop_id = db.Column(db.VARCHAR(255))
    shop_name = db.Column(db.VARCHAR(255))
    sender_id = db.Column(db.VARCHAR(255))
    sender_name = db.Column(db.VARCHAR(255))
    sender_phone = db.Column(db.VARCHAR(255))
    status = db.Column(db.Integer,default=0)
    goods_list = db.Column(db.Text)
    user_id = db.Column(db.Integer)
    nick_name = db.Column(db.VARCHAR(255))
    total_price = db.Column(db.FLOAT)
    address_text = db.Column(db.VARCHAR(255))
    price_times = db.Column(db.Integer)
    sex = db.Column(db.Integer)
    message = db.Column(db.VARCHAR(255))
    transaction_id = db.Column(db.VARCHAR(255))
    end_time = db.Column(db.VARCHAR(255))
    refund_num = db.Column(db.VARCHAR(255))
    refund_id = db.Column(db.VARCHAR(255))
    pay_method = db.Column(db.VARCHAR(255))
    order_name = db.Column(db.VARCHAR(255))
    order_desc = db.Column(db.VARCHAR(255))
    estimate_time = db.Column(db.VARCHAR(255))
    is_shop_delete = db.Column(db.Integer)
    is_user_delete = db.Column(db.Integer)
    is_sender_delete = db.Column(db.Integer)
    is_plat_delete = db.Column(db.Integer)
    add_time = db.Column(db.VARCHAR(255))
    pay_time = db.Column(db.VARCHAR(255))
    is_comment = db.Column(db.Integer, default=0)
    min = db.Column(db.FLOAT)
    real_money = db.Column(db.FLOAT)
    person_count = db.Column(db.Integer)
    fee = db.Column(db.VARCHAR(11))
    shop_account = db.Column(db.VARCHAR(255))
    sender_account = db.Column(db.VARCHAR(255))
    user_account = db.Column(db.VARCHAR(255))
    shop_phone = db.Column(db.VARCHAR(255))
    address_json = db.Column(db.VARCHAR(255))
    balance_money = db.Column(db.FLOAT)
    plate_fee = db.Column(db.FLOAT)
    discount_money = db.Column(db.FLOAT)
    cut_money = db.Column(db.FLOAT)
    is_print = db.Column(db.Integer)
    build_id = db.Column(db.Integer)
    order_count = db.Column(db.Integer)
    is_zan = db.Column(db.Integer)
    user_complain_id = db.Column(db.Integer)
    sender_complain_id = db.Column(db.Integer)
    shop_win = db.Column(db.FLOAT)
    sending_type = db.Column(db.Integer)
    is_plat = db.Column(db.Integer)