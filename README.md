# zapret_build-exe

Для сборки в единый exe:
1. В cmd перейти в корень папки
2. Скачать python и библиотеку pyinstaller (pip install pyinstaller)
3. Ввести команду:
python -m PyInstaller --onefile --windowed --uac-admin ^
--icon=iconmain.ico ^
--add-data "icon.ico;." ^
--add-data "zapret/zapret-winws/cygwin1.dll;zapret/zapret-winws" ^
--add-data "zapret/zapret-winws/list-discord.txt;zapret/zapret-winws" ^
--add-data "zapret/zapret-winws/list-general.txt;zapret/zapret-winws" ^
--add-data "zapret/zapret-winws/list-youtube.txt;zapret/zapret-winws" ^
--add-data "zapret/zapret-winws/quic_initial_www_google_com.bin;zapret/zapret-winws" ^
--add-data "zapret/zapret-winws/tls_clienthello_www_google_com.bin;zapret/zapret-winws" ^
--add-data "zapret/zapret-winws/WinDivert.dll;zapret/zapret-winws" ^
--add-data "zapret/zapret-winws/WinDivert64.sys;zapret/zapret-winws" ^
--add-data "zapret/zapret-winws/winws.exe;zapret/zapret-winws" ^
main.py
