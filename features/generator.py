import urllib.parse

class WazeGenerator():
    def generate_waze_link(address: str) -> str:
        address = address.strip()

        if " - " in address:
            street_num, district = address.split(" - ", 1)

            street_num = street_num.strip()
            district = district.strip()

            formatted = f"{street_num}, {district}"
        else:
            formatted = address

        encoded = urllib.parse.quote_plus(formatted)

        return f"https://waze.com/ul?q={encoded}"
    
    def generate_waze_coord(coord: str) -> str:
        coord = coord.strip()
        
        if "," in coord:
            lat, lon = coord.split(",", 1)
            
            lat = lat.strip()
            lon = lon.strip()
            
            formatted = f"{lat},{lon}"
        
            return f"https://waze.com/ul?ll={formatted}"
        
        return "Coordenada inválida."