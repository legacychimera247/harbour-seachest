# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       harbour-seachest

# >> macros
# << macros

Summary:    An unofficial Dropbox client for Sailfish OS.
Version:    0.4.1
Release:    1
Group:      Qt/Qt
License:    GNU GPLv3
URL:        https://mjeb.dev
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-seachest.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   amber-web-authorization
Requires:   libamberwebauthorization
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
An unofficial Dropbox client for Sailfish OS.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files
  
