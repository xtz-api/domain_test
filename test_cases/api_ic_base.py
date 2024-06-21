import json
import logging
from util.volc_ic_api.volc_ic_api import VolcIcApi


class IcService(object):
    def __init__(self, client, OpportunityID=None, Email=None, LicenseAddr=None, LicenseBack=None, LicenseFront=None, LicenseNum=None, Name=None, Phone=None, TemplateType=None,
                 TemplateID=None, ICID=None, BankID=None, TaxID=None, ButlerID=None, auto_delete=None, page_number=None, page_size=None, verify_status_mask=None, register_list=None, auto_renew=None, zone=None):
        self.client = client
        self.api = VolcIcApi(client)
        self.OpportunityID = OpportunityID
        self.Email = Email
        self.LicenseAddr = LicenseAddr
        self.LicenseBack = LicenseBack
        self.LicenseFront = LicenseFront
        self.LicenseNum = LicenseNum
        self.Name = Name
        self.Phone = Phone
        self.TempalteType = TemplateType
        self.TemplateID = TemplateID
        self.ICID = ICID
        self.BankID = BankID
        self.TaxID = TaxID
        self.ButlerID = ButlerID
        if auto_renew is not None:
            self.auto_renew = auto_renew
        else:
            self.auto_renew = False
        self.register_list = register_list
        if verify_status_mask is not None:
            self.verify_status_mask = verify_status_mask
        else:
            self.verify_status_mask = 1
        if zone is not None:
            self.zone = zone
        else:
            self.zone = ".com"
        if page_number is not None:
            self.page_number = page_number
        else:
            self.page_number = "1"
        if page_size is not None:
            self.page_size = page_size
        else:
            self.page_size = "0"
