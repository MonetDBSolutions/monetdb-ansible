MonetDB benchmark setup using Ansible
=====================================


Short version
-------------

TODO Concise step by step instructions for running the benchmarks


Ansible role reference
----------------------

Roles and their parameters


### Role `monetdb_package` ###

Installs MonetDB from binary packages.  When this role is finished,
MonetDB has been installed from project-specific binary packages.  The
role makes sure the MonetDB binaries are on the PATH, `monetdbd` is
started on its default port (50000) and will be restarted after a
reboot.

Required parameters: 

- `project_name`, used as a directory prefix while downloading the
  binary packages.

Optional parameters: 

- `packages_url`, URL of the packages tar file.  Defaults to
  `https://www.monetdbsolutions.com/downloads/<project_name>/<project_name>_<packages_os>_distribution_<packages_version>.tar.bz2`
  (*note:* does `.bz2` make sense for rpm/deb files that have already
  been compressed?  I think not.)

- `monetdb_version`, used in some package names, default `11.27.9`.
  (*note:* should there be a default at all?)

- `packages_version`, used to derive the default `packages_url`.
  Either timestamp-like (`20171030`, `20171107b`) or the default `latest`.

- `packages_os`, used to derive the default `packages_url`.  For
  example `xenial` or `fedora27` (*note:* right?)

- `packages_arch`, used to derive the default `packages_url`.

- `download_dir`, where to extract the tar file.  Defaults to `~/download/packages`.


### Role `project_setup` ###

This is an odds and ends role which sets up `.monetdb` and creates
and releases the necessary databases.
This role uses the parameters of the `tpch_benchmark` and
`atraf_benchmark` roles to decide which databases to create.

Also adds the current user to group `monetdb`, or whatever the value of `monetdb_group` is,
unless empty.  This is necessary because the binary packages
restrict access to members of this group.

Optional parameters:

- `databases`, defaults to the union of `atraf_db` if present and
  `tpch_db` if present  (*note:* used to be `db_name`).

- `monetdb_user`, defaults to `monetdb`.

- `monetdb_password`, defaults to `monetdb`.

- `dotmonetdb_dir`, directory in which to put `.monetdb`, defaults to
  the home directory.  If explicitly empty no file will be written.


### Role `tpch_bencmark` ###

Sets up the TPC-H benchmark.  

Required parameters:

- scale factor, ... ??

Optional parameters

- `tpch_db` database to load

### Role `atraf_benchmark` ###

TODO
