import subprocess
import os

uwsgi_pid_file = ".UWSGI_PID"


def kill_uwsgi():
    if os.path.exists(uwsgi_pid_file):
        print "Running uwsgi process found. Killing it..."
        with open(uwsgi_pid_file) as pid:
            subprocess.call(['kill', pid.readlines()[0].strip()])
        os.remove(uwsgi_pid_file)
        print "uwsgi stopped."


def start_uwsgi():
    print "Starting uwsgi..."
    kill_uwsgi()

    os.chdir("app")
    process = subprocess.Popen(
        ["uwsgi", "--ini", "server_configs/uwsgi.ini", "--enable-threads"])
    os.chdir("..")

    with open(uwsgi_pid_file, "w") as pid:
        pid.write(str(process.pid))
    print "uwsgi successfully started."


def handle_uwsgi(mode):
    if mode == "start":
        start_uwsgi()
    elif mode == "stop":
        kill_uwsgi()
    else:
        kill_uwsgi()
        start_uwsgi()
