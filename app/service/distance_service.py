# Service responsible for calculating geographical distance.

from geopy.distance import geodesic


class DistanceService:

    def is_within_distance(self, coord1, coord2, max_km):
        """
        Check if two coordinates are within a given distance.

        Args:
            coord1 (tuple): First coordinate (lat, lon).
            coord2 (tuple): Second coordinate (lat, lon).
            max_km (float): Maximum distance in kilometers.

        Returns:
            bool: True if within distance, otherwise False.
        """
        distance = geodesic(coord1, coord2).kilometers
        return distance <= max_km

    def filter_nearby(self, addresses, center_lat, center_lon, max_km):
        """
        Filter addresses within a given distance.

        Args:
            addresses (list[Address]): List of address entities.
            center_lat (float): Center latitude.
            center_lon (float): Center longitude.
            max_km (float): Maximum distance in kilometers.

        Returns:
            list[Address]: Addresses within the specified distance.
        """
        center_coords = (center_lat, center_lon)

        return [
            address
            for address in addresses
            if self.is_within_distance(
                center_coords,
                (address.latitude, address.longitude),
                max_km
            )
        ]