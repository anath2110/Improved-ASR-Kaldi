# -*- coding: utf-8 -*-
2. """ 
4.
5. 
6. """
7.
8. import requests
9. import re
10.
11. import xml.etree.cElementTree as ET
12.
13. def send_http_request(video_id, lang):
14. request = requests.get('http://video.google.com/timedtext?lang=' + lang + '&v=' + v
ideo_id)
15.
16. return request.text
17.
18. def parse_transcriptions_xml(xml):
19. root = ET.fromstring(xml)
20. transcript_text = ''
21. for child in root:
22. if child.tag == 'text':
23. transcript_text = transcript_text + ' ' + child.text
24. print(child.text)
25.
26. return transcript_text
27.
28. def remove_transcription_punctuation(text):
29. text = re.sub(r'[.,]','', text)
30. text = re.sub(r'[\n]',' ', text)
31. text = re.sub(r'"','\'', text)
32. text = re.sub(r''','\'', text)
33. text = re.sub(r' ',' ', text)
34.
35. return text
36.
37. if __name__ == '__main__':
38. video_id = 'iGPXkxeOfdk'
39. lang = 'en'
40.
41. xml_content = send_http_request(video_id, lang)
42.
43. transcript = parse_transcriptions_xml(xml_content)
44.
45. #Remove punctuation
46. transcript = remove_transcription_punctuation(transcript)
47. print(transcript)
48. with open('transcript', 'w') as text_file:
49. text_file.write(transcript)