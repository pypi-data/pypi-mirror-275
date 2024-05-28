import libtorrent as lt
import time
import tempfile
import os
import shutil
import mpv


class TorrentMPV:
    def __init__(self, magnet_link, percentage=10):
        self.magnet_link = magnet_link
        self.session = lt.session({
            'listen_interfaces': '0.0.0.0:6881'
        })
        self.download_directory = None
        self.handle = None
        self.player_process = None
        self.time_file = '.playback_time.txt'
        mpv_config_dir = os.path.join(os.path.expanduser("~"), ".config", "mpv")
        self.player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True, osc=True, config=True, config_dir=mpv_config_dir)
        self.player.observe_property('time-pos', self.time_observer)
        self.player.observe_property('playlist-pos', self.playlist_pos_observer)
        self.percentage = percentage / 100.0  # Convert percentage to a fraction

    def start_download(self):
        self.download_directory = tempfile.mkdtemp()
        print(f"Temporary download directory: {self.download_directory}")

        params = lt.add_torrent_params()
        params.save_path = self.download_directory
        params.storage_mode = lt.storage_mode_t.storage_mode_allocate
        params.url = self.magnet_link
        print("Adding torrent...")
        self.handle = self.session.add_torrent(params)
        print(f"Torrent handle created: {self.handle}")

        # Wait for metadata
        print("Waiting for metadata...")
        while not self.handle.has_metadata():
            time.sleep(1)
        print("Metadata acquired")

        self.handle.set_sequential_download(True)

        # Initially set the priorities for the first n% of each file
        self.set_priorities()

    def set_priorities(self, current_file_index=None):
        info = self.handle.get_torrent_info()
        if current_file_index is None:
            for file_index in range(info.num_files()):
                file = info.file_at(file_index)
                file_start_piece = file.offset // info.piece_length()
                file_end_piece = (file.offset + file.size) // info.piece_length()
                first_n_pieces = int((file_end_piece - file_start_piece) * self.percentage)
                for piece_index in range(file_start_piece, file_start_piece + first_n_pieces):
                    self.handle.piece_priority(piece_index, 7)  # Highest priority
            self.stream_video()
        else:
            print(f"Setting high priority for file index: {current_file_index}")
            for file_index in range(info.num_files()):
                file = info.file_at(file_index)
                file_start_piece = file.offset // info.piece_length()
                file_end_piece = (file.offset + file.size) // info.piece_length()
                priority = 7 if file_index == current_file_index else 1
                for piece_index in range(file_start_piece, file_end_piece):
                    self.handle.piece_priority(piece_index, priority)

    def stream_video(self):
        try:
            player_started = False

            while self.handle.status().state != lt.torrent_status.seeding:
                status = self.handle.status()
                print(f"Progress: {status.progress * 100:.2f}%")

                if status.progress >= 0.02 and not player_started:
                    self._launch_mpv()
                    player_started = True

                if self.player_process and self.player_process.poll() is not None:
                    print("MPV player exited.")
                    break

                time.sleep(5)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.cleanup()

    def time_observer(self, _name, value):
        if value is not None:
            time_str = 'Now playing at {:.2f}s'.format(value)
            self.write_time_to_file(time_str)

    def playlist_pos_observer(self, _name, value):
        if value is not None:
            print(f"Playlist position changed to: {value}")
            self.set_priorities(current_file_index=value)

    def write_time_to_file(self, time_str):
        with open(self.time_file, 'w') as file:
            file.write(time_str)

    def _launch_mpv(self):
        video_files = self._find_video_files()
        if video_files:
            print(f"Starting MPV with video files: {video_files}")

            self.player.loadfile(video_files[0])

            for video_file in video_files[1:]:
                print(f"Adding {video_file} to playlist")
                self.player.loadfile(video_file, mode='append-play')

            # Initially set the priorities for the first file
            self.set_priorities(current_file_index=0)

    def _find_video_files(self):
        video_files = []
        for file in self.handle.get_torrent_info().files():
            if file.path.endswith(('.mp4', '.mkv', '.avi', '.mov')):
                video_files.append(os.path.join(self.download_directory, file.path))
        return video_files

    def cleanup(self):
        print(f"Cleaning up download directory: {self.download_directory}")
        if self.handle:
            self.session.remove_torrent(self.handle)
        if self.download_directory and os.path.exists(self.download_directory):
            shutil.rmtree(self.download_directory)


if __name__ == '__main__':
    magnet_link = 'magnet:?xt=urn:btih:DD8255ECDC7CA55FB0BBF81323D87062DB1F6D1C&tr=udp%3A%2F%2Ftracker.bitsearch.to%3A1337%2Fannounce&tr=udp%3A%2F%2Fwww.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2F9.rarbg.com%3A2920%2Fannounce&tr=udp%3A%2F%2Ftracker.0x.tf%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&dn=%5BBitsearch.to%5D+Big+Buck+Bunny'

    streamer = TorrentMPV(magnet_link, percentage=5)  # Change percentage as needed
    streamer.start_download()
