# These and other macros are documented in dhd/droid-hal-device.inc

%define device falcon
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Moto G

%define installable_zip 1

%define straggler_files \
/init.mmi.boot.sh\
/init.mmi.touch.sh\
/init.qcom.ssr.sh\
/selinux_version\
/service_contexts\
%{nil}

%define local_hadk_build_project   1

%define android_config \
#define QCOM_BSP 1\
%{nil}

%include rpm/dhd/droid-hal-device.inc
