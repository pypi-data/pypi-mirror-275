import dataclasses
import datetime

import httpx
import pydantic

from unico_device_setuper.lib import auth

BLS_API_BASE_URL = 'https://api.bls.sygic.com/api/v1'


class GroupedOrderItem(pydantic.BaseModel):
    product_id: int = pydantic.Field(alias='productId')
    activation_type: str = pydantic.Field(alias='activationType')
    purchase_period: int = pydantic.Field(alias='purchasePeriod')
    product_name: str = pydantic.Field(alias='productName')
    readable_purchase_period: str = pydantic.Field(alias='readablePurchasePeriod')
    license_count: int = pydantic.Field(alias='licenseCount')
    free_license_count: int = pydantic.Field(alias='freeLicenseCount')
    activated_license_count: int = pydantic.Field(alias='activatedLicenseCount')
    deactivated_license_count: int = pydantic.Field(alias='deactivatedLicenseCount')
    expired_license_count: int = pydantic.Field(alias='expiredLicenseCount')
    outdated_license_count: int = pydantic.Field(alias='outdatedLicenseCount')
    dispatched_license_count: int = pydantic.Field(alias='dispatchedLicenseCount')
    prolonged_license_count: int = pydantic.Field(alias='prolongedLicenseCount')
    repair_count_licenses: int = pydantic.Field(alias='repairCountLicenses')
    product_identifier_type: str = pydantic.Field(alias='productIdentifierType')
    product_type: str = pydantic.Field(alias='productType')


class GetProductResponse(pydantic.BaseModel):
    grouped_order_items: list[GroupedOrderItem] = pydantic.Field(alias='groupedOrderItems')


class OrderItem(pydantic.BaseModel):
    order_item_id: int = pydantic.Field(alias='orderItemId')
    order_id: int = pydantic.Field(alias='orderId')
    order_name: str = pydantic.Field(alias='orderName')
    order_date: datetime.datetime = pydantic.Field(alias='orderDate')
    can_be_deleted: bool = pydantic.Field(alias='canBeDeleted')
    license_count: int = pydantic.Field(alias='licenseCount')
    free_license_count: int = pydantic.Field(alias='freeLicenseCount')
    activated_license_count: int = pydantic.Field(alias='activatedLicenseCount')
    deactivated_license_count: int = pydantic.Field(alias='deactivatedLicenseCount')
    expired_license_count: int = pydantic.Field(alias='expiredLicenseCount')
    outdated_license_count: int = pydantic.Field(alias='outdatedLicenseCount')
    dispatched_license_count: int = pydantic.Field(alias='dispatchedLicenseCount')
    prolonged_license_count: int = pydantic.Field(alias='prolongedLicenseCount')
    repair_count_licenses: int = pydantic.Field(alias='repairCountLicenses')
    product_identifier_type: str = pydantic.Field(alias='productIdentifierType')
    product_type: str = pydantic.Field(alias='productType')


@dataclasses.dataclass
class Client:
    http_client: httpx.AsyncClient
    api_key: str

    @staticmethod
    async def make(http_client: httpx.AsyncClient):
        return Client(http_client, await auth.get_sygic_api_key(http_client))

    async def get_products(self):
        response = await self.http_client.get(
            url=BLS_API_BASE_URL + '/myOrder/groupedOrderItems', headers={'X-api_key': self.api_key}
        )
        assert response.status_code == 200, response.text
        return GetProductResponse.model_validate_json(response.content).grouped_order_items

    async def get_orders_by_product(
        self, product_id: int, activation_type: str, purchase_period: int
    ):
        response = await self.http_client.get(
            url=BLS_API_BASE_URL + f'/myOrder/orderItems?productId={product_id}'
            f'&activationType={activation_type}'
            f'&purchasePeriod={purchase_period}'
        )
        assert response.status_code == 200, response.text
        return pydantic.TypeAdapter(list[OrderItem]).validate_json(response.content)

    async def register_licence(
        self, product_id: int, purchase_period: int, device_id: str, device_name: str | None
    ):
        await self.http_client.post(
            url=BLS_API_BASE_URL + '/activate',
            params={'productId': product_id, 'purchasePeriod': purchase_period},
            headers={'X-api_key': self.api_key},
            json=[
                {'licenseIdentifierType': 'device', 'identifier': device_id, 'note': device_name}
            ],
        )
