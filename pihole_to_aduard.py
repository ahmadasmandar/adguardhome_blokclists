import requests

def convert_pihole_to_adguard(pihole_url, output_file):
    try:
        # Download the Pi-hole blocklist
        response = requests.get(pihole_url)
        response.raise_for_status()  # Check for HTTP errors

        # Convert Pi-hole blocklist entries to AdGuard Home filter format
        adguard_entries = []
        for line in response.text.splitlines():
            # Skip empty lines and comments
            if line and not line.startswith('#'):
                # Convert each domain into AdGuard Home format
                adguard_entries.append(f"||{line.strip()}^")

        # Save the content to a file formatted for AdGuard
        with open(output_file, 'w') as file:
            file.write("\n".join(adguard_entries))

        print(f"Successfully converted Pi-hole blocklist to AdGuard format and saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading the Pi-hole blocklist: {e}")

# Usage
pihole_blocklist_url = "https://raw.githubusercontent.com/Ruddernation-Designs/Adobe-URL-Block-List/master/PiHole"  # Replace with your actual URL
output_adguard_list = "adobe_adguard_blocklist.txt"

convert_pihole_to_adguard(pihole_blocklist_url, output_adguard_list)
