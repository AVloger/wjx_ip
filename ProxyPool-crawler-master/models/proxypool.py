# -*- coding: utf-8 -*-
# @Desc: 数据库操作

from models.models import ProxyPool
from models.models import DBSession


def insert_into_proxypool(item):
    """插入代理IP"""

    ip_item = ProxyPool(item)
    session = DBSession()
    try:
        session.add(ip_item)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def update_ip(item):
    """更新代理IP"""

    ip_item = ProxyPool(item)
    session = DBSession()
    try:
        session.merge(ip_item)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def delete_ip(item):
    """删除代理IP"""

    session = DBSession()
    ip_item = session.query(ProxyPool).filter(ProxyPool.id == item['id']).first()
    if ip_item:
        try:
            session.delete(ip_item)
            session.commit()
        except Exception as e:
            raise e


def get_all_ip():
    """获取所有IP"""

    session = DBSession()
    ip_list = session.query(ProxyPool).all()
    result = [item.to_dict() for item in ip_list]
    return result
