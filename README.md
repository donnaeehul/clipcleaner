# ClipCleaner

ClipCleaner is a lightweight utility designed to clean and manage the clipboard on Windows. It enhances data handling by monitoring clipboard changes and preventing unnecessary clutter.

## Features

- Monitors the clipboard for changes
- Logs updates to the clipboard content
- Runs silently in the background
- Provides a simple interface for clipboard management

## Requirements

- Python 3.x
- Tkinter (included with standard Python installations)

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/clipcleaner.git
cd clipcleaner
```

## Usage

Run the `clip_cleaner.py` script to start monitoring the clipboard:

```bash
python clip_cleaner.py
```

A message box will appear to confirm that ClipCleaner is running. The application will then minimize to the background and start monitoring clipboard changes.

## Configuration

You can change the interval at which the clipboard is checked by modifying the `interval` parameter in the `ClipCleaner` class (default is 60 seconds).

```python
cleaner = ClipCleaner(interval=30)  # Check every 30 seconds
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.