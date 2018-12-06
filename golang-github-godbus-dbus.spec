# http://github.com/godbus/dbus

%global goipath         github.com/godbus/dbus
%global commit          37252881b3a87eaa2eb04b0ff2211f54f45199ab


%gometa -i

Name:           %{goname}
Version:        3
Release:        0.13%{?dist}
Summary:        Go client bindings for D-Bus
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
Simple library that implements native Go client bindings for the
D-Bus message bus system.

Features include:
Complete native implementation of the D-Bus message protocol
Go-like API (channels for signals / asynchronous method calls, Goroutine-safe
connections)
Subpackages that help with the introspection / property interfaces.

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks -d .

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.markdown

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 3-0.12.git3725288
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 3-0.11.20170620git3725288
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3-0.10.git3725288
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3-0.9.git3725288
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3-0.8.git3725288
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Jan Chaloupka <jchaloup@redhat.com> - 3-0.7.git3725288
- Bump to upstream 37252881b3a87eaa2eb04b0ff2211f54f45199ab
  resolves: #1463511

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3-0.6.gitc7fdd8b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Jan Chaloupka <jchaloup@redhat.com> - 3-0.5.gitc7fdd8b
- Polish the spec file
  related: #1249043

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-0.4.gitc7fdd8b
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-0.3.gitc7fdd8b
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3-0.2.gitc7fdd8b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 jchaloup <jchaloup@redhat.com> - 3-0.1.gitc7fdd8b
- Bump to upstream c7fdd8b5cd55e87b4e1f4e372cdb1db61dd6c66f
  related: #1249043

* Sat Sep 19 2015 jchaloup <jchaloup@redhat.com> - 2-0.5.git88765d8
- Bump to upstream 88765d85c0fdadcd98a54e30694fa4e4f5b51133
  related: #1249043

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 2-0.4.git939230d
- Update to spec-2.1
  related: #1249043

* Fri Jul 31 2015 jchaloup <jchaloup@redhat.com> - 2-0.3.git939230d
- Update spec file to spec-2.0
  resolves: #1249043

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-0.2.git939230d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 31 2015 jchaloup <jchaloup@redhat.com> - 2-0.1.git939230d
- Bump to upstream 939230d2086a4f1870e04c52e0a376c25bae0ec4
- Spec file polishing
  related: #1082734

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.gitcb98efb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 31 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.git
- Initial fedora package

