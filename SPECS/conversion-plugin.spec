Summary: XAPI plugin for starting the conversion VPX
Name: conversion-plugin
Version: 8.0.0
Release: 1.1
URL: https://github.com/xcp-ng-rpms/conversion-plugin
Source0: conversion
Source1: xcmxmlrpclib.py
License: BSD-like

BuildArch: noarch

%description
XCM XAPI plugin

%install
install -m 0755 -D %{SOURCE0} %{buildroot}/etc/xapi.d/plugins/conversion
install -m 0644 -D %{SOURCE1} %{buildroot}/etc/xapi.d/plugins/xcmxmlrpclib.py

%files
/etc/xapi.d/plugins/*

%changelog
* Thu Sep 13 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.0-3
- Initial package from XS's conversion-plugin-8.0.0-1
- Had to create spec file from scratch due to missing source RPM

