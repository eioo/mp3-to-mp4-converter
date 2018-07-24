# MP3 to MP4 converter

Bulk converts mp3 albums to mp4 files

## Getting Started

### Prerequisites

* Python 2.7
* [FFmpeg](https://www.ffmpeg.org/) (Windows executable included in repo)

### Usage

1. Create directory called `mp3` to project root.
2. Fill it with albums. Albums should have image file (.jpg/.png) and at least one .mp3 file in it.

Example folder structure:

```
Project
|
+-- main.py
+-- ffmpeg.exe
|
+-- mp3/
    |
    +-- Album1/
    |   |
    |   +-- Song1.mp3
    |   +-- Song2.mp3
    |   +-- Song3.mp3
    |   +-- AlbumArt.jpg
    |
    +-- Album2/
    |   |
    |   +-- Song1.mp3
    |   +-- Song2.mp3
    |   +-- Song3.mp3
    |   +-- Art.png
    |
    +-- Album3/
        |
        +-- Song1.mp3
        +-- Song2.mp3
        +-- Song3.mp3
        +-- SomeArt.jpg
```

3. Run the conversion by running `python main.py`. Files converted will go to `./mp4` folder.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details