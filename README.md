# CELL COUNTER
## Deep learning for wbc classification   and  image processing for rbc counting

### HOW TO USE IT :

   1-install : 
                      
         git clone https://github.com/saeed5959/CellCounter
         pip install -r requirements.txt
                      
   2-RBC :
   
         python3 main.py   --mode rbc_count   --img_path ./test_data/RBC/1.jpg
         
   2-WBC classify infer :
   
         python3 main.py   --mode wbc_classify_infer   --img_path ./test_data/WBC/classify/basophil.jpg  --model_path ./model.pth
         
   2-WBC classify train :
   
         python3 main.py --mode wbc_classify_train --dataset_file ./dataset_file.txt  --model_path ./model.pth
         
   2-WBC segmentation :
   
         python3 main.py --mode wbc_segment --img_path ./test_data/WBC/segment/main_image.jpg
                      
                      
                      
                      
### segmentation and classification and counting the cells in blood :

   1-red blood cell : 
                      
                      1- counting the numbers of RBC     RESULT : 99.25% in counting 
   
                      2- finding the radius of RBC       RESULT : mean = 99%  and variance = 90%  
                      
                      3- dataset : 322 images that averagely any image has 1000 RBC
   
   
   2-white blood cell : 
   
                      1- counting the numbers of WBC     RESULT : 100% in counting 
   
                      2- classification of WBC       RESULT : 92% in classification  
                      
                      3- dataset : 401 images that averagely any image has 3 WBC
  
                             

### blood cells

<img src="/test_data/RBC/1.jpg" width="450" height="200" border="20" title="blood cells">
                      



for medicl application , blood cells have a huge information about the diseases . so we can after taking a picture of these cells and processing and counting how many of these cells exist in the blood then we can detect a special desease 





### red blood cell

<img src="main_image.jpg" width="450" height="150" border="20">

### red blood cell after detection

<img src="crop_and_detect_image.jpg" width="450" height="150" border="20">


### esotrophil

<img src="eso-14882501911.jpg" width="450" height="150" border="20">
 
### lamphocyte
 
<img src="lam-10490525360.jpg" width="450" height="150" border="20">
 
### monocyte
 
<img src="mono-9264272505.jpg" width="450" height="150" border="20">

### neutrophile
 
<img src="neu-4021732975.jpg" width="450" height="150" border="20">

### basophill
 
<img src="98-1-4-2710.jpg" width="450" height="150" border="20">
