import sys, os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)

exe_path = resource_path("zapret/zapret-winws/winws.exe")

args_gen = [
            exe_path,
            "--wf-tcp=80,443,50000-65535",
            "--wf-udp=443,50000-65535",
            "--filter-udp=443",
            f'--hostlist={resource_path("zapret/zapret-winws/list-general.txt")}',
            "--dpi-desync=fake",
            "--dpi-desync-udplen-increment=10",
            "--dpi-desync-repeats=6",
            "--dpi-desync-udplen-pattern=0xDEADBEEF",
            f'--dpi-desync-fake-quic={resource_path("zapret/zapret-winws/quic_initial_www_google_com.bin")}',
            "--new",
            "--filter-udp=50000-65535",
            "--dpi-desync=fake,tamper",
            "--dpi-desync-any-protocol",
            f'--dpi-desync-fake-quic={resource_path("zapret/zapret-winws/quic_initial_www_google_com.bin")}',
            "--new",
            "--filter-tcp=80",
            "--dpi-desync=fake,split2",
            "--dpi-desync-autottl=2",
            "--dpi-desync-fooling=md5sig",
            "--new",
            "--filter-tcp=443",
            f'--hostlist={resource_path("zapret/zapret-winws/list-general.txt")}',
            "--dpi-desync=fake,split2",
            "--dpi-desync-autottl=2",
            "--dpi-desync-fooling=md5sig",
            f'--dpi-desync-fake-tls={resource_path("zapret/zapret-winws/tls_clienthello_www_google_com.bin")}',
            "--new",
            "--dpi-desync=fake,disorder2",
            "--dpi-desync-autottl=2",
            "--dpi-desync-fooling=md5sig"
        ]

args_dis = [
    "--wf-tcp=443-65535",
    "--wf-udp=443-65535",
    "--filter-udp=443",
    f'--hostlist="{resource_path("zapret/zapret-winws/list-discord.txt")}"',
    "--dpi-desync=fake",
    "--dpi-desync-udplen-increment=10",
    "--dpi-desync-repeats=6",
    "--dpi-desync-udplen-pattern=0xDEADBEEF",
    f'--dpi-desync-fake-quic="{resource_path("zapret/zapret-winws/quic_initial_www_google_com.bin")}"',
    "--new",
    "--filter-udp=50000-65535",
    "--dpi-desync=fake,tamper",
    "--dpi-desync-any-protocol",
    f'--dpi-desync-fake-quic="{resource_path("zapret/zapret-winws/quic_initial_www_google_com.bin")}"',
    "--new",
    "--filter-tcp=443",
    f'--hostlist="{resource_path("zapret/zapret-winws/list-discord.txt")}"',
    "--dpi-desync=fake,split2",
    "--dpi-desync-autottl=2",
    "--dpi-desync-fooling=md5sig",
    f'--dpi-desync-fake-tls="{resource_path("zapret/zapret-winws/tls_clienthello_www_google_com.bin")}"'
]

args_service = [
    "--wf-tcp=443-65535",
    "--wf-udp=443-65535",
    "--wf-tcp=80,443,50000-65535",
    "--wf-udp=443,50000-65535",
    "--filter-udp=443",
    f'--hostlist="{resource_path("zapret/zapret-winws/list-general.txt")}"',
    "--dpi-desync=fake",
    "--dpi-desync-udplen-increment=10",
    "--dpi-desync-repeats=6",
    "--dpi-desync-udplen-pattern=0xDEADBEEF",
    f'--dpi-desync-fake-quic="{resource_path("zapret/zapret-winws/quic_initial_www_google_com.bin")}"',
    "--new",
    "--filter-udp=50000-65535",
    "--dpi-desync=fake,tamper",
    "--dpi-desync-any-protocol",
    f'--dpi-desync-fake-quic="{resource_path("zapret/zapret-winws/quic_initial_www_google_com.bin")}"',
    "--new",
    "--filter-tcp=80",
    "--dpi-desync=fake,split2",
    "--dpi-desync-autottl=2",
    "--dpi-desync-fooling=md5sig",
    "--new",
    "--filter-tcp=443",
    f'--hostlist="{resource_path("zapret/zapret-winws/list-general.txt")}"',
    "--dpi-desync=fake,split2",
    "--dpi-desync-autottl=2",
    "--dpi-desync-fooling=md5sig",
    f'--dpi-desync-fake-tls="{resource_path("zapret/zapret-winws/tls_clienthello_www_google_com.bin")}"',
    "--new",
    "--dpi-desync=fake,disorder2",
    "--dpi-desync-autottl=2",
    "--dpi-desync-fooling=md5sig"
]
