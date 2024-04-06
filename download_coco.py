from utils.general import download, Path

coco_dir = '/home/hallvaeb/Code/tiling-experiment/yolov9/datasets/coco'

# Download labels
segments = False  # segment or box labels
url = 'https://github.com/WongKinYiu/yolov7/releases/download/v0.1/'
urls = [url + ('coco2017labels-segments.zip' if segments else 'coco2017labels.zip')]  # labels
download(urls, dir=coco_dir)

# Download data
urls = ['http://images.cocodataset.org/zips/val2017.zip']  # 7G, 41k images (optional)
download(urls, dir=coco_dir / 'images', threads=3)
