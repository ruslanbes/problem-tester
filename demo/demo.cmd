@echo off
for /D %%f in (.\*) do (
	cd %%f
	demo.cmd
	cd ..
)
