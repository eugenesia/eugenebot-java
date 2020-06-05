"""
Cleverbot chat function - keep browser open as a global object.
"""

import sys
import atexit
import time
import cleverbotfree.cbfree

def close_browser():
  print("Closing browser")
  cb.browser.close()

def chat(msg):
  try:
    print("Getting browser form")
    cb.get_form()
  except:
    sys.exit()
  print("Sending message %s" % msg)
  cb.send_input(msg)
  return cb.get_response()

cb = cleverbotfree.cbfree.Cleverbot()
try:
  print("Fetching URL on browser")
  cb.browser.get(cb.url)
except:
  close_browser()
  sys.exit()

# Close browser on exit
atexit.register(close_browser)

if __name__ == '__main__':
  resp = chat("Hello there")
  print(resp)
