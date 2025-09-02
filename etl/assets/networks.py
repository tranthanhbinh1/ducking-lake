import dagster as dg
from client import CityBikesClient
from etl.resources.postgres import PostgresResource
from db_models.networks import Network as NetworkModel


@dg.asset
def networks(postgres: PostgresResource):
    """
    Load all networks from City Bikes
    """
    client = CityBikesClient()
    networks = client.get_all_networks()

    # Insert
    for network in networks.networks:
        db_network = NetworkModel(
            id=network.id,
            name=network.name,
            city=network.location.city,
            country=network.location.country,
            latitude=network.location.latitude,
            longitude=network.location.longitude,
            company=network.company,
            href=network.href,
        )
        postgres.session.merge(db_network)  # Use merge to cover Upsert cases

    postgres.session.commit()
