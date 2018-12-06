# http://github.com/elazarl/go-bindata-assetfs

%global goipath         github.com/elazarl/go-bindata-assetfs
%global commit          3dcc96556217539f50599357fb481ac0dc7439b9


%gometa -i

Name:           golang-github-elazarl-go-bindata-assetfs
Version:        0
Release:        0.16%{?dist}
Summary:        Serve embedded files from jteeuwen/go-bindata
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

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
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.git3dcc965
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.14.20150624git3dcc965
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git3dcc965
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git3dcc965
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git3dcc965
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git3dcc965
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.git3dcc965
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git3dcc965
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git3dcc965
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.git3dcc965
- Update to spec-2.1
  related: #1247018

* Fri Jul 31 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.git3dcc965
- Update spec file to spec-2.0
  related: #1247018

* Mon Jul 27 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git3dcc965
- Choose the correct architecture
  resolves: #1247018

* Mon Jul 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git3dcc965
- Bump to upstream 3dcc96556217539f50599357fb481ac0dc7439b9
  resolves: #1244246

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.gitae4665c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 08 2014 Eric Paris <eparis@redhat.com - 0-0.1.gitae4665c
- Bump to upstream ae4665cf2d188c65764c73fe4af5378acc549510

