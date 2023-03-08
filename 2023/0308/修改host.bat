@echo off
set hosts_file=%windir%\System32\drivers\etc\hosts

REM 检查 hosts 文件中是否已存在行
findstr /c:"127.0.0.1 fastlabel-mysql" %hosts_file% > nul && set mysql_found=true
findstr /c:"127.0.0.1 fastlabel-redis" %hosts_file% > nul && set redis_found=true
findstr /c:"127.0.0.1 fastlabel-gateway" %hosts_file% > nul && set gateway_found=true
findstr /c:"127.0.0.1 fastlabel-register" %hosts_file% > nul && set register_found=true
findstr /c:"127.0.0.1 fastlabel-airun" %hosts_file% > nul && set airun_found=true
findstr /c:"127.0.0.1 fastlabel-base" %hosts_file% > nul && set base_found=true
findstr /c:"127.0.0.1 fastlabel-oss" %hosts_file% > nul && set oss_found=true
findstr /c:"127.0.0.1 fastlabel-websocket" %hosts_file% > nul && set websocket_found=true

REM Append the lines that are not found in the hosts file
if not defined localhost_found if not defined mysql_found if not defined redis_found if not defined gateway_found if not defined register_found if not defined airun_found if not defined base_found if not defined oss_found if not defined websocket_found  set file_need_modify=true

if defined file_need_modify echo. >> %hosts_file%
if defined file_need_modify echo ^# ATS HOST START  update time: %date% %time%>> %hosts_file%

if not defined mysql_found echo 127.0.0.1 fastlabel-mysql >> %hosts_file%
if not defined redis_found echo 127.0.0.1 fastlabel-redis >> %hosts_file%
if not defined gateway_found echo 127.0.0.1 fastlabel-gateway >> %hosts_file%
if not defined register_found echo 127.0.0.1 fastlabel-register >> %hosts_file%
if not defined airun_found echo 127.0.0.1 fastlabel-airun >> %hosts_file%
if not defined base_found echo 127.0.0.1 fastlabel-base >> %hosts_file%
if not defined oss_found echo 127.0.0.1 fastlabel-oss >> %hosts_file%
if not defined websocket_found echo 127.0.0.1 fastlabel-websocket >> %hosts_file%

if defined file_need_modify echo # ATS HOST END >> %hosts_file%

if not defined file_need_modify (ECHO host文件无需更新) ELSE (ECHO host文件已更新  update time: %date% %time%)
PAUSE