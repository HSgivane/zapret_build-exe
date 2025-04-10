# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('icon.ico', '.'), ('zapret/zapret-winws/cygwin1.dll', 'zapret/zapret-winws'), ('zapret/zapret-winws/list-discord.txt', 'zapret/zapret-winws'), ('zapret/zapret-winws/list-general.txt', 'zapret/zapret-winws'), ('zapret/zapret-winws/list-youtube.txt', 'zapret/zapret-winws'), ('zapret/zapret-winws/quic_initial_www_google_com.bin', 'zapret/zapret-winws'), ('zapret/zapret-winws/tls_clienthello_www_google_com.bin', 'zapret/zapret-winws'), ('zapret/zapret-winws/WinDivert.dll', 'zapret/zapret-winws'), ('zapret/zapret-winws/WinDivert64.sys', 'zapret/zapret-winws'), ('zapret/zapret-winws/winws.exe', 'zapret/zapret-winws')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    uac_admin=True,
    icon=['iconmain.ico'],
)
