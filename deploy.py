import os, winreg, subprocess, time, shutil


def main():
    _filedir = os.path.dirname(__file__)
    current_dir = _filedir if _filedir else os.getcwd()
    reg = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
    key = winreg.OpenKey(reg, "Local Settings\\Software\\Microsoft\\Windows\\Shell\\MuiCache", 0, winreg.KEY_READ)
    count_subkey = winreg.QueryInfoKey(key)[1]
    csgo_dir = steam_dir = None
    for i in range(count_subkey):
        subkey_name = winreg.EnumValue(key, i)
        if 'csgo.exe' in (value := subkey_name[0]):
            csgo_dir = os.path.dirname(value)
        elif 'steam.exe' in (value := subkey_name[0]):
            steam_dir = os.path.dirname(value)

            
    subprocess.run(['pip','install','-r','requirements.txt'])
    subprocess.run(['python','generate_shuffle.py'])
    time.sleep(5)
    def move(from_:str, to:str):
        shutil.copy2(current_dir+"/"+from_, csgo_dir+"/"+to)
    
    
    move("kreY.cfg","csgo/cfg")
    move("training.cfg","csgo/cfg")
    shutil.copy2(current_dir+"/", steam_dir+"/userdata/272086896/730/remote/cfg")


if __name__ == "__main__":
    main()