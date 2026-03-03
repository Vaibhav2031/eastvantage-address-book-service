# distance_service.py
# Service for calculating distances between addresses

from geopy.distance import geodesic

class DistanceService:
    def calculate_distance(self, address1, address2):
        # Placeholder for distance calculation logic
        pass
    
    def is_within_distance(self, coord1, coord2, max_km):
        distance = geodesic(coord1, coord2).kilometers
        return distance <= max_km

    def filter_nearby(self, addresses, center_lat, center_lon, max_km):
        center_coords = (center_lat, center_lon)
        return [
            address for address in addresses
            if self.is_within_distance(center_coords, (address.latitude, address.longitude), max_km)
        ]