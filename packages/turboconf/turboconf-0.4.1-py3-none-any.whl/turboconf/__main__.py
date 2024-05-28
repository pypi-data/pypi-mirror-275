import turboconf

tmpfile = turboconf.create_temporary_file("test", "txt")
turboconf.edit(tmpfile)
