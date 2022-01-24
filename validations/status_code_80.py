import datetime, pytz
from .validation_service import all_validations

class status_code_80:

    def __init__(self, root):
        self.errors = []
        self.warnings = []
        self.validations = all_validations(root)
    
    def run_all_validations(self):

        if not self.validations.HouseBillOfLadingNumber():
            self.errors.append('HouseBillOfLadingNumber')
        
        if not self.validations.ArrivalNoticeNumber():
            self.errors.append('ArrivalNoticeNumber')
        
        if not self.validations.OceanVEssel():
            self.errors.append('OceanVEssel')
        
        if not self.validations.ShipperReference():
            self.warnings.append('ShipperReference')
        
        if not self.validations.ForwarderReference():
            self.warnings.append('ForwarderReference')
        
        if not self.validations.PlaceOfReceiptOrPortOfLoading():
            self.errors.append('PlaceOfReceipt Or PortOfLoading')
        
        if not self.validations.ETSPlaceOfReceiptOrETSPortOfLoading():
            self.errors.append('ETSPlaceOfReceipt Or ETSPortOfLoading')
        
        if not self.validations.PortOfDischargeAndPlaceOfDelivery():
            self.errors.append('PortOfDischarge or PlaceOfDelivery')
        
        if not self.validations.ETAPortOfDischargeAndETAPlaceOfDelivery():
            self.errors.append('ETAPortOfDischarge and ETAPlaceOfDelivery')
        
        if not self.validations.StatusDateTimeDetails():
            self.errors.append('StatusDateTimeDetails')
        
        if not self.validations.CustomerAlias():
            self.errors.append('CustomerAlias')
        
        if not self.validations.ConsigneeReference():
            self.warnings.append('ConsigneeReference')
        
        if not self.validations.CommunicationReference():
            self.warnings.append('CommunicationReference')
        
        if not self.validations.PickupReference():
            self.warnings.append('PickupReference')
        
        if not self.validations.ContainerNumber():
            self.errors.append('ContainerNumber')
        
        if not self.validations.SealNumber():
            self.errors.append('SealNumber')

        if len(self.errors) > 0:
            return False, self.errors, self.warnings

        return True, self.errors, self.warnings