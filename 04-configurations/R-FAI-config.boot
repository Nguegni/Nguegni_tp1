interfaces {
    ethernet eth0 {
        address "198.51.100.1/30"
        hw-id "50:00:00:06:00:00"
        offload {
            gro
            gso
            sg
            tso
        }
    }
    ethernet eth1 {
        address "203.0.113.1/24"
        hw-id "50:00:00:06:00:01"
        offload {
            gro
            gso
            sg
            tso
        }
    }
    ethernet eth2 {
        hw-id "50:00:00:06:00:02"
        offload {
            gro
            gso
            sg
            tso
        }
    }
    ethernet eth3 {
        hw-id "50:00:00:06:00:03"
        offload {
            gro
            gso
            sg
            tso
        }
    }
    loopback lo {
    }
}
protocols {
    static {
        route 10.0.0.0/8 {
            next-hop 198.51.100.2 {
            }
        }
        route 172.16.0.0/12 {
            next-hop 198.51.100.2 {
            }
        }
    }
}
service {
    ntp {
        allow-client {
            address "127.0.0.0/8"
            address "169.254.0.0/16"
            address "10.0.0.0/8"
            address "172.16.0.0/12"
            address "192.168.0.0/16"
            address "::1/128"
            address "fe80::/10"
            address "fc00::/7"
        }
        server time1.vyos.net {
        }
        server time2.vyos.net {
        }
        server time3.vyos.net {
        }
    }
}
system {
    config-management {
        commit-revisions "100"
    }
    console {
        device ttyS0 {
            kernel
            speed "115200"
        }
    }
    host-name "R-FAI"
    login {
        operator-group default {
            command-policy {
                allow "*"
            }
        }
        user vyos {
            authentication {
                /* Empreinte du mot de passe expurgee : redefinir avant restauration. */
            }
        }
    }
    option {
        reboot-on-upgrade-failure "5"
    }
    syslog {
        local {
            facility all {
                level "info"
            }
            facility local7 {
                level "debug"
            }
        }
    }
}


