FROM influxdb
HEALTHCHECK --interval=5s --timeout=3s CMD curl -f http://localhost:8086 || nc -zv localhost 8086 || exit 1