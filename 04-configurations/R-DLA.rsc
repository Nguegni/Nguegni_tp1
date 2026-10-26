# 2026-10-25 04:33:29 by RouterOS 7.23.8
#
/interface ethernet set [ find default-name=ether1 ] disable-running-check=no
/interface ethernet set [ find default-name=ether2 ] disable-running-check=no
/interface ethernet set [ find default-name=ether3 ] disable-running-check=no
/interface ethernet set [ find default-name=ether4 ] disable-running-check=no
/ip pool add name=pool-dla ranges=10.20.10.100-10.20.10.200
/ip address add address=172.16.12.2/30 interface=ether1 network=172.16.12.0
/ip address add address=10.20.10.1/24 interface=ether2 network=10.20.10.0
/ip dhcp-client add disabled=yes interface=ether1 name=client1
/ip dhcp-server add address-pool=pool-dla interface=ether2 name=dhcp-dla
/ip dhcp-server network add address=10.20.10.0/24 dns-server=203.0.113.10 domain=camtrust.lab gateway=10.20.10.1
/ip route add dst-address=0.0.0.0/0 gateway=172.16.12.1
/system identity set name=R-DLA
