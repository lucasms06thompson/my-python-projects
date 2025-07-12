# File Organizer Script

A simple but powerful Python script to automatically organize files in a directory into categorized subfolders.

## Description

This script scans a specified directory and moves files into subfolders based on their file extension. For example, all `.jpg` and `.png` files are moved into an `Images` folder, and all `.pdf` and `.docx` files are moved into a `Documents` folder. Any files with un-categorized extensions are placed in an `Other` folder.

This helps to quickly clean up cluttered directories like your "Downloads" folder.

## Features

-   Scans a target directory for files.
-   Creates categorized subdirectories automatically (e.g., `Images`, `Documents`, `Archives`).
-   Moves files into the appropriate directory.
-   Groups unknown file types into an `Other` folder.
-   Easy to customize with new categories and file types.

## Prerequisites

-   Python 3.x

No external libraries are needed!

## Usage

1.  Navigate to this directory in your terminal:
    ```bash
    cd file-organizer
    ```
2.  Run the script by providing the path to the directory you want to organize.

    ```bash
    python organizer.py /path/to/your/cluttered/folder
    ```

3.  If you don't provide a path, the script will organize the files in its **current directory** by default.
    ```bash
    # This will organize the 'file-organizer' directory itself
    python organizer.py
    ```

### Example

**Before:**
