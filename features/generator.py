import urllib.parse

class WazeLink():
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