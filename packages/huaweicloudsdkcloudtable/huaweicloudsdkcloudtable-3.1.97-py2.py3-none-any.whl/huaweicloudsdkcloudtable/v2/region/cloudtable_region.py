# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class CloudTableRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CLOUDTABLE")

    CN_NORTH_1 = Region("cn-north-1",
                        "https://cloudtable.cn-north-1.myhuaweicloud.com")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://cloudtable.cn-north-4.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://cloudtable.cn-south-1.myhuaweicloud.com")
    CN_SOUTH_4 = Region("cn-south-4",
                        "https://cloudtable.cn-south-4.myhuaweicloud.com")
    CN_EAST_2 = Region("cn-east-2",
                        "https://cloudtable.cn-east-2.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://cloudtable.cn-east-3.myhuaweicloud.com")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://cloudtable.cn-southwest-2.myhuaweicloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://cloudtable.ap-southeast-1.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://cloudtable.ap-southeast-3.myhuaweicloud.com")
    CN_SOUTH_2 = Region("cn-south-2",
                        "https://cloudtable.cn-south-2.myhuaweicloud.com")
    CN_NORTH_9 = Region("cn-north-9",
                        "https://cloudtable.cn-north-9.myhuaweicloud.com")
    CN_NORTH_2 = Region("cn-north-2",
                        "https://cloudtable.cn-north-2.myhuaweicloud.com")

    static_fields = {
        "cn-north-1": CN_NORTH_1,
        "cn-north-4": CN_NORTH_4,
        "cn-south-1": CN_SOUTH_1,
        "cn-south-4": CN_SOUTH_4,
        "cn-east-2": CN_EAST_2,
        "cn-east-3": CN_EAST_3,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "cn-south-2": CN_SOUTH_2,
        "cn-north-9": CN_NORTH_9,
        "cn-north-2": CN_NORTH_2,
    }

    @classmethod
    def value_of(cls, region_id, static_fields=None):
        if not region_id:
            raise KeyError("Unexpected empty parameter: region_id")

        fields = static_fields or cls.static_fields

        region = cls._PROVIDER.get_region(region_id)
        if region:
            return region

        if region_id in fields:
            return fields.get(region_id)

        raise KeyError("region_id '%s' is not in the following supported regions of service 'CloudTable': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
