# PyTorr-Play

PyTorr-Play is a Python tool for searching torrents using the Jackett API, displaying results using `curses`/`rofi`, and downloading and playing the selected torrents using `mpv`.

## Features

- Search for torrents using the Jackett API.
- Display search results in a `curses`/`rofi` menu.
- Select and download torrents.
- Play downloaded torrents with `mpv` (or VLC, with `webtorrent-cli`).
- Maintain a history of downloaded torrents.

## Preview

[Watch the video on YouTube](https://youtu.be/7vZOBZaLPOk)

## Installation

### Using `pipx`

`pipx` allows you to install and run Python applications in isolated environments.

1. **Install pipx (if not already installed):**

    ```sh
    python -m pip install --user pipx
    python -m pipx ensurepath
    ```

2. **Install PyTorr-Play:**

    ```sh
    pipx install pytorr-play
    ```

### From Source

1. **Clone the repository:**

    ```sh
    git clone https://gitlab.com/imithrellas/pytorr-play.git
    cd pytorr-play
    ```

2. **Install Poetry (if not already installed):**

    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. **Install dependencies:**

    ```sh
    poetry install
    ```

4. **Install system dependencies:**

    - `Jackett`: [Refer to instalation and setup steps on Jackett GitHub page](https://github.com/Jackett/Jackett)
    - `webtorrent`: A streaming torrent client for the web. (Only needed for VLC, subject to change)
    - `mpv`: A media player based on MPlayer and mplayer2.

    Use your package manager to install these dependencies:

    ```sh
    sudo pacman -S mpv
    ```

5. **Activate the virtual environment:**

    ```sh
    poetry shell
    ```

## Configuration

### Generate the Default Configuration File

```sh
pytorr-play --generate-config
```

This will create a configuration file at `~/.config/torrent_watcher/config.yaml` with the following content:

```yaml
JACKETT_API_KEY: "your_api_key_here"
JACKET_PORT: 9117
JACKET_ADDRESS: "127.0.0.1"
```

### Edit the Configuration File

Replace `your_api_key_here` with your actual Jackett API key.

## Usage

### Search for Torrents

```sh
pytorr-play
```

This will prompt you to enter a search query and display the results in a `curses` menu.
Alternatively you can use Rofi, if you have it installed on your system.

```sh
pytorr-play --ui Rofi
```

### Show Torrent History

```sh
pytorr-play --history
```

This will display a table of previously downloaded torrents.

### Use a Custom Configuration File

```sh
pytorr-play --config /path/to/your/config.yaml
```

This allows you to specify a custom configuration file path.

## Arguments

- `-h`/`--help`: Show help.
- `--generate-config`: Generate the default configuration file.
- `--config <path>`: Specify a custom configuration file path.
- `--history`: Show torrent history.
- `--ui`: Choose UI (Curses/Rofi).

## Example

```sh
pytorr-play --config /home/user/custom_config.yaml
```

## Plans

- [x] Omit Webtorrent
- [x] Find a way to include timestamp in the history to be able to resume play.
- [ ] Include support for VLC

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.

## Legal Disclaimer

Neither I nor this tool promote or condone the distribution or consumption of illegal content via torrents. This tool is intended solely for legal uses, such as downloading and sharing open-source software, public domain content, and other legally distributable files. Users are responsible for ensuring that their usage complies with all applicable laws and regulations.
