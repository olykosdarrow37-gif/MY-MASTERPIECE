import pathlib, re, shutil

root = pathlib.Path("android/app/src/main")

# 1. Permissions + cleartext links
mf = root / "AndroidManifest.xml"
t = mf.read_text(encoding="utf-8")
perms = [
    '<uses-permission android:name="android.permission.READ_MEDIA_AUDIO" />',
    '<uses-permission android:name="android.permission.READ_MEDIA_VIDEO" />',
    '<uses-permission android:name="android.permission.READ_MEDIA_IMAGES" />',
    '<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" android:maxSdkVersion="32" />',
    '<uses-permission android:name="android.permission.WAKE_LOCK" />',
]
add = "".join("    " + p + "\n" for p in perms if p.split('"')[1] not in t)
t = t.replace("<application", add + "    <application", 1)
if "usesCleartextTraffic" not in t:
    t = t.replace("<application", '<application android:usesCleartextTraffic="true"', 1)
mf.write_text(t, encoding="utf-8")

# 2. App name
sx = root / "res/values/strings.xml"
s = sx.read_text(encoding="utf-8")
s = re.sub(r'(<string name="app_name">).*?(</string>)', r"\1BEWARE THE MAN OF TOMORROW!\2", s)
s = re.sub(r'(<string name="title_activity_main">).*?(</string>)', r"\1BEWARE THE MAN OF TOMORROW!\2", s)
sx.write_text(s, encoding="utf-8")

# 3. Icon background colour
bg = root / "res/values/ic_launcher_background.xml"
if bg.exists():
    b = bg.read_text(encoding="utf-8")
    b = re.sub(r"(<color name=\"ic_launcher_background\">).*?(</color>)", r"\1#1b110c\2", b)
    bg.write_text(b, encoding="utf-8")

# 4. Launcher icons (adaptive + legacy)
src = pathlib.Path("resources/icons")
for d in src.iterdir():
    dest = root / "res" / d.name
    dest.mkdir(parents=True, exist_ok=True)
    for f in d.iterdir():
        shutil.copy(f, dest / f.name)
print("Android project patched")

# 5. Splash screen: replace every splash.png the Capacitor template ships
res = root / "res"
for d in res.glob("drawable*"):
    f = d / "splash.png"
    if f.exists():
        name = "land.png" if "-land" in d.name else "port.png"
        shutil.copy(pathlib.Path("resources/splash") / name, f)
print("Splash screens replaced")
