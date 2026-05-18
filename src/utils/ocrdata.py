from rapidocr_onnxruntime import RapidOCR

# Initialize OCR
engine = RapidOCR()


def ocrcoords(target_word,screen):


    # Run OCR
    results, _ = engine(screen)
    

    for item in results:

        points = item[0]   # coordinates
        text = item[1]     # detected text
        conf = item[2]     # confidence
        text = text.replace(" ", "")
        #print(text, conf)

        # Match word
        if target_word.lower() in text.lower():

            print("FOUND:", text)

            # Get center coordinates
            x = int((points[0][0] + points[2][0]) / 2)
            y = int((points[0][1] + points[2][1]) / 2)

            print("Coordinates:", x, y)
            #pyautogui.moveTo(x, y)
            return(x,y)