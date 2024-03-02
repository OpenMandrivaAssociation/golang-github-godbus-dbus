%global debug_package %{nil}

# Run tests in check section
%bcond_with	check

# https://github.com/godbus/dbus
%global goipath		github.com/godbus/dbus
%global goaltipaths	github.com/godbus/dbus/v5
%global forgeurl	https://github.com/godbus/dbus
Version:		5.1.0

%gometa

Summary:	Native Go bindings for D-Bus
Name:		golang-github-godbus-dbus

Release:	1
Source0:	https://github.com/godbus/dbus/archive/v%{version}/dbus-%{version}.tar.gz
URL:		https://github.com/godbus/dbus
License:	BSD-2-Clause
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
%if %{with checks}
BuildRequires:	dbus-daemon
%endif

%description
This is a simple library that implements native Go client
bindings for the D-Bus message bus system.

Main features:

 *   Complete native implementation of the D-Bus message
     protocol
 *   Go-like API (channels for signals / asynchronous
     method calls, Goroutine-safe connections)
 *   Subpackages that help with the introspection/property
     interfaces

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n dbus-%{version}

%build
%gobuildroot
for cmd in $(ls -1 cmd) ; do
	%gobuild -o _bin/$cmd %{goipath}/cmd/$cmd
done

%install
%goinstall
for cmd in $(ls -1 _bin) ; do
	install -Dpm 0755 _bin/$cmd %{buildroot}%{_bindir}/$cmd
done

# install alternative name
ln -fs . %{buildroot}%{_datadir}/gocode/src/%{goaltipaths}
echo \"%{_datadir}/gocode/src/%{goaltipaths}\" >> devel.file-list

%check
%if %{with check}
%gochecks
%endif


