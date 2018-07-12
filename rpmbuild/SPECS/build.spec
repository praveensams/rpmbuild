Name: nginx
Version: 1.13.1
Release:        1%{?dist}
Summary: nginx builds

Group: test in groups
License: 1.2
URL:https://saminlinux.blogspot.in
Source0: wget https://nginx.org/download/nginx-1.13.1.tar.gz

requires: gcc,gcc++

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc



%changelog

