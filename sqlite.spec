# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       sqlite
Summary:    Library that implements an embeddable SQL database engine
Version:    3.7.11
Release:    1
Group:      Applications/Databases
License:    Public Domain
URL:        http://www.sqlite.org/download.html
Source0:    http://www.sqlite.org/sqlite-autoconf-3071100.tar.gz
Source100:  sqlite.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  readline-devel


%description
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host



%package devel
Summary:    Development tools for the sqlite3 embeddable SQL database engine
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the header files and development documentation
for %{name}. If you like to develop programs using %{name}, you will need
to install %{name}-devel.



%prep
%setup -q -n %{name}-autoconf-3071100

# >> setup
# << setup

%build
# >> build pre
export CFLAGS="$RPM_OPT_FLAGS -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_DISABLE_DIRSYNC=1 -DYYSTACKDEPTH=500 -Wall -DSQLITE_SECURE_DELETE -DSQLITE_ENABLE_FTS3 -DSQLITE_ENABLE_RTREE=1 -DSQLITE_SOUNDEX=1 -DNDEBUG -D_XOPEN_SOURCE=500 -DUSE_PREAD -DSQLITE_ENABLE_UNLOCK_NOTIFY=1 -DSQLITE_OMIT_LOOKASIDE=1"
# << build pre

%reconfigure --disable-static \
    --without-tcl \
    --disable-tcl \
    --enable-threadsafe \
    --enable-threads-override-locks

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre

# << install pre
%make_install

# >> install post
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
# >> files
%doc README
%{_bindir}/*
%{_libdir}/*.so.*
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/sqlite3.1.gz
# << files devel

