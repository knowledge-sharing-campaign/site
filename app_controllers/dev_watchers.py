import os
import subprocess


def murder(pid_file):
    if os.path.exists(pid_file):
        with open(pid_file) as pid:
            subprocess.call(["kill", str(pid.readlines()[0].strip())])
        os.remove(pid_file)


def compile_coffee_scripts(mode, dev_mode):
    coffee_compiler_pid_file = ".COFFEE_PID"

    print "Compiling coffeescript sources..."
    subprocess.call(["coffee", "--output", "app/static/js", "--compile", "app/static/coffee"])
    print "Done."

    if not dev_mode:
        return

    if mode == "start":
        murder(coffee_compiler_pid_file)

        process = subprocess.Popen(
            ["coffee", "--watch", "--output", "app/static/js", "--compile", "app/static/coffee"]
        )
        with open(coffee_compiler_pid_file, "w") as pid:
            pid.write(str(process.pid))
        print "live coffee compiler successfully started."
    elif mode == "stop":
        murder(coffee_compiler_pid_file)


def handle_static_root(mode, dev_mode):
    static_watcher_pid_file = ".STATIC_WATCHER_PID"
    subprocess.call(["rm", "-rf", "/opt/ksc/static/*"])
    subprocess.call(["mkdir", "-p", "/opt/ksc/static"])

    if not dev_mode:
        return

    if mode == "start":
        murder(static_watcher_pid_file)

        process = subprocess.Popen(["node", "sync.js"])
        with open(static_watcher_pid_file, "w") as pid:
            pid.write(str(process.pid))
        print "static root watcher successfully started."
    elif mode == "stop":
        murder(static_watcher_pid_file)
