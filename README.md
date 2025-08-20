# WiFiGuard

WiFiGuard is a **Windows-only CLI tool** that helps you quickly scan available Wi-Fi networks, categorize them into **secure** and **open (unsecure)** connections, and check the security of the Wi-Fi you are currently connected to.

It provides an easy way to identify if you are on a potentially unsafe Wi-Fi and displays your current network details like **SSID** and **IP address**.

---

## 🚀 Features

* Scan all available Wi-Fi networks.
* Classify them into **Secure** and **Open (Unsecure)**.
* Detect if you are connected to an **unsecure network**.
* Show current Wi-Fi details (**SSID + IP address**).
* Clean and simple command-line interface.

---

## ⚙️ Requirements

* **Operating System**: Windows (uses `netsh` and `ipconfig`).
* **Python Version**: Python 3.6+
* **Libraries**: No external dependencies (uses built-in Python modules: `subprocess`, `re`, `platform`).

---

## 📦 Installation

1. Clone or download this repository:

```bash
git clone https://github.com/rootcyco/wifiguard.git
cd wifiguard
```

2. Run the script with Python:

```bash
python wifiguard.py
```

---

## 🖥️ Usage

Simply run the script. The output will:

* List **Secure Wi-Fi networks**.
* List **Open Wi-Fi networks**.
* Warn if your **current network is unsecure**.
* Show your **SSID** and **IP Address**.

---

## 📌 Limitations

* Works **only on Windows** (uses `netsh`).
* Limited to showing SSID, security type, and IP address.
* Requires `netsh` and `ipconfig` commands to be available.

---

## 🔮 Future Enhancements

* Add cross-platform support (Linux/macOS).
* Export results to a file (CSV/JSON).
* Include signal strength and MAC address details.
* Build a **GUI version** for user-friendly monitoring.
