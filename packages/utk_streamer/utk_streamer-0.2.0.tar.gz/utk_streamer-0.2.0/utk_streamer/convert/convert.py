from lxml import etree

class TTAFConverter:
    def __init__(self, ttaf_file):
        self.ttaf_file = ttaf_file
        self.namespaces = {
            'ttaf': 'http://www.w3.org/2006/04/ttaf1',
            'tts': 'http://www.w3.org/2006/04/ttaf1#styling'
        }
        self.root = etree.parse(ttaf_file)
        self.root_as_str = etree.tostring(self.root)
        self.all_captions = self.get_paragraphs()


    def get_paragraphs(self):
        all = []
        paragraphs = [value for value in self.root.xpath("//ttaf:p",namespaces=self.namespaces)]
        for p in paragraphs:
            begin = p.xpath("./@begin")
            end = p.xpath("./@end")
            all.append({"begin": begin[0], "end": end[0], "caption": ''.join(p.itertext()).strip()})
        return all

    def write_vtt(self):
        with open(self.ttaf_file.replace('.xml', '.vtt'), 'w') as vtt:
            vtt.write('WEBVTT\n\n')
            i = 1
            for caption in self.all_captions:
                vtt.write(f"{i}\n")
                vtt.write(f"{caption.get('begin')}0 --> {caption.get('end')}0\n")
                vtt.write(f"{caption.get('caption')}\n\n")
                i+=1
        return


if __name__ == "__main__":
    x = TTAFConverter("fixtures/cc_AM-002.xml")
    x.write_vtt()



