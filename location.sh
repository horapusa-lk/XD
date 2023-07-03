curl -s https://ipinfo.io/$(curl -s https://ipinfo.io/ip)/json | grep loc | awk -F\" '{print $4}'
