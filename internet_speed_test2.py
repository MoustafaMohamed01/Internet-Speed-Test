import speedtest

test = speedtest.Speedtest()

print("Loading Server List...")
test.get_servers()

print("Choosing Best Server...")
best = test.get_best_server()

print(f"Found: {best['host']} , Located in {best['country']}")

print("Getting Download Speed...")
download = test.download()
print(f"DOWNLOAD: {download / 1024 / 1024:.2f} mbps")

print("Getting Upload Speed...")
upload = test.upload()
print(f"UPLOAD: {upload / 1024 / 1024:.2f} mbps")

ping = test.results.ping
print(f"Ping: {ping:.2f}")