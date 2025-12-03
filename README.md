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

<img width="1291" height="877" alt="image" src="https://github.com/user-attachments/assets/bca94877-2914-4475-815a-2095e051bafe" />
<img width="1045" height="888" alt="image" src="https://github.com/user-attachments/assets/6842bb75-004e-48d0-9347-06057bacd43b" />
<img width="838" height="735" alt="image" src="https://github.com/user-attachments/assets/483414cb-f41a-4d16-b841-f7460d553597" />





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


