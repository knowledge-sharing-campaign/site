import subprocess
import os

nginx_pid_file = ".NGINX_PID"


def render_nginx_config(port):
    print "Rendering config for nginx..."
    subprocess.call(['node', 'render_conf.js', str(port)])
    print "Config rendered."


def kill_nginx():
    if os.path.exists(nginx_pid_file):
        print "Running nginx process found. Killing it..."
        with open(nginx_pid_file) as pid:
            subprocess.call(['kill', pid.readlines()[0].strip()])
        os.remove(nginx_pid_file)
        print "nginx stopped."


def start_nginx(port):
    render_nginx_config(port)

    print "Starting nginx..."
    kill_nginx()

    process = subprocess.Popen(["nginx", "-c", os.getcwd() + "/app/server_configs/nginx.conf"])

    process.wait()
    if process.poll() != 0:
        print "nginx start failed."
    else:
        with open(nginx_pid_file, "w") as pid:
            pid.write(str(process.pid + 1))  # TODO: Possibly flaky PID check.
        print "nginx successfully started on port %d" % port


def handle_nginx(mode, port):
    if mode == "start":
        start_nginx(port)
    elif mode == "stop":
        kill_nginx()
    else:
        kill_nginx()
        start_nginx(port)
