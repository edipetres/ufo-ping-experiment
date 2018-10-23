import subprocess

def ping(hostname, ping_count):
  resp = subprocess.check_output(['ping', '-c', str(ping_count), hostname])
  respString = resp.decode('utf-8')
  respLines = respString.split('\n')
  line_with_stats = respLines[-2]
  avg_trip = line_with_stats.split(' = ')[1].split('/')[1]
  return avg_trip

hostnames = ['46.101.253.149', '128.199.144.199', '167.99.51.33']
ping_count = 5

print(f'Average round-trip for {ping_count} pings')

for hostname in hostnames:
  avg_result = ping(hostname, ping_count)
  print(f'{hostname}: {avg_result} ms')