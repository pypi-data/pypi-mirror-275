
from pytorr_play import PyTorrPlay
from config_utils import generate_config, load_config_from_path
from arg_parser import parse_args


def main():
    args = parse_args()

    if args.generate_config:
        generate_config()
    else:
        config_path = args.config if args.config else PyTorrPlay.CONFIG_FILE
        config = load_config_from_path(config_path)
        watcher = PyTorrPlay(config, args.ui, args.player)

        if args.history:
            watcher.show_history()
        else:
            watcher.main()


if __name__ == "__main__":
    main()
