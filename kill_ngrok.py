from pyngrok import ngrok

# Get all active tunnels
tunnels = ngrok.get_tunnels()
if tunnels:
    print(f"Found {len(tunnels)} active ngrok tunnels. Disconnecting them...")
    for tunnel in tunnels:
        ngrok.disconnect(tunnel.public_url)
        print(f"Disconnected tunnel: {tunnel.public_url}")
else:
    print("No active ngrok tunnels found.")

# This will also kill the ngrok process
ngrok.kill()
print("Ngrok process killed.")
