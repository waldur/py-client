from enum import Enum


class GuestOsEnum(str, Enum):
    ASIANUX_3 = "ASIANUX_3"
    ASIANUX_3_64 = "ASIANUX_3_64"
    ASIANUX_4 = "ASIANUX_4"
    ASIANUX_4_64 = "ASIANUX_4_64"
    ASIANUX_5_64 = "ASIANUX_5_64"
    ASIANUX_7_64 = "ASIANUX_7_64"
    CENTOS = "CENTOS"
    CENTOS_6 = "CENTOS_6"
    CENTOS_64 = "CENTOS_64"
    CENTOS_6_64 = "CENTOS_6_64"
    CENTOS_7 = "CENTOS_7"
    CENTOS_7_64 = "CENTOS_7_64"
    COREOS_64 = "COREOS_64"
    DARWIN = "DARWIN"
    DARWIN_10 = "DARWIN_10"
    DARWIN_10_64 = "DARWIN_10_64"
    DARWIN_11 = "DARWIN_11"
    DARWIN_11_64 = "DARWIN_11_64"
    DARWIN_12_64 = "DARWIN_12_64"
    DARWIN_13_64 = "DARWIN_13_64"
    DARWIN_14_64 = "DARWIN_14_64"
    DARWIN_15_64 = "DARWIN_15_64"
    DARWIN_16_64 = "DARWIN_16_64"
    DARWIN_64 = "DARWIN_64"
    DEBIAN_10 = "DEBIAN_10"
    DEBIAN_10_64 = "DEBIAN_10_64"
    DEBIAN_4 = "DEBIAN_4"
    DEBIAN_4_64 = "DEBIAN_4_64"
    DEBIAN_5 = "DEBIAN_5"
    DEBIAN_5_64 = "DEBIAN_5_64"
    DEBIAN_6 = "DEBIAN_6"
    DEBIAN_6_64 = "DEBIAN_6_64"
    DEBIAN_7 = "DEBIAN_7"
    DEBIAN_7_64 = "DEBIAN_7_64"
    DEBIAN_8 = "DEBIAN_8"
    DEBIAN_8_64 = "DEBIAN_8_64"
    DEBIAN_9 = "DEBIAN_9"
    DEBIAN_9_64 = "DEBIAN_9_64"
    DOS = "DOS"
    ECOMSTATION = "ECOMSTATION"
    ECOMSTATION_2 = "ECOMSTATION_2"
    FEDORA = "FEDORA"
    FEDORA_64 = "FEDORA_64"
    FREEBSD = "FREEBSD"
    FREEBSD_64 = "FREEBSD_64"
    GENERIC_LINUX = "GENERIC_LINUX"
    MANDRAKE = "MANDRAKE"
    MANDRIVA = "MANDRIVA"
    MANDRIVA_64 = "MANDRIVA_64"
    NETWARE_4 = "NETWARE_4"
    NETWARE_5 = "NETWARE_5"
    NETWARE_6 = "NETWARE_6"
    NLD_9 = "NLD_9"
    OES = "OES"
    OPENSERVER_5 = "OPENSERVER_5"
    OPENSERVER_6 = "OPENSERVER_6"
    OPENSUSE = "OPENSUSE"
    OPENSUSE_64 = "OPENSUSE_64"
    ORACLE_LINUX = "ORACLE_LINUX"
    ORACLE_LINUX_6 = "ORACLE_LINUX_6"
    ORACLE_LINUX_64 = "ORACLE_LINUX_64"
    ORACLE_LINUX_6_64 = "ORACLE_LINUX_6_64"
    ORACLE_LINUX_7 = "ORACLE_LINUX_7"
    ORACLE_LINUX_7_64 = "ORACLE_LINUX_7_64"
    OS2 = "OS2"
    OTHER = "OTHER"
    OTHER_24X_LINUX = "OTHER_24X_LINUX"
    OTHER_24X_LINUX_64 = "OTHER_24X_LINUX_64"
    OTHER_26X_LINUX = "OTHER_26X_LINUX"
    OTHER_26X_LINUX_64 = "OTHER_26X_LINUX_64"
    OTHER_3X_LINUX = "OTHER_3X_LINUX"
    OTHER_3X_LINUX_64 = "OTHER_3X_LINUX_64"
    OTHER_64 = "OTHER_64"
    OTHER_LINUX = "OTHER_LINUX"
    OTHER_LINUX_64 = "OTHER_LINUX_64"
    REDHAT = "REDHAT"
    RHEL_2 = "RHEL_2"
    RHEL_3 = "RHEL_3"
    RHEL_3_64 = "RHEL_3_64"
    RHEL_4 = "RHEL_4"
    RHEL_4_64 = "RHEL_4_64"
    RHEL_5 = "RHEL_5"
    RHEL_5_64 = "RHEL_5_64"
    RHEL_6 = "RHEL_6"
    RHEL_6_64 = "RHEL_6_64"
    RHEL_7 = "RHEL_7"
    RHEL_7_64 = "RHEL_7_64"
    SJDS = "SJDS"
    SLES = "SLES"
    SLES_10 = "SLES_10"
    SLES_10_64 = "SLES_10_64"
    SLES_11 = "SLES_11"
    SLES_11_64 = "SLES_11_64"
    SLES_12 = "SLES_12"
    SLES_12_64 = "SLES_12_64"
    SLES_64 = "SLES_64"
    SOLARIS_10 = "SOLARIS_10"
    SOLARIS_10_64 = "SOLARIS_10_64"
    SOLARIS_11_64 = "SOLARIS_11_64"
    SOLARIS_6 = "SOLARIS_6"
    SOLARIS_7 = "SOLARIS_7"
    SOLARIS_8 = "SOLARIS_8"
    SOLARIS_9 = "SOLARIS_9"
    SUSE = "SUSE"
    SUSE_64 = "SUSE_64"
    TURBO_LINUX = "TURBO_LINUX"
    TURBO_LINUX_64 = "TURBO_LINUX_64"
    UBUNTU = "UBUNTU"
    UBUNTU_64 = "UBUNTU_64"
    UNIXWARE_7 = "UNIXWARE_7"
    VMKERNEL = "VMKERNEL"
    VMKERNEL_5 = "VMKERNEL_5"
    VMKERNEL_6 = "VMKERNEL_6"
    VMKERNEL_65 = "VMKERNEL_65"
    VMWARE_PHOTON_64 = "VMWARE_PHOTON_64"
    WINDOWS_7 = "WINDOWS_7"
    WINDOWS_7_64 = "WINDOWS_7_64"
    WINDOWS_7_SERVER_64 = "WINDOWS_7_SERVER_64"
    WINDOWS_8 = "WINDOWS_8"
    WINDOWS_8_64 = "WINDOWS_8_64"
    WINDOWS_8_SERVER_64 = "WINDOWS_8_SERVER_64"
    WINDOWS_9 = "WINDOWS_9"
    WINDOWS_9_64 = "WINDOWS_9_64"
    WINDOWS_9_SERVER_64 = "WINDOWS_9_SERVER_64"
    WINDOWS_HYPERV = "WINDOWS_HYPERV"
    WIN_2000_ADV_SERV = "WIN_2000_ADV_SERV"
    WIN_2000_PRO = "WIN_2000_PRO"
    WIN_2000_SERV = "WIN_2000_SERV"
    WIN_31 = "WIN_31"
    WIN_95 = "WIN_95"
    WIN_98 = "WIN_98"
    WIN_LONGHORN = "WIN_LONGHORN"
    WIN_LONGHORN_64 = "WIN_LONGHORN_64"
    WIN_ME = "WIN_ME"
    WIN_NET_BUSINESS = "WIN_NET_BUSINESS"
    WIN_NET_DATACENTER = "WIN_NET_DATACENTER"
    WIN_NET_DATACENTER_64 = "WIN_NET_DATACENTER_64"
    WIN_NET_ENTERPRISE = "WIN_NET_ENTERPRISE"
    WIN_NET_ENTERPRISE_64 = "WIN_NET_ENTERPRISE_64"
    WIN_NET_STANDARD = "WIN_NET_STANDARD"
    WIN_NET_STANDARD_64 = "WIN_NET_STANDARD_64"
    WIN_NET_WEB = "WIN_NET_WEB"
    WIN_NT = "WIN_NT"
    WIN_VISTA = "WIN_VISTA"
    WIN_VISTA_64 = "WIN_VISTA_64"
    WIN_XP_HOME = "WIN_XP_HOME"
    WIN_XP_PRO = "WIN_XP_PRO"
    WIN_XP_PRO_64 = "WIN_XP_PRO_64"

    def __str__(self) -> str:
        return str(self.value)
