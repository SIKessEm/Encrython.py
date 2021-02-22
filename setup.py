#-------------------------------------------------------------------------------
# Name:        sikessem-encryption
# Purpose:
#
# Author:      SIGUI Kessé Emmanuel
#
# Created:     18/02/2021
# Copyright:   (c) SIKessEm 2021
# Licence:     MIT
#-------------------------------------------------------------------------------


from cx_Freeze import setup, Executable

executables = [Executable(script = "crypter.py")]

buildOptions = dict(includes = ["string"])

setup(
    name = "Crypter",
    version = "cli-1.0.0",
    description = "Data encryption",
    author = "SIGUI Kessé Emmanuel",
    options = dict(build_exe = buildOptions),
    executables = executables
)

