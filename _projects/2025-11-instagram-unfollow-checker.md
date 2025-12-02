---
date: 2025-06-01
title: "Instagram Unfollow Checker"
collection: projects
permalink: /projects/2025-06-instagram-unfollow-checker
excerpt: "A cross-platform GUI application that identifies Instagram accounts you follow that don't follow you back, with session management and 2FA support."
venue: "Personal Project"
last_modified_at: 2025-12-02 00:00:00
---

A desktop application with a modern GUI that logs into your Instagram account, fetches your follower and following lists, and identifies accounts you follow that don't follow you back.

### Features

- **Modern GUI**: Easy-to-use graphical interface built with Python
- **Session Management**: Saves login sessions to avoid repeated logins
- **2FA Support**: Handles Two-Factor Authentication via pop-up prompt
- **Cross-Platform**: Pre-built executables for Windows, macOS, and Linux
- **Privacy-Focused**: All operations occur locally; no data sent to third parties

### How It Works

1. Enter your Instagram username
2. The app checks for an existing session file
3. If no session exists, enter your password to authenticate
4. Handles 2FA if enabled on your account
5. Fetches your followers and following lists
6. Displays non-followers in the app and saves to `not_following_back.txt`

### Technologies Used

- Python
- Tkinter (GUI)
- Instaloader (Instagram API)
- PyInstaller (cross-platform builds)

### GitHub Repository

[View the project on GitHub](https://github.com/agopalareddy/instagram-unfollow-checker)

Pre-built executables available on the [Releases page](https://github.com/agopalareddy/instagram-unfollow-checker/releases).
