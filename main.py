import urllib.parse

def generate_waze_link(address: str) -> str:
    format_address = urllib.parse.quote_plus(address)
    link = f"https://waze.com/ul?q={format_address}"
    return link

if __name__ == "__main__":
    while True:
        address = input("Digite o endereço completo: ")
        link = generate_waze_link(address)
        print("\n🔗 Link do Waze:")
        print(link)