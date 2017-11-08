MonetDB benchmark setup using Ansible
=====================================


Short version
-------------

TODO Concise step by step instructions for running the benchmarks


Ansible role reference
----------------------

Roles and their parameters


### Role `monetdb-package` ###

Installs MonetDB from binary packages.  When this role is finished,
MonetDB has been installed from project-specific binary packages.  The
role makes sure the MonetDB binaries are on the PATH, `monetdbd` is
started on its default port (50000) and will be restarted after a
reboot.

Required parameters: 

- `project-name`, used as a directory prefix while downloading the
  binary packages.

Optional parameters: 

- `packages-url`, URL of the packages tar file.  Defaults to
  `https://www.monetdbsolutions.com/downloads/<project-name>/<project-name>_<packages_os>_distribution_<packages_version>.tar.bz2`
  (*note:* does `.bz2` make sense for rpm/deb files that have already
  been compressed?  I think not.)

- `packages_version`, used to derive the default `packages_url`.
  Either timestamp-like (`20171030`, `20171107b`) or the default `latest`.

- `packages-os`, used to derive the default `packages-url`.  For
  example `xenial` or `fedora27` (*note:* right?)

- `packages-arch`, used to derive the default `packages-url`.

- `download_dir`, where to extract the tar file.  Defaults to `~/download/packages`.


### Role `monetdb-setup` ###

Sets up `.monetdb` and creates and starts the necessary databases.
This role uses the parameters of the `tpch-benchmark` and
`atraf-benchmark` roles to decide which databases to start.

Optional parameters:

- `databases`, defaults to the union of `atraf_db` if present and
  `tpch_db` if present  (*note:* used to be `db_name`).

- `monetdb_user`, defaults to `monetdb`.

- `monetdb_password`, defaults to `monetdb`.

- `dotmonetdb_dir`, directory in which to put `.monetdb`, defaults to
  the home directory.  If explicitly empty no file will be written.


### Role `tpch-bencmark` ###

Sets up the TPC-H benchmark.  

Required parameters:

- scale factor, ... ??

Optional parameters

- `tpch_db` database to load

### Role `atraf-benchmark` ###

TODO
