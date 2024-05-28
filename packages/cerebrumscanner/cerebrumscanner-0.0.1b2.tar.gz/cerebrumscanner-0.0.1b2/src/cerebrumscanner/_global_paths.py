import os

__path_dict__ = {}

__path_dict__['common'] = os.path.dirname(__file__)
__path_dict__['common-assets'] = os.path.join(__path_dict__['common'],'assets')
__path_dict__['common-configs'] = os.path.join(__path_dict__['common'],'configs')
__path_dict__['common-models'] = os.path.join(__path_dict__['common'],'models')
__path_dict__['common-lib'] = os.path.join(__path_dict__['common'],'lib')
__path_dict__['common-sample-data'] = os.path.join(__path_dict__['common'],'sample_data')
__path_dict__['common-kvfiles'] = os.path.join(__path_dict__['common'],'kvfiles')

__path_dict__['sample-data-json-path'] = os.path.join(__path_dict__['common-sample-data'],'X40135202726.json')
__path_dict__['sample-data-nifti-path'] = os.path.join(__path_dict__['common-sample-data'],'X40135202726')

__path_dict__['home'] = os.path.expanduser("~")

__path_dict__['dot-cerebrum-scanner'] = os.path.join(__path_dict__['home'],'.cerebrum-scanner')

__path_dict__['dot-cerebrum-scanner-tmp'] = os.path.join(__path_dict__['home'],'.cerebrum-scanner','tmp')
__path_dict__['dot-cerebrum-scanner-jobs'] = os.path.join(__path_dict__['home'],'.cerebrum-scanner','jobs')
__path_dict__['dot-cerebrum-scanner-jobs-pending'] = os.path.join(__path_dict__['dot-cerebrum-scanner-jobs'],'pending')
__path_dict__['dot-cerebrum-scanner-jobs-sent'] = os.path.join(__path_dict__['dot-cerebrum-scanner-jobs'],'sent')
__path_dict__['dot-cerebrum-scanner-jobs-received'] = os.path.join(__path_dict__['dot-cerebrum-scanner-jobs'],'received')

__path_dict__['dot-cerebrum-scanner-data'] = os.path.join(__path_dict__['home'],'.cerebrum-scanner','data')


for _,pth in __path_dict__.items():
    if os.path.exists(pth): pass
    else: os.mkdir(pth)
