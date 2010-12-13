%define abiquo_basedir /opt/abiquo

Name:     abiquo-cloud-node
Version:  1.6
Release:  1
Summary:  Abiquo Cloud Node setup package
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
#Source0:  README
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: libvirt
BuildArch: noarch

%description
Next Generation Cloud Management Solution

This package prepares the host to work as a Cloud Node.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.

%post
# save current configs
cp %{_sysconfdir}/libvirt/libvirtd.conf %{_sysconfdir}/libvirt/libvirtd.conf.rpmsave
cp %{_sysconfdir}/sysconfig/libvirtd %{_sysconfdir}/sysconfig/libvirtd.rpmsave

cat > /etc/libvirt/libvirtd.conf <<EOF
listen_tls = 0
listen_tcp = 1
tcp_port = "16509"
#unix_sock_group = "libvirt"
#unix_sock_ro_perms = "0777"
#unix_sock_rw_perms = "0770"
#unix_sock_dir = "/var/run/libvirt"
auth_unix_ro = "none"
auth_unix_rw = "none"
auth_tcp = "none"
auth_tls = "none"
log_level = 3
log_outputs="3:syslog:libvirtd"

EOF

cat > /etc/sysconfig/libvirtd <<EOF
LIBVIRTD_ARGS="--listen"
EOF



%files
%defattr(-,root,root,-)

%changelog
* Mon Oct 25 2010 Sergio Rubio srubio@abiquo.com 1.6-1
- Initial Release
