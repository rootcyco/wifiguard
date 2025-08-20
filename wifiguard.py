import subprocess
import re
import platform

def get_current_wifi_details():
    try:
        # Fetch current Wi-Fi details using netsh
        output = subprocess.check_output(
            ["netsh", "wlan", "show", "interfaces"],
            stderr=subprocess.STDOUT
        ).decode(errors="ignore")

        details = {
            "SSID": None,
            "IP Address": None
        }

        # Retrieve SSID
        ssid_match = re.search(r"^\s*SSID\s+:\s(.+)$", output, re.MULTILINE)
        details["SSID"] = ssid_match.group(1).strip() if ssid_match else "N/A"

        # Fetch IP Address using ipconfig
        ip_output = subprocess.check_output(
            ["ipconfig"],
            stderr=subprocess.STDOUT
        ).decode(errors="ignore")

        ip_match = re.search(r"IPv4 Address.*: (\d+\.\d+\.\d+\.\d+)", ip_output)
        details["IP Address"] = ip_match.group(1) if ip_match else None

        return details
    except subprocess.CalledProcessError as e:
        print("Error fetching Wi-Fi details:", e.output.decode(errors="ignore"))
        return None

def scan_and_sort_wifi_networks():
    if platform.system().lower() != "windows":
        print("⚠️ This script only works on Windows using 'netsh'.")
        return

    try:
        output = subprocess.check_output(
            ["netsh", "wlan", "show", "networks", "mode=bssid"],
            stderr=subprocess.STDOUT
        ).decode(errors="ignore")
    except subprocess.CalledProcessError as e:
        print("❌ Error running netsh command:")
        print(e.output.decode(errors="ignore"))
        return

    ssids = re.findall(r"SSID \d+ : (.+)", output)
    authentications = re.findall(r"Authentication\s+: (.+)", output)

    if not ssids:
        print("🔍 No Wi-Fi networks found.")
        return

    secure = []
    open_ = []

    for ssid, auth in zip(ssids, authentications):
        entry = (ssid.strip(), auth.strip())
        if auth.strip().lower() == "open":
            open_.append(entry)
        else:
            secure.append(entry)

    current_ssid = get_current_wifi_details()

    print("\n🔒 Secure Wi-Fi Networks:")
    if secure:
        for i, (ssid, auth) in enumerate(sorted(set(secure)), 1):
            print(f"{i:2d}. SSID: {ssid:<30} | Security: {auth}")
    else:
        print("🚫 No secure networks found.")

    print("\n🔓 Open (Unsecure) Wi-Fi Networks:")
    if open_:
        for i, (ssid, auth) in enumerate(sorted(set(open_)), 1):
            print(f"{i:2d}. SSID: {ssid:<30} | Security: {auth}")
    else:
        print("✅ No open (unsecure) networks detected.")

    # Warn if currently connected to an open network
    if current_ssid:
        current_ssid_name = current_ssid["SSID"]
        for ssid, auth in open_:
            if ssid == current_ssid_name:
                print(f"\n⚠️ WARNING: You are currently connected to an UNSECURE Wi-Fi network: '{current_ssid_name}'")
                break
        else:
            print(f"\n📶 You are connected to: '{current_ssid_name}' (Secure)")

        # Display detailed information about the current Wi-Fi connection (only SSID and IP Address)
        print(f"\n🔗 Current Wi-Fi Details:")
        print(f"  SSID: {current_ssid['SSID']}")
        print(f"  IP Address: {current_ssid['IP Address']}" if current_ssid['IP Address'] else "  IP Address: Unavailable")
    else:
        print("\n📶 You are not currently connected to any Wi-Fi network.")

# Run it
scan_and_sort_wifi_networks()
