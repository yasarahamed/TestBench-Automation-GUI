Build Image
--------------------
docker build -t name .


                                        Running Image
----------------------------------------------------------------------------------------------

1)  steps to run a Tkinter GUI in container is diffferent from other applications as you 
    cannot run a Tkinter GUI app without X11 or a windowing system — because Tkinter is built 
    to create graphical windows, and it needs a display server to render them
2)  Tkinter is a thin wrapper around Tcl/Tk, which relies on an underlying window system like 
    X11 (on Linux/macOS) or GDI/Windows APIs (on Windows). When running inside Docker, there’s 
    no native GUI or display environment, so it has to rely on the host’s X server to show the window.
---------------------------------------------------------------------------------------------
Prerequisites:
---------------------------------------------------------------------------------------------
1) Docker Desktop installed

2) XQuartz installed: https://www.xquartz.org

3) Your Docker image built (e.g. testbench-gui)
--------------------
One-Time Setup: 
--------------------
1)  Install XQuartz and restart your Mac after installation.

2)  Open XQuartz, go to Security
    ✅ Enable "Allow connections from network clients"

3)  Restart XQuartz.

4) In terminal type 
    xhost + 127.0.0.1


Run Command
------------------------------------------

export DISPLAY=host.docker.internal:0  # Set DISPLAY variable for Docker

docker run -it --rm -e DISPLAY=$DISPLAY image_name
