import requests
import platform
from plyer import notification
import xml.etree.ElementTree as ET
from fuzzywuzzy import fuzz
from datetime import datetime
import subprocess
import os
import json
from tabulate import tabulate
from ui_methods import get_ui
from streamer import TorrentMPV


class PyTorrPlay:
    CONFIG_DIR = os.path.join(os.path.expanduser(
        "~"), ".config", "torrent_watcher")
    CONFIG_FILE = os.path.join(CONFIG_DIR, "config.yaml")
    HISTORY_DIR = os.path.join(os.path.expanduser("~"), ".torrent_watcher")
    HISTORY_FILE = os.path.join(HISTORY_DIR, "history.json")
    HISTORY_LIMIT = 16

    def __init__(self, config, ui_type, player):
        self.config = config
        self.JACKETT_API_KEY = config.get("JACKETT_API_KEY", "")
        self.JACKET_PORT = config.get("JACKET_PORT", 9117)
        self.JACKET_ADDRESS = config.get("JACKET_ADDRESS", "127.0.0.1")
        self.BASE_URL = f"http://{self.JACKET_ADDRESS}:{self.JACKET_PORT}/api/v2.0/indexers/all/results/torznab?apikey={self.JACKETT_API_KEY}&q="
        self.PLAYER = player

        if not os.path.exists(self.HISTORY_DIR):
            os.makedirs(self.HISTORY_DIR)
        self.history = self.load_history()

        # Initialize UI
        self.ui = get_ui(ui_type)

    def notify(self, message):
        title = "Notification"
        system = platform.system()

        if system in ['Linux', 'Darwin', 'Windows']:
            notification.notify(
                title=title,
                message=message,
                app_name='PyTorr-Play',
                timeout=10  # duration in seconds
            )
        else:
            print("Unsupported OS")

    def load_history(self):
        if os.path.exists(self.HISTORY_FILE):
            with open(self.HISTORY_FILE, 'r') as f:
                return json.load(f)
        return []

    def save_history(self):
        with open(self.HISTORY_FILE, 'w') as f:
            json.dump(self.history, f)

    def add_to_history(self, title, magnet):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history = [
            item for item in self.history if item['magnet'] != magnet]
        self.history.insert(
            0, {'title': title, 'magnet': magnet, 'timestamp': timestamp})
        if len(self.history) > self.HISTORY_LIMIT:
            self.history.pop()
        self.save_history()

    def show_history(self):
        if self.history:
            headers = ["Title", "Magnet", "Timestamp"]
            table = []
            for item in self.history:
                shortened_magnet = item['magnet'][:10] + \
                    "..." + item['magnet'][-10:]
                table.append(
                    [item['title'], shortened_magnet, item['timestamp']])
            print(tabulate(table, headers, tablefmt="grid"))
        else:
            print("No history available.")

    def fetch_results(self, query):
        self.notify("Fetching tracker data...")
        url = self.BASE_URL + query
        response = requests.get(url)
        response.raise_for_status()
        self.notify("Finished fetching tracker data.")
        return response.content

    def parse_xml(self, xml_data):
        ns = {'torznab': 'http://torznab.com/schemas/2015/feed'}
        root = ET.fromstring(xml_data)
        items = []
        for item in root.findall(".//item"):
            title = item.find("title").text
            seeders = int(
                item.find("torznab:attr[@name='seeders']", ns).attrib['value'])
            link = item.find("link").text
            magnet_element = item.find("torznab:attr[@name='magneturl']", ns)
            magnet = magnet_element.attrib['value'] if magnet_element is not None else None

            if magnet:
                items.append({'title': title, 'seeders': seeders,
                             'link': link, 'magnet': magnet})
        return items

    def sort_results(self, items, query):
        for item in items:
            item['score'] = fuzz.partial_ratio(
                item['title'].lower(), query.lower())
        sorted_items = sorted(
            items, key=lambda x: (-x['seeders'], -x['score']))
        return sorted_items

    def main(self):
        selected_option = self.ui.history_menu(self.history)
        if not selected_option:
            return

        if selected_option == "Search for a new torrent":
            query = self.ui.input("Enter your search query:")
            if not query:
                return

            xml_data = self.fetch_results(query)
            items = self.parse_xml(xml_data)
            sorted_items = self.sort_results(items, query)

            options = [
                f"{item['title']} - Seeders: {item['seeders']}" for item in sorted_items]
            selected_option = self.ui.menu(options)

            if selected_option:
                selected_item = next(item for item in sorted_items if f"{item['title']} - Seeders: {item['seeders']}" == selected_option)
        else:
            selected_item = next(
                (item for item in self.history if item['magnet']
                 == selected_option),
                None
            )

        if selected_item['magnet']:
            self.notify(f"Starting torrent download: {selected_item['title']}")
            self.add_to_history(
                selected_item['title'], selected_item['magnet'])
            if self.PLAYER == "mpv":
                player = TorrentMPV(selected_item['magnet'])
                player.start_download()
                player.stream_video()
                self.notify("Starting playback with mpv...")
            else:
                subprocess.run(['webtorrent', 'download', '--playlist', f'--vlc', '-u', '100', selected_item['magnet']])
                self.notify("Starting playback with vlc...")
        else:
            print("No magnet link found for the selected torrent.")
