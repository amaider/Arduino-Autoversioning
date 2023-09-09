# Arduino-Autoversioning
Automatically increments the Build number in 
```c
#define SKETCH_VERSION "1.0.0+23"
``` 
before building.

# platform.txt
```
~/Library/Arduino15/packages/esp8266/hardware/esp8266/3.1.2/platform.txt  
```
add this at line 13 (or before similar lines)

```
recipe.hooks.prebuild.0.pattern={runtime.platform.path}/tools/autoversioning.py --path "{build.project_name}"
```

# autoversioning.py
move to folder
```
~/Library/Arduino15/packages/esp8266/hardware/esp8266/3.1.2/tools
```
