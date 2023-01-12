# txt_search
"""
Created on Sat Aug 13 18:09:13 2022

@author: harik
"""

import time
import os
import codecs

loc = 'C:/Users/harik/Desktop/dtp/Downloads/txt/'
loc = 'C:/python/anaconda/pkgs/spyder-5.1.5-py39haa95532_1/'+\
                                            'Lib/site-packages/spyder/config/'
loc = 'G:/My Drive/Mine/Programming/Python/Codes/imp/'
loc = 'G:/My Drive/Mine/'
loc = '/home/hari/zHari/Programming/ChromePlugin/videospeed-master/'
# to_find = 'tnurbanepay'.lower()
to_find = 'node_template_runtime'.lower()
to_find = 'chrome.browserActio'.lower()
need_in_title = []
# need_in_title = ['.rs']
# need_in_title = []
no_need_in_title = []
# no_need_in_title = ['.pyc', '.pdf', '.png']
sub_directory = True

print()
print()
if need_in_title:
    print('NEED in title', need_in_title)
if no_need_in_title:
    print('NO NEED in title', no_need_in_title)
print()

class text_search:
    def txt_search(self):
        tot_count = 0
        all_files = [x for x in os.walk(loc)]
        if not sub_directory:
            all_files = [all_files[0]]
        tc = []
        for dirr in all_files:
            if not dirr[-1]:
                continue
            for txt in dirr[-1]:
                if not self.can_pass(txt):
                    continue
                name = f'{dirr[0]}/{txt}'
                # print(name)
                tc.append(name)
                tot_count+=1
                if not tot_count%50:
                    print('Count CHECK>> ' + name)
                # with open(name) as f:
                try:
                    with codecs.open(name, 'r', encoding='utf-8',
                                     errors='ignore') as f:
                        lines = f.read().lower()
                    if to_find in lines:
                        print()
                        print('FOUND:::', name)
                        print()
                except:
                    pass

    def can_pass(self, txt):
        for tmp1 in need_in_title:
            if not txt.endswith(tmp1):
                return False
        for tmp1 in no_need_in_title:
            if txt.endswith(tmp1):
                return False
        return True
            

def main():
    a = text_search()
    a.txt_search()
   
if __name__ == '__main__':
    start_time = time.time()
    main()
    print(), print(f'---{time.time()-start_time} seconds Full ---')
    # winsound.Beep(1000, 500) # (frequency, duration)
