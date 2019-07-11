#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-reporting-api
Version  : 2.0.6
Release  : 3
URL      : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-api/2.0.6/maven-reporting-api-2.0.6.jar
Source0  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-api/2.0.6/maven-reporting-api-2.0.6.jar
Source1  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-api/2.0.6/maven-reporting-api-2.0.6.pom
Source2  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-api/2.0.7/maven-reporting-api-2.0.7.jar
Source3  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-api/2.0.7/maven-reporting-api-2.0.7.pom
Source4  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-api/2.0.9/maven-reporting-api-2.0.9.jar
Source5  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-api/2.0.9/maven-reporting-api-2.0.9.pom
Source6  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-api/2.2.0/maven-reporting-api-2.2.0.jar
Source7  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-api/2.2.0/maven-reporting-api-2.2.0.pom
Source8  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-api/2.2.1/maven-reporting-api-2.2.1.jar
Source9  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-api/2.2.1/maven-reporting-api-2.2.1.pom
Source10  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-api/3.0/maven-reporting-api-3.0.jar
Source11  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-api/3.0/maven-reporting-api-3.0.pom
Source12  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting/2.0.6/maven-reporting-2.0.6.pom
Source13  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting/2.0.7/maven-reporting-2.0.7.pom
Source14  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting/2.2.0/maven-reporting-2.2.0.pom
Source15  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting/2.2.1/maven-reporting-2.2.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-reporting-api-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-reporting-api package.
Group: Data

%description data
data components for the mvn-maven-reporting-api package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.6
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.6
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.7
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.7
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.9
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.9

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.9
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.9

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.2.0
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.2.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.2.0
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.2.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.2.1
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.2.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.2.1
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.2.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/3.0
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/3.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/3.0
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/3.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting/2.0.6
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting/2.0.6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting/2.0.7
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting/2.0.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting/2.2.0
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting/2.2.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting/2.2.1
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting/2.2.1


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.6/maven-reporting-api-2.0.6.jar
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.6/maven-reporting-api-2.0.6.pom
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.7/maven-reporting-api-2.0.7.jar
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.7/maven-reporting-api-2.0.7.pom
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.9/maven-reporting-api-2.0.9.jar
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.0.9/maven-reporting-api-2.0.9.pom
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.2.0/maven-reporting-api-2.2.0.jar
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.2.0/maven-reporting-api-2.2.0.pom
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.2.1/maven-reporting-api-2.2.1.jar
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/2.2.1/maven-reporting-api-2.2.1.pom
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/3.0/maven-reporting-api-3.0.jar
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-api/3.0/maven-reporting-api-3.0.pom
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting/2.0.6/maven-reporting-2.0.6.pom
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting/2.0.7/maven-reporting-2.0.7.pom
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting/2.2.0/maven-reporting-2.2.0.pom
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting/2.2.1/maven-reporting-2.2.1.pom
