# ClipboardHist

ClipboardHist is a simple tool for managing clipboard history.

## Installation

```sh
pip install clipboardhist
```

# Usage
```py
from clipboardhist import ClipboardHist

# Create an instance of ClipboardHist
clipboard_hist = ClipboardHist(max_size=5)

# Start monitoring the clipboard
clipboard_hist.watch_clipboard(interval=1)
```

## Support
For questions or bug reports, feel free to open an issue on [GitHub](https://github.com/h1l2o).

## License
This project is licensed under the MIT License - see the LICENSE file for details.