# Music Playlist App

A simple object-oriented Python app to manage a music playlist, including local and online songs, with recently played history and polymorphic playback simulation.

## Features

- **OOP Design:**  
  - Base `Song` class stores song info as a tuple `(name, artist, length_seconds)`.
  - `LocalSong` and `OnlineSong` subclasses override the `play()` method, simulating local file playback and online streaming.
- **Playlist Management:**  
  - Add or remove songs by name or index.
  - Shuffle playlist.
  - Play songs with polymorphic playback.
  - View playlist and recently played history (tracks last N songs).
- **Easy Demo/Test:**  
  - Script can be run directly to see basic usage and outputs.

## Requirements

- Python 3.7+
- No external dependencies.

## Usage

Run the script:

```bash
python music_playlist_app.py
```

Example output:
<img width="1291" height="853" alt="image" src="https://github.com/user-attachments/assets/fd38c60f-578b-4ea4-be06-08a0676a001d" />
<img width="777" height="717" alt="image" src="https://github.com/user-attachments/assets/d7786613-e429-4c03-b0e4-fa65c9fa58a4" />






## Main Classes

- **Song** (`name`, `artist`, `length_seconds`)  
  Base song container; info stored as a tuple.
- **LocalSong** (inherits Song)  
  Represents locally stored music files.
- **OnlineSong** (inherits Song)  
  Represents online streaming tracks.
- **Playlist**  
  Playlist manager; handles collections of songs, playback, shuffling, recently played queue.

## Extending

You can add new playback types by subclassing `Song` and overriding `play()`.  
Integrate real music file players or streaming libraries to replace the print/sleep simulation.

## License

MIT


