from base_utils import Endpoint, RequestBuilder


class ItemAPI:

    @staticmethod
    def create_item(body):
        return (
            RequestBuilder()
            .with_method("POST")
            .with_endpoint(Endpoint.CREATE_ITEM.value)
            .with_json(body)
            .send()
        )

    @staticmethod
    def get_item_by_id(item_id):
        return (
            RequestBuilder()
            .with_endpoint(Endpoint.GET_ITEM_BY_ID.value.format(id=item_id))
            .send()
        )

    @staticmethod
    def get_items_by_seller(seller_id):
        return (
            RequestBuilder()
            .with_endpoint(Endpoint.GET_ITEMS_BY_SELLER.value.format(sellerID=seller_id))
            .send()
        )


class StatisticAPI:

    @staticmethod
    def get_statistic(item_id):
        return (
            RequestBuilder()
            .with_endpoint(Endpoint.GET_STATISTIC.value.format(id=item_id))
            .send()
        )
