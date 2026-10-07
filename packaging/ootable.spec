Name:           ootable
Version:        0.1.0
Release:        1%{?dist}
Summary:        Renders markdown, JSON, or CSV into auto-sized Unicode terminal grid tables.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ootable
Source0:        ootable-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ootable is a sovereign, capability-bounded UNICODE TABLES written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ootable
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ootable-uninstall

%files
/usr/bin/ootable
/usr/bin/ootable-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
