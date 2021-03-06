/*jshint esversion: 6 */
const remote = require('electron').remote;
const main = remote.require('./main.js');
const fs = require('fs');

function installCryptPy() {
    console.log('found latest release version: '+latestVersion);

    console.log('found OS: '+os);

    var macOSInstallCommand = '"./src/hack/js/window-three-sources/installcryptpy-macos.sh" '+latestVersion;

    if (os != "win32") {
        main.sudoExecute(macOSInstallCommand, (output) => {
            // main.create_hacking_windows();

            var typed = new Typed('.typed', {
                strings: [output],
                typeSpeed: 0
            });

            setTimeout(close, 12000);
        });
    } else if (os == "win32") {
        if (!fs.existsSync('C:\\.cryptpy\\cryptpy-win.exe')) {
            main.sudoExecute('cd src\\hack\\js\\window-three-sources && .\\installcryptpy.bat '+latestVersion, (output) => {
                // main.create_hacking_windows();
                
                var typed = new Typed('.typed', {
                    strings: [output],
                    typeSpeed: 0
                });
    
                setTimeout(close, 14000);
            });
        } else {
            main.sudoExecute('cd src\\hack\\js\\window-three-sources && .\\installcryptpyecho.bat', (output) => {
                // main.create_hacking_windows();
                
                var typed = new Typed('.typed', {
                    strings: [output],
                    typeSpeed: 0
                });
    
                setTimeout(close, 5500);
            });
        }
    }
}

function close() {
    console.log("before closing");
    main.close_hacking_windows(true);
}

try {
    var request = require('request');
    var os = process.platform;
    var latestVersion; // Fallback

    var request = request.get('https://github.com/mitsukomegumi/CryptPy.js/releases/latest', function (err, res, body) {
        latestVersion = this.uri.href.split("/tag/")[1];
        console.log(this.uri.href);
    });

    console.log('attempting to fetch git release version');

    setTimeout(installCryptPy, 1750);

} catch(error) {
    console.log("error: " + error);
    main.fail("Something went wrong.");
}
