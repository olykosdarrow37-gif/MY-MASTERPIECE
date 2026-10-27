# BEWARE THE MAN OF TOMORROW! – Android APK

1. Create a new GitHub repository and upload **everything in this folder** (keep the `.github` folder).
2. Open the repo's **Actions** tab → **Build Android APK** → **Run workflow** (it also runs on every push to `main`).
3. When it finishes (about 5–8 min), open the run and download **scoiatael-apk** from *Artifacts*.
4. Unzip it, copy `app-debug.apk` to your phone and install it (allow "install unknown apps" when asked).

The player itself lives in `www/index.html`. Edit it, push, and a new APK is built.
