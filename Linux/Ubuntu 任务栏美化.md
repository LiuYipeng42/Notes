# Ubuntu 任务栏美化

```shell
#将dock移动到窗口底部位置，如果习惯左边也可以不执行该行命令
gsettings set org.gnome.shell.extensions.dash-to-dock dock-position "BOTTOM"
#根据屏幕大小，给dock中的图标设置一个合适的大小值，习惯为64,48或32
gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 32
#居中显示
gsettings set org.gnome.shell.extensions.dash-to-dock extend-height false
#移动鼠标到dock位置时自动显示
gsettings set org.gnome.shell.extensions.dash-to-dock autohide true
#全屏模式时自动隐藏Dock
gsettings set org.gnome.shell.extensions.dash-to-dock autohide-in-fullscreen true
#默认隐藏DOCK
gsettings set org.gnome.shell.extensions.dash-to-dock dock-fixed false
#隐藏延迟时间，通过该时间可以解决因DOCK隐藏导致菜单移动的问题，默认0.2
gsettings set org.gnome.shell.extensions.dash-to-dock hide-delay 10.0
#设置“应用”图标为左边,根据个人习惯，习惯右边的可以不用执行该行
gsettings set org.gnome.shell.extensions.dash-to-dock show-apps-at-top true
#点击DOCK中的图标后缩小应用窗口 默认为'previews'
gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize'
```

